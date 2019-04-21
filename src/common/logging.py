"""Utilities to log data to standard output."""

from datetime import datetime

PRIORITY_NAME_MAPPINGS = {
    0: 'Verbose',
    1: 'Debug',
    2: 'Warning',
    3: 'Error'
}

DEFAULT_LOG_FILENAME_FORMAT = '%Y-%m-%dT%H%z'
DEFAULT_LOG_MESSAGE_FORMAT = '[{priority}] [{timestamp}]: {message}'


class InvalidLogPriorityError(Exception):
    """Raised when a DigibodHubLogger tries to log with an invalid priority.

    See the DigibodHubLogger for a list of valid priorities.
    """


class DigibodHubLogger:
    """The primary logging utility for the Digibod Augment Hub.

    Every message has an associated priority:
        0 - Verbose: For when you're desperate to find some certain information
        1 - Debug (Default): For information that might be useful in debugging
        2 - Warning: For Hub conditions that are unusual but won't impact use
        3 - Error: For completely unexpected exceptions or Hub conditions
    """

    def __init__(self, logging_threshold: int = 1, output_to_file: bool = True,
                 log_filename_format: str = DEFAULT_LOG_FILENAME_FORMAT,
                 log_message_format: str = DEFAULT_LOG_MESSAGE_FORMAT):
        """Create a new DigibodHubLogger with a desired log threshold.

        If no logging_threshold is specified, a threshold of 1 will be used.
        """
        self._threshold = logging_threshold
        self.should_output_to_file = output_to_file
        self._log_filename_format = log_filename_format
        self._log_message_format = log_message_format

    def set_logging_threshold(self, threshold: int):
        """Set the minimum log priority before messages are displayed on stdout. 

        Args:
            threshold (int): The new minimum log priority.
        """
        self._threshold = threshold

    @staticmethod
    def map_priority_to_name(priority: int):
        if priority < 0 or priority > 3:
            raise InvalidLogPriorityError(
                '{} is not a valid log priority.'.format(priority))
        return PRIORITY_NAME_MAPPINGS[priority]

    def log(self, level: int = 1, message: str, *args):
        """Print the given message to stdout.

        In order for a message to be displayed, its priority must be greater
        than or equal to the current logging_threshold.

        If output_to_file is True, all messages and their priorities will be
        logged to a file.

        Args:
            level (int): The priority of the message, debug by default.
            message (str): The message to log, supporting string templates.
            *args: Any string parameters to be formatted into message.
        """
        if level >= self._threshold:
            print(message, args)
        if self.should_output_to_file:
            # TODO: Put logs in {root_directory}/logs
            filename = 'logs/{}.txt'.format(
                datetime.strftime(self._log_filename_format))
            with open(filename, 'w+') as f:
                line_content = self._log_message_format.format(
                    priority=self.map_priority_to_name(level),
                    timestamp=timestamp, message=message)
                f.write(line_content)
                # TODO: Handle logging on multiple threads.
