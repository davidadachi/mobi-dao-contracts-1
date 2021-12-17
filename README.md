# curve-dao-contracts

Vyper contracts used in the [Mobius] governance and staking system.

## Overview

Mobius DAO consists of a modified instance of Compound's Governor Bravo. The Comp token is replaced with a locked voting token (veMOBI) for votes. These contracts handle the contracts for the liquid token MOBI, as well as the system of locking MOBI (veMOBI). veMOBI can then be used to direct future MOBI allocation amongst the various staking contracts, all which is handled in a decentralized manner by the token holders. 

## Testing and Development

### Dependencies

- [python3](https://www.python.org/downloads/release/python-368/) version 3.6 or greater, python3-dev
- [vyper](https://github.com/vyperlang/vyper) version [0.2.8](https://github.com/vyperlang/vyper/releases/tag/v0.2.8)
- [brownie](https://github.com/iamdefinitelyahuman/brownie) - tested with version [1.14.6](https://github.com/eth-brownie/brownie/releases/tag/v1.14.6)
- [brownie-token-tester](https://github.com/iamdefinitelyahuman/brownie-token-tester) - tested with version [0.2.2](https://github.com/iamdefinitelyahuman/brownie-token-tester/releases/tag/v0.2.2)
- [ganache-cli](https://github.com/trufflesuite/ganache-cli) - tested with version [6.12.1](https://github.com/trufflesuite/ganache-cli/releases/tag/v6.12.1)

### Setup

To get started, first create and initialize a Python [virtual environment](https://docs.python.org/3/library/venv.html). Next, clone the repo and install the developer dependencies:

```bash
git clone https://github.com/curvefi/curve-dao-contracts.git
cd curve-dao-contracts
pip install -r requirements.txt
```

### Running the Tests

The test suite is split between [unit](tests/unitary) and [integration](tests/integration) tests. To run the entire suite:

```bash
brownie test
```

To run only the unit tests or integration tests:

```bash
brownie test tests/unitary
brownie test tests/integration
```

## Deployment

See the [deployment documentation](scripts/deployment/README.md) for detailed information on how to deploy Mobius DAO.

## Audits and Security

Curve DAO contracts have been audited by Trail of Bits and Quantstamp. These audit reports are made available on the [Curve website](https://dao.curve.fi/audits).

There is also an active [bug bounty](https://www.curve.fi/bugbounty) for issues which can lead to substantial loss of money, critical bugs such as a broken live-ness condition, or irreversible loss of funds.

## Resources

You may find the following guides useful:

1. [Curve and Curve DAO Resources](https://resources.curve.fi/)
2. [How to earn and claim MOBI](https://guides.curve.fi/how-to-earn-and-claim-crv/)
3. [Voting and vote locking on Curve DAO](https://guides.curve.fi/voting-and-vote-locking-curve-dao/)

## License

This project is licensed under the [MIT](LICENSE) license.
