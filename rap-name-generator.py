# Guided Exploration No. 3
# Colton Sahota

# This imports the random library
import random

# This creates an empty list called possible_names
possible_names = []

# This opens the rap-names-output.txt file and allows this program to write in it
outputFile = open('rap-names-output.txt', 'w')

# This tells python to open the rap-names.txt file and assign it to the variable dataFile, then do stuff with it
with open('rap-names.txt', 'r') as dataFile:
    # This is iterates through each line of the file
    for name in dataFile:
        # This removes the line feed from the line, and then puts the name in the possible_names list
        possible_names.append(name.rstrip())

# This asks the user how many names they want and stores the entered value in the variable count
count = int(input('How many rap names would you like to create? '))
# This asks the user how many parts they want in each name and then stores this value in the variable parts
parts = int(input('How many parts should the name contain? '))

# This is a counted loop that will execute count times (count is the value that the user entered above)
for i in range(count):
    # This creates an empty list named name_parts
    name_parts = []
    # This is a counted loop that will execute parts times (parts is the value that the user entered above)
    for j in range(parts):
        # This takes a random element from the possible_names list and adds it to the name_parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # This joins the name parts together and writes the full name to the rap-names-output.txt file
    outputFile.write(f"{' '.join(name_parts)}\n")
    # This joins the name parts together and prints the full name in the terminal
    print(f"{' '.join(name_parts)}")

# This closes the rap-names-output.txt file
outputFile.close()
