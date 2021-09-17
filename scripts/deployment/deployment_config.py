"""
Deployment Configuration file
=============================
This script holds customizeable / sensetive values related to the DAO deployment scripts.
See `README.md` in this directory for more information on how deployment works.
"""

from brownie import rpc, web3, accounts
from web3 import middleware
from web3.gas_strategies.time_based import fast_gas_price_strategy as gas_strategy

LP_VESTING_JSON = "early-users-mobius.json"
DEPLOYMENTS_JSON = "deployments.json"
REQUIRED_CONFIRMATIONS = 3

# Aragon agent address - set after the Aragon DAO is deployed
ARAGON_AGENT = None

YEAR = 86400 * 365 

DECIMAL = 10 ** 18

# `VestingEscrow` contracts to be deployed
STANDARD_ESCROWS = [
    {  # Founder
        "duration": 1 * YEAR,
        "can_disable": False,
        "admin": "0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c",
        "recipients": {
            "0x622d8A2DEe6aaf4f00Cc1bC9e74509ce7a18FF7D": 100_000_000 * DECIMAL, # Dahlia multisig
            "0xB811Ad5C016c37d9f40dffA8fc360F9B3fFC0d2A": 30_000_000 * DECIMAL, # Dylan
            "0x08b6601066b441510b7546c5412e3AbB8e3a4434": 20_000_000 * DECIMAL, # 0xHuman
            "0xf617a242B862799D547044f28cC2dB3124c64817": 50_000_000 * DECIMAL, # OpenCelo multisig
        },
    },
    {  # Investors
        "duration": 1 * YEAR,
        "can_disable": False,
        "admin": "0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c",
        "recipients": {
            "0x197d9C534366B77Af02c4Bf5412ECFe69A041622": 18_000_000 * DECIMAL, # Flori
        },
    },
    {  # Advisors and partners with known addresses
        "duration": 1 * YEAR,
        "can_disable": False,
        "admin": "0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c",  # Mobius
        "recipients": {
            "0xf773C3F00F119985e98cfdF33BB20dcb778fe677": 10_000_000 * DECIMAL, # Alex Witt
            "0xF2d3af8181600faa5C1BEE7398fcE1277a3B049A":  2_000_000 * DECIMAL # Moss
        },
    },
    # {  # Employees
    #     "duration": 2 * YEAR,
    #     "can_disable": True,
    #     "admin": "0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c",  # Mobius
    #     "recipients": {
    #         "0xBe286d574b1Ea46f54955Bd856821f84DFd20b2e": 30_303030302325581395348837,
    #         "0x825AA4A8F72ab6AE0C55D840759711bBe00a9304": 15_151515151162790697674418,
    #         "0x94dFcE828c3DAaF6492f1B6F66f9a1825254D24B": 7_878787878604651162790697,
    #         "0x6632EdA2685EABFb7B3B45669CFa5441349485d3": 3_030303030232558139534883,
    #         "0x0Ac51a4E170bF73e7ac54283E61C9717EAc2A241": 7_878787878604651162790697,
    #     },
    # },
]

# `VestingEscrowFactory` contracts to be deployed
FACTORY_ESCROWS = [
    # {  # Advisors with unknown addresses
    #     "admin": "0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c",  # Mobius
    #     "amount": 14_016820183895092715910255,
    # },
    # {  # Rest of employee coins
    #     "admin": "0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c",  # Mobius
    #     "amount": 26_666666666046511627906979,
    # },
    # {  # Community fund
    #     "admin": "0x16E319d8dAFeF25AAcec0dF0f1E349819D36993c",  # set to DAO  XXX
    #     "amount": 151_515151511627906976744186,
    # },
]


def get_live_admin():
    # Admin and funding admin account objects used for in a live environment
    # May be created via accounts.load(name) or accounts.add(privkey)
    # https://eth-brownie.readthedocs.io/en/stable/account-management.html
    admin = accounts.load('dev-1')  #
    funding_admins = [admin, admin, admin, admin]
    return admin, funding_admins


if not rpc.is_active():
    # logic that only executes in a live environment
    web3.eth.setGasPriceStrategy(gas_strategy)
    web3.middleware_onion.add(middleware.time_based_cache_middleware)
    web3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
    web3.middleware_onion.add(middleware.simple_cache_middleware)
