import random
from bicycle_industry import Bicycle
from bicycle_industry import Bikeshop
from bicycle_industry import Customer
if __name__ == '__main__':
    
    bike_A = Bicycle("Bike A", 10, 150)
    bike_B = Bicycle("Bike B", 20, 250)
    bike_C = Bicycle("Bike C", 30, 400)
    bike_D = Bicycle("Bike D", 40, 450)
    bike_E = Bicycle("Bike E", 50, 550)
    bike_F = Bicycle("Bike F", 55, 900)
    
    
    GoodBikes_inventory = [bike_A, bike_B, bike_C, bike_D, bike_E, bike_F]
    
    GoodBikes = Bikeshop("GoodBikes", 1.2, GoodBikes_inventory)
    
    
    customer1 = Customer("customerA", 200)
    customer2 = Customer("customerB", 500)
    customer3 = Customer("customerC", 1000)
    
    customerlist = [customer1, customer2, customer3]
    
    
        
    print ("The inventory of {0} is as follows: ".format(GoodBikes.name))
    for bike in GoodBikes_inventory:
        print ("{0}, which originally cost ${1} for {2} to buy. {2} is selling it for ${3}.".format(bike.model_name, bike.cost,GoodBikes.name, GoodBikes.sellingprice(bike)))
    print("\n")
        
    for customer in customerlist:
        print ("{0} has a budget of ${1} and can thus afford any of the following bikes: ".format(customer.customername, customer.budget))
        for bike in customer.potential_bikes(GoodBikes):
             print (bike.model_name)
    profit_earned = 0
    for customer in customerlist:
        bought_bike = random.choice(customer.potential_bikes(GoodBikes))
        new_budget = customer.budget - GoodBikes.sellingprice(bought_bike)
        print ("{0} bought {1}, which cost ${2}. {0} now has ${3} remaining in his budget.".format(customer.customername, bought_bike.model_name,GoodBikes.sellingprice(bought_bike),new_budget))
        profit_earned += GoodBikes.profit(bought_bike)
        GoodBikes.inventory.remove(bought_bike)
        
    print ("The remaining bikes in the {0} inventory are: ".format(GoodBikes.name))
    for bike in GoodBikes.inventory:
        print ("{0}, which is selling for ${1}.".format(bike.model_name, GoodBikes.sellingprice(bike)))
    print ("In total, {0} made ${1} of profit.".format(GoodBikes.name, profit_earned))