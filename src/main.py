#!/usr/bin/env python3
"""The primary entrypoint into monitoring Digibod components."""

import time

from threading import Thread
from smbus import SMBus
from train import DigibodTrainer


class SensorSnapshot:
    """A container for sensor values obtained at a given moment.

    Attributes:
        x (float): The horizontal axis movement
        y (float): The vertical axis movement
        z (float): The deptch axis movement
    """

    def __init__(self, x: float, y: float, z: float, flex: float):
        self.x = x
        self.y = y
        self.z = z
        self.flex = flex


class AugmentControllerMonitor(Thread):
    """A utility that interacts with Digibod Augment Controllers.

    This monitor observes and sends data to and from one or more Digibod
    Augment Controllers over I2C.
    """

    CONTROLLER_I2C_MIN_ADDRESS = 0x10
    CONTROLLER_I2C_MAX_ADDRESS = 0x15

    def __init__(self):
        super().__init__()
        self._should_stop = False
        self._bus = SMBus(1)
        self._snapshot_observers = []

    def start_monitoring(self):
        """Begin listening to Augment Controllers over I2C."""
        self.start()
        self.join()

    def add_observer(self, *args):
        """Add an observer called when sensor values are updated."""
        for observer in args:
            self._snapshot_observers.append(observer)

    def remove_observer(self, observer):
        """Remove an observer."""
        self._snapshot_observers.remove(observer)

    def run(self):
        """Continuously poll connected Augment Controllers and notify callbacks."""
        while not self._should_stop:
            for address in range(
                    CONTROLLER_I2C_MIN_ADDRESS, CONTROLLER_I2C_MAX_ADDRESS): 
                snap = self.get_snapshot(address)
                self._notify_callbacks(snap)

    def stop_monitoring(self):
        """Allow this thread to stop."""
        self._should_stop = True

    def get_snapshot(i2c_address: int) -> SensorSnapshot:
        """Fetch an Augment's sensor values."""
        snapshot = SensorSnapshot()
        return snapshot

    def _notify_observers(self, snapshot: SensorSnapshot):
        for callback in self._snapshot_observers:
            callback(snapshot)

class AssistantCommandMonitor(Thread):
    """A thread that monitors a microphone for Google Assistant queries

    TODO: Set up Google Assistant
    """

    def __init__(self):
        super().__init__()
        self._should_stop = False

    def start_monitoring(self):
        """Begin listening to assistant queries"""
        self.start()
        self.join()

    def run(self):
        while not self._should_stop:
            pass

    def stop_monitoring(self):
        """Allow this thread to stop"""
        self._should_stop = True


class LocalConnectionManager(Thread):
    """A manager for connecting to external monitoring devices.

    This manager primarily uses Bluetooth to """

    def findDevices() -> list:
        """Return a list of open Bluetooth devices."""


class APIServer(Thread):
   """A server that handles incoming HTTP requests for sensor data"""

    def start():
        """Begin listening to HTTP requests."""


class CommandInterpreter:
    """A wrapper for data collection and inference functions.

    Attributes:
        is_training (bool): True if the program is waiting for training
                            to finish
    """

    def __init__(self):
        self.is_training = False
        self._trainer = DigibodTrainer()

    def collect_data(self, millis: bool = 2000):
        """Temporarily begin collecting sensor snapshots."""

    def train(self):
        """Synchronously begin training a new model"""
        self.is_training = True
        # TODO: Begin training with trainer
        self.is_training = False

    def infer(self, snapshot_length: int = 100):
        """Briefly collect sensor values and determine taken action

        Args:
            snapshot_length (int): The amount of milliseconds
                                   used to collect data to infer the action.
        """


def main():
    """Start all Digibod Augment Hub primary functions.

    This function starts Augment Controller data monitoring as well as
     Assistant query monitoring.
    """
    augment_monitor = AugmentControllerMonitor()
    assistant_monitor = AssistantCommandMonitor()
    augment_monitor.start_monitoring()
    assistant_monitor.start_monitoring()


if __name__ == '__main__':
    main()
