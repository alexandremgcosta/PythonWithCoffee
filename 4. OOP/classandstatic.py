class FixedFloat:
    def __init__(self, amount):
        self.amount = amount
        
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    
    # cls - Representa a class que foi chamada
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1+value2)
    
number = FixedFloat(18.5749)
print(number)

# Como o metodo from_sum() tem o @classmethod podemos simplesmente
# chamar o método da class sem antes crir-mos um objeto da class

new_number = FixedFloat.from_sum(19.4444, 0.6564111)
print(new_number)




class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'
        
    def __repr__(self):
        return f'<FixedFloat {self.symbol}{self.amount:.2f}>'
    

money = Euro(18.7998)
print(money)

another_money = Euro.from_sum(14.888, 9.999)
print(another_money)