'''
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
'''

class Household(object):
    def __init__(self):
        self.__area = 0
        self.__name = ""
    
    # METHODS
    def calc_area(self, l, w):
        a = int(l) * int(w)
        return a
    
    # HOUSEHOLD NAME - GET/SET
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
    
    # HOUSEHOLD PERIMETER - GET/SET
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, a):
        self.__area = a


import random
class Dog(object):
    def __init__(self):
        self.__name = ""
        self.__breed = ""
    
    # METHODS
    def randomizer(self):
        return random.randint(0,9)
    
    def dog_picker(self, b, a):
        self.name = self.names(self.randomizer())
        
        if b == "no":
            self.breed = self.small_breed(self.randomizer())
        elif (b == "yes") & (a < 400):
            self.breed = self.small_breed(self.randomizer())
        elif (b == "yes") & (a >= 400):
            self.breed = self.large_breed(self.randomizer())
        
        return self.name + " the " + self.breed
    
    def names(self, num):
        dog_names = ["Lucky","Sparky","Coco","Buddy","Honey","Milo","Sassy","Shadow","Rocky","Riki"]
        return dog_names[num]
    
    def small_breed(self, num):
        breeds = ["Maltese","French Bulldog","Chihuahua","Boston Terrier","Miniature Pinscher","Yorkie","Shih Tzu","Papillon","Dachshund","Pug"]
        return breeds[num]
    
    def large_breed(self, num):
        breeds = ["Boxer","Golden Retriever","Shetland Sheepdog","Siberian Husky","American Bulldog","German Shepherd","Dalmation","Labrador Retriever","Rottweiler","Shiba Inu"]
        return breeds[num]
    
    # DOG NAME - GET/SET
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
    
    # DOG BREED - GET/SET
    @property
    def breed(self):
        return self.__breed
    
    @breed.setter
    def breed(self, n):
        self.__breed = n