age = 66
""" if age < 4:
    print('your admission cost is $0.')
elif age < 18:
    print('your admission cost is $25.')
else:
    print('your admission cost is $45.') """

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")