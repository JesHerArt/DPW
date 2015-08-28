'''
Jessica J. Hernandez
August 26, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Dynamic Site Assignment
'''

#importing the classes from the other python files in the project
import webapp2
from pages import Page, ContentPage
from data import Skylander, Data

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        #conditional to verify if any GET key/value pairs exists
        if self.request.GET:
            #create variable to store the value of the skylander key
            #to then do a check for its' sting value
            value = self.request.GET["skylander"]
            #create instance of the Content Page class
            p = ContentPage() 
            #create an instance of the Data class
            s = Data()
            
            #create for loop of the extent of the skylanders attribute from
            #the content page page class and then set the title using the 
            #page class setters. also use the nav_builder method to pass in
            #the skylanders attribute array from the content page class and 
            #also pass in the skylanders attribute array from the data class
            #which is holding all the data objects. last, use the content_builder
            #method to construct the html depending on which skylander is being
            #viewed and pass in the specific skylander. 
            for i in range(len(p._skylanders)):
                if(value == p._skylanders[i]):
                    p.title = s.skylanders[i].name.title() + " | "
                    p.nav_builder(p._skylanders, s.skylanders[i])
                    p.content_builder(s.skylanders[i])
            
            #print the response to the web brower
            self.response.write(p.print_out())
        else:
            #create an instance of the page super class
            p = Page()
            #use nav builder method with the skylanders attribute to
            #create the full nav bar.
            p.nav_builder(p._skylanders)
            
            #if no GET key/value pairs exist, print out a standard page
            #from the generix page super class.
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
