
 # Ask the user to enter a number that's not from -10 to 10. If they enter -10 to 10, ask them to enter another number. If they do NOT enter a number from -10 to 10, quit and print "Good job".

# userNumber = int(input("Enter a number that's NOT -10 to 10"))

# while userNumber > -10 and userNumber < 10:
# 	userNumber2 = int(input("Try again"))
# print("good job")


# Ask the user to enter a name to invite to their party until they enter 'q' to quit. Save all of the names in a string with hyphens between them.

birthdayGirl = input("Enter a name for the birthday party")
nameList = ""
while(birthdayGirl != 'q'):
	nameList = nameList + " - " + birthdayGirl 
	birthdayGirl = input("Enter a name for the birthday party")
print(nameList)
