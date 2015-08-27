'''
Jessica J. Hernandez
August 26, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Dynamic Site Assignment
'''

#ABSTRACT PAGE CLASS
class Page(object):
    def __init__(self):
        self.__title = "Skylanders Spyro's Adventure Characters"
        
        self.head = '''
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link type="text/css" rel="stylesheet" href="css/style.css"/>
        <!--Google Fonts-->
        
    </head>
    <body>
        <div id="container">
        '''
        
        self.body = '''
        
        '''
        
        self.content = '''
        
        '''
        
        self.close = '''
        </div>
        <footer>
            <p>&copy; 2015 Jessica J. Hernandez - Student at Full Sail University<br>All content taken from: <a href="https://www.skylanders.com/characters#fire/ssa" target="_blank">https://www.skylanders.com/characters#fire/ssa</a></p>
        </footer>
    </body>
</html>
        '''


#CONTENT PAGE CLASS
class ContentPage(Page):
    def __init__(self):
        