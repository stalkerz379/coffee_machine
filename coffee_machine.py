from collections import namedtuple

Ingredient = namedtuple('Ingredient', ['cost', 'measurement', 'printable_name'], defaults=[0, None, None])


class Drink:

    def __init__(self,  water: Ingredient, milk: Ingredient, coffee_beans: Ingredient, disposable_cups: Ingredient,
                 money: Ingredient, name: str) -> None:
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.name = name
        self.__ingredients = (self.water, self.milk, self.coffee_beans, self.disposable_cups, self.money)

    def __str__(self) -> str:
        return f"Drink: {self.name}\n" \
               f"{self.water.printable_name}: {self.water.cost, self.water.measurement}\n{self.milk.printable_name}: {self.milk.cost, self.milk.measurement}\n" \
               f"{self.coffee_beans.printable_name}: {self.coffee_beans.cost, self.coffee_beans.measurement}\n" \
               f"{self.disposable_cups.printable_name}: {self.disposable_cups.cost, self.disposable_cups.measurement}\n" \
               f"{self.money.printable_name}: {self.money.cost, self.money.measurement}\n"

    @property
    def ingredients(self):
        return self.__ingredients


class Cappuccino(Drink):
    def __init__(self, water, milk, coffee_beans, disposable_cups, money, name):
        super(Cappuccino, self).__init__(water, milk, coffee_beans, disposable_cups, money, name)


class Espresso(Drink):
    def __init__(self, water, milk, coffee_beans, disposable_cups, money, name):
        super().__init__(water, milk, coffee_beans, disposable_cups, money, name)


class Latte(Drink):
    def __init__(self, water, milk, coffee_beans, disposable_cups, money, name):
        super().__init__(water, milk, coffee_beans, disposable_cups, money, name)


class CoffeeMachine:

    def __init__(self, water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        self._available_drinks = []
        self.__ingredients = (self.water, self.milk, self.coffee_beans, self.disposable_cups, self.money)

    def __str__(self):
        return f"The coffee machine has:\n{self.water} of water\n" \
               f"{self.milk} of milk\n{self.coffee_beans} of coffee beans\n" \
               f"{self.disposable_cups} of disposable cups\n" \
               f"${self.money} of money"

    @property
    def ingredients(self):
        return self.__ingredients

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add:\n'))
        self.milk += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable coffee cups you want to add:\n"))

    def buy(self, drink: Drink):
        if isinstance(drink, Drink):
            self.decrease_resources(drink)
        else:
            print(f'Sorry, drink should be an instance of <class Drink>. Given drink {type(drink)}')

    def decrease_resources(self, drink: Drink) -> None:
        if isinstance(drink, Drink) and drink in self._available_drinks:
            for machine, drink_ in zip([self.water, self.milk, self.coffee_beans, self.disposable_cups], drink.ingredients):
                is_possible_to_make_drink = self.control_resources(machine, drink_.cost)
                if not is_possible_to_make_drink:
                    print(f'Sorry, not enough {drink_.printable_name}')
                    return None
            print('I have enough resources, making you a coffee!')
            self.water -= drink.water.cost
            self.milk -= drink.milk.cost
            self.coffee_beans -= drink.coffee_beans.cost
            self.disposable_cups -= drink.disposable_cups.cost
            self.money += drink.money.cost

    @staticmethod
    def control_resources(attribute, other_attribute):
        if attribute - other_attribute >= 0:
            return True
        return False

    def give_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def add_drink(self, drinks: list[Drink]):
        self._available_drinks.extend(drink for drink in drinks if isinstance(drink, Drink))

    def remove_drink(self, drink: Drink):
        if isinstance(drink, Drink) and drink in self._available_drinks:
            self._available_drinks.pop(self._available_drinks.index(drink))
        else:
            print(f'Sorry, removed failed. Drink should be an instance of <class Drink> and been added to automate.Given drink {type(drink)}')

    @staticmethod
    def user_options():
        options = ['buy', 'fill', 'take', 'exit', 'remaining']
        user_input = input('Write action (buy, fill, take, remaining, exit):\n').strip().lower()
        while user_input not in options:
            print('Wrong option. Please, select again')
            user_input = input('Write action (buy, fill, take, remaining, exit):\n')
        return user_input

    def print_drinks(self):
        for ind, drink in enumerate(self._available_drinks, 1):
            print(f"{ind} - {drink.name}", end=', ')

    def menu(self):
        user_choice = self.user_options()
        match user_choice:
            case 'fill':
                self.fill()
            case 'remaining':
                print(self)
            case 'take':
                self.give_money()
            case 'exit':
                exit()
            case 'buy':
                drink_ = input(
                    'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n').strip().lower()
                if drink_ == 'back':
                    return self.menu()
                elif drink_ not in [str(num) for num in range(1, len(self._available_drinks) + 1)]:
                    print('Wrong option. Please, select again')
                    return None
                drink = self._available_drinks[int(drink_) - 1]
                self.buy(drink)
            case _:
                print('Wrong option. Please, select again')


def main():
    coffee_machine = CoffeeMachine()
    cappuccino = Cappuccino(water=Ingredient(200, 'ml', 'water'),
                            milk=Ingredient(100, 'ml', 'milk'),
                            coffee_beans=Ingredient(12, 'g', 'coffee beans'),
                            money=Ingredient(6, 'dollars', 'money'),
                            disposable_cups=Ingredient(1, 'sht', 'disposable cups'),
                            name='cappuccino')
    latte = Latte(water=Ingredient(350, 'ml', 'water'),
                  milk=Ingredient(75, 'ml', 'milk'),
                  coffee_beans=Ingredient(20, 'g', 'coffee beans'),
                  money=Ingredient(7, 'dollars', 'money'),
                  disposable_cups=Ingredient(1, 'sht', 'disposable cups'),
                  name='latte')
    espresso = Espresso(water=Ingredient(250, 'ml', 'water'),
                        milk=Ingredient(0, 'ml', 'milk'),
                        coffee_beans=Ingredient(16, 'g', 'coffee beans'),
                        money=Ingredient(4, 'dollars', 'money'),
                        disposable_cups=Ingredient(1, 'sht', 'disposable cups'),
                        name='espresso')
    coffee_machine.add_drink([cappuccino, latte, espresso])
    while True:
        coffee_machine.menu()


if __name__ == "__main__":
    main()
