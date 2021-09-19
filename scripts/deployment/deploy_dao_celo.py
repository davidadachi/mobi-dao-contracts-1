import json

from brownie import (
    ERC20MOBI,
    GaugeController,
    LiquidityGaugeV3,
    LiquidityGaugeReward,
    Minter,
    PoolProxy,
    VotingEscrow,
    accounts,
    history,
    network
)
network.gas_limit(8000000)

from . import deployment_config as config

# TODO set weights!

# name, type weight
GAUGE_TYPES = [
    ("Liquidity", 10 ** 18),
]

# lp token, gauge weight
POOL_TOKENS = {
    "USDC_O": ("0xd7Bf6946b740930c60131044bD2F08787e1DdBd4", 50),
    "ETH_O": ("0x846b784Ab5302155542c1B3952B54305F220fd84", 15),
    "BTC_O": ("0x8cD0E2F11ed2E896a8307280dEEEE15B27e46BbE", 15),
    "USDC_M": ("0x635aec36c4b61bac5eB1C3EEe191147d006F8a21", 15),
    "USDT_M": ("0xC7a4c6EF4A16Dc24634Cc2A951bA5Fec4398f7e0", 5),
}


# lp token, reward contract, reward token, gauge weight
REWARD_POOL_TOKENS = {}

def live_part_one():
    admin, _ = config.get_live_admin()
    deploy_part_one(admin, config.REQUIRED_CONFIRMATIONS, config.DEPLOYMENTS_JSON)


def live_part_two():
    admin, _ = config.get_live_admin()
    with open(config.DEPLOYMENTS_JSON) as fp:
        deployments = json.load(fp)
    token = ERC20MOBI.at(deployments["ERC20MOBI"])
    voting_escrow = VotingEscrow.at(deployments["VotingEscrow"])

    deploy_part_two(
        admin, token, voting_escrow, config.REQUIRED_CONFIRMATIONS, config.DEPLOYMENTS_JSON
    )


def development():
    accounts.load("dev-1")
    token, voting_escrow = deploy_part_one(accounts[0])
    deploy_part_two(accounts[0], token, voting_escrow)


def deploy_part_one(admin, confs=1, deployments_json=None):
    token = ERC20MOBI.deploy("Mobius DAO Token", "MOBI", 18, {"from": admin, "required_confs": confs})
    voting_escrow = VotingEscrow.deploy(
        token,
        "Vote-escrowed MOBI",
        "veMOBI",
        "veMOBI_1.0.0",
        {"from": admin, "required_confs": confs},
    )
    deployments = {
        "ERC20MOBI": token.address,
        "VotingEscrow": voting_escrow.address,
    }
    if deployments_json is not None:
        with open(deployments_json, "w") as fp:
            json.dump(deployments, fp)
        print(f"Deployment addresses saved to {deployments_json}")

    return token, voting_escrow


def deploy_part_two(admin, token, voting_escrow, confs=1, deployments_json=None):
    token.start_epoch_time_write({"from": admin})
    gauge_controller = GaugeController.deploy(
        token, voting_escrow, {"from": admin, "required_confs": confs}
    )
    for name, weight in GAUGE_TYPES:
        gauge_controller.add_type(name, weight, {"from": admin, "required_confs": confs})

    pool_proxy = PoolProxy.deploy(admin, admin, admin, {"from": admin, "required_confs": confs})
    minter = Minter.deploy(token, gauge_controller, {"from": admin, "required_confs": confs})
    token.set_minter(minter, {"from": admin, "required_confs": confs})

    deployments = {
        "ERC20MOBI": token.address,
        "VotingEscrow": voting_escrow.address,
        "GaugeController": gauge_controller.address,
        "Minter": minter.address,
        "LiquidityGaugeV3": {},
        "LiquidityGaugeReward": {},
        "PoolProxy": pool_proxy.address,
    }
    for name, (lp_token, weight) in POOL_TOKENS.items():
        gauge = LiquidityGaugeV3.deploy(lp_token, minter, admin, {"from": admin, "required_confs": confs})
        gauge_controller.add_gauge(gauge, 0, weight, {"from": admin, "required_confs": confs})
        deployments["LiquidityGaugeV3"][name] = gauge.address
    
    for (name, (lp_token, reward_claim, reward_token, weight)) in REWARD_POOL_TOKENS.items():
        gauge = LiquidityGaugeReward.deploy(
            lp_token, minter, reward_claim, reward_token, {"from": admin, "required_confs": confs}
        )
        gauge_controller.add_gauge(gauge, 0, weight, {"from": admin, "required_confs": confs})
        deployments["LiquidityGaugeReward"][name] = gauge.address
    gauge_controller.initiate_for_farming({"from": admin, "required_confs": confs})

    print(f"Deployment complete! Total gas used: {sum(i.gas_used for i in history)}")
    if deployments_json is not None:
        with open(deployments_json, "w") as fp:
            json.dump(deployments, fp)
        print(f"Deployment addresses saved to {deployments_json}")
