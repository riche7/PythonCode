#           Hospital Example
# Patient_name = input("Enter the patient name: ")
# print("Welcome " + Patient_name) 
# Patient_age = input("Enter the patient's age: ")
# Patient_status = " and is a new patient"
# print(Patient_name + " is " + Patient_age + Patient_status)

# name = input("Pleas, enter your name: ")
# print("Howdy " + name)
# color = input("What is your favorite color? ")
# print(name + ' likes ' + color)

#           Birth Year Example
# Birth_year = input("Enter your birth year: ")
# current_age = 2021 - int(Birth_year)
# print("You are: ", current_age, " years old.")

#           Calculator
# a = float(input("Enter the first number: "))
# b = float(input("Enter the second number: "))
# c = a + b
# print("The sum is: ", c)

#           Object, Function, Method
# Patient_name = 'Anderson Annylusse Riche'
# print(Patient_name.replace('Annylusse', 'Anilus'))

#           Conditions
                #1
# tempeture = int(input("Enter the tempeture: "))

# if tempeture < 17:
#    print("It's cold.")
#  elif tempeture > 25:
#      print("It's hot.")
# else:
#    print("It's cool.")

#               #2
# is_hot = False
# is_cold = True

# if is_hot:
#    print("It's hot.")
# elif is_cold:
#    print("It's cold")
# else:
#    print("It's cool.")

#               #3
#           Weight
# Weight = float(input("Enter you weight: "))
# Weight_Type = (input("(L)bs or (K)g: ")) # asking the weight in kilogram or pound

# if Weight_Type.upper() == "L": # makes lower case to upper case
#    converted = Weight / 0.45
#    print(f"You are {converted} pounds.")
# else:
#    converted = Weight * 0.45
#    print(f"You are {converted} kilos.")

#               #4
# print('the price of this house is', 1000000000)
# client_credit = int(input("Enter your credit here: "))
# Credit = 1000000000

# if client_credit >= Credit:
#    print("You will need to put down 10%.")
#    down_payment = 0.1 * Credit
#    print("Your down payment is: $", down_payment)
# else:
#    print("You will need to put down 20%.")
#    down_payment = 0.2 * Credit
#    print("Your down payment is: $", down_payment)

#               #5
# name = input("Enter your name here: ")

# if len(name) < 3:
#    print("Name must be at least 3 characters. Try it again.")
# elif len(name) > 50:
#    print("Name can be a maximum of 50 characters. Try it again.")
# else:
#    print("name looks good.")

#           Convert weight
# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

#           While loops
# a = 1

# while a <= 10:
#    print(a * '|')
#    a += 1


#                   #2 Guessing game
# correct_number = 10
# guessing_times = 3
# guess_count = 0

# while guess_count < guessing_times:
#    player_input = int(input("Enter the guessing number: "))
#    guess_count += 1

#    if player_input == correct_number:    
#        print("Yeah!!! You win!")
#        break
# else:
#        print("Sorry. You enter the wrong numbers.")

#           Lists
# names = ['John', 'Sam', 'Mary', 'Peter', 'Jack', 'Sandra', 'Brown']
# print(names[2]) # sort out the Mary
# print(names[-2]) # Sort out Sandra
# names[2] = "Vanessa" # replace Mary  by Cassandra
# print(names[0:3]) # print a range

#       List object
# numbers = [1, 2, 3, 4, 5]
# numbers.append(7) # adds a new item in the list
# numbers.insert(0, -1) # adds a new item in a specific place
# numbers.remove(2) # removes items from a list
# numbers.clear() # removes all items from the list
# print( 2 in numbers) # checks if an item exist in the list
# print(len(numbers)) # return the number of item in the list

#           For Loops
# numbers = [1, 2, 3, 4, 5, 6]
# for item in numbers:
#    print(item)

#           Range Function
# numbers = range(10) # contains a range of number from 0 to 9
# for number in numbers:
#    print(number) 
#            or
# for number in range(10):
#   print(number)

# range(5, 10) # 5 is considered to be the starting value amd 10 the second value in the range
# range(5, 10, 2) # 5 is considered to be the starting value, 10 the second value, and 2 is considered to be the steps

#           Tuples
# numbers = (1, 2, 3, 4, 5) # we use parenthesis to define tuples and they cannot be change
