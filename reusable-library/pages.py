'''
Jessica J. Hernandez
August 19, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Reusable Library Assignment
'''

class FormPage(object):
    def __init__(self):
        self.__title = "Miami-Dade County Animal Shelter | Dog Adoption Suggestion Form"
        self.__head = """
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link type="text/css" rel="stylesheet" href="css/style.css"/>
        <!--Google Fonts-->
    </head>
    <body>
        <div id="container">
        """
        
        self.__body = """
        TESTING
        """
        
        self.__close = """
        </div>
    </body>
</html>
        """
    
    def print_out(self):
        whole_page = self.head + self.body + self.close
        whole_page = whole_page.format(**locals())
        return whole_page
    
    @property
    def title(self):
        return self.__title
    
    @property
    def head(self):
        return self.__head
    
    @property
    def body(self):
        return self.__body
    
    @property
    def close(self):
        return self.__close

class ResultPage(object):
    def __init__(self):
        pass