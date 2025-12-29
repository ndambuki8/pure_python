names_age = {"jane":23, "kerry":45, "tim":24, "peter":27}

def your_age():
    # convert name to lowercase letters
    name = input("Please enter your name: ").lower()
    # Use for loop to iterate over the dictionary 
    for key in names_age.keys():
        if key == name:
            # use the get method to access a specific value
            return f'Hi {name} ! You are {names_age[key]} years old'
        else:
            # if name not in dictionary
            while name not in names_age.keys():
                age = input("Your name is not in the db, "
                            "Please enter your age: ").lower()
                names_age.update({name: age})
                return f'Hi {name} ! You are {names_age.get(name)} years old'
            
print(your_age())