import json

from brownie import (
    ERC20MOBI,
    GaugeController,
    LiquidityGaugeV3,
    LiquidityGaugeReward,
    Minter,
    PoolProxy,
    VotingEscrow,
    ZERO_ADDRESS,
    accounts,
    history,
    network
)
network.gas_limit(8000000)
STAKE = 'a694fc3a'
WITHDRAW = '2e1a7d4d'
REWARD = '3d18b912'
FUNC_SIGNATURES = '0x' + STAKE + WITHDRAW + REWARD + '0000000000000000000000000000000000000000'
GAUGE_ADDRESSES = ['0x2459BDb59a3BF6Ab6C412Ac0b220e7CDA1D4ea26']
STAKING_ADDRESSES = ['0xe8B286649713447D8d5fBeBC28c731830d19B6C9']
REWARDS_TOKENS_ADDR = ['0x00400fcbf0816bebb94654259de7273f4a05c762', '0x17700282592D6917F6A73D0bF8AcCf4D578c131e']

def main():
    numTokens = len(REWARDS_TOKENS_ADDR)
    if numTokens > 8:
        print("Too many tokens! Aborting")
        return
    if numTokens == 0:
        print("No rewards tokens specified, aborting")
        return
    admin = accounts.load('dev-1')
    externalRewards = REWARDS_TOKENS_ADDR + [ZERO_ADDRESS] * (8 - numTokens)
    for (GAUGE_ADDRESS, STAKING_ADDRESS) in zip(GAUGE_ADDRESSES, STAKING_ADDRESSES):
        gauge = LiquidityGaugeV3.at(GAUGE_ADDRESS)
        gauge.set_rewards(STAKING_ADDRESS, FUNC_SIGNATURES, externalRewards, {'from': admin})
    
    
# ##############################################################################################
# # Testing Purposes Only
# ##############################################################################################

# STAKING_ADDRESSES = ['0x04B7e6ccDE22Ca49dF72BEA1e49F83E58Bf7f59C', '0x6911c4a315Ca6D4E398756a8a9F55E1309539AA2', ]
# def fund_rewards():
    