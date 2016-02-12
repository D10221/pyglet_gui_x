from event import Event

class ModelBase:
    def __init__(self):
        self.change_event = Event()

    def on_changed(self, key: str, value: object) -> ():
        self.change_event.invoke(key, value)

