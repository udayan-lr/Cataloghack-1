products = [
    {"name": "T-Shirt", "size": "Medium", "description": "A white medium-sized T-Shirt"},
    {"name": "Jeans", "size": "32", "description": "Comfortable Levi's size 32 jeans"},
    {"name": "Shoes", "size": "8", "description": "Nike running shoes"},
    {"name": "Jacket", "size": "Large", "description": "A warm and trendy large-sized jacket"},
    {"name": "Watch", "size": "Customizable", "description": "A classy Rolex watch"},]
cart = []
def display_products():
    print("Available Products:")
    for i, product in enumerate(products):
        print(str(i+1)+". "+product["name"]+"-"+product["size"]+"-"+product["description"])

def try_on_product(product_index):
    product=products[product_index]
    print("Trying on: "+product["name"]+" (Size: "+product["size"]+")")
    print("Description: "+product["description"])
    fit_result="This fits you perfectly!"
    print("Fit result: "+fit_result)

def add_to_cart(product_index):
    product=products[product_index]
    cart.append(product)
    print(product["name"]+" added to cart.")
def checkout():
    print("Checking out with the following items:")
    for item in cart:
        print("- "+item["name"]+" (Size: "+item["size"]+")")
    print("Thank you for shopping!")

while True:
    print("\n1. Display Products\n2. Try On Product\n3. Add to Cart\n4. Checkout\n5. Exit \n")
    choice=input("Choose an option: ")
    if choice=='1':
        display_products()
    elif choice=='2':
        product_index=int(input("Enter product number to try on: "))-1
        try_on_product(product_index)
    elif choice=='3':
        product_index=int(input("Enter product number to add to cart: "))-1
        add_to_cart(product_index)
    elif choice=='4':
        checkout()
    elif choice=='5':
        break
    else:
        print("Invalid choice, please try again.")

