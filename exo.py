#           Hospital Example
# Patient_name = input("Enter the patient name: ")
# print("Welcome " + Patient_name) 
# Patient_age = input("Enter the patient's age: ")
# Patient_status = " and is a new patient"
# print(Patient_name + " is " + Patient_age + Patient_status)

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

#           Condition
# tempeture = int(input("Enter the tempeture: "))

# if tempeture <= 20:
#    print("It's cold.")
# elif tempeture >= 20:
#    print("It's hot")
# else:
#    print("It's cool.")

#           Weight
# Weight = float(input("Enter you weight: "))
# Weight_Type = (input("(K)g or (L)bs: ")) # asking the weight in kilogram or pound

# if Weight_Type.upper() == "K": # makes lower case to upper case
#    converted = Weight / 0.45
#    print("Weight in Pound is: ", converted)
# else:
#    converted = Weight * 0.45
#    print("Weight in Kgs is: ",  converted)

#           While loops
# a = 1

# while a <= 10:
#    print(a * '|')
#    a += 1

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
