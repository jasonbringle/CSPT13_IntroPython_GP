# class TestClass:
#     pass

# a = TestClass()
# b = TestClass()
# print(a)

# print(b)

class SecondClass:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "%s %s" % (self.num1, self.num2)
    
    def __repr__(self):
        return "%s %s" % (self.num1, self.num2)

TheClass = SecondClass("people","suck")

print(TheClass)