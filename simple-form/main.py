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
        p = Page()
        
        if self.request.GET:
            full_name = self.request.GET['full_name']
            email = self.request.GET['email']
            phone = self.request.GET['phone']
            amount = self.request.GET['amount']
            billing = self.request.GET['billing']
            payment = self.request.GET['payment']
            
            headings = ["Name:", "Email:", "Phone:", "Amount:", "Billing:", "Payment:"]
            results = [full_name, email, phone, amount, billing, payment]
            
            p.body = '''
            <h3>Donation Confirmation</h3>
            '''
            
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
                
            p.body += '''
            <h3>Thank you for your support!</h3>
            '''
            
            self.response.write(p.print_out())
        else:
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
