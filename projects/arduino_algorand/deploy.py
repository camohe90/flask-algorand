from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    PayParams
)

from dotenv import load_dotenv
import os
import algokit_utils 
    
from smart_contracts.artifacts.arduino_algorand.client import ArduinoAlgorandClient

load_dotenv()
PASSPHRASE = os.environ.get("PASSPHRASE")

print("--------------------------------------------")
print("Processing account...")

algorand = AlgorandClient.test_net()
account = algokit_utils.get_account_from_mnemonic(PASSPHRASE)


app_client = ArduinoAlgorandClient(
    algod_client = algorand.client.algod,
    sender = account.address,
    signer= account.signer
)

result = app_client.create_bare()

print(result)

state = 5
response = app_client.set(state=state)
print(f"Called set on {app_client.app_id}")
print(f"with name={state}, received: {response.return_value}") 


