class Wallet:

    #first thing to run when you make a new class
    #outline required user-provided input values here
    def __init__(self,initial_amount=0):
        #save the user-provided initial_amount as an attribute
        #self refers any project you are working with
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
                return 'not enough money'
        else:
            self.balance = self.balance - amount
            return f'remaining balance: {self.balance}'
        
    def add_cash(self, amount):
         self.balance = self.balance + amount
         return f'new balance of: {self.balance}'

        #__repr__ method
        #changes how the object is looked when it is printed out
        #The presence of the self keyword allows me to access or
        #modify class attributes within this function
            
    def __repr__(self):
        return f'Wallet with balance of: ${self.balance}'

if __name__ == '__main__':
    Wallet1 = Wallet(100)
    Wallet2 = Wallet(50)
    Wallet3 = Wallet(3000)
    print (Wallet1)
    print(Wallet2)
    print(Wallet3)

 

