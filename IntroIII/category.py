class Category:
    def __init__(self, name, products): #; products add later):
        self.name = name
        self.products = products


    def __str__(self):
        return f"No Products in {self.name}"