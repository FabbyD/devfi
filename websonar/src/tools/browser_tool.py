import pyautogui
from timer import Timer
from .tool import Tool

class BrowserTool(Tool):

    def __init__(self):
        super().__init__()
        self.scroll_timer = None
        self.scroll_interval = 0.5
        self.last_hold_zone = -1

    def on_tap(self, zone):
        if zone == 0:
            self.enter()
        elif zone == 1:
            self.shift_tab()

    def on_hold(self, zone):
        if self.scroll_timer is None:
            self.scroll_timer = Timer()
        elif zone != self.last_hold_zone:
            self.scroll_timer.start()
        elif self.scroll_timer.duration() > self.scroll_interval:
            if zone == 0:
                self.scroll_down()
            elif zone == 1:
                self.tab()
            elif zone == 2:
                self.scroll_up()
            self.scroll_timer.start()
        self.last_hold_zone = zone

    def on_swipe_in(self):
        self.forward()

    def on_swipe_out(self):
        self.back()

    def tab(self):
        print('tab')
        pyautogui.press('tab')

    def shift_tab(self):
        print('shift-tab')
        pyautogui.keyDown('shift')
        pyautogui.press('tab')
        pyautogui.keyUp('shift')

    def enter(self):
        print('enter')
        pyautogui.press('enter')

    def scroll_up(self):
        print('scroll up')
        pyautogui.keyDown('shift')
        pyautogui.press('space')
        pyautogui.keyUp('shift')

    def scroll_down(self):
        print('scroll down')
        pyautogui.press('space')

    def back(self):
        print('back')
        pyautogui.keyDown('alt')
        pyautogui.press('left')
        pyautogui.keyUp('alt')

    def forward(self):
        print('forward')
        pyautogui.keyDown('alt')
        pyautogui.press('right')
        pyautogui.keyUp('alt')
