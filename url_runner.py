import requests
import json

session = requests.session()

def get(url, query_data=None, headers=None, return_json=False, keep_alive=True):
    if keep_alive:
        res = session.get(url, params=query_data, headers=headers)
    else:
        res = requests.get(url, params=query_data, headers=headers)

    if return_json is True:
        return res.json()
    else:
        return res.text

def post(url, data=None, headers=None, return_json=False, keep_alive=True):
    if keep_alive:
        res = requests.post(url, data=json.dumps(data), headers=headers)
    else:
        res = session.post(url, data=json.dumps(data), headers=headers)

    if return_json is True:
        return res.json()
    else:
        return res.text

def put(url, data=None, headers=None, return_json=False, keep_alive=True):
    if keep_alive:
        res = requests.put(url, data=json.dumps(data), headers=headers)
    else:
        res = session.put(url, data=json.dumps(data), headers=headers)

    if return_json is True:
        return res.json()
    else:
        return res.text

def delete(url, data=None, headers=None, return_json=False, keep_alive=True):
    if keep_alive:
        res = requests.delete(url, data=json.dumps(data), headers=headers)
    else:
        res = session.delete(url, data=json.dumps(data), headers=headers)

    if return_json is True:
        return res.json()
    else:
        return res.text