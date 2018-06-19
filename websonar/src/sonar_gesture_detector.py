from timer import Timer
from gesture_detector import GestureDetector

class SonarGestureDetector(GestureDetector):
    def __init__(self):
        super().__init__()

        self.last_zones = []

        # Time limits
        self.hold_time = 1

        # Timers
        self.in_timer = None
        self.in_zone_timer = None

    @property
    def last_zone(self):
        return self.last_zones[-1]

    def reset(self):
        self.in_timer = None
        self.in_zone_timer = None
        self.last_zones = []

    def on_enter_zone(self, zone):
        if not self.in_timer:
            self.in_timer = Timer()
        if not self.in_zone_timer:
            self.in_zone_timer = Timer()

        self.in_zone_timer.start()
        self.last_zones.append(zone)

    def on_out(self, distance):
        if self.test_tap():
            self.tap()
        elif self.test_swipe_in():
            self.swipe_in()
        elif self.test_swipe_out():
            self.swipe_out()
        elif self.test_wiggle():
            self.wiggle()
        self.reset()

    def on_register(self, distances):
        if self.test_hold():
            self.hold()

    def test_tap(self):
        dur = self.in_timer.duration()
        return len(self.last_zones) == 1 and dur < self.hold_time

    def test_hold(self):
        return self.in_zone_timer and self.in_zone_timer.duration() >= self.hold_time

    def test_swipe_in(self):
        return self.last_zones == [2,1,0]

    def test_swipe_out(self):
        return self.last_zones == [0,1,2]

    def test_wiggle(self):
        return self.last_zones == [0,1,0]

    def tap(self):
        self.notify('on_tap', self.last_zone)

    def hold(self):
        self.notify('on_hold', self.last_zone)

    def swipe_in(self):
        self.notify('on_swipe_in')

    def swipe_out(self):
        self.notify('on_swipe_out')

    def wiggle(self):
        print('wiggle')
        self.notify('on_wiggle')

