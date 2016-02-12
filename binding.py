from string import Template

from model_base import ModelBase


def get_dictionary(instance: object) -> dict:
    return {key: value for key, value in
            [(attribute, getattr(instance, attribute))
             for attribute in dir(instance)
             if not attribute.startswith('__')
             and not attribute.startswith('_')
             and not attribute.endswith('_event')]
            if not callable(value)}


class Binding:
    def __init__(self, context: ModelBase, path: str, template: str = None):
        """

        :param context:
        :param path:
        :param template:
        """
        self.template = template
        self.path = path
        self.context = context
        context.change_event += self.on_change

    setter = (lambda x: ())

    def apply_binding(self):
        self.on_change(self.path, None)

    _model_props = None

    @property
    def model_props(self):
        if self._model_props is None:
            self._model_props = get_dictionary(self.context)
        return self._model_props

    def on_change(self, key: str, value: object) -> ():
        if self.path == key and self.setter is not None:
            if self.template is not None:
                value = Template(self.template).safe_substitute(self.model_props)
            else:
                if value is None:
                    value = self.model_props.__getitem__(self.path)
            # ..
            self.setter(value)
