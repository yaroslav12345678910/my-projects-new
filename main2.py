import arcade

from constants import *


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    view = GameView()
    window.show_view(view)

    arcade.run()


if __name__ == '__main__':
    main()
