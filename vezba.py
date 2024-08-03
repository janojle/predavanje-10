import json

# with open("data/products.json", "r") as file:
#   products = json.load(file)
#   print(products)

from  methods import  load_file


products = load_file("data/products.json")
users = load_file("data/user.json")
print(products)
print(users)
