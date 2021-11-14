'''
    TODO: Implement the rest of them lmao
'''

class Relationship():
    pass

class OneToMany(Relationship):
    _value: set
    def __init__(self, model: object, mapped_by: str, inverse_mapped_by: str):
        self.model = model
        self.mapped_by = mapped_by    
        self.inverse_mapped_by = inverse_mapped_by
        self._value = set()

    def add(self, item):
        self._value.add(item)

    def save(self):
        for item in self._value:
            item.save()
    
    def get(self):
        managed = getattr(self.foobar, '__managed__')
        if not managed:
            return self._value
            
        reverse = getattr(self.foobar, self.inverse_mapped_by)
        raw = self.model.get_all_where({ self.mapped_by: reverse })
        return raw
