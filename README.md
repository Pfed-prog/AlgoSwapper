# AlgorandDeFi

On Ubuntu 20.04

```bash
python3 -m virtualenv project
source project/bin/activate
pip3 install -r requirements.txt
```

### Example of Queries

Include API token in the headers:

```
curl -X GET "https://testnet-algorand.api.purestake.io/ps2/v2/applications/70171358"

curl -X GET "https://testnet-algorand.api.purestake.io/ps2/v2/applications/70171358?include-all=True"

curl -X GET "https://testnet-algorand.api.purestake.io/idx2/v2/accounts"

curl -X GET "https://testnet-algorand.api.purestake.io/idx2/v2/accounts?asset-id=43994923"
```

### Liquidity Pools

https://academy.binance.com/en/articles/what-are-liquidity-pools-in-defi

Liquidity pools are the backbone of many decentralized exchanges (DEX), such as Uniswap. Users called liquidity providers (LP) add an equal value of two tokens in a pool to create a market. In exchange for providing their funds, they earn trading fees from the trades that happen in their pool, proportional to their share of the total liquidity.
As anyone can be a liquidity provider, AMMs have made market making more accessible.

## Sandbox
All of the examples were developed on a local network with local addresses. To duplicate the results and run the examples on your own, you will first need to make sure that you have an Algorand node running and `goal` set up with at least three accounts. 

repository structure:
|__Sandbox
|__AlgoSwapper

```
cd sandbox
```

to start an instance:
```
./sandbox up
```
to list accounts:
```
./sandbox goal account list
```


Example account: DJ24DOMQY6GWI4NY6CFSQFNWREIQYTN6ABQU7DTIBY5KTGGENF3F2RSMJU

To access the TEAL contracts in the node, we have to copy them into our sandbox.

```
./sandbox copyTo ../AlgoSwapper/counter/counter.teal
./sandbox copyTo ../AlgoSwapper/counter/counter_clear.teal
```
### Deploy the Smart Contract

```
./sandbox goal app create --creator DJ24DOMQY6GWI4NY6CFSQFNWREIQYTN6ABQU7DTIBY5KTGGENF3F2RSMJU --global-byteslices 0 --global-ints 1 --local-byteslices 0 --local-ints 0 --approval-prog counter.teal --clear-prog counter_clear.teal
```

Logs:

```
Attempting to create app (approval size 49, hash P3JCINPYNWCX54B6OCN4HWXTLJ2ZUPORDFMBPHPJECVIZNHRS4VQ; clear size 4, hash BJATCHES5YJZJ7JITYMVLSSIQAVAWBQRVGPQUDT5AZ2QSLDSXWWA)
Issued transaction from account DJ24DOMQY6GWI4NY6CFSQFNWREIQYTN6ABQU7DTIBY5KTGGENF3F2RSMJU, txid 5ADIFLSEAB5FOTHN47FIE5KZV6VLLYOIPK5SQA4B2DBNYQXTYCIA (fee 1000)
Transaction 5ADIFLSEAB5FOTHN47FIE5KZV6VLLYOIPK5SQA4B2DBNYQXTYCIA still pending as of round 22225
Transaction 5ADIFLSEAB5FOTHN47FIE5KZV6VLLYOIPK5SQA4B2DBNYQXTYCIA still pending as of round 22226
Transaction 5ADIFLSEAB5FOTHN47FIE5KZV6VLLYOIPK5SQA4B2DBNYQXTYCIA committed in round 22227
Created app with app index 1
```

### Call the Smart Contract
```
./sandbox goal app call --from DJ24DOMQY6GWI4NY6CFSQFNWREIQYTN6ABQU7DTIBY5KTGGENF3F2RSMJU --app-id 1
```
Logs:
```
Issued transaction from account DJ24DOMQY6GWI4NY6CFSQFNWREIQYTN6ABQU7DTIBY5KTGGENF3F2RSMJU, txid 72JOG33S3DKMGQ3EOEXW26NQDRWJ7T4S2GRH2OC6Y3AH7UF5DLDA (fee 1000)
Transaction 72JOG33S3DKMGQ3EOEXW26NQDRWJ7T4S2GRH2OC6Y3AH7UF5DLDA still pending as of round 22325
Transaction 72JOG33S3DKMGQ3EOEXW26NQDRWJ7T4S2GRH2OC6Y3AH7UF5DLDA still pending as of round 22326
Transaction 72JOG33S3DKMGQ3EOEXW26NQDRWJ7T4S2GRH2OC6Y3AH7UF5DLDA committed in round 22327
```

### Read Value
```
./sandbox goal app read --global --app-id 1
```