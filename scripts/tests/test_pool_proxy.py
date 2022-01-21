from brownie import (
    PoolProxy,
    accounts,
    network
)

POOL = "0xec5BFbF56d887D4D80a9b17B5b1dd5ACf01EcF00"
POOL_PROXY = "0xafC19985d0054a5cB8278ABA211668AE16198D51"
ZERO = "0x0000000000000000000000000000000000000000"

def main():
  network.gas_limit(8000000)
  admin = accounts.load('dahlia_alice')

  # part one
  # PoolProxy.deploy(admin, admin, {"from": admin})

  # part two
  pool_proxy = PoolProxy.at(POOL_PROXY)

  zeroes = [POOL]
  for _ in range(19):
    zeroes.append(ZERO)
  
  # make sure no functions revert
  pool_proxy.withdraw_admin_fees(POOL, {"from": admin})
  pool_proxy.withdraw_many(zeroes, {"from": admin})
  pool_proxy.kill_me(POOL, {"from": admin})
  pool_proxy.unkill_me(POOL, {"from": admin})
  pool_proxy.set_admin_fee(POOL, 10 ** 6, {"from": admin})
  pool_proxy.set_fee(POOL, 10 ** 5, {"from": admin})
  pool_proxy.set_deposit_fee(POOL, 10 ** 5, {"from": admin})
  pool_proxy.set_withdraw_fee(POOL, 10 ** 6, {"from": admin})
  pool_proxy.ramp_A(POOL, 75, 1649772031, {"from": admin})
  pool_proxy.stop_ramp_A(POOL, {"from": admin})
  pool_proxy.set_dev_addr(POOL, admin, {"from": admin})
  pool_proxy.transfer_ownership(POOL, pool_proxy.address, {"from": admin})
  pool_proxy.renounce_ownership(POOL, {"from": admin})
