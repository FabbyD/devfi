import serial
from collection import deque
from timer import Timer
from gesture_detector import GestureDetector

class SonarGestureDetector(GestureDetector):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        self.tests = [ getattr(self, test) for test in dir(self) if test.startswith('test_') and callable(getattr(self, test)) ]
        
        # Zone definitions
        self.max_short = 20
        self.max_mid   = 40
        self.max_far   = 100
        self.tolerance = 5

        # Timer
        self.timer = None

        # Buffers
        self.values = deque()
        self.max_qsize = 1000

        # Indicates if something is in front of the sonar
        self.detecting = False

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
        return distance > 0 and distance < self.max_far
    
    def up(self):
        self.detecting = False

    def down(self):
        self.timer = Timer()
        self.reset_values()
        self.detecting = True

    def register(self, distance):
        if len(q) > max_qsize:
            q.pop()
        q.appendleft(distance)

    def reset_values(self):
        self.values.clear()

    def process_distance(self):
        distance = self.read_distance()

        if self.detecting and not self.in_range(distance):
            self.up()
        elif not self.detecting and self.in_range(distance):
            self.down()

        self.register(distance)

    def detect(self):
        self.process_distance()

    def test_close_tap(self):
        
        print(self.test_close_tap.__name__)

    def test_far_tap(self):
        #print(self.test_far_tap.__name__)
        pass

    def test_close_hold(self):
        #print(self.test_close_hold.__name__)
        pass

    def test_far_hold(self):
        #print(self.test_far_hold.__name__)
        pass


