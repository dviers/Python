# Author: David V
# Python Group Session - DAY 3
# if = Do some action only if some condition is TUE
#       Else do something else

age = int(input("Enter Your Age: "))

if age >= 18 and age < 100:
    print("You have now sold your soul to me!")
elif age < 0:
    print("You haven't even been born yet, dude!")
elif age >= 100:
    print("You are too old. Your soul is too wrinkled!")
else:
    print("You must me over 18 to sell your soul to me!")


response = input("Would you like some food? (Y/N): ")
if response == "Y":
      print("You have some food!")
else:
      print("NO FOOD FOR YOU!")

name = input("Enter your name: ")
if name == "":
    print("You did not type in your name, fool!")
else:
    print(f"Hello {name}")

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

online = False
if online:
    print("The user is online")
else:
    print("The user is not online")