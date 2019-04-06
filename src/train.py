"""Utilities used to train machine learning models."""

class DigibodSensorExample:
    """A single training example that maps sensor inputs to an output."""

    def __init__(self, sensor_values: list, name):
        pass

    def convert_to_dataframe(self):
        """Convert this example into a more usable form for training"""

    def __str__(self):
        """Return a raw sensor data representation of this example"""

class DigibodTrainer:
    """
    A classifier that can be retrained to map arbitrary fuzzy inputs
    to arbitrary outputs.
    """

    def __init__(self):
        pass

    def train(self):
        """Begin training a model using this trainer's examples"""

    def add_example(self, example: DigibodSensorExample):
        """Add an example to the next training batch"""

    def reset(self):
        """Remove all training examples and their mappings"""
