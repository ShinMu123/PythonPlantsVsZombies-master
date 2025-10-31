import pygame as pg
from source import tool
from source import constants as c
from source.state import mainmenu, screen, level, auth_screen_fixed as auth_screen, leaderboard_screen
import os

def main():
    pg.init()
    screen_surface = pg.display.set_mode((800, 600))
    pg.display.set_caption("Plants vs Zombies")
    print("[MAIN] Initialized pygame and window created", flush=True)

    # --- Load ảnh vào tool.GFX ---
    tool.load_gfx(c.GRAPHICS_PATH)

    # --- Tạo Control ---
    game = tool.Control()
    game.screen = screen_surface
    game.font = pg.font.SysFont("consolas", 20, bold=True)

    # --- Tạo state ---
    state_dict = {
        c.MAIN_MENU: mainmenu.Menu(),
        c.GAME_VICTORY: screen.GameVictoryScreen(),
        c.GAME_LOSE: screen.GameLoseScreen(),
        c.LEVEL: level.Level(),
        c.AUTH_SCREEN: auth_screen.AuthScreen(),
        c.LEADERBOARD_SCREEN: leaderboard_screen.LeaderboardScreen()
    }
    game.setup_states(state_dict, c.MAIN_MENU)
    print("[MAIN] Entering game loop...", flush=True)
    game.main()
    print("[MAIN] Exited game loop", flush=True)
    pg.quit()
