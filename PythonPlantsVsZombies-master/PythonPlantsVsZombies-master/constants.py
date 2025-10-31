import os

# ...existing code...

# Thời gian hiện tại dùng trong game
CURRENT_TIME = 'current_time'

# Trạng thái màn hình
MAIN_MENU = 'main_menu'
LOAD_SCREEN = 'load_screen'
LEVEL = 'level'
GAME_VICTORY = 'game_victory'
GAME_OVER = 'game_over'
AUTH_SCREEN = 'auth'
LEADERBOARD_SCREEN = 'leaderboard'

# Đường dẫn resources (tự tạo đường dẫn tuyệt đối dựa trên project)
BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GRAPHICS_PATH = os.path.join(BASE_PATH, 'resources', 'graphics')

# Key cho ảnh trong GFX
MAIN_MENU_IMAGE = 'MainMenu'
OPTION_ADVENTURE = 'Adventure'

# GFX mapping -> đường dẫn file thực tế
GFX = {
    MAIN_MENU_IMAGE: os.path.join(GRAPHICS_PATH, 'MainMenu.png'),
    OPTION_ADVENTURE + '_0': os.path.join(GRAPHICS_PATH, 'Adventure_0.png'),
    OPTION_ADVENTURE + '_1': os.path.join(GRAPHICS_PATH, 'Adventure_1.png'),
    # ...existing code...
}

# ...existing code...