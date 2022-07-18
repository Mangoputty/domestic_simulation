import simpy
import random
import statistics
class Home(object):
    def __init__(self, env,num_furniture,robot):
        self.env = env
        self.num_furniture = simpy.Resource(env, num_furniture)
class Robot(object):
    def __init__(self,hardness,num_limbs,min_size,max_length):
        self.hardness=hardness #or whatever function/equation I'd use for hardness
        self.num_limbs=num_limbs
        self

def begin(env, robot, Home):
    arrival_time = env.now

def move_across(env,num_furniture,robot)
    
