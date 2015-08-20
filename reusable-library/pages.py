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
        <link href='http://fonts.googleapis.com/css?family=Expletus+Sans:400,700,500italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Lato:400,700,900,300' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <div id="container">
        """
        
        self.__body = """
            <header>
                <h1>Miami-Dade County Animal Shelter</h1>
                <h2>Proudly supported by the ASPCA</h2>
            </header>
            
            <hr>
            
            <div id="content">
                <h3>Dog Adoption Suggestion Form</h3>
                <h4>Find the perfect dog for your type of home!</h4>
                
                <form id="adopt_suggest_form" method="GET">
                    
                    <p>Please fill out all form fields.</p>
                    
                    <hr>
                    
                    <div class="form_group">
                        <label for="full_name">Your Name</label><br />
                        <div class="inputs">
                            <input type="text" class="input" id="first_name" name="first_name" placeholder="First Name" required />
                            <input type="text" class="input" id="last_name" name="last_name" placeholder="Last Name" required />
                        </div>
                    </div>
                    
                    <div class="form_group">
                        <label for="backyard">Do you have a backyard?</label>
                        <div id="radio_buttons" class="inputs">
                            <label for="yes"><input type="radio" id="yes" name="backyard" value="yes" checked /> Yes</label>
                            <label for="no"><input type="radio" id="no" name="backyard" value="no" /> No</label>
                        </div>
                    </div>
                    
                    <div class="form_group">
                        <label for="area">What is the length x width of your backyard? (in feet)</label><br />
                        <div class="inputs">
                            <span>Length: <input type="number" id="length" name="length" class="area" placeholder="--" min="0" max="999" required /> ft.</span>
                            <span id="mid"> x </span>
                            <span>Width: <input type="number" id="width" name="width" class="area" placeholder="--" min="0" max="999" required /> ft.</span>
                        </div>
                    </div>
                    
                    <hr>
                    
                    <div class="form_group">
                        <input type="submit" id="submit_form" class="btn" value="Submit" />
                    </div>
                </form>
            </div>
        """
        
        self.__close = """
        </div>
        <footer>
            <p>&copy; 2015 Jessica J. Hernandez - Student at Full Sail University</p>
        </footer>
        <script src="js/jquery.js"></script>
        <script src="js/main.js"></script>
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
        self.__title = "Miami-Dade County Animal Shelter | Dog Adoption Suggestion Form Results"
        self.__head = """
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link type="text/css" rel="stylesheet" href="css/style.css"/>
        <!--Google Fonts-->
        <link href='http://fonts.googleapis.com/css?family=Expletus+Sans:400,700,500italic' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Lato:400,700,900,300' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <div id="container">
            <header>
                <h1>Miami-Dade County Animal Shelter</h1>
                <h2>Proudly supported by the ASPCA</h2>
            </header>
            
            <hr>
        """
        
        self.__body = ""
        
        self.__close = """
        </div>
        <footer>
            <p>&copy; 2015 Jessica J. Hernandez - Student at Full Sail University<br />
            All images used are from: https://pixabay.com/</p>
        </footer>
        <script src="js/jquery.js"></script>
        <script src="js/main.js"></script>
    </body>
</html>
        """
    
    def print_out(self):
        whole_page = self.head + self.body + self.close
        whole_page = whole_page.format(**locals())
        return whole_page
    
    def generate_body(self, first_name, last_name, area, dog, image):
        if area < 400:
            backyard = "Even with having a home that has no backyard, "
        elif area >= 400:
            backyard = """Since you have a home with a """ + str(area) + """ sq.ft. backyard, """
        
        self.body = """
            <div id="content">
                <h3>Dog Adoption Suggestion Form Results</h3>
                <h4>Find the perfect dog for your type of home!</h4>
                
                <br />
                <p class="result" id="greeting">Hi, """ + first_name + """!</p>
                <p class="result">Thank you for using our Dog Adoption Suggestion Form. We're really happy to hear that you're choosing to adopt a new furry friend for your home.</p>
                <p class="result">""" + backyard + """ the perfect match for the """ + last_name + """ household would definitely have to be:</p>
                <p class="result" id="dog">""" + dog + """</p>
                <img src="images/""" + image + """ " />
                <input type="button" id="adopt" class="btn result" value="Adopt Me Now!" /> or 
                <input type="button" id="again" class="btn result" value="Refresh Search" />
            </div>
        """
    
    @property
    def title(self):
        return self.__title
    
    @property
    def head(self):
        return self.__head
    
    @property
    def body(self):
        return self.__body
    
    @body.setter
    def body(self, b):
        self.__body = b
    
    @property
    def close(self):
        return self.__close