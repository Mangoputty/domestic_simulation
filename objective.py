import simpy
import random
import statistics

env = simpy.Environment()

class Room(object):
    def __init__(self,furniture,chargers,dirtiness):
        self.num_furniture = furniture
        self.dirtiness=dirtiness
        self.chargers=chargers



class Robot(object):
    def __init__(self,width,height,charge):
        self.width=width
        self.height=height
        self.charge=charge

    def charge(self):
        if room.chargers>0:
            self.charge=100

    def clean(self):
        if charge>0.2:
            room.dirtiness=room.dirtiness-(room.dirtiness-0.05)
            charge=charge-0.1
            if self.charge<0.2:
                robot.charge
            if room.dirtiness>0.1:
                room.clean

        


room1=Room(random.random(),random.randint(1,5),random.random())

room2=Room(random.random(),random.randint(1,5),random.random())

room3=Room(random.random(),random.randint(1,5),random.random())

robot=Robot(5,7,1)
