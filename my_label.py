from pyglet_gui.core import Viewer
from pyglet_gui.gui import Label

from binding import Binding


class MyLabel(Label):
    def __init__(self, path: str = None, binding: Binding = None):
        Viewer.__init__(self)
        Label.__init__(self)
        self.path = 'label' if path is None else path
        # ...
        if binding is not None:
            binding.setter = lambda value: self.set_text(value)
        # ...
        pass


def LabelFactory(model ,path):
        binding = Binding(context=model, path=path)
        label = Label(path='label')
        binding.setter = lambda value: label.set_text(value)
        if label.is_loaded:
            binding.apply_binding()

        return label