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
        self._skylanders = ['eruptor','gill grunt', 'terrafin', 'stealth elf', 'warnado', 'trigger happy', 'spyro', 'hex']
        self._title = "Skylanders Spyro's Adventure Characters"
        
        self.__head = '''
<!doctype html>
<html>
    <head>
        <title>{self._title}</title>
        <link type="text/css" rel="stylesheet" href="css/style.css"/>
        <!--Google Fonts-->
        
    </head>'''
        
        self.__body = '''
    <body>
        <div id="container">
            <header>
                <a href="/"><h1>Skylanders Spyro's Adventure</h1></a>
            </header>'''
        
        self._navbar = ''' '''
        
        self._content = '''
            <div id="content">
                <h1>Skylander Characters</h1>
                <p>This site is dedicated to some of the characters from the Skylanders Spyro's Adventure video game.</p>
                <p>By clicking the links on the navbar you'll be able to learn details about some of the top characters from Spyro's Adventure relating to their background information, which versions they are available in, and even the standard power stats they possess. Each Skylander has their own element and therefore you can see one of each element to get to know a little bit about each one.</p>
            </div>
        '''
        
        self.__close = '''
        </div>
        <footer>
            <p>&copy; 2015 Jessica J. Hernandez - Student at Full Sail University<br>Data content from: <a href="https://www.skylanders.com/characters#fire/ssa" target="_blank">www.skylanders.com</a></p>
        </footer>
    </body>
</html>
        '''
    
    def print_out(self):
        whole_page = self.head + self.body + self._navbar + self._content + self.close
        whole_page = whole_page.format(**locals())
        return whole_page
    
    def nav_builder(self, chars):
        self._navbar = '''
            <nav>
                <ul>'''
        
        for item in chars:
            self._navbar += '''
                    <a href='?skylander=''' + item + ''''><li>''' + item.title() + '''</li></a>'''        
        
        self._navbar += '''
                </ul>
            </nav>'''
    
    @property
    def head(self):
        return self.__head
    
    @property
    def body(self):
        return self.__body
    
    @property
    def close(self):
        return self.__close
    
    @property
    def title(self):
        pass
    
    @title.setter
    def title(self, t):
        self._title = t + self._title


#CONTENT PAGE CLASS
class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__() #Page.__init__()        
    
    def nav_builder(self, chars, s):
        self._navbar = '''
            <nav>
                <ul>'''
        
        for item in chars:
            if( item == s.name ):
                self._navbar += '''
                    <a href='?skylander=''' + item + ''''><li class="active">''' + item.title() + '''</li></a>''' 
            else:
                self._navbar += '''
                    <a href='?skylander=''' + item + ''''><li>''' + item.title() + '''</li></a>'''        
        
        self._navbar += '''
                </ul>
            </nav>'''
    
    def content_builder(self, s):
        self._content = '''
            <div id="content">
                <h2>''' + s.name.title() + '''</h2>
            </div>
        '''