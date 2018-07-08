class Car():
    def __init__(self,model,year,Topspeed):
      self.model=model
      self.year=year
      self.Topspeed=Topspeed
   

    def gearChange(self):
      print("gear of your car has been change")


    def info(self):
      print("car model is {} and topspeed is {} ".format(self.model,self.Topspeed))


class SportsCar(Car):
      def __init__(self,model,year,Topspeed,accelration,colour):
        super().__init__(model,year,Topspeed)
        self.accelration=accelration
        self.colour=colour
      def info(self):
        print("info of sports car is {} ".format(self.horsepower)) 
class SuperSportsCar(SportsCar):
      def __init__(self,model,year,Topspeed,accelration,colour,horsepower):
        super().__init__(model,year,Topspeed,accelration,colour)
        self.horsepower=horsepower

      
its=SuperSportsCar("porn",2018,400,"300kmph in 2 sec","grey","200hp" )
its.info()
