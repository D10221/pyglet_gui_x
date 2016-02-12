import json
import os
import sys

from pyglet import app, window, graphics
from pyglet_gui import constants as pyglet_gui_constants
from pyglet_gui.buttons import OneTimeButton
from pyglet_gui.containers import VerticalContainer
from pyglet_gui.gui import Button
from pyglet_gui.manager import Manager
from pyglet_gui.theme import Theme

from model import Model
from my_label import MyLabel, Binding, LabelFactory

sys.path.insert(0, os.path.abspath('../'))

Window = window.Window
Batch = graphics.Batch
Label = MyLabel

win = Window(640, 480, resizable=True, vsync=True)
batch = Batch()

model = Model()


@win.event
def on_draw():
    win.clear()
    batch.draw()


with open('theme/theme.json') as j:
    theme = Theme(json.load(j), resources_path='theme/')


# Set up a Manager
manager = Manager(
    VerticalContainer([
        # ...
        Label(binding=Binding(context=model, path="title")),
        # ...
        VerticalContainer([
            # ...
            Label(binding=Binding(template="$message", context=model, path="message")),
            # ...
            Button("Button 1", on_press=model.set_title(".")),
            OneTimeButton("Button 2", on_release=model.click),
            Button("Button 3"),
            LabelFactory(model, "message")
        ])
    ], align=pyglet_gui_constants.HALIGN_RIGHT, padding=5),
    window=win,
    batch=batch,
    theme=theme)

def draw(key:str, value:object):
    batch.draw()
    # print("manager: draw")

model.change_event += draw

if __name__ == "__main__":
    app.run()



