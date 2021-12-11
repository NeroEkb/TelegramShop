class Item:
    def __init__(self, id, category, name, descrition, price, amount_in_stock, img):
        self.ID = id
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

    def add(self, id, item_list):
        for item in item_list:
            if item.ID == id:
                self.list.append(item)

    def get_items(self):
        return [[item.name, self.list.count(item), item.price * self.list.count(item)] for item in set(self.list)]

    def get_total(self, total=0):
        for item in self.list:
            total += item.price * self.list.count(item)
        return total
