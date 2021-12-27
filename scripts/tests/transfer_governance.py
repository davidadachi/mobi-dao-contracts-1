from brownie import (
  GaugeProxy,
  GaugeController,
  LiquidityGaugeV3,
  PoolProxy,
  accounts,
  network
)

GAUGE_CONTROLLER = "0xF8eABb30A124AAc16B9eD6aFaed830BE30fB128E"
GAUGE = "0xBe66E91445E68f9EeF6A4d79596B4e130F7A1B0f"
GOVERNANCE = "0xDC4c8ca5C18A18A08a64a30B369E7a8B40e5fbcC"

def main():
  network.gas_limit(8000000)
  admin = accounts.load('kyle_personal')

  # part one
  gauge_proxy = GaugeProxy.deploy(GOVERNANCE, admin, {"from": admin})
  pool_proxy = PoolProxy.deploy(GOVERNANCE, admin, {"from": admin})

  # part two
  liquidity_gauge = LiquidityGaugeV3.at(GAUGE)
  liquidity_gauge.commit_transfer_ownership(gauge_proxy, {"from": admin})
  gauge_proxy.accept_transfer_ownership(GAUGE, {"from": admin})

  # part three
  gauge_controller = GaugeController.at(GAUGE_CONTROLLER)
  gauge_controller.commit_transfer_ownership(GOVERNANCE, {"from": admin})
  gauge_controller.apply_transfer_ownership({"from": admin})
