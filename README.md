# AlgorandDeFi

On Ubuntu 20.04

```bash

python3 -m virtualenv project
source project/bin/activate
pip3 install -r requirements.txt
```

### Example of Queries

Include API token in the headers

curl -X GET "https://testnet-algorand.api.purestake.io/ps2/v2/applications/70171358"

curl -X GET "https://testnet-algorand.api.purestake.io/ps2/v2/applications/70171358?include-all=True"

curl -X GET "https://testnet-algorand.api.purestake.io/idx2/v2/accounts"

curl -X GET "https://testnet-algorand.api.purestake.io/idx2/v2/accounts?asset-id=43994923"


### Liquidity Pools

https://academy.binance.com/en/articles/what-are-liquidity-pools-in-defi

Liquidity pools are the backbone of many decentralized exchanges (DEX), such as Uniswap. Users called liquidity providers (LP) add an equal value of two tokens in a pool to create a market. In exchange for providing their funds, they earn trading fees from the trades that happen in their pool, proportional to their share of the total liquidity.
As anyone can be a liquidity provider, AMMs have made market making more accessible.

