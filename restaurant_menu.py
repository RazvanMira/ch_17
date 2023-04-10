def read_menu():
    products = []

    while True:
        input_product = input("Please type in a product: ")
        if input_product == "":
            break
        input_price = input(f"Please type in a price for {input_product}: ")
        if input_price == "":
            break
        products.append([input_product, input_price])

    return products


def display_menu(products, width):
    header = "Menu"
    formatted_header = header.center(width)
    print(formatted_header)

    for product, price in products:
        formatted_product = product.ljust(width - 3, ".")
        formatted_price = price.rjust(3)
        print(formatted_product + formatted_price)


def main():
    products = read_menu()
    width = int(input("Please type in a width for the menu: "))
    display_menu(products)


if __name__ == "__main__":
    main()