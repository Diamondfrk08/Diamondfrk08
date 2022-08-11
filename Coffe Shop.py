#lets build a robot brista!!

print("Hello, Welcome to Wyatt's Coffee Shop!!!!!")

name = input("What Is Your Name? \n")

if name == "ben":
    print("\n you are not welcome")
else:
    print("Hello " + name + ", thank you so much for coming in today \n\n")
    menu = "Black Coffee, Espresso, Latte, Cappucino"
    print(
        name +
        ', what would you like from are menu today? Here is what we are serving. \n\n'
        + menu)

order = input()

price = 8

quantity = input("How Many Coffess Do you want?\n")

total = price * int(quantity)
print(" Thank You. Your toal is : $" + str(total))

print("\n sounds good " + name + ", We'll have your " + quantity + " " +
      order + " ready for you in a moment.")

close = input('\npress enter to close')
