class vehicle():
    def __init__(self):
        self.type - "generic vehicle"


class car(vehicle):
    def __init__(self,color,sound):
        self.color = color
        self.sound = sound
        self.wheels = 4


class motorcyle(vehicle):
    def __init__ (self,color, sound):
        self.color = color
        self.sound = sound
        self.wheels = 2
