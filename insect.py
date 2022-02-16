import random

class Insectclass:
     def __init__(self,wings,legs):
        self.wings = wings
        self.legs = legs
        self.flight = 0
        
    
     def flight_len (self):
        self.flight = random.randint(0, 10)

     def get_flight (self):
         return self.flight


    
 