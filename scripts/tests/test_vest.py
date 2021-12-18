from brownie import (
    VestingEscrow,
    ERC20MOBI
)

from web3.gas_strategies.time_based import fast_gas_price_strategy as gas_strategy


def main():
    token = ERC20MOBI.at("0x4B0BdD00F9b944fdaaAa3938647E3a9166B4532c")
    vesting = VestingEscrow.at("0x9ff6d45F5900D7aCBdCb6d79fFFf22C9F63dF040")

    print(vesting.vestedSupply())
    print(vesting.vestedOf("0x59A6AbC89C158ef88d5872CaB4aC3B08474883D9"))
    print(vesting.balanceOf("0x59A6AbC89C158ef88d5872CaB4aC3B08474883D9"))
    print('initial locked:', vesting.initial_locked("0x59A6AbC89C158ef88d5872CaB4aC3B08474883D9"))
    print(vesting.initial_locked_supply())
    print(vesting.unallocated_supply())
    print(vesting.token())
    print(token.balanceOf(vesting.address))

    print(token.start_epoch_time())
    print(token.rate())
    print(token.mining_epoch())
    print(token.available_supply())

    print('start:', vesting.start_time())
    print('end:', vesting.end_time())


