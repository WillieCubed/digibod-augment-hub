"""A web server to interact with data on this Augment Hub."""

import netifaces as ni
from flask import Flask, render_template

app = Flask(__name__)

class AugmentInfo:
    """Details about a Digibod Augment.

    Attributes:
        name (str): The user-readable name of this Augment
    """
    def __init__(self, name: str):
        self.name = name


def get_local_ip() -> str:
    """Return the IP address of this device on the local network."""
    addresses = ni.ifaddresses('wlan0')
    ip = addresses[ni.AF_INET][0]['addr']
    return ip


@app.route('/')
def home():
    """Render a page showing system status and a list of augments."""
    return render_template('index.html')


@app.route('/connect')
def manage_connections():
    """Render a page allowing the device to pair with a local device."""
    return render_template('connect.html')


@app.route('/acceptConnection/<device_id>')
def accept_connection(device_id: str):
    """Trigger a connection to a local device.
    # TODO: Show loading screen then redirect to home


    Args:
        device_id (str): The Bluetooth address to connect to
    """


@app.route('/augment/<id>')
def augment_status(id: str):
    """Render a page for monitoring the status of an augment."""
    # TODO: Get augment info and separate it into usable form
    return render_template('augment.html')

def start():
    """Start the local Flask server.

    This opens up a server using the IP address found with get_local_ip.
    """
    ip = get_local_ip()
    app.run(debug=True, host=ip)
