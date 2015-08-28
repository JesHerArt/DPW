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
        <link href='https://fonts.googleapis.com/css?family=Cabin:400,700' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Raleway:900' rel='stylesheet' type='text/css'>
    </head>'''
        
        self.__body = '''
    <body>
        <div id="container">
            <header>
                <h1><a href="/">Skylanders Spyro's Adventure</a></h1>
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
                <p id="sl_description"><img class="char_img" src="images/characters/''' + s.image + '''" alt="''' + s.name.title() + ''' Image" title="''' + s.name.title() + ''' Image" /> ''' + s.description + '''</p>
                <hr>
                <h3>Character Versions:</h3>
                <p>'''
        
        for i in range(len(s.char_versions)):
            if(i == len(s.char_versions)-1):
                self._content += s.char_versions[i]
            else:
                self._content += s.char_versions[i] + " | "
        
        self._content += '''
            <hr>
            <h3 class="element"><img class="element_img" src="images/elements/''' + s.el_img + '''" alt="" title="" />''' + s.element + ''' Element</h3>
            <hr>
            <h3>Power Stats:</h3>
            <div class="stats">'''
        
        for i in range(len(s.power_stats)):
            if(i==0):
                self._content += '''<div class="stat" id="power" style="width:''' + str(s.power_stats[i]) + '''%;">Power</div><div class="percentage">''' + str(s.power_stats[i]) + '''%</div>'''
            if(i==1):
                self._content += '''<div class="stat" id="armor" style="width:''' + str(s.power_stats[i]) + '''%;">Armor</div>'''
            if(i==2):
                self._content += '''<div class="stat" id="agility" style="width:''' + str(s.power_stats[i]) + '''%;">Agility</div>'''
            if(i==3):
                self._content += '''<div class="stat" id="luck" style="width:''' + str(s.power_stats[i]) + '''%;">Luck</div>'''
        
        self._content += '''
            </div>'''
        
        self._content += '''
            </div>'''