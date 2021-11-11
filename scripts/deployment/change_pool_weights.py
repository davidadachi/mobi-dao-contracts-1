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

GAUGE_TYPES = [
    ("Liquidity", 10 ** 18),
]

# Name, address, new weight
GAUGE_INFO = [
    ("USDC Optics", "0xdAA2ab880b7f3D5697e6F85e63c28b9120AA9E07", 5000),
    ("BTC", "0x1A8938a37093d34581B21bAd2AE7DC1c19150C05", 750),
    ("ETH", "0xD38e76E17E66b562B61c149Ca0EE53CEa1145733", 750),
    ("USDT Moss", "0xe2d6095685248F38Ae9fef1b360D772b78Ea19D1", 500),
    ("USDC Moss", "0xd1B3C05FE24bda6F52e704daf1ACBa8c440d8573", 1000),
    ("USDC Polygon", "0x52517feb1Fc6141d5CF6718111C7Cc0FD764fA5d", 500),
    ("USDC Solana", "0x27D9Bfa5F864862BeDC23cFab7e00b6b94488CC6", 1500)
    ("aaUSDC", "0xF2ae5c2D2D2eD13dd324C0942163054fc4A3D4d9")
]

TO_ADD = [
    #("USDC Polygon", "0xf5b454cF47Caca418D95930AA03975Ee4bf409bc", 0)
    # ("USDC Solana", "0xAFEe90ab6A2D3B265262f94F6e437E7f6d94e26E", 0)
    #("pUSD Meta", "0x57f008172cF89b972db3db7dD032e66BE4AF1A8c", 0)
    # ("pEUR", "0x2642Ab16Bfb7A8b36EE42c9CbA2289C4Ca9F33b9", 0),
    # ("pCELO", "0x4D6B17828d0173668e8Eb730106444556a98c0F9", 0)
    # ("pUSD", "0x18d71b8664E69D6Dd61C79247dBf12bFAaf66C10", 0)
    ("aaUSDC", "0x730e677f39C4Ca96012c394B9Da09A025E922F81", 0)
]

GAUGE_CONTROLLER = '0x7530E03056D3a8eD0323e61091ea2f17a1aC5C25'
MINTER = '0x5F0200CA03196D5b817E2044a0Bb0D837e0A7823'
confs = 3

def deploy_gauges():
    admin = accounts.load('dev-1')
    minter = Minter.at(MINTER)
    controller = GaugeController.at(GAUGE_CONTROLLER)
    for (name, lp, weight) in TO_ADD:
        gauge = LiquidityGaugeV3.deploy(lp, minter, admin, {"from": admin, "required_confs": confs})
        controller.add_gauge(gauge, 0, weight, {"from": admin, "required_confs": confs})
        print("Gauge: ", name, " At: ", gauge)


# def weights():
#     admin = accounts.load('dev-1')
#     minter = Minter.at(MINTER)
#     controller = GaugeController.at(GAUGE_CONTROLLER)
        
#     for (name, address, weight) in GAUGE_INFO:
#         controller.change_gauge_weight(address, weight, {"from": admin})
        
def checkpoint():
    admin = accounts.load('dev-1')
    controller = GaugeController.at(GAUGE_CONTROLLER)
        
    for (name, address, weight) in GAUGE_INFO:
        controller.checkpoint_gauge(address, {"from": admin})
