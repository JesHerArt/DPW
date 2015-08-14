'''
Jessica J. Hernandez
August 11, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Simple Form Assignment
'''

class Page(object):
    def __init__(self):
        self.title = "Sea Turtle Donation Form"
        self.css = "css/style.css"
        self.head = '''
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link type="text/css" rel="stylesheet" href="{self.css}"/>
    </head>
    <body>
        <div id="container">
        '''
        
        self.body = '''
        
        '''
        
        self.close = '''
        </div>
    </body>
</html>
        '''
        
    def print_out(self):
        page_construct = self.head + self.body + self.close
        page_construct = page_construct.format(**locals())
        return page_construct