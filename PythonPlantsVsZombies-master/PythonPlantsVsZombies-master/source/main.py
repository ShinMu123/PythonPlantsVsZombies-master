__author__ = 'marble_xu'

from . import tool
from . import constants as c
from .state import mainmenu, screen, level

def main():
    """
    Khởi tạo Control và các trạng thái chính của game.
    Các chú thích tiếng Việt: đây là điểm bắt đầu của game.
    """
    # Tạo đối tượng Control (vòng lặp chính, xử lý sự kiện)
    game = tool.Control()
    # Đăng ký các trạng thái: Menu chính, Màn chơi, Thắng/Thua
    state_dict = {c.MAIN_MENU: mainmenu.Menu(),
                  c.GAME_VICTORY: screen.GameVictoryScreen(),
                  c.GAME_LOSE: screen.GameLoseScreen(),
                  c.LEVEL: level.Level()}
    game.setup_states(state_dict, c.MAIN_MENU)
    # Bắt đầu vòng lặp chính
    game.main()