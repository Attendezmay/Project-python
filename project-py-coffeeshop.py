#funtion: choose type of coffee
def coffee_type():
  print("\n ---Choose the type of coffee---")
  print("1. Hot 55 bath")
  print("2. Cold 60 bath")

#function: summary of order
def order():
  if coffee_number == 1 and coffee_price == 1:
    print("\n ---You choose Hot Espresso 55 bath---")
  elif coffee_number == 1 and coffee_price == 2:
    print("\n ---You choose Cold Espresso 60 bath---")
  elif coffee_number == 2 and coffee_price == 1:
    print("\n ---You choose Hot Cappucino 55 bath---")
  elif coffee_number == 2 and coffee_price == 2:
    print("\n ---You choose Cold Cappucino 60 bath---")
  elif coffee_number == 3 and coffee_price == 1:
    print("\n ---You choose Hot Latte 55 bath---")
  elif coffee_number == 3 and coffee_price == 2:
    print("\n ---You choose Cold Latte 60 bath---")
  


print('''---Welcome to "Another Cup :)" Coffee shop---
\n
Please type 1 to show menu:''')


show_menu = int(input())
#can access the menu
if show_menu == 1:
  print("\n ---Choose the menu---")
  print("1. Espresso")
  print("2. Cappucino")
  print("3. Latte")
  print("\n Select coffee:")

  #choose menu (1,2,3)
  coffee_number = int(input())
  if coffee_number == 1:
     coffee_type()
  elif coffee_number == 2:
     coffee_type()
  elif coffee_number == 3:
     coffee_type()

  #select type
  print("\n Select Type:")
  coffee_price = int(input())
  if coffee_price == 1:
     order()
  elif coffee_price == 2:  
     order()

  #bill
  print("\n Input your money:")
  payment = int(input())
  
  if coffee_price == 1:
    if payment >= 55:
      bill = payment - 55
      print("You received a chance of %d bath" %bill)
      print("--- Thank you :D ---")
    else:
      print("Not enough money")
      print("Please try again.")
      
  elif coffee_price == 2:
    if payment >= 60:
     bill = payment - 60
     print("\n You received a chance of %d bath" %bill)
     print("--- Thank you :D ---")
    else:
     print("Not enough money")
     print("Please try again.")

  

#can't access the menu
else:
  print("\n Sorry, something went wrong :(")
  