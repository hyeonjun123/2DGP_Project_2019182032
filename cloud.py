from pico2d import load_image



class Cloud:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.image = load_image('cloud.png')


    def draw(self):
        self.image.draw(800//2, 549//2)

    def update(self):
        pass

