import requests as http

from client.constants import *


def rest_response(rv):
    return rv.json() if rv.status_code == 200 else rv.text


def callback_response(rv):
    return rv.status_code, rv.text


def send_rest_message(message):
    rv = http.post(
        url=HOST+REST_MESSAGE_URL,
        json={
            "sender": SENDER_ID,
            "message": message
        }
    )
    return rest_response(rv)


def send_callback_message(message):
    rv = http.post(
        url=HOST+CALLBACK_MESSAGE_URL,
        json={
            "sender": SENDER_ID,
            "message": message
        }
    )
    return callback_response(rv)


def status():
    rv = http.get(
        url=HOST + STATUS_URL
    )
    return get_response(rv)


def parse(text):
    rv = http.post(
        url=HOST + PARSE_URL,
        json={
            'text': text
        }
    )
    return get_response(rv)
