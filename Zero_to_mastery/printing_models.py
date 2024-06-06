def printing_models(unprinted_designs, completed_designs):
    """
    Simulate printing designs until none left
    Move each design to completed_designs
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_designs.append(current_design)


def show_completed_designs(completed_designs):
    print('\nThe following models were printed:')
    for completed_design in completed_designs:
        print(completed_design)


unprinted_designs = ['phone case', 'iPhone 16', 'Samsung Galaxy chip set']
completed_designs = []

printing_models(unprinted_designs[:], completed_designs)
show_completed_designs(completed_designs)



