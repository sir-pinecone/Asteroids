class GameObject(object):
    # TODO: 
    # - Store vertex info for drawing
    # - Write a draw method

    def __init__(self, pos, vel, mass):
        self.pos = pos
        self.vel = vel
        self.m = mass
        self.force = Vector3()
        
    def apply_force(self, force):
        self.force += force

    def simulate(self, dt):
        """
        Calculate the new velocity and position for this object,
        with respect to the change in time. This is using the 
        Euler method for sake of simplicity.
        """
        self.vel += (self.force / self.m) * dt
        self.pos += self.vel * dt

