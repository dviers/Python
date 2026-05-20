##name = input('What is your name? ')
##age = (input('What is your age? '))country = input('What country do you live in? ')
##message = f"Hello {name}, I see you are {age} years old. And you live in {country}"
##print(message)

try:
    salary = float(input('What is your salary?: '))
    if salary >= 100000.00:
      print ("You are rich")
    else:
        print("you are not rich")
except ValueError:
    print("invalid salary")
except:
    print("someting went wrong")