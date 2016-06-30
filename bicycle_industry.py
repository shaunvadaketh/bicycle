class Bicycle(object):
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost
   
class Bikeshop(object):
    def __init__(self, name, margin, inventory):
        self.name = name
        self.margin = margin
        self.inventory = inventory
    def sellingprice(self,bike):
        selling_price = bike.cost * self.margin
        return selling_price
    def profit(self,bike):
        profit = self.sellingprice(bike) - bike.cost
        return profit
   
class Customer(object):
    
    def __init__(self, customername, budget):
        self.customername = customername
        self.budget = budget
    def potential_bikes(self, bikeshop):    
        potentialbikes = []
        for bike in bikeshop.inventory:
            if bikeshop.sellingprice(bike) <= self.budget:
                potentialbikes.append(bike)
        return potentialbikes
                
   