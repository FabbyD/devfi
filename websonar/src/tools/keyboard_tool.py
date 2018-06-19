import subprocess
import time
import pyautogui
from timer import Timer
from .tool import Tool

class KeyboardTool(Tool):
    def __init__(self):
        super().__init__()
        self.width, self.height = pyautogui.size()
        self.row_offsets = [115, 305, 330, 290]
        self.xstep = 50
        self.ystep = 30

        self.pointer_timer = Timer()
        self.pointer_tick = 0.5

    def show(self):
        subprocess.Popen(["onboard"])

    def hide(self):
        subprocess.Popen(["pkill", "onboard"])

    def move_pointer(self, x, y):
        if self.pointer_timer.duration() >= self.pointer_tick:
            pyautogui.moveTo(x, y)
            self.pointer_timer.start()

    def init_pointer(self):
        pyautogui.moveTo(115, 900)

    def click(self):
        pyautogui.click()

    def right(self):
        x, y = pyautogui.position()
        self.move_pointer(min(x+self.xstep, self.width), y)

    def left(self):
        x, y = pyautogui.position()
        self.move_pointer(max(x-self.xstep, 0), y)

    def down(self):
        x, y = pyautogui.position()
        self.move_pointer(x, min(y+self.ystep, self.height))

    def up(self):
        x, y = pyautogui.position()
        self.move_pointer(x, max(y-self.ystep, 0))

    def on_hold(self, zone):
        if zone == 0:
            self.right()
        elif zone == 2:
            self.left()

    def on_swipe_in(self):
        self.up()

    def on_swipe_out(self):
        self.down()

    def on_tap(self, zone):
        self.click()

def main():
    kb = Keyboard()
    kb.show()
    kb.init_pointer()
    for i in range(5):
        time.sleep(0.5)
        kb.right()
    kb.click()
    for i in range(3):
        time.sleep(1)
        kb.left()
    for i in range(2):
        time.sleep(1)
        kb.down()
    for i in range(1):
        time.sleep(1)
        kb.up()
    kb.hide()

if __name__ == "__main__":
    main()
