'''
Jessica J. Hernandez
August 26, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Dynamic Site Assignment
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        #conditional to verify if any GET key/value pairs exists
        if self.request.GET:
            
            self.response.write('print out dynamic page based on get value')
        else:
            #if no GET key/value pairs exist, print out a standard page
            self.response.write('print standard page')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
