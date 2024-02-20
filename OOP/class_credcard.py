
class CreditCard:
    '''represents a basic consumer credit card'''

    def __init__(self, acnt, limit):
        self._acnt = acnt
        self._limit = limit
        self._balance = 0 #assumers zero balance owed at object construction

    def get(self, field):
        if field=="acnt":
            return self._acnt        
        elif field=="limit":
            return self._limit       
        elif field=="balance":
            return self._balance      
        else:
            print("not a valid field")
            return None

    def charge(self, price):
        if self._balance + price > self._limit:
            return False
        else:
            self._balance = self._balance + price
            return True
    
    def make_payment(self, payment):
        self._balance = self._balance - payment

