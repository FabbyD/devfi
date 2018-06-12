from timer import Timer
from gesture_detector import GestureDetector

class SonarGestureDetector(GestureDetector):
    def __init__(self):
        super().__init__()
        self.tests = [ getattr(self, test) for test in dir(self) if test.startswith('test_') and callable(getattr(self, test)) ]
        
        # Zone definitions
        self.max_short = 20
        self.max_mid   = 40
        self.max_far   = 100
        self.tolerance = 5

        # Timer
        self.timer = None

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


