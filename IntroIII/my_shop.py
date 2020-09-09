from store import Store
# from category import Category
from data_for_store import cats

# cats = {
#     "hands": Category("Hands"),
#     "heads": Category("Heads"),
#     "shoes": Category("Shoes"),
#     "thingy": Category("Thingy"),
# }

# hands = Category("Hands") 
# heads = Category("Heads")
# shoes = Category("Shoes")
# thingy = Category("Thingy")

my_store = Store("Bobs Place", [cats["hands"], cats["heads"], cats["shoes"],cats["thingy"]])

print(my_store)
# print(repr(my_store))

selection = 0

while selection != len(my_store.categories) +1 :

    selection = input("Please select the number of a department")

    try:

        selection = int(selection)
        if selection == len(my_store.categories) + 1:
            print("Thanks for coming {my_store.name}")
        elif selection > 0 and selection <= len(my_store.categories):
            print(my_store.categories[selection -1])
        else:
            print('Please select a vaild number')

    except ValueError:
        print("Please enter a number.")

    # print(f"the user selected {selection}")