import random

import arcade

from constants import *


class MovingSprite(arcade.Sprite):

    def update(self):
        super(MovingSprite, self).update()

        if self.right < 0 or self.right > SCREEN_WIDTH + 200:
            self.remove_from_sprite_lists()

    def destroy(self):
        self.remove_from_sprite_lists()


class Meteor(MovingSprite):
    meteor_sprites_images = [
        'meteorGrey_big1.png'
        'meteorGrey_big2.png'
        'meteorGrey_big3.png'
        'meteorGrey_big4.png'
        'meteorGrey_med1.png'
        'meteorGrey_med2.png'
        'meteorGrey_small1.png'
        'meteorGrey_small2.png'
        'meteorGrey_tiny1.png'
        'meteorGrey_tiny2.png'

    ]

    def __init__(self):
        super(Meteor, self).__init__(
            f":resources:/images/space_shooter/{random.choice(self.meteor_sprites_images)}",
            SCALING, hit_box_algorithm='Detailed')
        self.left = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 80)
        self.top = random.randint(10, SCREEN_HEIGHT - 10)
        self.velocity = (random.randint(-20, -5), 0)


class Star(MovingSprite):
    def __init__(self):
        super(Star, self).__init__(f":resources:/images/items/star.png", SCALING)

        self.left = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 80)
        self.top = random.randint(10, SCREEN_HEIGHT - 10)
        self.velocity = (random.randint(-5, -5), 0)


class Shoot(MovingSprite):
    def __init__(self, x, y):
        super(Shoot, self).__init__(f":resources:/images/space_shooter/laserBlue01", SCALING)

        self.left = x
        self.top = y
        self.velocity = (30, 0)
