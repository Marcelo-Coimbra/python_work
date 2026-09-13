""" def make_pizza(*toppings):
    print(toppings)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese') """

""" def make_pizza(*toppings):
    print("\nMaking a pizaa with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese') """

def make_pizza(size, *toppings):
    print(f"\nMaking a {toppings}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'peperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')