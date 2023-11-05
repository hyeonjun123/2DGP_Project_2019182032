from pico2d import load_image


class background2:
    def __init__(self):
        self.image = load_image('background.png')

    def draw(self):
        self.image.draw(800//2, 549//2)
    def update(self):
        pass
