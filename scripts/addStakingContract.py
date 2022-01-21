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
GAUGE_ADDRESSES = ['0x107F94409746E8c8E6eFF139A100D17D9ca7FdfE'] # ['0xE7195E651Cc47853f0054d85c8ADFc79D532929f', '0xD0d57a6689188F854F996BEAE0Cb1949FDB5FF86', '0xCAEd243de23264Bdd8297c6eECcF320846eee18A']
STAKING_ADDRESSES = ['0x84282839bE40c037fbcc7867320c386E83CFDB62'] # ['0xca54a6cC4E9C7D1EEEA044D3e7Bd7FE145b59bEf', '0x64d996b71a5867886814bC9d45d2822Bde027122', '0xC99cDa8FFd6fb7bC31d56932713a447cd48A6Bff']
REWARDS_TOKENS_ADDR = ['0x471EcE3750Da237f93B8E339c536989b8978a438'] # ['0x00400fcbf0816bebb94654259de7273f4a05c762', '0x17700282592D6917F6A73D0bF8AcCf4D578c131e']

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
    