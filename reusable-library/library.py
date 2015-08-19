'''
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
'''

class Composer(object):
    def __init__(self):
        self.__perimeter = 0
        self.__name = ""
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n
        print n
    
    @property
    def perimeter(self):
        return self.__perimeter
    
    @perimeter.setter
    def perimeter(self, p):
        self.__perimeter = p
        print p
    
    def calc_perimeter(self, l, w):
        p = (int(l) * 2) + (int(w) * 2)
        return p

class Dog(object):
    def __init__(self):
        pass