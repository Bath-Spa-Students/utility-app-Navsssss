#Dictionary for snacks
snacks={"1":{"Snack":"Kurkure Small","RATE":"2","Stock Available":10},
        "2":{"Snack":"Kurkure Large","RATE":"5","Stock Available":10},
        "3":{"Snack":"Oman Chips","RATE":"0.50","Stock Available":10},
        "4":{"Snack":"Bugles  Large","RATE":"4.50","Stock Available":10},
        "5":{"Snack":"Lays Maxx Large","RATE":"5","Stock Available":10},
        "6":{"Snack":"Doritos","RATE":"5.50","Stock Available":10},
        "7":{"Snack":"Pringles","RATE":"8","Stock Available":10},
        "8":{"Snack":"cheetos","RATE":"3.50","Stock Available":10}
        }
#Dictionary for drinks
drinks={"1":{"Drink":"Mouutain Dew","RATE":"2.50","Stock Available":10},
        "2":{"Drink":"7UP","RATE":"2.50","Stock Available":10},
        "3":{"Drink":"Coke","RATE":"2.50","Stock Available":10},
        "4":{"Drink":"Miranda","RATE":"2.50","Stock Available":10},
        "5":{"Drink":"Laban Up","RATE":"0.50","Stock Available":10},
        "6":{"Drink":"Soda","RATE":"1.50","Stock Available":10},
        "7":{"Drink":"Barbican","RATE":"3","Stock Available":10}
        }
#Making a menu listing all the Snacks and drinks in the menu with its rate and stock
def print_menu():
 print("-----------------------------------------------------------------")
 print("""HELLO!

What Would you like to have today!""") 

 print("""+----------------------------------------------------------------------------+
|                               VENDING MACHINE                              |
|                                                                            |
|                                    MENU                                    |
+----------------------------------------------------------------------------+
|                                   SNACKS                                   |
+----------------------------------------------------------------------------+
|Code|            ITEMS                 |       PRICE       | Stock Available|
+----------------------------------------------------------------------------+
| 01 | Kurkure Small                    |       2.00        |       10       | 
| 02 | Kurkure Large                    |       5.00        |       10       |
| 03 | Oman chips                       |       1.50        |       10       |
| 04 | Bugles Large                     |       4.50        |       10       |
| 05 | Lays Maxx Large                  |       5.00        |       10       |
| 06 | Doritos                          |       5.50        |       10       |
| 07 | pringles                         |       8.00        |       10       |  
| 08 | Cheetos                          |       3.50        |       10       |
+----------------------------------------------------------------------------+
|                                   DRINKS                                   |
+----------------------------------------------------------------------------+
|Code|              ITEMS               |      PRICE      |  Stock Available |
+----------------------------------------------------------------------------+
| 01 | Mountain Dew                     |      2.00       |       10         |
| 02 | 7up                              |      2.00       |       10         |
| 03 | Coke                             |      1.50       |       10         |
| 04 | Miranda                          |      4.50       |       10         |
| 05 | Laban Up                         |      1.00       |       10         |
| 05 | Soda                             |      1.00       |       10         |
| 05 | Barbican                         |      1.00       |       10         |  
+----------------------------------------------------------------------------+""") 
#Making it in loop so users can use multiple times.
while True:
  
  snack_code=None
  drink_code=None
  TOTAL=0
  print_menu()
  
   
#Then we make a variable snack_code where you can input the snack you like to have
  while True:
   snack_code= input("Which Snack Would you like to have?:")
   if snack_code in snacks:
    break
   else:
     print("Wrong Code")
     
  current_snack=snacks[str(snack_code)]
#When you give the code to the preffered snack, it prints the name of the snack with the rate of the snack.
  print("You have chosen "+current_snack["Snack"]+".The prize is $"+current_snack["RATE"])
#You can select how many of the preffered item you want from the Stock Available.
  on_the_market= current_snack["Stock Available"]

  while True:
    print("The stock available for "+current_snack["Snack"]+" is "+str(current_snack["Stock Available"]))
    user_quantity= int(input("How many of "+current_snack["Snack"]+" Do you want?:"))
    if on_the_market - user_quantity>=0:
     current_snack["Stock Available"] -= user_quantity
     TOTAL+=user_quantity*float(current_snack["RATE"]) 
     break
    else:
     print("Out of stock")
  
  else:
   print("Wrong input")
 
#This is the choice if you want to buy a drink.
  drink_required=input("Would you like a Drink?(enter 0 to continue or any other key to stop):")
#If the user inputs 0, it will continue the user to which drink he prefers or
#If the user doesnt want to buy drinks, they can input any key of thier preference 
#which directly takes them to the total amount of the snacks.
  if drink_required== "0":
#The user can input the code of the preffered drink.
#If the user inputs a wrong code, it will show Wrong code until 
#the user has input the correct code. 
   while True:
    drink_code=input("Which drink would you like to have?:")
    if drink_code in drinks:
       current_drink=drinks[str(drink_code)]
       break
    else:
      print("Wrong Code")
#The preffered item and the rate is shown after the user inputs the preffered item code.
   print("You have chosen "+current_drink["Drink"]+".The prize is $"+current_drink["RATE"])
   on_the_market= current_drink["On the Market"]
   while True:
    print("The stock available for "+current_drink["Drink"]+" is "+str(current_drink["On the Market"]))
#The user can input how much of the preffered drink the user wants.
#If the user inputs more than the available stock on the market.
# it shows that its out of stock.
    user_quantity= int(input("How many of "+current_drink["Drink"]+" Do you want?:"))
    if on_the_market - user_quantity>=0:
     current_drink["On the Market"] -= user_quantity
#The total amount of the price of the drink is multiplied 
#by the number of times the user has brought
     TOTAL+=user_quantity*float(current_drink["RATE"]) 
     break 
    else:
     print("Out of stock")
          
   
#The total amount of the preffered items the user has input.  
  while True:
      TC=input("YOUR TOTAL IS $"+str(TOTAL)+".please enter the amount here to succesfuly complete the purchase:")
      if TC==str(TOTAL):
       print("Thank you for your purchase! We are happy to serve you.")
       break
      else:
         print("Sorry!You have entered the wrong amount.Please enter the correct amount.")
