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
            value = self.request.GET["skylander"]
            p = ContentPage()
            s = Data()
            
            print p._title
            
            for i in range(len(p._skylanders)):
                if(value == p._skylanders[i]):
                    p.title = s.skylanders[i].name.title() + " | "
                    p.nav_builder(p._skylanders, s.skylanders[i])
                    p.content_builder(s.skylanders[i])
            
            self.response.write(p.print_out())
        else:
            p = Page()
            p.nav_builder(p._skylanders)
            #if no GET key/value pairs exist, print out a standard page
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
