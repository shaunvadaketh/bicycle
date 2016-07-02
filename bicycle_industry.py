class Bicycle(object):
    def __init__(self, model_name, weight, wheels, frame):
        self.model_name = model_name
        self.weight = weight
        self.wheels = wheels
        self.frame = frame
    
        self.bike_cost = (2 * wheels.wheelcost) + frame.framecost
        
class Bikeshop(object):
    
    def __init__(self, name, margin, inventory):
        self.name = name
        self.margin = margin
        self.inventory = inventory
    def sellingprice(self,bike):
        selling_price = bike.bike_cost * self.margin
        return selling_price
    def profit(self,bike):
        profit = self.sellingprice(bike) - bike.bike_cost
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

class Wheels(object):
    def __init__(self, wheelname, weight, wheelcost):
        self.wheelname = wheelname
        self.weight = weight
        self.wheelcost = wheelcost

class Frames(object):
    def __init__(self, material, weight, framecost):
        self.material = material
        self.weight = weight
        self.framecost = framecost
        
   