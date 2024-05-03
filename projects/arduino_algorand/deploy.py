from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    PayParams
)

from smart_contracts.artifacts.arduino_algorand.client import ArduinoAlgorandClient

algorand = AlgorandClient.default_local_net()
dispenser = algorand.account.dispenser()
creator = algorand.account.random()
print(dispenser.address)

algorand.send.payment(
    PayParams(
        sender = dispenser.address,
        receiver = creator.address,
        amount = 10_000_00
    )
)

app_client = ArduinoAlgorandClient(
    algod_client = algorand.client.algod,
    sender = creator.address,
    signer = creator.signer
)

result = app_client.create_bare()

print(result)

state = "ON"
response = app_client.set(state=state)
print(f"Called set on {app_client.app_id}")
print(f"with name={state}, received: {response.return_value}")


