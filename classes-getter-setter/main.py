import webapp2
from pages import Page #from {package} import {class}

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        p.title = "My Page!"
        p.css = "css/styles.css"
        p.body = "Miss Piggy likes Kermit the Frog"
        self.response.write(p.whole_page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
