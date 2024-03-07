import math
import pygame as pg
from settings import *


class Sensor:
    def __init__(self, angle, surface):
        self.surface = surface
        self.angle = angle
        self.length = 0
        self.hit_point = None

    def draw(self, car):
        if self.hit_point:
            pg.draw.line(SCREEN, (0, 0, 255), (car.x, car.y), self.hit_point)
            pg.draw.circle(SCREEN, (0, 255, 0), self.hit_point, 3)

    def update(self, car, track):
        self.raycast(track, car)

    def raycast(self, track, car):
        # Calculate angle of ray
        c = math.cos(math.radians(car.angle + self.angle))
        s = math.sin(math.radians(car.angle + self.angle))

        # Get flipped mask based on ray angle
        flip_x = c < 0
        flip_y = s < 0
        flipped_mask = track.masks[flip_x][flip_y]

        # Cast ray as long as possible
        x_dest = 400 + 1000 * abs(c)
        y_dest = 400 + 1000 * abs(s)

        # Draw ray on surface
        self.surface.fill((0, 0, 0, 0))
        pg.draw.line(self.surface, (255, 255, 255), (400, 400), (x_dest, y_dest))
        beam_mask = pg.mask.from_surface(self.surface)

        # Calculate offset based on position and which mask was used
        offset_x = 400 - car.x if flip_x else car.x - 400
        offset_y = 400 - car.y if flip_y else car.y - 400
        hit = flipped_mask.overlap(beam_mask, (offset_x, offset_y))

        # Get point of intersection with ray and edge of track
        if hit is not None and (hit[0] != car.x or hit[1] != car.y):
            hx = 799 - hit[0] if flip_x else hit[0]
            hy = 799 - hit[1] if flip_y else hit[1]
            self.hit_point = (hx, hy)

            # Calculate total length of ray
            self.length = math.sqrt(
                (car.x - self.hit_point[0]) ** 2 + (car.y - self.hit_point[1]) ** 2
            )
