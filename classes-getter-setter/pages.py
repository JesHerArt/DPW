class Page(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.__css = "css/styles.css"
        
        self.head = """
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type=""text/css />
    </head>
    <body>
        """
        
        self.__body = "Welcome to my OOP Python page!"
        
        self.close = """
    </body>
</html>
        """
        
        self.whole_page = ""
    
    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())
    
    # BODY
    @property #getter - needed for locals in the self.head component
    def body(self):
        return self.__body
    
    @body.setter #setter/decorator
    def body(self, new_body):
        self.__body = new_body
        self.update()
    
    # TITLE
    @property #getter - needed for locals in the self.head component
    def title(self):
        return self.__title
    
    @title.setter #setter/decorator
    def title(self, new_title):
        self.__title = new_title
        self.update()
    
    # CSS
    @property #getter - needed for locals in the self.head component
    def css(self):
        return self.__css
    
    @css.setter #setter/decorator
    def css(self, new_css_file):
        self.__css = new_css_file
        self.update()