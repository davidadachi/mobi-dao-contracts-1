from brownie import (
    GaugeController,
    GaugeProxy,
    LiquidityGaugeV3,
    network,
    accounts,
)

from web3.gas_strategies.time_based import fast_gas_price_strategy as gas_strategy


def main():
  network.gas_limit(8000000)
  # admin = accounts.load("kyle_personal")

  minter = "0x2B52d2160b088029f689D481BD1f5D3E83e57ba8"
  lp = "0xc792813d9B318fEdF95323720A3da378627731f6"
  gauge_proxy = GaugeProxy.at('0x61eBd5a8051b255E1bd6dcE769DeA4349aF8B40b')
  gauge_controller = GaugeController.at("0xF8eABb30A124AAc16B9eD6aFaed830BE30fB128E")

  print(gauge_controller.n_gauges())
  print(gauge_controller.n_gauge_types())
  print(gauge_controller.gauges(2))

  # gauge = LiquidityGaugeV3.deploy(lp, minter, admin, {"from": admin})
  # gauge.commit_transfer_ownership(gauge_proxy, {"from": admin})
  # gauge_proxy.accept_transfer_ownership(gauge, {"from": admin})

