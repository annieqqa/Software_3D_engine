import random
from object_3d import *
'''
1. vertices np.array(vertices)
self.vertices = np.array([x, y, z, 1])

collision
'''



class particle(Object3D):
    def __init__(self, x=0, y=0, z=0, i=0, j=0, k=0):
        self.x = x
        self.y = y
        self.z = z
        self.vertives = np.array([
            random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), 1])
        self.i = i
        self.j = j
        self.k = k
    def xCoord(self):
        return self.x

class parSys():
    def __init__(self, N=10, T=298, dt=0.1, l=1, w=1, h=1):
        self.N = N # number of particles
        self.T = T # temperature
        self.dt = dt # -(pg.time.get_ticks() % 0.005)
        self.l = l # length of the box
        self.w = w # width of the box
        self.h = h # height of the box
        self.particles = []
    def initialize_particles(self):
        # initialize particles randomly
        for i in range(self.N):
            p = particle()
            p.x = random.uniform(0, self.l)
            p.y = random.uniform(0, self.w)
            p.z = random.uniform(0, self.h)
            p.i = random.uniform(0, .1)
            p.j = random.uniform(0, .1)
            p.k = random.uniform(0, .1)
            self.particles.append(p)
    def update_particles(self):
        # update particles
        for i in range(self.N):
            p = self.particles[i]
            p.x = p.x + p.i*self.dt
            p.y = p.y + p.j*self.dt
            p.z = p.z + p.k*self.dt
            if p.x > self.l or p.x < 0:
                p.i = -p.i
            if p.y > self.w or p.y < 0:
                p.j = -p.j
            if p.z > self.h or p.z < 0:
                p.k = -p.k
    def get_particles(self):
        x = []
        y = []
        for i in range(self.N):
            p = self.particles[i]
            x.append(p.x)
            y.append(p.y)
        return x, y
        

