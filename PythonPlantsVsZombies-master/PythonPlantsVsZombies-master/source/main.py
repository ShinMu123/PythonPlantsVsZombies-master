# source/main.py
TIME_SCALE = 2.0
__author__ = 'marble_xu'

import pygame as pg
from . import tool
from . import constants as c
from .state import mainmenu, screen as screen_states, level, auth_screen_fixed as auth_screen, leaderboard_screen

def main():
    """
    Điểm bắt đầu của game.
    """
    # Khởi tạo pygame
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Plants vs Zombies")

    # Tạo Control
    game = tool.Control()
    game.screen = screen
    game.font = pg.font.SysFont("consolas", 20, bold=True)

    # Đăng ký các trạng thái
    state_dict = {
        c.MAIN_MENU: mainmenu.Menu(),
        c.GAME_VICTORY: screen_states.GameVictoryScreen(),
        c.GAME_LOSE: screen_states.GameLoseScreen(),
        c.LEVEL: level.Level(),
        c.AUTH_SCREEN: auth_screen.AuthScreen(),
        c.LEADERBOARD_SCREEN: leaderboard_screen.LeaderboardScreen()
    }

    game.setup_states(state_dict, c.MAIN_MENU)

    # Chạy vòng lặp chính
    game.main()

    # Kết thúc pygame khi thoát
    pg.quit()
