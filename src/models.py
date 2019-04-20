"""All the models used to contain sensor data."""

from json import JSONEncoder

class LightSensorSnapshot:
    """A container for photoresistor data collected at a given moment.

    Attributes:
        resistance (float): The observed brightness measured in ohms. Resistance
            is inversely proportional to brightness, so the greater the
            resistance the darker the observed brightness is.
    """

    def __init__(self, resistance: float):
        self.resistance = resistance


class FlexSensorSnapshot:
    """A container for flex sensor data collected at a given moment.

    Attributes:
        resistance (float): The resistance in ohms of the sensor
    """

    def __init__(self, resistance: float):
        self.resistance = resistance


class AccelerometerSnapshot:
    """A container for accelerometer sensor values obtained at a given moment.

    Attributes:
        x (float): The horizontal axis movement
        y (float): The vertical axis movement
        z (float): The deptch axis movement
    """

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

class SensorSnapshot:
    """A container for data for all attatched senors at a given moment.

    Attributes:
        timestamp: Time since the beginning of the UNIX epoch (milliseconds
            since 1970-01-01T00:00:00Z)
        acc_snaps (list): A list of AccelerometerSnapshots
        flex_snaps (list): A list of FlexSensorSnapshots
        light_snaps (LightSensorSnapshot): A list of LightSensorSnapshots
    """

    def __init__(self, timestamp: float, acc_snaps: list, flex_snaps: list,
            light_snaps: float):
        self.timestamp = timestamp
        self.acc_snaps = acc_snaps
        self.flex_snaps = flex_snaps

    def to_json(self) -> str:
        """Convert this SensorSnapshot into JSON form.

        Returns:
            A serialized JSON string containing all the attributes of this
            SensorSnapshot.
        """
        return JSONEncoder().encode(vars(self))