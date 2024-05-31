import os
import time

import algokit_utils
import serial.tools.list_ports
from algokit_utils.beta.algorand_client import (
    AlgorandClient,
)
from dotenv import load_dotenv
from flask import Flask, render_template, request

from smart_contracts.artifacts.arduino_algorand.client import ArduinoAlgorandClient

app = Flask(__name__)

data_recorded = []

load_dotenv()
PASSPHRASE = os.environ.get("PASSPHRASE")

print("--------------------------------------------")
print("Processing account...")

algorand = AlgorandClient.test_net()
account = algokit_utils.get_account_from_mnemonic(PASSPHRASE)

app_client = ArduinoAlgorandClient(
    algod_client = algorand.client.algod,
    sender = account.address,
    signer= account.signer,
    app_id = 659435122
)

@app.route('/')
def index():
    return render_template('index.html', message=None, data= data_recorded)

@app.route('/read', methods=['POST'])
def read():

    response = app_client.read_total()
    print(f"Called read on {app_client.app_id}")
    message = f"the state received is: {response.return_value}"
    print(message)

    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portsList = []
    
    serialInst.baudrate = 115200
    serialInst.port = "/dev/ttyACM0"
    serialInst.open()
    print("Ready to send data to Arduino")
    time.sleep(2)
    response = str(response.return_value)
    command_sent = response.encode('utf-8')
    serialInst.write(command_sent)

    return render_template('index.html', message=message, data= data_recorded)

@app.route('/write', methods=['POST'])
def write():
    
    state = int(request.form["state"])
    response = app_client.set(state=state)
    tx_id = response.tx_id
    print(f"Called set on {app_client.app_id}")
    data_recorded.append((tx_id,state))

    return render_template('index.html', message=None,data= data_recorded)


if __name__ == '__main__':
    app.run(debug=True)
