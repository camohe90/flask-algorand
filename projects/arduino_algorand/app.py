from flask import Flask, render_template, request
from algokit_utils.beta.algorand_client import (
    AlgorandClient,
)

from smart_contracts.artifacts.arduino_algorand.client import ArduinoAlgorandClient
import serial.tools.list_ports
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message=None)

@app.route('/read', methods=['POST'])
def read():
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
    message = f"the state received is: {response.return_value}"

    print(message)
    

    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portsList = []

    for one in ports:
        portsList.append(str(one))
        print("Port to be used" + str(one))

    serialInst.baudrate = 115200
    serialInst.port = "/dev/ttyACM0"
    serialInst.open()
    print("Ready to send data to Arduino")
    time.sleep(3)
    response = response.return_value
    command_sent = response.encode('utf-8')
    serialInst.write(command_sent)

    return render_template('index.html', message=message)

@app.route('/write', methods=['POST'])
def write():
    algorand = AlgorandClient.default_local_net()
    dispenser = algorand.account.dispenser()
    app_client = ArduinoAlgorandClient(
        algod_client = algorand.client.algod,
        sender = dispenser.address,
        signer = dispenser.signer,
        app_id = 1031
    )
    
    state = request.form["state"]
    print(state)
    response = app_client.set(state=state)
    print(f"Called set on {app_client.app_id}")
    message = f"sent blink={state}, received: {response.return_value}"


    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
