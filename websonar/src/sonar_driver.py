import serial
from collections import deque

class SonarDriver():
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('/dev/ttyACM0', 9600)

        # Zone definitions
        self.max_distance = 100
        self.tolerance = 5

        # Buffers
        self.values = deque()
        self.max_qsize = 1000

        # Indicates if something is in front of the sonar
        self.detecting = False

        # Event listeners
        self.on_up = []
        self.on_down = []
        self.on_register = []

    def reset_values(self):
        self.values.clear()

    def read_distance(self):
        try:
            line = self.ser.readline()
            distance = line.decode("utf-8").strip()
            return int(distance)
        except UnicodeDecodeError as e:
            return -1
        except ValueError as e:
            return -1

    def in_range(self, distance):
        return distance > 0 and distance < self.max_distance

    def up(self):
        self.detecting = False
        for callback in self.on_up:
            callback()

    def down(self):
        self.reset_values()
        self.detecting = True
        for callback in self.on_down:
            callback()

    def register(self, distance):
        if len(self.values) > self.max_qsize:
            self.values.pop()
        self.values.appendleft(distance)
        for callback in self.on_register:
            callback(distance)

    def drive(self):
        distance = self.read_distance()
        if self.detecting and not self.in_range(distance):
            self.up()
        elif not self.detecting and self.in_range(distance):
            self.down()
        if self.detecting:
            self.register(distance)

