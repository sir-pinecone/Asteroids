from random import random

from objectmanager import ObjectManager
from gameobject import Particle
from physics import Simulation
from vector3 import Vector3
import config 
import log


class Scene(object):
    '''Base Class'''
    def __init__(self):
        self.manager = ObjectManager()
        self.simulation = Simulation()

    def init(self):
        pass

    def update(self, dt):
        #log.info("Updating the scene")

        # first reset all forces on the objects
        self.manager.reset_forces()
       
        # apply forces on the objects
        self.solve()
        
        # now update the objects
        self.manager.update(dt)     

    def draw(self):
        self.manager.draw()

    def reset(self):
        '''Reset the scene (just objects for now)'''
        self.manager.reset_all()


class GameplayScene(Scene):
    NUM_PARTICLES = 100 # Number of particle objects to create

    def __init__(self):
        self.gravity = Vector3(0.0, -9.81, 0.0)
        super(GameplayScene, self).__init__() # init the base cls

    def init(self):
        log.info("Initiating the gameplay scene")

        # Create the game objects
        objects = []
        for x in range(GameplayScene.NUM_PARTICLES):
            mass = random() * 13.5
            # class will set the vel
            obj = Particle(x, mass, pos=Vector3(config.objects['POSITION']))
            # Start with a bloom
            self.__bloom(obj)
            objects.append(obj)

        # Add the objects to a manager
        self.manager.add(objects)
    
    def solve(self):
        # Called before the objects are updated.
        # This method allows you to work with the objects before 
        #simulating them
        for obj in self.manager.all():
            # Apply gravity
            obj.apply_force(self.gravity * obj.mass)

            # Check if this object isn't moving or if its life has run out.
            if obj.life > 4.0 and obj.vel.is_shorter_than(
                    config.objects['MIN_VELOCITY']):
                self.__bloom(obj)   

    def __bloom(self, obj):
            # Reset it
            obj.reset(pos=Vector3(config.objects['POSITION']))

