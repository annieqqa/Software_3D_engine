from object_3d import *
from camera import *
from projection import *
import pygame as pg

class SoftwareRender:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.mixer.music.load("collision-sound-effect.mp3")
        pg.mixer.music.set_volume(0.7)

        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        # for simulation purposes
        self.number_of_particles = 10
        self.number_of_collisions = 0
        self.create_objects()

    def create_objects(self):
        self.points = []
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.cube = Cube(self)
        self.cube.translate([0.2, 0.4, 0.2])
        for i in range(self.number_of_particles):
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
                pg.mixer.music.play()
                # print(self.number_of_collisions)
    
    def draw_text(self, txt, x=0,y=0):
        img = self.font.render(txt, True, pg.Color('white'))
        self.screen.blit(img,(x,y))

    def run(self):
        while True:
            self.draw()
            col_txt = "No. of Collisions: " + str(self.number_of_collisions)
            self.draw_text(txt = col_txt, x=0, y=0)
            rate_txt = "No. of Collisions per number of ticks: " + str(round(self.number_of_collisions/pg.time.get_ticks(),3))
            self.draw_text(txt = rate_txt, x=0, y=30)
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()