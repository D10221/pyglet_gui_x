import json
import os
import sys
import xml.etree.ElementTree as Et

from pyglet import app, window, graphics
from pyglet_gui.manager import Manager
from pyglet_gui.theme import Theme

from ui_builder import load_ui

sys.path.insert(0, os.path.abspath('../'))

Window = window.Window
Batch = graphics.Batch

win = Window(640, 480, resizable=True, vsync=True)

batch = Batch()


@win.event
def on_draw():
    win.clear()
    batch.draw()


with open('theme/theme.json') as j:
    theme = Theme(json.load(j), resources_path='theme/')


if __name__ == "__main__":
    builder = load_ui(Et.parse('ui.xml').getroot())
    # Set up a Manager
    manager = Manager(
        load_ui(path="ui.xml"),
        window=win,
        batch=batch,
        theme=theme)

if __name__ == "__main__":
    app.run()
