def user_options():
    options = ['buy', 'fill', 'take', 'exit', 'remaining']
    user_input = input('Write action (buy, fill, take, remaining, exit):\n')
    if user_input in options:
        return user_input
    else:
        print('Wrong option. Please, select again')
        return user_options()


def calculate_ingredients_needed_for_coffee():
    espresso = {'water': (250, 'ml'), 'milk': (0, 'ml'), 'coffee beans': (16, 'g'), 'money': (4, 'dollars'), 'disposable cups': (1, 'sht')}
    latte = {'water': (350, 'ml'), 'milk': (75, 'ml'), 'coffee beans': (20, 'g'), 'money': (7, 'dollars'), 'disposable cups': (1, 'sht')}
    cappuccino = {'water': (200, 'ml'), 'milk': (100, 'ml'), 'coffee beans': (12, 'g'), 'money': (6, 'dollars'), 'disposable cups': (1, 'sht')}
    ingredients = [espresso, latte, cappuccino]
    return ingredients


def available_ingredients():
    ingredients_available = {'water': [400, 'ml'], 'milk': [540, 'ml'], 'coffee beans': [120, 'g'], 'disposable cups': [9, 'sht'], 'money': [550, 'dollars']}
    #ingredients_available.setdefault('water', (int(input('Write how many ml of water the coffee machine has:\n')), 'ml'))
    #ingredients_available.setdefault('milk', (int(input('Write how many ml of milk the coffee machine has:\n')), 'ml'))
    #ingredients_available.setdefault('coffee beans', (int(input('Write how many grams of coffee beans the coffee machine has:\n')), 'g'))
    return ingredients_available


def buying_coffee(ingredients_available):
    espresso = {'water': (250, 'ml'), 'milk': (0, 'ml'), 'coffee beans': (16, 'g'), 'money': (4, 'dollars'), 'disposable cups': (1, 'sht')}
    latte = {'water': (350, 'ml'), 'milk': (75, 'ml'), 'coffee beans': (20, 'g'), 'money': (7, 'dollars'), 'disposable cups': (1, 'sht')}
    cappuccino = {'water': (200, 'ml'), 'milk': (100, 'ml'), 'coffee beans': (12, 'g'), 'money': (6, 'dollars'), 'disposable cups': (1, 'sht')}

    user_choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
    if user_choice == "back":
        return ingredients_available
    elif int(user_choice) == 1:
        result_of_check, cur_key = check(espresso, ingredients_available)
        if result_of_check == 'I have enough resources, making you a coffee!':
            print('I have enough resources, making you a coffee!')
            ingredients_available = calculation_suppliers(espresso, ingredients_available)
            return ingredients_available
        print(f'Sorry, not enough {cur_key}!')
        return ingredients_available
    elif int(user_choice) == 2:
        result_of_check, cur_key = check(latte, ingredients_available)
        if result_of_check == "I have enough resources, making you a coffee!":
            print('I have enough resources, making you a coffee!')
            ingredients_available = calculation_suppliers(latte, ingredients_available)
            return ingredients_available
        print(f'Sorry, not enough {cur_key}!')
        return ingredients_available
    elif int(user_choice) == 3:
        result_of_check, cur_key = check(cappuccino, ingredients_available)
        if result_of_check == 'I have enough resources, making you a coffee!':
            print('I have enough resources, making you a coffee!')
            ingredients_available = calculation_suppliers(cappuccino, ingredients_available)
            return ingredients_available
        print(f'Sorry, not enough {cur_key}!')
        return ingredients_available
    else:
        print('Wrong choice. Please, select again')
    return buying_coffee(ingredients_available)


def check(ingredient, ingredients_available):
    cur_key = ''
    for key in ingredient.keys():
        if key != 'money':
            if ingredients_available[key][0] - ingredient[key][0] < 0:
                cur_key = key
                return f'Sorry, not enough {key}!', cur_key
    return 'I have enough resources, making you a coffee!', cur_key


def calculation_suppliers(ingredient, ingredients_available):
    for key in ingredient.keys():
        if key != 'money':
            ingredients_available[key][0] = ingredients_available[key][0] - ingredient[key][0]
        else:
            ingredients_available[key][0] = ingredients_available[key][0] + ingredient[key][0]
    return ingredients_available


def filling_automate(ingredients_available):
    ingredients_available['water'][0] += int(input('Write how many ml of water you want to add:\n'))
    ingredients_available['milk'][0] += int(input("Write how many ml of milk you want to add:\n"))
    ingredients_available['coffee beans'][0] += int(input("Write how many grams of coffee beans you want to add:\n"))
    ingredients_available['disposable cups'][0] += int(input("Write how many disposable coffee cups you want to add:\n"))
    return ingredients_available


def take_money(ingredients_available):
    print(f'I gave you ${ingredients_available["money"][0]}')
    ingredients_available['money'][0] = 0
    return ingredients_available


def printing_ingredients(ingredients_in_stock):
    print('The coffee machine has:')
    for key in ingredients_in_stock.keys():
        if key != "money":
            print(f'{ingredients_in_stock[key][0]} of {key}')
        else:
            print(f'${ingredients_in_stock[key][0]} of {key}')
    return ''

# not used now, can be used for multiple cups options
def calculation(water_available, milk_available, coffee_beans_available):
    cups, water, milk, coffee_beans = 0, 0, 0, 0
    ingredients_for_one_cup = calculate_ingredients_needed_for_coffee()
    while water <= water_available and milk <= milk_available and coffee_beans <= coffee_beans_available:
        water += ingredients_for_one_cup['water'][0]
        milk += ingredients_for_one_cup['milk'][0]
        coffee_beans += ingredients_for_one_cup['coffee beans'][0]
        cups += 1
    if water > water_available or milk > milk_available or coffee_beans > coffee_beans_available:
        cups -= 1
    return cups

# not used now, can be used for multiple cups options
def check_if_possible_to_make_coffee(ingredients_available):
    user_input = how_many_coffee_needed()
    water_available = ingredients_available["water"][0]
    milk_available = ingredients_available["milk"][0]
    coffee_beans_available = ingredients_available["coffee beans"][0]
    cups = calculation(water_available, milk_available, coffee_beans_available)
    if cups > user_input:
        return f"Yes, I can make that amount of coffee (and even {cups - user_input} more than that)"
    elif cups == user_input:
        return f"Yes, I can make that amount of coffee"
    else:
        return f"No, I can make only {cups} cups of coffee"


def operations_with_automate():
    ingredients = available_ingredients()

    user_input = user_options()
    while user_input != 'exit':
        if user_input == 'fill':
            ingredients = filling_automate(ingredients)
            # printing_ingredients(ingredients)
        elif user_input == 'buy':
            ingredients = buying_coffee(ingredients)
            # printing_ingredients(ingredients)
        elif user_input == "take":
            ingredients = take_money(ingredients)
            # printing_ingredients(ingredients)
        elif user_input == "remaining":
            printing_ingredients(ingredients)
        user_input = user_options()

    return ''


print(operations_with_automate())