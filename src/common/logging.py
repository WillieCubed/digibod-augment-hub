"""Utilities to log data to standard output."""

class DigibodHubLogger:
    """The primary logging utility for the Digibod Augment Hub.
    
    Every message has an associated priority:
        0 - Verbose: For when you're desperate to find some certain information
        1 - Debug (Default): For information that might be useful in debugging
        2 - Warning: For Hub conditions that are unusual but won't impact use
        3 - Error: For completely unexpected exceptions or Hub conditions
    """

    def __init__(self, logging_threshold: int = 1):
        """Create a new DigibodHubLogger with a desired log threshold.
        
        If no logging_threshold is specified, a threshold of 1 will be used.
        """
        self._threshold = logging_threshold

    def set_logging_threshold(self, threshold: int):
        """Set the minimum log priority before messages are displayed on stdout. 

        Args:
            threshold (int): The new minimum log priority.
        """
        self._threshold = threshold

    def log(self, level: int = 1, message: str, *args):
        """Print the given message to stdout.
        
        In order for a message to be displayed, its priority must be greater
        than or equal to the current logging_threshold.

        Args:
            level (int): The priority of the message, debug by default.
            message (str): The message to log, supporting string templates.
            *args: Any string parameters to be formatted into message.
        """
        if level >= self._threshold:
            print(message, args)
        