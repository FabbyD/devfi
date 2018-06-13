from timer import Timer
from gesture_detector import GestureDetector

class SonarGestureDetector(GestureDetector):
    def __init__(self):
        super().__init__()
    
        self.last_zones = []

        # Timers
        self.in_timer = None
        self.zone_timers = {}

    def on_enter_zone(self, zone):
        if not self.in_timer:
            self.in_timer = Timer()
        if zone not in self.zone_timers:
            self.zone_timers[zone] = Timer()
        self.zone_timers[zone].start()
        self.last_zones.append(zone)
        
    def on_out(self, distance):
        dur = self.in_timer.duration()
        if len(self.last_zones) == 1 and dur < 1:
            print('tap in zone ' + str(self.last_zones[-1]))

        self.last_zones = []
        self.in_timer = None

    def on_register(self, distances):
        pass

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


