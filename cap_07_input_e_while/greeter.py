""" name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!") """

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhats is your name? "
#prompt = prompt + "\nWhats is your name? "

name = input(prompt)
print(f"\nHello, {name.title()}!")
