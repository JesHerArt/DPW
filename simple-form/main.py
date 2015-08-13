'''
Jessica J. Hernandez
August 11, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Simple Form Assignment
'''

import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
