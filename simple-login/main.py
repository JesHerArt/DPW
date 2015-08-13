#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

'''
name
date
class
assignment
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): #function that starts everything. Initializing function a.k.a. catalyst
        page_head = '''
<!doctype html>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''
        
        #page_body = '''<form method="GET">
        #    <label>Name</label><input type="text" name="user" />
        #    <label>Email</label><input type="text" name="email" />
        #    <input type="submit" value="Submit" />'''
        
        page_body = '''
        <a href="?email=mickey@disney.com&user=Mickey">Mickey</a><br/>
        <a href="?email=donald@disney.com&user=Donald">Donald</a><br/>
        <a href="?email=minnie@disney.com&user=Minnie">Minnie</a><br/>
        <a href="?email=pluto@disney.com&user=Pluto">Pluto</a>
        '''
        
        page_close = '''
        </form>
    </body>
</html>'''
        
        if self.request.GET:
            #store info we got from the form
            user = self.request.GET['user']
            email = self.request.GET['email']
            self.response.write(page_head + user + ' ' + email + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #PRINT

#never touch this
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
