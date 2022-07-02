from abc import ABC, abstractmethod
class Bank(ABC):
    @abstractmethod
    def loan(self): pass

    @abstractmethod
    def credit(self): pass

    @abstractmethod
    def debit(self): pass

class HDFC(Bank):
    @property
    def loan(self):
        print("We can Provide 7.5% Interest Loan")
    @property
    def credit(self):
        print("HDFC Provide Credit")  
    @property
    def debit(self):
        print("HDFC Provide Debit")      
    @property
    def card(self):
        print("HDFC Provide Credit Card")    

o=HDFC()
o.loan
o.credit
o.debit
o.card
