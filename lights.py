import requests

# Set the URL for the Arduino
arduino_url = "http://172.20.10.4"


def turn_on_relay():
    try:
        payload = {'relay': '1', 'state': '1'}
        requests.get(arduino_url + '/update', params=payload)
        return 'Light is ON'
    except:
        return 'Light is not connected'


def turn_off_relay():
    try:
        payload = {'relay': '1', 'state': '0'}
        requests.get(arduino_url + '/update', params=payload)
        return 'Light is OFF'
    except:
        return 'Light is not connected'
