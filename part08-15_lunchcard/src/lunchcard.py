class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"
    
    def eat_lunch(self):
        if self.balance >= 2.60:
            self.balance -= 2.60  
    
    def eat_special(self):
        if self.balance >= 4.60:
            self.balance -= 4.60  
    
    def deposit_money(self, ammount: float):
        if ammount < 0:
            raise ValueError("The input was negative")
        elif ammount > 0:
            self.balance += ammount
            







    
    
# card = LunchCard(10)
# print(card)
# card.deposit_money(15)
# print(card)
# card.deposit_money(10)
# print(card)
# card.deposit_money(200)
# print(card)