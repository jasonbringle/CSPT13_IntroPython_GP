class Store:
    def __init__(self, name, categories):
        # Attributies
        self.name = name
        self.categories = categories

    def __str__(self):
        ret = f"{self.name}\n"
        for i, c in enumerate(self.categories):
            ret += "     " + str(i + 1) + ": " + c.name + "\n"
        ret += "     " + str(i + 2) + ": Exit"

        return ret

    def __repr__ (self):
        return f"Store({self.name},  {self.categories})"

    