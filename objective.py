import simpy
import random
import statistics



class Room():
    def __init__(self,furniture,chargers,dirtiness):
        self.num_furniture = furniture
        self.dirtiness=dirtiness
        self.chargers=chargers

class House():
    def __init__(self, rooms, connections):
        pass

class Robot():
    def __init__(self,width,height,charge, start_room):
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
