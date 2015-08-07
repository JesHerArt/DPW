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
favorite_number = int(raw_input("  2. Enter your favorite number:  "))
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
color_choice = raw_input("  9. Enter the color that you prefer (red, blue or green):  ")

if color_choice == "red":
    money_amount = colors["red"]
elif color_choice == "blue":
    money_amount = colors["blue"]
elif color_choice == "green":
    money_amount = colors["green"]

car = raw_input(" 10. Enter the Make and Model of your favorite car:  ")
cereal = raw_input(" 11. Enter the name of any cereal:  ")
element = raw_input(" 12. Enter the name of any element on the Periodic Table:  ")
unusual_job = raw_input(" 13. Enter the name of an uncommon job:  ")

addition = 0
string_of_numbers = ""
for i in range(0,len(winning_numbers)):
    addition += winning_numbers[i]
    
    if i == len(winning_numbers) - 1:
        string_of_numbers += "and " + str(winning_numbers[i])
    else:
        string_of_numbers += str(winning_numbers[i]) + ", "
    
    i += 1    

if addition <= 66:
    money_amount += favorite_number
elif addition >= 67 & addition <= 132:
    money_amount *= favorite_number
elif addition >= 133 & addition <= 200:
    money_amount = addition / favorite_number

def jobCreator(adj,job):    
    new_job = adj + " " + job
    return new_job

wacky_job = jobCreator(adjective,unusual_job);

exclamations = ""
for i in range(0,favorite_number):
    exclamations += "!"
    i += 1

raw_input("\n\nYour new diary entry was submitted. Press enter to continue.\n\n")

import datetime
d = datetime.datetime.now()
print ("\t|\n\t|\tDATE: %s/%s/%s" % (d.month, d.day, d.year))

diary_entry = '''\t|
\t|\tMy dearest {color_choice} diary, 
\t|
\t|\tToday has been the most peculiar day I've had in a long time...
\t|
\t|\tI won the lotto{exclamations}
\t|
\t|\tIt all started when I was feelling {feeling1} and I decided to go
\t|\tto the {cartoon_character} gas station to fill up my tank. As I
\t|\twas about to grab some {candy}, I thought about using the money
\t|\tto buy a lotto ticket instead because I was having this {feeling2}
\t|\tfeeling that I should play the numbers: {string_of_numbers}.
\t|\tAs I was waiting for it to be 6PM, I had a strange urge to eat
\t|\ta bowl of {dog_food} dog food. Then the time had come and the
\t|\twinning numbers were displayed.. and it was I who had won
\t|\tthe {money_amount} million dollars!!! First thing that came to mind
\t|\twas that I had to go buy my dream car, a {car}. I immediately
\t|\traced down to the nearest dealer to go buy my new car. After, as I'm
\t|\tdriving down the {cereal} express way to break in my new car, I
\t|\thear a sudden {element} explosion between the two vehicles driving right
\t|\tbehind me and that's when... I woke up and realized that I in fact
\t|\tdid NOT win the lotto and I most definitely was not able to buy my
\t|\tbeloved {car}. Talk about a bubble buster! Therefore, I need to
\t|\tcontinue living my life as a {wacky_job}, which will
\t|\tprobably never earn me enough anyways. So please {color_choice} diary...
\t|\tnever speak of this "day" to me ever again.
\t|
\t|\tStay awesome Gotham!
\t|

'''

diary_entry = diary_entry.format(**locals())
print diary_entry

raw_input("Thank you for playing. Press enter to exit.\n\n")