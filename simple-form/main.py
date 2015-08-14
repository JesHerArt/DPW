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
            full_name = self.request.GET['user']
            email = self.request.GET['email']
            phone = self.request.GET['phone']
            amount = self.request.GET['amount']
            billing = self.request.GET['billing']
            payment = self.request.GET['payment']
            
            p.body = '''
            
            '''
            
            self.response.write(p.print_out())
        else:
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
