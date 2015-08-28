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
        #public sttribute for the skylanders being used on the site.
        self._skylanders = ['eruptor','gill grunt', 'terrafin', 'stealth elf', 'warnado', 'trigger happy', 'spyro', 'hex']
        
        #protected attibute for the title of the web page.
        self._title = "Skylanders Spyro's Adventure Characters"
        
        #private head attribute for the page super class. the head will not be altered.
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
        
        #private body attribute for the page super class. the body will not be altered.
        self.__body = '''
    <body>
        <div id="container">
            <header>
                <h1><a href="/">Skylanders Spyro's Adventure</a></h1>
            </header>'''
        
        #protected attibute for the navbar of the web page. empty string for now.
        self._navbar = ''' '''
        
        #protected attibute for the content of the web page.
        #this has the html that will be displayed if no key/value pairs are found in GET.
        self._content = '''
            <div id="content">
                <h2>Skylander Characters</h2>
                <p>This site is dedicated to some of the characters from the Skylanders Spyro's Adventure video game.</p>
                <p>By clicking the links on the navbar you'll be able to learn details about some of the top characters from Spyro's Adventure relating to their background information, which versions they are available in, and even the standard power stats they possess. Each Skylander has their own element and therefore you can see one of each element to get to know a little bit about each one.</p>
                <img id="logo" src="images/skylanders_logo.png" alt="Skylanders Logo" title="Skylanders Logo" />
            </div>
        '''
        
        #private close attribute for the page super class. the closing will not be altered.
        self.__close = '''
        </div>
        <footer>
            <p>&copy; 2015 Jessica J. Hernandez - Student at Full Sail University<br>Data content from: <a href="https://www.skylanders.com/characters#fire/ssa" target="_blank">www.skylanders.com</a><br>All images found on Google Images | All Skylanders belong to Activision and not of my own</p>
        </footer>
    </body>
</html>
        '''
    
    # METHODS
    #generic print_out method created to concatenate all elements of the page
    #and is returned when the method is called. also compiles local elements. 
    def print_out(self):
        whole_page = self.head + self.body + self._navbar + self._content + self.close
        whole_page = whole_page.format(**locals())
        return whole_page
    
    #nav builder method is to create the nav bar from the list of skylanders in the
    #skylanders public attribute array.
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
    
    # PAGE HEAD - GET
    #returns the private head attribute
    @property
    def head(self):
        return self.__head
    
    # PAGE BODY - GET
    #returns the private body attribute
    @property
    def body(self):
        return self.__body
    
    # PAGE CLOSE - GET
    #returns the private close attribute
    @property
    def close(self):
        return self.__close
    
    # PAGE TITLE - GET/SET
    #passed
    @property
    def title(self):
        pass
    
    #the setter is used to change the protected title attribute
    @title.setter
    def title(self, t):
        self._title = t + self._title




#CONTENT PAGE CLASS
class ContentPage(Page):
    def __init__(self):
        #this calls the init function from the Page super class
        super(ContentPage, self).__init__() #Page.__init__()        
    
    #polymorphic nav_builder method which overides the orignal from the Page
    #super class and it also takes 3 parameters
    # this method will re-write the nav bar to make sure the current list item is active.
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
    
    #the content builder method takes in the skylander data object from main.py
    #and it this concatenates all the content together to create the content page
    #for the specific skylanders.
    def content_builder(self, s):
        #skylander name, description and image to start off with
        self._content = '''
            <div id="content">
                <h2>''' + s.name.title() + '''</h2>
                <p id="sl_description"><img class="char_img" src="images/characters/''' + s.image + '''" alt="''' + s.name.title() + ''' Image" title="''' + s.name.title() + ''' Image" /> ''' + s.description + '''</p>
                <hr>
                <h3>Character Versions:</h3>
                <p>'''
        
        #for loop used to concatenate the character versions with pipe spacers in between
        for i in range(len(s.char_versions)):
            if(i == len(s.char_versions)-1):
                self._content += s.char_versions[i]
            else:
                self._content += s.char_versions[i] + " | "
        
        #concatenate the skylander element and element image
        self._content += '''
                <hr>
                <h3 class="element"><img class="element_img" src="images/elements/''' + s.el_img + '''" alt="''' + s.element + ''' Element Image" title="''' + s.element + ''' Element Image" />''' + s.element + ''' Element</h3>
                <hr>
                <h3>Power Stats:</h3>
                <div class="stats">'''
        
        #for loop to concatenate the power stats for all 4 stat types and make a bar chart
        for i in range(len(s.power_stats)):
            if(i==0):
                self._content += '''
                    <div class="stat" id="power" style="width:''' + str(s.power_stats[i]  - 15) + '''%;">Power</div><div class="percentage">''' + str(s.power_stats[i]) + '''%</div><br>'''
            if(i==1):
                self._content += '''
                    <div class="stat" id="armor" style="width:''' + str(s.power_stats[i]  - 15) + '''%;">Armor</div><div class="percentage">''' + str(s.power_stats[i]) + '''%</div><br>'''
            if(i==2):
                self._content += '''
                    <div class="stat" id="agility" style="width:''' + str(s.power_stats[i]  - 15) + '''%;">Agility</div><div class="percentage">''' + str(s.power_stats[i]) + '''%</div><br>'''
            if(i==3):
                self._content += '''
                    <div class="stat" id="luck" style="width:''' + str(s.power_stats[i]  - 15) + '''%;">Luck</div><div class="percentage">''' + str(s.power_stats[i]) + '''%</div><br>'''
        
        #the ending divs to close everything
        self._content += '''
                </div>
            </div>'''