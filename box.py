from constants import colors
import random

import pygame


class Box:
    def __init__(
        self, color, point, size, s_time, duration, side_len, display_res
    ) -> None:
        self.color = color
        self.point = point
        self.size = size
        self.s_time = s_time
        self.duration = duration
        self.hitcount = 0
        self.score = 0
        self.side_len = side_len
        self.display_res = display_res

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.point, self.size))

    def interpolate_color(self):
        factor = min(((pygame.time.get_ticks() - self.s_time) / self.duration), 0.025)

        #PLayer failed to click on time
        if factor >= 0.025:
            self.shift_pos()
            self.score -= 1

        color1 = self.color
        color2 = colors["red"]

        new_color = (
            int(color1[0] + (color2[0] - color1[0]) * factor),
            int(color1[1] + (color2[1] - color1[1]) * factor),
            int(color1[2] + (color2[2] - color1[2]) * factor),
        )
        self.color = new_color

    def shift_pos(self):
        display_width, display_height = self.display_res
        new_point = (
            random.randint(self.side_len, display_width - self.side_len),
            random.randint(self.side_len, display_height - self.side_len),
        )
        self.point = new_point
        self.color = colors["green"]
        self.s_time = pygame.time.get_ticks()

    def update(self, color=None, point=None, size=None, s_time=None, duration=None):
        if color != None:
            self.color = color

        if point != None:
            self.point = point

        if size != None:
            self.size = size

        if s_time != None:
            self.s_time = s_time

        if duration != None:
            self.duration = duration


