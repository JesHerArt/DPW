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
        self._title = "Skylanders Spyro's Adventure Characters"
        
        self.__head = '''
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
        
        self.__body = '''
        
        '''
        
        self._content = '''
        
        '''
        
        self.__close = '''
        </div>
        <footer>
            <p>&copy; 2015 Jessica J. Hernandez - Student at Full Sail University<br>All content taken from: <a href="https://www.skylanders.com/characters#fire/ssa" target="_blank">https://www.skylanders.com/characters#fire/ssa</a></p>
        </footer>
    </body>
</html>
        '''
    
    def print_out(self):
        whole_page = self.head + self.body + self._content + self.close
        whole_page = whole_page.format(**locals())
        return whole_page
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, t):
        self._title = t
    
    @property
    def head(self):
        return self.__head
    
    @property
    def body(self):
        return self.__body
    
    @property
    def close(self):
        return self.__close


#CONTENT PAGE CLASS
class ContentPage(Page):
    def __init__(self):
        self.title = "{self.skylander}Skylanders Spyro's Adventure Characters"
        