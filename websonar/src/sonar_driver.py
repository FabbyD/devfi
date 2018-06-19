import serial
from collections import deque
from observable import Observable
import sys


class SonarDriver(Observable):

    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('/dev/ttyACM0', 9600)

        # Zone definitions
        self.max_distance = 100
        self.tolerance = 5

        # Zone definitions
        self.zones = (0,10,17,40)
        self.OUT = len(self.zones) - 1
        self.tolerance = 1
        self.current_zone = self.OUT

        # Buffers
        self.values = deque()
        self.max_qsize = 1000
        self.next_zone = self.OUT
        self.next_zone_count = 1

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
        return distance > 0 and distance < self.zones[-1]

    def confirm_zone(self, zone):
        if zone == self.next_zone:
            self.next_zone_count += 1
        else:
            self.next_zone_count = 1
        self.next_zone = zone
        return self.next_zone_count >= 7

    def get_zone(self, distance):
        next_zone = self.OUT
        start = self.zones[0]
        for i in range(1,len(self.zones)):
            end = self.zones[i]
            if distance >= start and distance < end:
                next_zone = i-1
                break
            start = end
        if self.confirm_zone(next_zone):
            return next_zone
        else:
            return self.current_zone

    def enter_zone(self, zone):
        print('enter zone ' + str(zone))
        self.reset_values()
        self.current_zone = zone
        self.notify('on_enter_zone', zone)

    def out(self, distance):
        print('out ' + str(distance))
        self.current_zone = self.OUT
        self.notify('on_out', self.values)

    def register(self, distance):
        #print(distance)
        if len(self.values) > self.max_qsize:
            self.values.pop()
        self.values.appendleft(distance)
        self.notify('on_register', self.values)

    def over_tolerance(self, distance, zone):
        # check if the user is in the zone enough to change
        if zone < self.current_zone:
            boundary = self.zones[self.current_zone]
            return distance < (boundary - self.tolerance)
        elif zone > self.current_zone:
            boundary = self.zones[zone]
            return distance > (boundary + self.tolerance)
        else:
            return False

    def drive(self):
        distance = self.read_distance()
        zone = self.get_zone(distance)

        if self.current_zone != self.OUT and zone == self.OUT and self.over_tolerance(distance, zone):
            # no longer detecting something in range
            self.out(distance)
        elif zone != self.OUT and self.current_zone != zone and self.over_tolerance(distance, zone):
            # changed zone
            self.enter_zone(zone)

        if zone != self.OUT:
            # register new distance
            self.register(distance)

