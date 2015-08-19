'''
Jessica J. Hernandez
August 11, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Simple Form Assignment
'''

import webapp2
from pages import FormPage, ResultPage
from library import Composer, Dog

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        #conditional to verify if any GET key/value pairs exists
        if self.request.GET:
            #pass in the GET values to the classes from library.py
            pass
        else:
            #if no GET key/value pairs exist, print out the standard page
            pass


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
