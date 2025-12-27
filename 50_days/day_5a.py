def my_discount():
    price = int(input("Enter the price: "))
    discount = int(input("Enter the discount: "))
    aft_disc = price * (100-discount)/100
    return 'Price after discount is ', aft_disc

print(my_discount())    