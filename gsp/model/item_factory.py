from model.item import Item

class ItemFactory:
    def __init__(self):
        self.item_dict = dict()
    
    def get_item(self, value):
        item = self.item_dict.get(value)
        if item == None:
            item = Item(value)
            self.item_dict[hash(item)] = item.value
            #print(self.item_dict.items())
        return item
