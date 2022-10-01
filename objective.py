import simpy
import random
import statistics

env = simpy.Environment()

<<<<<<< HEAD
class Room(object):
    def __init__(self,env,furniture,chargers,dirtiness):
        self.env=env
=======

class Room():
    def __init__(self,furniture,chargers,dirtiness):
>>>>>>> c4e20674df760036f447474addfb1f71121c994d
        self.num_furniture = furniture
        self.dirtiness=dirtiness
        self.chargers=chargers

class House():
    def __init__(self, rooms, connections):
        pass

<<<<<<< HEAD

class Robot(object):
    def __init__(self,env,width,height,charge):
        self.env=env
=======
class Robot():
    def __init__(self,width,height,charge, start_room):
>>>>>>> c4e20674df760036f447474addfb1f71121c994d
        self.width=width
        self.height=height
        self.charge=charge
        self.room = start_room

        
    def charge(self):
        if self.room.chargers>0:
            self.charge=100

    def clean(self):
        if charge>0.2:
            self.room.dirtiness=self.room.dirtiness-(self.room.dirtiness-0.05)
            charge=charge-0.1
        else:
            robot.charge
    
    def move(self, room):
        pass


if __name__ == "__main__":
    env = simpy.Environment()


    room1=Room(random.random(),random.randint(1,5),random.random())

    room2=Room(random.random(),random.randint(1,5),random.random())

    room3=Room(random.random(),random.randint(1,5),random.random())

    robot=Robot(5,7,1, room1)
