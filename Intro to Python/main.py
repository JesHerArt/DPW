#print "hello world!"
#one line comments
'''
multi line comment
a.k.a. Doc Strings
'''

# use underscores for variables in ptyhon, opposed to camel casing
first_name = "Kermit"
last_name = "The Frog"
#print first_name

#response = raw_input("Enter your name:  ")
#print "Hello there, ", response

birth_year = 1992
current_year = 2015
age = current_year - birth_year
#print "You are " + str(age) + " years old"
# int(var)

# ++ and -- do not exists in python

'''
JS.....
if(condition){
    //do stuff
    }
python.....
if condition:
    #stuff to do
'''

# CONDITIONALS
budget = 90

if budget > 100:
    brand = "nike"
    print "Yay! We can buy cool " + brand + " shoes"
elif budget > 50:
    #print "We can at least get some generic sneakers"
    pass
else:
    #print "No cool shoes for me."
    pass

# ARRAYS & DICTIONARIES
characters = ["Leia","Luke","Chewy","Lando"]
characters.append("Obi Won")
#print characters[0]

movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]

# LOOPS - WHILE AND FOR
# while loop used when the amount of times to loop through is unknown
'''
i=0
while i<9:
    print "The count is: ", i
    i = i+1

#for loop
for i in range(0,10):
    print "The count is: ", i
    i += 1

#"for each" loop
rappers = ["Tupac","Nas","Biggie Smalls"]
for r in rappers:
    print r
'''

# FUNCTIONS
def calcArea(h, w):
    area = h * w
    return area

a = calcArea(20, 40);
#print "Area: " + str(a)


weight = 200
height = 63
message = '''
Your height is {height} and your weight is {weight}
'''
message = message.format(**locals())
print message

title = "Contact Us"
body = "You can contact us at contact@us.com"

message2 = '''
<!doctype html>
<html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        {body}
    </body>
</html>
'''
message2 = message2.format(**locals())
print message2
