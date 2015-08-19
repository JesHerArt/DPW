'''
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
'''

class Household(object):
    def __init__(self):
        self.__perimeter = 0
        self.__name = ""
    
    def calc_perimeter(self, l, w):
        p = (int(l) * 2) + (int(w) * 2)
        return p
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
    
    @property
    def perimeter(self):
        return self.__perimeter
    
    @perimeter.setter
    def perimeter(self, p):
        self.__perimeter = p

class Dog(object):
    def __init__(self):
        self.__name = ""
        self.__breed = ""
    
    def randomizer(self):
        pass
    
    def names(self, num):
        dog_names = []
        return dog_names[num]
    
    def small_breed(self, num):
        breeds = []
        return breeds[num]
    
    def large_breed(self, num):
        breeds = []
        return breeds[num]
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
    
    @property
    def breed(self):
        return self.__name
    
    @breed.setter
    def breed(self, n):
        self.__breed = n