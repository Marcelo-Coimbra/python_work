""" request_toppings = 'mushrooms'

if request_toppings != 'anchovies':
    print("Hold the anchovies!") """

""" request_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in request_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in request_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in request_toppings:
    print("Adding extra cheese.")

print('\nFinished making your pizza!') """

""" request_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for request_topping in request_toppings:
    if request_topping == 'green peppers':
        print("Sorry, we are out of green peppers rigth now.")
    else:
        print(f"Adding {request_topping}.")

print("\nFinishing make your pizza!") """

""" request_toppings = []

if request_toppings:
    for request_topping in request_toppings:
        print(f"Adding {request_topping}.")
        print("\nFinishing make your pizza!")
else:
    print("Are you sure you want a plain pizza?") """

available_toopings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pinapple', 'extra cheese']
request_toppings = ['mushrooms', 'french fries', 'extra cheese']

for request_topping in request_toppings:
    if request_topping in available_toopings:
        print(f"Adding {request_topping}.")
    else:
        print(f"Sorry, we don't have {request_topping}.")

print("\nFinishing make your pizza!")
