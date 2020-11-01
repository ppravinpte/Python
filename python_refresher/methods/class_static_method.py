''' Use of static method and class method.''' 
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def __str__(self):
        return "{}".format(self.name)
        #return f"{self.name}"

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name, plus " - franchise"
        return Store(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It is in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))

store = Store("Test")
print(Store.franchise(store)) # o/p: Test - franchise
print(Store.store_details(store)) # o/p: 0

store2 = Store("Amazon")
print(Store.franchise(store2)) # o/p: Amazon - franchise

store2.add_item("Keyboard", 160)
print(store2.stock_price())    # o/p: 160
print(Store.store_details(store2)) # o/p: Amazon, total stock price: 160
