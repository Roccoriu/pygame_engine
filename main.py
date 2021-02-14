import pygame as pg
from src.lib.aux_json import read_json


class Main():
    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.config = read_json('assets/configs/config.json')
        self.config.update(read_json('assets/configs/dynamic.json'))

        self.screen = pg.display.set_mode(
            (self.config['width'], self.config['height']))

        self.screen.set_caption(self.config['title'])
        self.clock = pg.time.Clock()

        self.playing = True

    def run(self):
        while self.playing:
            pass

    def events(self):
        pass


if __name__ == '__main__':
    game = Main()
    game.run()
