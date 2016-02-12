from model_base import ModelBase


class Model(ModelBase):
    # ...
    def __init__(self):
        super().__init__()
        self._title = 'hello'
        self._message = 'Try (SHIFT+)TAB and ENTER?'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if(self._title == value):
            return
        self._title = value
        self.on_changed('title',value)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str):
        if self._message == value:
            return
        self._message = value
        self.on_changed('message',value)

    def click(self, *arg):
        self.message += '.'
        pass

    def func_to_click(self, func) -> callable(object):
        return ( lambda x: func(self) )
        pass

    def set_title(self, param: str) :
        def setter(pressed: bool):
            self.title += "."
        return setter


