import serial
from gesture_detector import GestureDetector

class SonarGestureDetector(GestureDetector):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('/dev/ttyACM0', 9600)

        self.dist_actions = [
            ((0,10), self.test1),
            ((10,20), self.test2),
            ((20,30), self.test3)
        ]

    def read_distance(self):
        try:
            line = self.ser.readline()
            distance = line.decode("utf-8").strip()
            return int(distance)
        except UnicodeDecodeError as e:
            return -1
        except ValueError as e:
            return -1

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')

    def test3(self):
        print('test3')

    def detect(self):
        distance = self.read_distance()
        print(distance)
        for action in self.dist_actions:
            start, end = action[0]
            action = action[1]
            if distance > start and distance < end:
                action()

