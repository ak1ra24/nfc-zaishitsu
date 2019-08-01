# coding utf-8
from __future__ import print_function
from ctypes import *
import pprint
import slackweb
from time import sleep
import requests
import json
import nfc

def post_idm(idm):
    url = "Google App Scripts URL"
    method = "POST"
    headers = {"Content-Type" : "application/json"}

    obj = {"idm": idm}
    json_data = json.dumps(obj).encode("utf-8")

    response = requests.post(url, json_data, headers)
    pprint.pprint(response)

def connected(tag):
    tag = str(tag)
    idm = tag.split("ID=")[1]
    print(idm)
    post_idm(idm)
    return idm


while True:
    clf = nfc.ContactlessFrontend('usb')
    clf.connect(rdwr={'on-connect': connected}) # now touch a tag
    clf.close()
