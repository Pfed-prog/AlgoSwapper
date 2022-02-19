import os
#from dotenv import load_dotenv

from algosdk import account
from algosdk.v2client.algod import AlgodClient
from algosdk.future.transaction import ApplicationCallTxn

#load_dotenv()

#SECRET_KEY = os.getenv("API_KEY")

private_key, public_address = account.generate_account()

#algod_addr   = 'https://testnet-algorand.api.purestake.io/ps2'
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

algod_client = AlgodClient(algod_token, algod_address)
suggested_parameters = algod_client.suggested_params()
suggested_parameters.flat_fee = True
#suggested_parameters.fee = 2_000

print(algod_client.status())