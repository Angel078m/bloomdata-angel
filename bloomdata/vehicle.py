#vehicles im listing in craiglist
#this is the parent class
class Vehicle:

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage

    def honk(self):
        return 'HOOOOOOOOOOONK!'
    
    def drive(self, miles_driven):
        self.mileage =+ miles_driven
        return self.mileage
    
    

    def __repr__(self):
        return f'A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles'
        

if __name__=='__main__':
    my_vehicle = Vehicle('Toyota', 'Camry', 'gray', 2015, 6000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)

    print (my_vehicle)


#this is th child class
#putting (Vehicle) makes convertible inherit the class
class Convertible(Vehicle):

    def __init__(self, make, model, color, year, mileage, top_down=True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    
    
    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return'Top in now up!'
        else:
            self.top_down = True
            return 'Top is now down!'
    

    def __repr__(self):
        return f'A {self.color} {self.year} {self.make} {self.model} convetible with {self.mileage} miles'
            

if __name__=='__main__':
    my_vehicle = Convertible('Toyota', 'Camry', 'gray', 2015, 6000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    # print(my_vehicle.honk())
    # print(my_vehicle.drive(1234))
    # print(my_vehicle.mileage)

    print (my_vehicle)
    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status())

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    

    
    



