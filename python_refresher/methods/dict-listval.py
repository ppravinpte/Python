''' Example of static and class method. Used seprate lists to form a dictionary  
 with key: multiple values combinations to be used for processing'''
class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })
        return self.items

    def stock_price(self):
        total = 0
        for item in self.items:
            print('item =',item) 
            # o/p:item = {'name': ['fevicol', 'pepsodent', 'colgate'], 'price': [20, 40, 10]}
            print("(item['price']):", item['price'])
            # o/p:(item['price']): [20, 40, 10]
            return sum(item['price'])

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
print('coming output=',Store.franchise(store))
print(Store.franchise(store))
print('coming output=',Store.franchise(store))

#print((store.franchise("Test")).name)

store2 = Store("Amazon")
print('Output=',Store.franchise(store2))
'''
'''
#print(store2.add_item("Keyboard",160)) o/p: [{'name': 'Keyboard', 'price': 160}]
list_name = ['fevicol','pepsodent','colgate']
list_price =[20,40,10]
print(store2.add_item(list_name,list_price))
#o/p: [{'name': ['fevicol', 'pepsodent', 'colgate'], 'price': [20, 40, 10]}]
print("Total price is:",int(store2.stock_price())) 
# o/p: Total price is: 70
