'''
Jessica J. Hernandez
August 11, 2015
Design Patterns for Web Programming
201508-01 | Professor Wainman
Simple Form Assignment
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
        
        """
        
        self.__close = """
        </div>
    </body>
</html>
        """
    
    @property
    def title(self):
        return self.__title

class ResultPage(object):
    def __init__(self):
        pass