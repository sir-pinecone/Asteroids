from OpenGL.GL import *
from random import random

from vector3 import Vector3


class GameObject(object):
    # TODO: 
    # - Store vertex info for drawing
    # - Write a draw method
    # - move stuff to inherited class
    # - create a default vector 
    
    def __init__(self, id, mass, pos=None, vel=None):
        self.id = id
        self.mass = mass
        self.reset(pos, vel)

    def reset(self, pos=None, vel=None):
        if not pos:
            pos = Vector3(0.0, 0.0, 0.0)
        if not vel:
            vel = Vector3(0.0, 0.0, 0.0)

        self.life = 0.0
        self.force = Vector3()
        self.color = [random(), random(), random()]

    def apply_force(self, force):
        self.force += force

    def update(self, dt):
        """
        Calculate the new velocity and position for this object,
        with respect to the change in time. This is using the 
        Euler method for sake of simplicity.
        """
        self.life += dt # Update the life counter
        self.vel += (self.force / self.mass) * dt
        self.pos += self.vel * dt
        
    def draw(self):
        glColor3fv(self.color)
        glVertex3fv(self.pos)


class Particle(GameObject):
    REBOUND_FACTOR = 0.3
    MAX_VELOCITY = 5.0

    def __init__(self, *args, **kargs):
        super(Particle, self).__init__(*args, **kargs)

    def reset(self, pos=None, vel=None):
        self.pos = pos if pos else Vector3(0.0, 30.0, 0.0)
        self.vel = vel if vel else \
                Vector3((random() * 2.0 - 1.0) * Particle.MAX_VELOCITY,
                        (random() * 4.0 - 1.0) * Particle.MAX_VELOCITY,
                        (random() * 2.0 - 1.0) * Particle.MAX_VELOCITY)
        super(Particle, self).reset()

    def update(self, dt):
        super(Particle, self).update(dt)

        # do a bounce
        if self.pos[1] < 0.0 and self.vel[1] < 0.0:
            self.vel *= Particle.REBOUND_FACTOR # slow it down
            self.vel[1] *= -1 # "bounce" by flipping vertical vel

class Meteor(GameObject):
    pass

    
