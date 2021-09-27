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
    ("USDC Optics", "0xdAA2ab880b7f3D5697e6F85e63c28b9120AA9E07", 60),
    ("BTC", "0x1A8938a37093d34581B21bAd2AE7DC1c19150C05", 10),
    ("ETH", "0xD38e76E17E66b562B61c149Ca0EE53CEa1145733", 10),
    ("USDT Moss", "0xe2d6095685248F38Ae9fef1b360D772b78Ea19D1", 5),
    ("USDC Moss", "0xd1B3C05FE24bda6F52e704daf1ACBa8c440d8573", 15),
    ("USDC Polygon", "0x52517feb1Fc6141d5CF6718111C7Cc0FD764fA5d", 0)
]

TO_ADD = [
    ("USDC Polygon", "0xf5b454cF47Caca418D95930AA03975Ee4bf409bc", 0)
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


def weights():
    admin = accounts.load('dev-1')
    minter = Minter.at(MINTER)
    controller = GaugeController.at(GAUGE_CONTROLLER)
        
    for (name, address, weight) in GAUGE_INFO:
        controller.change_gauge_weight(address, weight, {"from": admin})
        
def checkpoint():
    admin = accounts.load('dev-1')
    controller = GaugeController.at(GAUGE_CONTROLLER)
        
    for (name, address, weight) in GAUGE_INFO:
        controller.checkpoint_gauge(address, {"from": admin})
