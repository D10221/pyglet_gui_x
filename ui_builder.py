import ast
import re
import xml.etree.ElementTree as Et

from pyglet_gui.buttons import Button
from pyglet_gui.containers import VerticalContainer, HorizontalContainer
from pyglet_gui.gui import Label


def is_container(xe: Et) -> bool:
    return [VerticalContainer.__name__, HorizontalContainer.__name__].__contains__(xe.tag)


def parse_element(root: Et):
    assert Et.iselement(root)
    if not is_container(root):
        return create_ui_element(root, None)
    children = []
    for child in root:
        children.append(parse_element(child))
    return create_ui_element(root, children)


def parse_attributes(**kwargs):
    return {key: parse_primitive(value) for key, value in kwargs.items()}


def parse_primitive(value: str):
    found = re.findall('\{(.*)\}', value)
    if found.__len__() > 0:
        try:
            return ast.literal_eval(found[0])
        except ValueError as e:
            print("error: ", str(e))
    return value


def create_ui_element(xe: Et, children: []):
    d = parse_attributes(**xe.attrib)
    if xe.tag == VerticalContainer.__name__:
        # align=HALIGN_CENTER, padding=5
        return VerticalContainer(
            children,
            align=d.get('align', 0),
            padding=d.get('padding', 5)
        )
    if xe.tag == HorizontalContainer.__name__:
        # align=HALIGN_CENTER, padding=5
        return HorizontalContainer(
            children,
            align=d.get('align', 0),
            padding=d.get('padding', 5)
        )
    elif xe.tag == Label.__name__:
        return Label(
            text=d.get('text'),
            bold=d.get('bold', False),
            italic=d.get('italic', False),
            font_name=d.get('font_name', None),
            font_size=d.get('font_size', None),
            color=d.get('color', None),
            path=d.get('path', None)
        )
    elif xe.tag == Button.__name__:
        return Button(**xe.attrib)
    else:
        raise NotImplemented()


def load_ui(root: Et = None, path: str = None):
    if root is not None:
        return parse_element(root)
    if path is not None:
        assert  isinstance(path, str)
        return parse_element(Et.parse(path).getroot())
