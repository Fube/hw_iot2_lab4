'''
    TODO: Implement the rest of them lmao
'''

class Relationship():
    pass

class OneToMany(Relationship):
    __value__: set
    def __init__(self, model: object, mapped_by: str, inverse_mapped_by: str):
        self.model = model
        self.mapped_by = mapped_by    
        self.inverse_mapped_by = inverse_mapped_by
        self.__value__ = set()

    def add(self, item):
        self.__value__.add(item)

    def save(self):
        for item in self.__value__:
            item.save()
    

