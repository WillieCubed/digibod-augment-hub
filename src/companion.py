"""Classes for connecting to and sending data to Digibod Companion Devices."""

import bluetooth

from threading import Thread
from bluetooth import BluetoothSocket, BluetoothError
from models import SensorSnapshot

class CompanionDeviceBridge(Thread):
    """A manager for connecting to external monitoring device.

    This manager uses Bluetooth to connect to establish a connection with a
    Digibod Companion Device.
    """

    def __init__(self):
        self._socket = BluetoothSocket(bluetooth.RFCOMM)
        self._is_connected = False

    def find_devices(self, discovery_time: int = 20) -> list:
        """Look for currently discoverable Bluetooth devices.

        Args:
            discovery_time (int): The number of seconds (20 by default) to
                discover available Bluetooth devices.

        Returns:
            A list of discoverable Bluetooth devices.
        """
        nearby_devices = bluetooth.discover_devices(
                bluetooth.RFCOMM, duration=discovery_time)
        return nearby_devices

    def connect_to_device(self, bluetooth_address: str, port: int = 1):
        """Initiate a Bluetooth connection to a Companion Device.
        
        Args:
            bluetooth_address (str): The address of the device to connect to.
            port (int): 1 by default.
        """
        try:
            self._socket.connect((bluetooth_address, port))
            self.is_connected = True
        except BluetoothError as e:
            # TODO: Handle error
            print(e)

    def disconnect_from_device(self):
        self._socket.close()
        self.is_connected = False

    def send_snapshot(self, snapshot: SensorSnapshot):
        """Send a SensorSnapshot to the connected companion device.

        Args:
            snapshot (SensorSnapshot): Sensor data to send.
        """
        # TODO: Send snapshot
        self._socket.send(snapshot.to_json())

    def is_connected(self) -> bool:
        """Return True if this bridge is connected to a client device."""
        return self._is_connected

