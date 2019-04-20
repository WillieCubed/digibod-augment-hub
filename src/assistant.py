"""Classes used to listen to Assistant input and respond to queries."""

from threading import Thread

class AssistantCommandMonitor(Thread):
    """A thread that monitors a microphone for Google Assistant queries.

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
