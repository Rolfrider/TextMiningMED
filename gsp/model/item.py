import time

class Item:
    def __init__(self, value):
        self.value = value
        
    def __key(self):
        return (self.value, str(time.time()).encode('utf-8'))
    
    def __hash__(self):
        h = abs(hash(str(self.value)))
        return h
        
    def __eq__(self, other):
        if isinstance(other, Item):
            return self.value == other.value
        return NotImplemented
