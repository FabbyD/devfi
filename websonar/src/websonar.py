from tools import BrowserTool, KeyboardTool
import platform

class WebSonar:
    def __init__(self):
        self.tool = BrowserTool()
        self.has_keyboard = platform.system() == 'Linux'
        if self.has_keyboard:
            print('Keyboard enabled!')

    def __getattr__(self, name):
        if hasattr(self.tool, name):
            return getattr(self.tool, name)
        else:
            raise AttributeError

    def on_wiggle(self):
        if self.has_keyboard:
            self.swap_tools()

    def swap_tools(self):
        if isinstance(self.tool, BrowserTool):
            self.tool = KeyboardTool()
            self.tool.show()
            self.tool.init_pointer()
        elif isinstance(self.tool, KeyboardTool):
            self.tool.hide()
            self.tool = BrowserTool()
        else:
            print('Wrong tool detected.')
