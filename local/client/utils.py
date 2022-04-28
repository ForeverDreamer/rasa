import requests as http

from client.constants import *


def get_response(rv):
    return rv.json() if rv.status_code == 200 else rv.text


def send_message(message):
    rv = http.post(
        url=HOST+SEND_MESSAGE_URL,
        json={
            "sender": SENDER_ID,
            "message": message
        }
    )
    return get_response(rv)


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
