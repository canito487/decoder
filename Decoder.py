__author__ = 'alex.hernandez'

import sys
import os
import urllib


# Create the restart function to restart the program

def restart_program():
	python = sys.executable
	os.execl(python, python, *sys.argv)


# Ask the user which type of encoding
print ("\n")

# Store the type of encoding
answer = raw_input("What type of encoding do you have? \n 1 = Base64 \n 2 = Hex \n 3 = URL Encoding \n > ")

# Run the function that corresponds to the type of encoding using conditional statements
if answer == "1":
	sixtyFour = raw_input("Please paste encoded string: ")
	print ("\n Your clear text string is: \n")
	print sixtyFour.decode("base64")
	print ("\n")
elif answer == "2":
	hex1 = raw_input("Please paste encoded string: ")
	print ("\n Your clear text string is: \n")
	print hex1.decode("hex")
	print ("\n")

elif answer == "3":
	url1 = raw_input("Please paste encoded string: ")
	print ("\n Your cleartext string is: \n")
	print urllib.unquote(url1).decode('utf8')
	print ("\n")

else:
	print ("Please type in a correct answer!")

# Call the restart function
print "PRESS CTRL + C AT ANYTIME TO CLOSE THE PROGRAM"
restart_program()
