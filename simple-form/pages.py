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
        self.header_img = "images/baby_turtle.jpg"
        self.head = '''
<!doctype html>
<html>
    <head>
        <title>{self.title}</title>
        <link type="text/css" rel="stylesheet" href="{self.css}"/>
        <!--Google Font-->
        <link href='http://fonts.googleapis.com/css?family=Alegreya+Sans+SC:900' rel='stylesheet' type='text/css'>
        <link href='http://fonts.googleapis.com/css?family=Roboto:400,500,700' rel='stylesheet' type='text/css'>
    </head>
    <body>
        <div id="container">
        '''
        
        self.header = '''
            <header>
                <img src="{self.header_img}" alt="Turtle hatching on its way to the sea" title="Turtle hatching on its way to the sea" />
                <h1>Sea Turtle Donation Form</h1>
                <h2>Help protect our loving sea turtles from becoming endangered any further. Every donation helps contibute to the rehabilitation costs for Sea Turtles all around the world.</h2>
            </header>
        '''
        
        self.body = '''
            <form method="GET" id="donation_form">
                <div class="form-group">
                    <div class="left-col">
                        <label for="full_name">Name</label>
                    </div>
                    <div class="right-col">
                        <input class="input" type="text" id="full_name" name="full_name" placeholder="Full Name" required />
                    </div>
                </div>
                
                <div class="form-group">
                    <div class="left-col">
                        <label for="email">Email</label>
                    </div>
                    <div class="right-col">
                        <input class="input" type="email" id="email" name="email" placeholder="Email Address" required />
                    </div>
                </div>
                
                <div class="form-group">
                    <div class="left-col">
                        <label for="phone">Phone</label>
                    </div>
                    <div class="right-col">
                        <input class="input" type="text" id="phone" name="phone" placeholder="(000) 000-0000" required />
                    </div>
                </div>
                
                <div class="form-group">
                    <div class="left-col">
                        <label for="amount">Donation Amount</label>
                    </div>
                    <div class="right-col">
                        <div class="billing_option"><input type="radio" name="amount" value="$5.00" /> <p class="radio-option">$5.00</p></div>
                        <div class="billing_option"><input type="radio" name="amount" value="$10.00" /> <p class="radio-option">$10.00</p></div>
                        <div class="billing_option"><input type="radio" name="amount" value="$20.00" checked /> <p class="radio-option">$20.00</p></div>
                        <div class="billing_option"><input type="radio" name="amount" value="$30.00" /> <p class="radio-option">$30.00</p></div>
                        <div class="billing_option"><input type="radio" name="amount" value="$50.00" /> <p class="radio-option">$50.00</p></div>
                    </div>
                </div>
                
                <div class="form-group">
                    <div class="left-col">
                        <label for="billing">Billing Frequency</label>
                    </div>
                    <div class="right-col">
                        <select name="billing" required>
                            <option select="selected" value="select">Select Option</option>
                            <option id="weekly_billing" value="Weekly">Weekly</option>
                            <option id="monthly_billing" value="Monthly">Monthly</option>
                            <option id="yearly_billing" value="Yearly">Yearly</option>
                        </select>
                    </div>
                </div>
                
                <div class="form-group">
                    <div class="left-col">
                        <label for="payment">Payment Option</label>
                    </div>
                    <div class="right-col payment">
                        <div class="payment_option"><input type="radio" name="payment" value="Credit Card" checked /> <p class="radio-option">Credit Card</p></div>
                        <div class="payment_option"><input type="radio" name="payment" value="PayPal" /> <p class="radio-option">PayPal</p></div>
                        <div class="payment_option"><input type="radio" name="payment" value="Google Wallet" /> <p class="radio-option">Google Wallet</p></div>
                        <hr>
                        <div class="payment_option"><input type="radio" name="payment" value="Cash" /> <p class="radio-option">Cash (Send my invoice by mail)</p></div>
                    </div>
                </div>
                
                <div class="form-group">
                    <div class="left-col"></div>
                    <div class="right-col">
                        <input class="btn" type="submit" value="Submit" />
                    </div>
                </div>
            </form>
        '''
        
        self.close = '''
        </div>
    </body>
</html>
        '''
        
    def print_out(self):
        page_construct = self.head + self.header + self.body + self.close
        page_construct = page_construct.format(**locals())
        return page_construct