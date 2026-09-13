""" # sem função
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have printed: ")
for completed_model in completed_models:
    print(completed_model) """

# com funções
# unprinted_designs[:] - cópia da lista, alternativa a copy()
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"- Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
copy_unprinted_designs = unprinted_designs.copy()
original = unprinted_designs[:]

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print(f"estado atual: {unprinted_designs}")
print(f"original: {original}")
print(f"cópia: {copy_unprinted_designs}")