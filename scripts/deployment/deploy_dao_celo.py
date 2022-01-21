import json

from brownie import (
    ERC20MOBI,
    GaugeController,
    LiquidityGaugeV3,
    LiquidityGaugeReward,
    Minter,
    PoolProxy,
    GaugeProxy,
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
    "name": ("0xC7128fC9D8c0bc45a68a50b2B65bF6F18df3DFA3", 100)
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
    token = ERC20MOBI.at("0xA04E399d9b42F1B8F3b11f0685282BfA41912a0a")
    voting_escrow = VotingEscrow.at("0xd2Fc9ebE9602340f9917794d1B549cA3A275dd9f")

    deploy_part_two(
        admin, token, voting_escrow, config.REQUIRED_CONFIRMATIONS, config.DEPLOYMENTS_JSON
    )


def development():
    accounts.load("kyle_personal")
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
    # gauge_controller = GaugeController.deploy(
    #     token, voting_escrow, {"from": admin, "required_confs": confs}
    # )
    # for name, weight in GAUGE_TYPES:
    #     gauge_controller.add_type(name, weight, {"from": admin, "required_confs": confs})

    # pool_proxy = PoolProxy.deploy(admin, admin, {"from": admin, "required_confs": confs})
    # minter = Minter.deploy(token, gauge_controller, {"from": admin, "required_confs": confs})

    minter = "0x2B52d2160b088029f689D481BD1f5D3E83e57ba8"
    gauge_controller = GaugeController.at("0xF8eABb30A124AAc16B9eD6aFaed830BE30fB128E")
    # pool_proxy = "0x46bDD2b18E261f8170B0114Cd558D31e998031cc"
    # liquidity_gauge = "0x7399CB1bE49fc0A070DD3F925224b5422cb41687"

    # # token.set_minter(minter, {"from": admin, "required_confs": confs})

    deployments = {
        "ERC20MOBI": token.address,
        "VotingEscrow": voting_escrow.address,
        "GaugeController": gauge_controller.address,
        "Minter": minter,
        "LiquidityGaugeV3": {},
        "LiquidityGaugeReward": {},
    }
    for name, (lp_token, weight) in POOL_TOKENS.items():
        gauge = LiquidityGaugeV3.deploy(lp_token, minter, admin, {"from": admin, "required_confs": confs})
        gauge_controller.add_gauge(gauge, 0, weight, {"from": admin, "required_confs": confs})
        deployments["LiquidityGaugeV3"][name] = gauge.address
    
    # for (name, (lp_token, reward_claim, reward_token, weight)) in REWARD_POOL_TOKENS.items():
    #     gauge = LiquidityGaugeReward.deploy(
    #         lp_token, minter, reward_claim, reward_token, {"from": admin, "required_confs": confs}
    #     )
    #     gauge_controller.add_gauge(gauge, 0, weight, {"from": admin, "required_confs": confs})
    #     deployments["LiquidityGaugeReward"][name] = gauge.address
    # gauge_controller.initiate_for_farming({"from": admin, "required_confs": confs})

    # print(f"Deployment complete! Total gas used: {sum(i.gas_used for i in history)}")
    # if deployments_json is not None:
    #     with open(deployments_json, "w") as fp:
    #         json.dump(deployments, fp)
    #     print(f"Deployment addresses saved to {deployments_json}")
