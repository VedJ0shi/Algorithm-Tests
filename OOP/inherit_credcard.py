import class_credcard

class BankCard(class_credcard.CreditCard):
    '''represents a bank card with method to charge interest on outstanding balance'''

    def __init__(self, acnt, limit, rate):
        super().__init__(acnt, limit) #calls inherited constructor of parent class
        self._rate = rate #interest rate


    def assess(self):
        if self._balance > 0:
            self._balance = self._balance*(1 + self._rate)
        if not super().charge(0): 
            self._rate = self._rate*1.1 #raise next month's interest rate for exceeding limit










