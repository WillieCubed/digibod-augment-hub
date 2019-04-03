#!/usr/bin/env python3

from smbus import SMBus
from threading import Thread
import time


I2C_SLAVE_ADDRESS = 0x8

bus = SMBus(1)


class SensorSnapshot:
    """A container for sensor values obtained at a given moment."""
    def __init__(self, x: float, y: float, z: float, flex: float):
    self.x = x
    self.y = y
    self.z = z
    self.flex = flex


def send_number(value):
    bus.write_byte(I2C_SLAVE_ADDRESS, value)
    
    return -1


def read_value():
    number = bus.read_byte(I2C_SLAVE_ADDRESS)
    return number


def on_i2c_receive():

    print(
    pass


def monitor_augment_controllers():
    while True:
        pass


def watch_assistant():
    while True:
        pass


def main():
    augment_monitor_thread = Thread(target=monitor_augment_controllers, args=[])
    assistant_thread = Thread(target=watch_assistant, args=[])
    augment_monitor_thread.start()
    augment_monitor_thread.join()
    assistant_thread.start()
    assistant_thread.join()


if __name__ is '__main__':
    main()
