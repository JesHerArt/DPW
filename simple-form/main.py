'''
Jessica J. Hernandez
August 11, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Simple Form Assignment
'''

import webapp2
from pages import Page #importing the Page class from pages.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page() #instantiating the page class 
        
        #conditional to verify if any GET key/value pairs exists
        if self.request.GET:
            #initializing variables to the values of the GET keys
            full_name = self.request.GET['full_name']
            email = self.request.GET['email']
            phone = self.request.GET['phone']
            amount = self.request.GET['amount']
            billing = self.request.GET['billing']
            payment = self.request.GET['payment']
            
            #creating two arrays. 1 for the heading names and 1 to hold
            #the variables holding the values of the GET keys.
            headings = ["Name:", "Email:", "Phone:", "Donation Amount:", "Billing Frequency:", "Payment Option:"]
            results = [full_name, email, phone, amount, billing, payment]
            
            #altering the body of the p instance of Page
            p.body = '''
            <h3>Donation Confirmation</h3>
            '''
            
            #have a loop to create the result page from submitting the form
            #loop through for the length of the array. heading array is used here also.
            for i in range(0,len(results)):
                p.body += '''
                <div class="result">
                    <div class="left-col">
                        <h4>''' + headings[i] + '''</h4>
                    </div>
                    <div class="right-col">
                        <p>''' + results[i] + '''</p>
                    </div>
                </div>
            '''
            
            #thank you message at the end of the results.
            p.body += '''
            <h3>Thank you for your support!</h3>
            '''
            
            #use the print_out method to print the new page
            self.response.write(p.print_out())
        else:
            #if no GET key/value pairs exist, print out the standard page with the print_out method
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
