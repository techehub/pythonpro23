from abc import  ABC, abstractmethod

class Car (ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
       pass

    @abstractmethod
    def stop(self):
        pass

class Nano (Car):
    def start (self):
        print ("Staring nano")
    def accelerate (self):
        print ("Acclerat4 nano")
    def stop (self):
        print ("Stopping nano")

class Benz(Car):
    def start (self):
        print ("Staring Benz")
    def accelerate (self):
        print ("Acclerat4 Benz")
    def stop (self):
        print ("Stopping Benz")

class Bike:
    def start(self):
        print("Staring Bike")

    def accelerate(self):
        print("Acclerate Bike")

    def stop(self):
        print("Stopping Bike")


class Person:
    def drive (self, car):
        car.start ()
        car.accelerate()
        car.stop ()


car1 = Nano ()
car2 = Benz ()
b1 = Bike ()
p1= Person ()
p1.drive (car1)
p1.drive (car2)





