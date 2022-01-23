import json

from brownie import (
    ERC20MOBI,
    LiquidityGaugeV3,
    FeeDistributor,
    PoolProxy,
    VotingEscrow,
    ZERO_ADDRESS,
    accounts,
    history,
    network
)
network.gas_limit(8000000)

MOBIUS_BASE_BURNER = '0x1cD9fd825Df14E6A03DE9259427ae106353e9995'

TIMELOCK = '0x7d9Af9dF33D6CAB895B4cF3422D790cbE98B48c8'
MULTI_SIG = '0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c'

POOL_PROXY_OWNER = TIMELOCK
POOL_EMERGENCY_OWNER = MULTI_SIG

VEMOBI_ADDRESS = '0xd813a846aa9d572140d7abbb4efac8cd786b4c0e'
FEE_TOKEN = '0x73a210637f6F6B7005512677Ba6B3C96bb4AA44B'

FEE_ADMIN = MULTI_SIG
EMERGENCY_RETURN = TIMELOCK

START_TIME = 1642811506

def main():
    admin = accounts.load('dev-1')
    auth = {'from': admin}
    distributor = FeeDistributor.deploy(VEMOBI_ADDRESS, START_TIME, FEE_TOKEN, FEE_ADMIN, EMERGENCY_RETURN, auth)


def test_deploy():
    MOBIUS_BASE_BURNER = '0x1cD9fd825Df14E6A03DE9259427ae106353e9995'
    POOL_PROXY_OWNER = '0x6c0d6Fba3bcdb224278474E8d524F19c6BB55850'
    POOL_EMERGENCY_OWNER = '0x6c0d6Fba3bcdb224278474E8d524F19c6BB55850'
    VEMOBI_ADDRESS = '0x536CBB53a8b8dCcbC4406b063E7B7CaD05861fa5'
    FEE_TOKEN = '0x73a210637f6F6B7005512677Ba6B3C96bb4AA44B'
    FEE_ADMIN = '0x6c0d6Fba3bcdb224278474E8d524F19c6BB55850'
    EMERGENCY_RETURN = '0x6c0d6Fba3bcdb224278474E8d524F19c6BB55850'
    USDC = '0x2A3684e9Dc20B857375EA04235F2F7edBe818FA7'
    START_TIME = 1642811506

    admin = accounts.load('dev-1')
    auth = {'from': admin}
    distributor = FeeDistributor.deploy(VEMOBI_ADDRESS, START_TIME, FEE_TOKEN, FEE_ADMIN, EMERGENCY_RETURN, auth)
    proxy = PoolProxy.deploy(POOL_PROXY_OWNER, POOL_EMERGENCY_OWNER, auth)

    setBurner = proxy.set_burner(USDC, MOBIUS_BASE_BURNER, auth)

    print('Burner set at: {setBurner}')
    print('Distributor: {distributor.address}')
    print('Proxy: {proxy.address}')


    
    
    
# ##############################################################################################
# # Testing Purposes Only
# ##############################################################################################

# STAKING_ADDRESSES = ['0x04B7e6ccDE22Ca49dF72BEA1e49F83E58Bf7f59C', '0x6911c4a315Ca6D4E398756a8a9F55E1309539AA2', ]
# def fund_rewards():
    