shop_name = "Smart Shop"
owner = "Mg Mg"
total_sales = 250000
is_open = True

products = ["rice", "oil", "sugar", "milk"]
new_products = ["coffee", "tea"]

print(type(shop_name),type(owner),type(total_sales),type(is_open))

total_sales = 250000
if total_sales > 200000:
    print("Sales target achieved")
else:
    print("Sales target not achieved")

products = ["rice", "oil", "sugar", "milk"]
print(products[0:2])

products = ["rice", "oil", "sugar", "milk"]
products[2] = "salt"
print(products)

products = ["rice", "oil", "sugar", "milk"]
products.append("eggs")
print(products)

products = ["rice", "oil", "sugar", "milk"]
products.insert(1,"bread")
print(products)

products = ["rice", "oil", "sugar", "milk"]
products.extend(new_products)
print(products)

products = ["rice", "oil", "sugar", "milk"]
products.remove("oil")
print(products)

products = ["rice", "oil", "sugar", "milk"]
products.pop(1)
print(products)

products = ["rice", "oil", "sugar", "milk"]
del products[0]
print(products)


print(products)