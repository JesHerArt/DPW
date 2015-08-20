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
        self.__first_name = ""
        self.__last_name = ""
    
    # METHODS
    def calc_area(self, l, w):
        a = int(l) * int(w)
        return a
    
    # FIRST NAME - GET/SET
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, n):
        self.__first_name = n.title()
    
    # HOUSEHOLD NAME - GET/SET
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, n):
        self.__last_name = n.title()
    
    # HOUSEHOLD AREA - GET/SET
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
        self.__image = ""
    
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
        image = ["small/maltese.jpg","small/french-bulldog.jpg","small/chihuahua.jpg","small/boston.jpg","small/miniature-pinscher.jpg","small/yorkie.jpg","small/shihtzu.jpg","small/papillon.jpg","small/dachshund.jpg","small/pug.jpg"]
        self.image = image[num]
        return breeds[num]
    
    def large_breed(self, num):
        breeds = ["Boxer","Golden Retriever","Shetland Sheepdog","Siberian Husky","American Bulldog","German Shepherd","Dalmatian","Labrador Retriever","Rottweiler","Shiba Inu"]
        image = ["large/boxer.jpg","large/golden.jpg","large/shetland.jpg","large/husky.jpg","large/american-bulldog.jpg","large/german-shepherd.jpg","large/dalmatian.jpg","large/labrador.jpg","large/rottweiler.jpg","large/shiba-inu.jpg"]
        self.image = image[num]
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
    
    # DOG IMAGE - GET/SET
    @property
    def image(self):
        return self.__image
    
    @image.setter
    def image(self, i):
        self.__image = i