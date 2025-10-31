import pygame as pg
from source import main as game_main

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Plants vs Zombies")

    game = game_main.Control()  # tạo Control
    game.screen = screen  # gán màn hình
    game.font = pg.font.SysFont("consolas", 20, bold=True)
    game.main()
    pg.quit()
