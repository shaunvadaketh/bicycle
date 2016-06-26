class Bicycle(object):
    def __init__(self, model_name, weight, cost):
        self.model_name = model_name
        self.weight = weight
        self.cost = cost
    # def __repr__(self):
    #     return "\n{0} weighs {1} pounds and costs ${2} to produce.".format(
    #         self.model_name, self.weight, self.cost)
class Bikeshop(object):
    def __init__(self, name, margin, inventory):
        self.name = name
        self.margin = margin
        self.inventory = inventory
    def sellingprice(self,bike):
        selling_price = bike.cost * 1.2
        return selling_price
    def profit(self,bike):
        profit = self.sellingprice(bike) - bike.cost
        return profit
    # def __repr__(self):
    #     return "{0} has an inventory of {1} bikes, and their information is as follows : {2}.".format(self.name, len(self.inventory), self.inventory)
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
                
    # def __repr__(self):
    #     return "{0} has ${1}.".format(self.customername, self.budget)