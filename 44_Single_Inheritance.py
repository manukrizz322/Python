class Nokia:
    company="Nokia India"
    website="www.nokia-india.com"

    @property
    def contact_details(self):
        print("Address :Cherry Road,Near Bus Stand,Salem")

class Nokia1100(Nokia):
    def __init__(self):
        self.name="Nokia 1100"
        self.year=1998

    @property
    def product_details(self):
        print("Name    : ",self.name)    
        print("Year    : ",self.year)
        print("Company : ",self.company)
        print("Website : ",self.website)


mobile=Nokia1100()
mobile.product_details
mobile.contact_details       