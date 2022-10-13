# coffee_machine
## Project that simulates the work of the coffee machine. 


### Description
Let's start with a program that makes you a coffee – virtual coffee, of course. In this project, you will implement functionality that simulates a real coffee machine. It can run out of ingredients, such as milk or coffee beans, it can offer you various types of coffee, and, finally, it will take money for the prepared drink.

### Requirements
#### Stage 1: Ingredient calculator
Let's break the task into several steps:

- [x] First, read the numbers of coffee drinks from the input.
- [x] Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
- [x] Output the required ingredient amounts back to the user.

#### Stage 2:  Estimate the number of servings

Write a program that does the following:

- [x] It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.
- [x] If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".
- [x] If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", where N is the number of additional cups of coffee that the coffee machine can make.
- [x] If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee".
- [x] Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.

#### Stage 3: Buy, fill, take!
Write a program that offers to buy one cup of coffee or to fill the supplies or to take its money out. Note that the program is supposed to do one of the mentioned actions at a time. It should also calculate the amounts of remaining ingredients and how much money is left. Display the quantity of supplies before and after purchase.

- [x] First, your program reads one option from the standard input, which can be "buy", "fill", "take". If a user wants to buy some coffee, the input is "buy". If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be "fill". If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input "take".
- [x] If the user writes "buy" then they must choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino.
- [x] For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
- [x] For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
- [x] And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
- [x] If the user writes "fill", the program should ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine.
- [x] If the user writes "take" the program should give all the money that it earned from selling coffee.
At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.

#### Stage 4: Keep track of the supplies
- [x] Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: "remaining" and "exit".
- [x] Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.
- [x] And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, they should be able to type "back" to return into the main cycle.

#### Stage 5: Refactor
- [x] Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a single method.