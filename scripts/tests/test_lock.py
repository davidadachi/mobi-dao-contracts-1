from brownie import (
    VotingEscrow,
    ERC20MOBI,
    accounts,
    network
)

# from web3.gas_strategies.time_based import fast_gas_price_strategy as gas_strategy

people = [
  '0xc59cd8251ABb06C307819D0beb95546CB4de172f',
  '0xB811Ad5C016c37d9f40dffA8fc360F9B3fFC0d2A',
  '0xE35E97438Fd16593e285546260C8585dea7909Dd'
]


def main():
  network.gas_limit(8000000)
  admin = accounts.load("kyle_personal")
  # token = ERC20MOBI.at("0x17a139f275102bBaB5BcbF1c4b7143F08B635EA2")
  voting = VotingEscrow.at("0xE9d0375cd6fC027A1a0eC39BB4c9928E5aBec27e")
  token = ERC20MOBI.at(voting.token())
  # token.approve(voting.address, 2**256-1, {"from": admin})
  # voting.create_lock(6600000000000000000000000, 1765026690, {"from": admin})
  # for p in people:
  token.transfer('0x7DFAFF53284Aac673D48EA3fA1D70844b7F62E24', 100 * 10 ** 24, {'from': admin})
  # print(voting.balanceOfAt("0x59A6AbC89C158ef88d5872CaB4aC3B08474883D9", 10369880))
  # print(token.balanceOf("0x59A6AbC89C158ef88d5872CaB4aC3B08474883D9"))
  # print(voting.token())
    