class Entity(object):
    def __init__(self, table):
        self.table = table


    def __call__(self, clazz):

        class Wrapped(clazz):
            table = self.table
            def new_method(self, value):
                return value * 2

        return Wrapped

