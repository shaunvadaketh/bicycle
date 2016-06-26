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
    
    for customer in customerlist:
        print (customer.customername)
        for bike in customer.potential_bikes(GoodBikes):
             print (bike.model_name)
        