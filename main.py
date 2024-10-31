    cat_attributes = {
        "intelligence": 10,
        "energy": 50,
        "weight": 10,
    }

    print("Welcome to my cat game!")
    name = input("Enter name:")
    while True:
        option = input("What would you like to do? \n 1. Play with your cat \n2. Train your cat \n3. show stats")

        if option == '1':
            # change the cat's attributes here
            pass
        elif option == '2':
            pass
        else:
            pass
        if cat_attributes['energy'] < 0:
            pass
