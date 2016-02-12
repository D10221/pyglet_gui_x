class Event(object):

    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def invoke(self, key:str, value:object):
        for handler in self.__handlers:
            try:
                handler(key,value)
            except ValueError:
                print(key,value)



    def clear(self, obj):
        for handler in self.__handlers:
            if handler.im_self == obj:
                self.__handlers.remove(handler)
