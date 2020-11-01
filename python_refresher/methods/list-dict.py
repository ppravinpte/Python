''' Example of static and class method using list with Dict records dictionary having key: single values'''
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return f"{self.name}"

    def add_item(self, dict):
        for name, price in dict.items():
            print('name=',name)
            print('price=',price)
            self.items.append({
                'name': name,
                'price': price
        })
        return self.items

    def stock_price(self):
        total = 0
        for item in self.items:
            print('item =',item) 
            # o/p:item = {'name': 'fevicol', 'price': 20}
            print("(item['price']):", item['price'])
            # o/p:(item['price']): 20
            total+=item['price']
        return total

    @classmethod
    def franchise(cls, store):
        #return cls(store.name + " - franchise")

        # Return another store, with the same name as the argument's name, plus " - franchise"
        return Store(store.name + " - franchise")
        #return cls(store.name + " - franchise")  # replace Store with cls.

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))

store = Store("Test")
print(Store.franchise(store))                       # o/p: Test - franchise
dict = {'fevicol':20,'pepsodent':40,'colgate':10}
print('add_item=',store.add_item(dict))
#o/p: [{'name': 'fevicol', 'price': 20}, {'name': 'pepsodent', 'price': 40}, {'name': 'colgate', 'price': 10}]
print('stock_price=',store.stock_price())           #o/p: 70
print('store_details=',Store.store_details(store))  #o/p: Test, total stock price: 70
