#declaring a class
class vehicle():
   def __init__(self, make, model, year, color, sound):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
    self._sound = sound
 
class Car(vehicle):
    def __init__(self, make, model, year, color, sound):
       super().__init__(make, model, year, color, sound)
       
       self._wheels = 4
       
    def honk(self):
       return self._sound
    
    @property 
    def wheels(self):
        return self._wheels

class motorcyle(vehicle):
    def __init__ (self, make, model, year, color, sound):
        super().__init__(make, model, year, color, sound)

        self._wheels = 2 
    
    @property 
    def wheels(self):
        return self._wheels
        
