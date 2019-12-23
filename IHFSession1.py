# Write code that prints hello world
print("Hello World")

# Print the numbers 1 to 5 on a single line
print("1, 2, 3, 4, 5")

# Write a script where Hello and World are printed on two separate lines
print("Hello \n World")

# Write a script that prints a list of names tabbed on separate lines
print("Alice \t \n Bob \t \n Charlie")

# Write code that prints the value of 2 + 2
print (2 + 2)

# Write code that prints the value of 5.7 subtracted from 3.4
print (5.7 - 3.4)

#Write code that prints the value of 8 multiplied by 7
print(8*7)

# Write code that prints the value of 144 divided by 12
print(144/12)

#Write code that prints the value of the remainder of 67 divided by 12
remainder = 67 % 12
print(remainder)

# Write code that finds the value of 20 from 4 - 2 * 6 / 3 * 5
value = (4 - 2) * 6 / 3 * 5
print(value)

# Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. Print out the string: Rectangle of width <x> and height <y> has an area of <area>
width = 5
height = 2
area = width*height

print("Rectangle of width " + str(width) + " and height " + str(height) + " has an area of " + str(area))

#Write code that prints the length of the string, 'python'
var = "python"
print(len(var))

# Print out the first and third letter of the word 'python'
print(var[0])
print(var[2])

#Ask the user to enter their name, and print out "Hello, "
name = raw_input("What is your name? ")
print("Hello " + name)

# Ask the user to enter their age tell them how old they will be in 15 years time
age = int(raw_input("What is your age? "))
future_age = age + 15
print(future_age)


# Combine the two input statements above and print out the message "Hello, , you are currently years old. In 15 years time you will be <age_in_15_years_time>"
print ("You are currently " + str(age) + " years old. In 15 years you will be " + str(future_age))

# Ask the user to enter their hometown, print it out in uppercase letters
hometown = raw_input("What is your hometown? ")
print(hometown.upper())

#Ask for the user's name, if they are called "Bob", print "Welcome Bob!"
name = raw_input("What is your name? ")

if name.lower() == "bob":
    print("Welcome Bob!")

#Ask for the user's name, if they are not called "Alice", print "You're not Alice!"
username = raw_input("What is your name? ")
if username.lower() != "alice":
    print("You're not Alice")

#Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". If they get it wrong, print "Password failure"
password = raw_input("What is your password? ")
if password == "qwerty123":
    print("You have successfully logged in")
else:
    print("Password failure")

# Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd"
number = raw_input("Enter a number")
if number % 2:
    print("Number is odd")
else
    print("Number is even")

# Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
number_1 = raw_input("Please enter your first number: "))
number_2 = raw_input("Please enter your second number: "))
total = number_1 + number_2

if total > 21:
    print("Bust")
else:
    print("Safe")
