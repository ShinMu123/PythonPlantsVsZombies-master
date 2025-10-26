TIME_SCALE=2.0
__author__ = 'marble_xu'

from . import tool
from . import constants as c
from .state import mainmenu, screen, level, auth_screen_fixed as auth_screen, leaderboard_screen

def main():
    """
    Khởi tạo Control và các trạng thái chính của game.
    Các chú thích tiếng Việt: đây là điểm bắt đầu của game.
    """
    # Tạo đối tượng Control (vòng lặp chính, xử lý sự kiện)
    game = tool.Control()
    # Đăng ký các trạng thái: Menu chính, Màn chơi, Thắng/Thua, Đăng nhập, Bảng xếp hạng
    state_dict = {c.MAIN_MENU: mainmenu.Menu(),
                  c.GAME_VICTORY: screen.GameVictoryScreen(),
                  c.GAME_LOSE: screen.GameLoseScreen(),
                  c.LEVEL: level.Level(),
                  c.AUTH_SCREEN: auth_screen.AuthScreen(),
                  c.LEADERBOARD_SCREEN: leaderboard_screen.LeaderboardScreen()}
    game.setup_states(state_dict, c.MAIN_MENU)
    # Bắt đầu vòng lặp chính
    game.main()