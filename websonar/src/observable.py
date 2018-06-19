class Observable():
    def __init__(self):
        # Event listeners
        self.listeners = []

    def notify(self, event, *args, **kwargs):
        for listener in self.listeners:
            func = getattr(listener, event, None)
            if func:
                func(*args, **kwargs)

    def add_listener(self, listener):
        self.listeners.append(listener)
