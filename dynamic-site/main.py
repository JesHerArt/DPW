'''
Jessica J. Hernandez
August 26, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Dynamic Site Assignment
'''

import webapp2
from pages import Page, ContentPage
from data import Skylander, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        #conditional to verify if any GET key/value pairs exists
        if self.request.GET:
            skylander = self.request.GET["skylander"]
            p = ContentPage()
            
            if(skylander == "eruptor"):
                s = Data()
                s.skylanders[0]
            elif(skylander == "gill"):
                s = Data()
                s.skylanders[1]
            elif(skylander == "terra"):
                s = Data()
                s.skylanders[2]
            elif(skylander == "elf"):
                s = Data()
                s.skylanders[3]
            elif(skylander == "warnado"):
                s = Data()
                s.skylanders[4]
            elif(skylander == "trigger"):
                s = Data()
                s.skylanders[5]
            elif(skylander == "spyro"):
                s = Data()
                s.skylanders[6]
            elif(skylander == "hex"):
                s = Data()
                s.skylanders[7]
            
            self.response.write('print out dynamic page based on get value')
        else:
            #if no GET key/value pairs exist, print out a standard page
            self.response.write('print standard page')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
