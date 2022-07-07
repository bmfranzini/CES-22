class Pizza:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost


class MassaDePizza(Pizza):
    cost = 7.0


class Decorator(Pizza):
    def __init__(self, pizza):
        self.component = pizza
        
    def getTotalCost(self):
        return self.component.getTotalCost() + Pizza.getTotalCost(self)
    
    def getDescription(self):
        return self.component.getDescription() + '' +Pizza.getDescription(self)
    

class QueijoMussarela(Decorator):
    cost = 5.0
    
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        
        
class Cebola(Decorator):
    cost = 2.0
    
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        
        
class Ovo(Decorator):
    cost = 1.5
    
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        
        
class Presunto(Decorator):
    cost = 6.0
    
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        
        
class Tomate(Decorator):
    cost = 4.0
    
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)


class Manjericao(Decorator):
    cost = 2.0
    
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

