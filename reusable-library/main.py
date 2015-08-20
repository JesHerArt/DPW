'''
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
'''

#importing the classes from the other python files in the project
import webapp2
from pages import FormPage, ResultPage
from library import Household, Dog

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        #conditional to verify if any GET key/value pairs exists
        if self.request.GET:
            #pass in the GET values to the attributes in the Household class
            h = Household() #create an instance of the household class
            h.first_name = self.request.GET["first_name"] #set the first name to the first_name GET value
            h.last_name = self.request.GET["last_name"] #set the last name to the last_name GET value
            #set the srea by using the calc_area utility method in the household class
            h.area = h.calc_area(self.request.GET["length"], self.request.GET["width"])
            
            #create an instance of the dog class
            d = Dog()
            
            rp = ResultPage() #create an instance of the results page class
            #use the generate_body utility method to accept arguments of all the attributes
            #needed to generate the message that appears on the results page.
            #the return result of the dog_picker utility method is passed in as an argument as well
            rp.generate_body(h.first_name, h.last_name, h.area, d.dog_picker(self.request.GET["backyard"], h.area), d.image)
            
            #print the result to the browser
            self.response.write(rp.print_out())
        else:
            #if no GET key/value pairs exist, print out the standard form page
            fp = FormPage()#create an instance of the form page class
            self.response.write(fp.print_out()) #print the result to the browser


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
