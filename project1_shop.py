put = "Fill in the goods"
print(put)
goods = dict(name='apples', prices=67, number=100)
print(goods)
n = "Enter the quantity of goods"
print(n)
def apples (n):
    return n - 1
print(apples(int(input())))
if apples == 0:
    print("apples are not in stock")
else:
    print("there are apples")

# ShoppingCart
items_in_cart = {"product": 'apples', "price": 67}
def add_item(product, price):
    if not product in items_in_cart:
        print("product added")
    else:
        print("product is already in the cart")
    return product + price
print(add_item("apple", "67"))

def remove_item(product):
    if product in items_in_cart:
        del items_in_cart[product]
        print("product removed")
    else:
        print("product is not in the cart")

# Customer database

database = {
"first customer": {
    "name": 'Amy Blank',
    "phone_number": 99876,
    "email": "blank_a@gmail.com",
    "address": 'Chicago'},
"second customer": {
     "name": 'Jonh Smith',
     "phone_number": 88765,
     "email": 'smoith.j@gmail.com',
     "address": 'New York' },
}


def format_print(text, val):
    print(text)
    for k, v in val.items():
        print(f'{k} - {v}')
    print()


for k, v in database.items():
    if "first customer" == k:
        format_print("About first customer: ", v)
    elif "second customer" == k:
        format_print("About second customer: ", v)












