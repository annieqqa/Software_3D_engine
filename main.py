from object_3d import *
from camera import *
from projection import *
from particles import *
import pygame as pg


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()
        # for simulation purposes
        self.number_of_collisions = 0

    def create_objects(self):
        self.points = []
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.cube = Cube(self)
        self.cube.translate([0.2, 0.4, 0.2])
        for i in range(10):
            self.points.append(Point(self))
        self.world_axes = Axes(self)
        self.world_axes.scale(2.5)
        # self.object = self.get_object_from_file('resources/t_34_obj.obj')
        # self.object.rotate_y(-math.pi / 4)

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                    print ([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.world_axes.draw()
        self.cube.draw()
        for point in self.points:
            point.draw()
            if (point.movement()):
                self.number_of_collisions += 1
        

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            print(self.number_of_collisions / pg.time.get_ticks())


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()