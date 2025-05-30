from collections import deque

from sprite_object import *

class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/shotgun', scale=3.0, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
            for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.idle_image = self.images[-1]
        self.image = self.idle_image
        self.damage = 50

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                # self.images.rotate(-1)
                # self.image = self.images[-1]
                self.image = self.images[self.frame_counter]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0
                    self.image = self.idle_image

    def draw(self):
        self.game.screen.blit(self.image, self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()