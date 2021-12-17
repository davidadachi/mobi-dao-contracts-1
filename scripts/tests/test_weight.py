from brownie import (
    GaugeController,
)

from web3.gas_strategies.time_based import fast_gas_price_strategy as gas_strategy

def main():
    gc = GaugeController.at('0x7530E03056D3a8eD0323e61091ea2f17a1aC5C25')

    ousdce = gc.get_gauge_weight('0xdAA2ab880b7f3D5697e6F85e63c28b9120AA9E07')
    ausdcs = gc.get_gauge_weight('0x27D9Bfa5F864862BeDC23cFab7e00b6b94488CC6')
    ousdcp = gc.get_gauge_weight('0x52517feb1Fc6141d5CF6718111C7Cc0FD764fA5d')
    btc = gc.get_gauge_weight('0x1A8938a37093d34581B21bAd2AE7DC1c19150C05')
    eth = gc.get_gauge_weight('0xD38e76E17E66b562B61c149Ca0EE53CEa1145733')
    usdtm = gc.get_gauge_weight('0xe2d6095685248F38Ae9fef1b360D772b78Ea19D1')
    usdcm = gc.get_gauge_weight('0xd1B3C05FE24bda6F52e704daf1ACBa8c440d8573')
    total = (ousdce + ausdcs + ousdcp + btc + eth + usdtm + usdcm)
    print(ousdce / total)
    print(gc.gauge_relative_weight('0xdAA2ab880b7f3D5697e6F85e63c28b9120AA9E07', 1633544322))
    print(ausdcs/ total)
    print(btc / total)
    print(eth / total)
    print(ousdcp / total)
    print(usdtm / total)
    print(usdcm / total)
    print(total)
    print(gc.get_total_weight())
