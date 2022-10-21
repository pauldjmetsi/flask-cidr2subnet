import socket
import struct
from flask import Flask, request
import flask
from app_service import AppService
import json

app = Flask(__name__)
appService = AppService();


@app.route('/')
def home():
    return "App Works!!!"


@app.route('/api/tasks')
def tasks():
    return appService.get_tasks()


## Custom POST to convert subnet to cidr ##
@app.route('/api/convert-cidr', methods=['POST'])
def create_task():
    # check body is a valid json
    try: 
        request_data = request.get_json()
    except: 
        resp = flask.Response(json.dumps({'error': "Your body is not a valid json."}), 400)
        resp.headers['Content-Type']="application/json"
        return resp

    # check body has key subnet 
    if "cidr" not in request_data: 
        resp = flask.Response(json.dumps({'error': "Your body must contain key 'cidr'."}), 400)
        resp.headers['Content-Type']="application/json"
        return resp

    # covert subnet to cidr 
    try: 
        cidr_address = request_data['cidr']
        network, net_bits = cidr_address.split('/')
        host_bits = 32 - int(net_bits)
        netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
        resp = flask.Response(json.dumps({'netmask': netmask}))
        resp.headers['Content-Type']="application/json"
        return resp
    except: 
        resp = flask.Response(json.dumps({'error': "There was a problem decoding your subnet. Please provide a valid cidr address."}), 400)
        resp.headers['Content-Type']="application/json"
        return resp


@app.route('/api/task', methods=['PUT'])
def update_task():
    request_data = request.get_json()
    return appService.update_task(request_data['task'])


@app.route('/api/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    return appService.delete_task(id)

