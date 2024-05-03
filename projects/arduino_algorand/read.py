from algokit_utils.beta.algorand_client import (
    AlgorandClient,
)

from smart_contracts.artifacts.arduino_algorand.client import ArduinoAlgorandClient
import serial.tools.list_ports
import time

algorand = AlgorandClient.default_local_net()
dispenser = algorand.account.dispenser()

app_client = ArduinoAlgorandClient(
    algod_client = algorand.client.algod,
    sender = dispenser.address,
    signer = dispenser.signer,
    app_id = 1031
)


response = app_client.read_total()
print(f"Called read on {app_client.app_id}")
print(f"the state received is: {response.return_value}")


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print("Port to be used" + str(one))

#com = input("Select Com Port for Arduino #: ")

serialInst.baudrate = 115200
serialInst.port = "/dev/ttyACM0"
serialInst.open()
print("Ready to send data to Arduino")
time.sleep(3)
response = response.return_value
command_sent = response.encode('utf-8')
serialInst.write(command_sent)
  


   

