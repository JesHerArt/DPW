'''
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
'''

import webapp2
from pages import FormPage, ResultPage
from library import Household, Dog

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        #conditional to verify if any GET key/value pairs exists
        if self.request.GET:
            #pass in the GET values to the attributes in the Household class
            h = Household()
            h.name = self.request.GET["name"]
            h.area = h.calc_area(self.request.GET["length"], self.request.GET["width"])
            
            d = Dog()
            #d.dog_picker(self.request.GET["backyard"], h.area)
            
            rp = ResultPage()
            rp.generate_body(h.name, h.area, d.dog_picker(self.request.GET["backyard"], h.area))
            self.response.write(rp.print_out())
        else:
            #if no GET key/value pairs exist, print out the standard page
            fp = FormPage()
            self.response.write(fp.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
