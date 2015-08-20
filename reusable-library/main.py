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
            h.first_name = self.request.GET["first_name"]
            h.last_name = self.request.GET["last_name"]
            h.area = h.calc_area(self.request.GET["length"], self.request.GET["width"])
            
            #create the instance of a dog
            d = Dog()
            
            rp = ResultPage()
            rp.generate_body(h.first_name, h.last_name, h.area, d.dog_picker(self.request.GET["backyard"], h.area), d.image)
            self.response.write(rp.print_out())
        else:
            #if no GET key/value pairs exist, print out the standard form page
            fp = FormPage()
            self.response.write(fp.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
