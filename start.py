import os
from dotenv import load_dotenv

from algosdk import account
from algosdk.v2client.algod import AlgodClient
from algosdk.future.transaction import ApplicationCallTxn

load_dotenv()

SECRET_KEY = os.getenv("API_KEY")

private_key, public_address = account.generate_account()

algod_addr   = 'https://testnet-algorand.api.purestake.io/ps2'

algod_header = {
    'User-Agent': 'Minimal-PyTeal-SDK-Demo/0.1',
    'X-API-Key': SECRET_KEY
}

algod_client = AlgodClient(
    SECRET_KEY,
    algod_addr,
    algod_header
)

suggested_parameters = algod_client.suggested_params()
suggested_parameters.flat_fee = True
#suggested_parameters.fee = 2_000

# calls the applicaitioon with parameters
#https://py-algorand-sdk.readthedocs.io/en/latest/algosdk/future/transaction.html#algosdk.future.transaction.ApplicationCallTxn
txn1 = ApplicationCallTxn(
    private_key,
    suggested_parameters,
    70171358, # index (int) – index of the application to call; 0 if creating a new application
    None,
    app_args=[str.encode("add_liquidity"), str.encode("69768909")], #app_args (list[bytes], optional) – list of arguments to the application, each argument itself a buf
    foreign_assets=[69768909] #foreign_assets (list[int], optional) – list of assets involved in call
)
