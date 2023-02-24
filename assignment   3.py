 #Computer Application In Civil Engineering (CE 257)
"""
KENNEDY NYARKO
6942921


Github account: Rankinglamar
Github link: https://github.com/Rankinglamar/Data-Structures
"""


#List of available cars and their prices
CarsInStock={
    'Toyota Camry': 300000,
    'Honda Civic':250000,
    'Nissan Altima':280000,
    'Ford Mustang':450000,
    'Chevrolet Corvette':960000,
    'BMW 3 Series':500000,
    'Mercedes-Benz C-Class':955000,
    'Audi A4':400000,
    'Lexus ES':450000,
    'Infinity Q50':735000,
    'Tesla Model s':880000,
    'Porsche 911':900000,
    'Mazda CX-5':350000,
    'Subaru Forester':350000,
    'Jeep Wrangler':450000,
    'Land Rover Range Rover':990000,
    'Volvo XC90':556000,
    'Toyota Highlander':740000,
    'Honda CR-V':350000,
    'Nissan Rogue':300000,
    'Ford Escape': 300000,
    'Chevrolet Equinox':278000,
    'BMW X5':650000,
    'Mercedes-Benz GLC':755000,
    'Audi Q5':500000,
    'Lexus RX':550000,
    'Infinity QX50':475000,
    'Tesla Model Y':600000,
    'Porsche Cayenne':860000,
    'Mazda MX-5 Miata':255000,
    'Jeep Grand Cherokee':650000,
}


#Ask user for their car brand
CarBrand= input("Enter your car brand: ")

#Check if car brand is in the CarsInStock dictionary
if CarBrand in CarsInStock:
    print("The", CarBrand, "is available.")
    print("The price for the", CarBrand, "is",CarsInStock[CarBrand], "$")
else:
    print("Sorry, the", CarBrand,"is not availble.")