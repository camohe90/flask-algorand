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
    sender = dispenser.address,
    signer = dispenser.signer,
    app_id = 1031
)


state = input("How many times would you like the LED to blink?")
response = app_client.set(state=state)
print(f"Called set on {app_client.app_id}")
print(f"with name={state}, received: {response.return_value}")


