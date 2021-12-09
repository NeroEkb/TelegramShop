class Item:
    def __init__(self, ID, category, name, descrition, price, amount_in_stock, img):
        self.ID = ID
        self.category = category
        self.name = name
        self.description = descrition
        self.price = price
        self.amount = amount_in_stock
        self.img = img

    def __str__(self):
        return f"name : {self.name}"


class Cart:
    def __init__(self):
        self.list = []

    def add(self, id, itemlist):
        for item in itemlist:
            if item.ID == id:
                self.list.append(item)

    def getItems(self):
        return [[item.name, self.list.count(item), item.price * self.list.count(item)] for item in set(self.list)]
