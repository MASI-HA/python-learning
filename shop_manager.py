products = [
    {"name": "phone", "price": 2400000, "stock": 10, "is_available": True},
    {"name": "laptop", "price": 34590000, "stock": 7, "is_available": False},
    {
        "name": "car",
        "price": 1647500000000,
        "stock": 2,
        "is_available": False,
    },
    {
        "name": "headphon",
        "price": 1450000,
        "stock": 2,
        "is_available": True,
    },
]


print(products)
while True:
    for product in products:
        print(
            f"name : {product['name']}, price : {product['price']} , stock : {product['stock']} , is_available{product['is_available']}"
        )

    name = input("enter name of product : ")
    price = int(input("enter your price of product : "))
    stock = int(input("enter your product inventory : "))

    new_product = {"name": name, "price": price, "stock": stock, "is_available": True}
    products.append(new_product)
    print(len(products))

    for product in products:
        if product["is_available"] == True:
            print(f"available : {product['name']}")

    last_product = products[-1]
    if last_product["price"] >= 10000:
        print("This is an expensive item!")
    else:
        print("normal price")

    again = input("Do you want to add another product? (yes/no): ")
    if again != "yes":
        break
