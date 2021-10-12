import json
from pathlib import Path
from flask import Flask, request
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_OWN_KEY'

folder = "metadata"
if not os.path.exists(folder):
    os.mkdir(folder)

policy = "POLICYID"
locked_addr = "CONTRACT"
owner_addr = "OWNER_ADDR"


@app.route('/mint', methods=['POST'])
def createjson():

    # setting status 100
    response_status = "100"
    data = request.json
    print(data)

    metadata = data['metadata']
    trx_id = data['trx_id']
    price = data['price'] * 1000000
    nft_id = metadata['id']
    quantity = metadata['quantity']

    metadata['name'] = metadata['name'].replace(' ', '')
    metadata.pop('quantity')
    metadata.pop('price')
    file_name = f'./metadata/{metadata["name"]}{nft_id}.json'
    Path("./metadata").mkdir(parents=True, exist_ok=True)
    nft = {}

    if os.path.exists(file_name):
        # NFT already exist with this name thanks
        response_status = "401"
    return {"status": response_status}


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
