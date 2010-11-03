from random import random
from OpenGL.GL import *

from vector3 import Vector3
from gameobject import GameObject
import log


class ObjectManager(object):
    def __init__(self):
        self.gObjects = []

    def add(self, obj):
        '''Add an game object to the list'''
        # Make sure we're adding an instance of game objects
        # or a list of them
        if type(obj) == list: 
            # TODO: check if list has correct type
            self.gObjects.extend(obj)
        else:
            assert(isinstance(obj, GameObject))
            self.gObjects.append(obj) 
    
    def get(self, index):
        '''Returns an object'''
        assert(index < len(self.gObjects))
        return self.gObjects[index]

    def all(self):
        '''Returns all objects'''
        return self.gObjects
    
    def apply_force(self, force):
        '''Force is applied to all objects'''
        for o in self.gObjects:
            o.apply_force(force)

    def update(self, dt):
        '''Update all of the game objects'''
        #log.info("updating the manager")
        for o in self.gObjects:
            o.update(dt)

    def draw(self):
        '''Tell the game objects to draw themselves'''
        glBegin(GL_POINTS)
        for o in self.gObjects:
            o.draw()
        glEnd() 
    
    def reset_forces(self):
        #log.info("resetting all forces")
        for o in self.gObjects:
            o.force.zero()

    def reset_all(self):
        '''Results all of the objects'''
        for o in self.gObjects:
            o.reset()

