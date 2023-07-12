# Хеш-функции
d = {}
d = dict()
d = {'key1': 1, 'key2': 2}
d['key3'] = 3
del d['key3']
print(d)
print(d['key1'])
print(d.get('key3', 3))

class TestKey1:
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"TestKey1({self.value})"
    
d = {}
d[TestKey1(1)] = 1
d[TestKey1(1)] = 1
print(d)


class TestKey2:
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"TestKey2({self.value})"
    
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return isinstance(other, TestKey2) and self.value == other.value
d = {}
d[TestKey2(1)] = 1
d[TestKey2(1)] = 1
print(d)