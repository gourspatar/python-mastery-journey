class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


product1 = Product("Laptop", 50000)
product2 = Product("Phone", 30000)

print(product1 < product2)
print(product2 < product1)