import arcade


class GameView(arcade.View):

    def __init__(self):
        super(GameView, self).__init__()
        self.player = None
        self.score = 0
        self.background = None
        self.meteors = arcade.SpriteList()
        self.stars = arcade.SpriteList()
        self.shoots = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.csscolor.BLACK)
        self.background = arcade.Sprite(':resources:images/backgrounds/stars.png', BACKGROUND_SCALING)
        self.player = arcade.Sprite
