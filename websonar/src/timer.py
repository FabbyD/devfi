import time

class Timer:
    def __init__(self):
        self._start = None
        self._end = None
        self._lap = None
        self.start()

    def start(self):
        self._start = time.time()

    def stop(self):
        self._end = time.time()

    def lap(self):
        self._lap = time.time()

    def lap_duration(self):
        last_lap = self._lap or self._start
        return last_lap - time.time()

    def duration(self):
        end = self._end
        if end is None:
            end = time.time()
        return end - self._start
