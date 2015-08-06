'''
Jessica J. Hernandez | ID: 0004631401
Full Sail University
Design Patterns for Web Programming | 201508-01
Week 1 | MadLib
'''

welcome_message = '''
*****************************************************************
*\t\t\t\t\t\t\t\t*
* \tThank you for playing Jessica's MadLib mini game!\t*
*\tIn this game you be asked a series of questions  \t*
*\tand a diary entry will be compiled based on the  \t*
*\tanswers you provided.\t\t\t\t\t*
*\t\t\t\t\t\t   Enjoy!\t*
*\t\t\t\t\t\t\t\t*
*****************************************************************
'''

print welcome_message

raw_input("Your questions will now begin. Press enter to continue.\n\n")

adjective = raw_input("  1. Enter an adjective:  ")
exclamations = int(raw_input("  2. Enter your favorite number:  "))
feeling1 = raw_input("  3. Enter a feeling:  ")
cartoon_character = raw_input("  4. Enter the name of a cartoon character:  ")
candy = raw_input("  5. Enter the name of your favorite candy:  ")
feeling2 = raw_input("  6. Enter another feeling:  ")

print "  7. You will now enter four different numbers as prompted"
winning_numbers = []
winning_numbers.append(int(raw_input("\tEnter a number between 1-50:  ")))
winning_numbers.append(int(raw_input("\tEnter a second number between 1-50:  ")))
winning_numbers.append(int(raw_input("\tEnter a third number between 1-50:  ")))
winning_numbers.append(int(raw_input("\tEnter a fourth number between 1-50:  ")))

dog_food = raw_input("  8. Enter the name of a brand of dog food:  ")

colors = dict()
colors = {"red":10,"blue":20,"green":30}
color_choice = raw_input("  9. Which color do you prefer? red, blue or green?:  ")

if color_choice == "red":
    money_amount = colors["red"]
elif color_choice == "blue":
    money_amount = colors["blue"]
elif color_choice == "green":
    money_amount = colors["green"]