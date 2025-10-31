# tool.py

import pygame as pg
from . import constants as c
import os
from collections import defaultdict

# ===============================
# Base class cho tất cả các màn game
# ===============================
class State:
    def __init__(self):
        self.done = False
        self.next = None
        self.game_info = {}

    def startup(self, current_time, game_info):
        pass

    def cleanup(self):
        # Trả về game_info để state kế tiếp nhận đầy đủ dữ liệu (LEVEL_NUM, CURRENT_TIME, ...)
        return getattr(self, 'game_info', {})

    def update(self, screen, keys, current_time, mouse_pos, mouse_click, events):
        pass

# ===============================
# Control class để quản lý game loop, state, input
# ===============================
class Control:
    def __init__(self):
        self.screen = None
        self.done = False
        self.clock = pg.time.Clock()
        self.fps = 60
        self.keys = None
        self.mouse_pos = None
        self.mouse_click = [False, False, False]
        self.current_time = 0.0
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.game_info = {
            c.CURRENT_TIME: 0.0,
            c.LEVEL_NUM: c.START_LEVEL_NUM
        }

        self.font = None
        self.show_fps = True

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, self.game_info)

    def update(self, events):
        if self.screen:
            self.keys = pg.key.get_pressed()

        self.current_time = pg.time.get_ticks()
        if self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time, self.mouse_pos, self.mouse_click, events)

        self.mouse_pos = None
        self.mouse_click = [False, False, False]

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)

    def event_loop(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                if self.screen:
                    self.keys = pg.key.get_pressed()
                if event.key == pg.K_F3:
                    self.show_fps = not self.show_fps
            elif event.type == pg.KEYUP:
                if self.screen:
                    self.keys = pg.key.get_pressed()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                self.mouse_click = pg.mouse.get_pressed()

    def main(self):
        if self.screen is None:
            raise RuntimeError("Control.screen chưa được gán! Gọi pg.display.set_mode() trước.")
        if self.font is None:
            self.font = pg.font.SysFont("consolas", 20, bold=True)

        global SCREEN
        SCREEN = self.screen

        while not self.done:
            events = pg.event.get()
            self.event_loop(events)
            self.update(events)

            if self.show_fps:
                fps = int(self.clock.get_fps())
                fps_text = self.font.render(f"FPS: {fps}", True, (255, 255, 0))
                self.screen.blit(fps_text, (10, 10))

            pg.display.flip()
            self.clock.tick(self.fps)

        print("game over")

# ===============================
# GFX dictionary và hàm tiện ích load ảnh
# ===============================
GFX = {}
SCREEN = None

# Một số rect cắt ảnh theo tên (tùy chọn). Hiện để trống để tránh lỗi thuộc tính.
PLANT_RECT = {}
# Mặc định x = 0 cho zombie frames nếu không chỉ định
ZOMBIE_RECT = defaultdict(lambda: {'x': 0})

def load_gfx(folder, colorkey=(255,0,255), accept=(".png",".jpg",".bmp")):
    """
    Load ảnh từ thư mục đồ họa. Hỗ trợ:
    - Nạp ảnh ở root vào GFX[name]
    - Tạo danh sách background tại GFX['Background'] từ Items/Background/Background_*.{png|jpg|bmp}
    """
    if not os.path.isdir(folder):
        return

    # Nạp ảnh ở root folder (giữ hành vi cũ)
    for pic in os.listdir(folder):
        path = os.path.join(folder, pic)
        if not os.path.isfile(path):
            continue
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(path).convert_alpha()
            if colorkey is not None:
                img.set_colorkey(colorkey)
            GFX[name] = img

    # Nạp thư mục Screen: map tên file -> Surface
    screen_dir = os.path.join(folder, 'Screen')
    if os.path.isdir(screen_dir):
        for pic in os.listdir(screen_dir):
            path = os.path.join(screen_dir, pic)
            if not os.path.isfile(path):
                continue
            name, ext = os.path.splitext(pic)
            if ext.lower() in accept:
                try:
                    img = pg.image.load(path).convert_alpha()
                except Exception:
                    img = pg.image.load(path).convert()
                if colorkey is not None:
                    img.set_colorkey(colorkey)
                GFX[name] = img

    # Nạp thư mục Cards: map tên file -> Surface
    cards_dir = os.path.join(folder, 'Cards')
    if os.path.isdir(cards_dir):
        for pic in os.listdir(cards_dir):
            path = os.path.join(cards_dir, pic)
            if not os.path.isfile(path):
                continue
            name, ext = os.path.splitext(pic)
            if ext.lower() in accept:
                try:
                    img = pg.image.load(path).convert_alpha()
                except Exception:
                    img = pg.image.load(path).convert()
                if colorkey is not None:
                    img.set_colorkey(colorkey)
                GFX[name] = img

    # Nạp background theo danh sách chỉ số
    bg_dir = os.path.join(folder, 'Items', 'Background')
    if os.path.isdir(bg_dir):
        backgrounds = []
        index = 0
        while True:
            # chấp nhận cả .png và .jpg
            candidates = [
                os.path.join(bg_dir, f'Background_{index}.png'),
                os.path.join(bg_dir, f'Background_{index}.jpg'),
                os.path.join(bg_dir, f'Background_{index}.bmp'),
            ]
            existing = next((p for p in candidates if os.path.isfile(p)), None)
            if not existing:
                break
            img = pg.image.load(existing).convert()
            backgrounds.append(img)
            index += 1
        if backgrounds:
            GFX[c.BACKGROUND_NAME] = backgrounds

    # Nạp các thư mục có hoạt ảnh nhiều frame: Plants, Zombies, Bullets
    def load_sequence_dir(target_dir):
        files = [f for f in os.listdir(target_dir)
                 if os.path.isfile(os.path.join(target_dir, f)) and os.path.splitext(f)[1].lower() in accept]
        if not files:
            return []
        def sort_key(name):
            base, _ = os.path.splitext(name)
            # Ưu tiên số ở cuối tên file, ví dụ SunFlower_12 -> 12
            parts = base.rsplit('_', 1)
            if len(parts) == 2 and parts[1].isdigit():
                return int(parts[1])
            return base
        files.sort(key=sort_key)
        frames = []
        for pic in files:
            path = os.path.join(target_dir, pic)
            try:
                img = pg.image.load(path).convert_alpha()
            except Exception:
                img = pg.image.load(path).convert()
            if colorkey is not None:
                img.set_colorkey(colorkey)
            frames.append(img)
        return frames

    def load_recursive_sequences(base_name):
        base_dir = os.path.join(folder, base_name)
        if not os.path.isdir(base_dir):
            return
        for root, dirs, _ in os.walk(base_dir):
            # Nếu root chứa trực tiếp các frame, dùng tên thư mục làm key
            frames = load_sequence_dir(root)
            if frames:
                key = os.path.basename(root)
                GFX[key] = frames

    for name in ['Plants', 'Zombies', 'Bullets']:
        load_recursive_sequences(name)

def get_image(sheet, x, y, width, height, colorkey=None, scale=1.0):
    """
    Cắt một hình từ sheet (Surface hoặc đường dẫn file) và scale nếu cần.
    """
    # Cho phép truyền vào đường dẫn file ảnh thay vì Surface
    if isinstance(sheet, str):
        loaded = pg.image.load(sheet).convert_alpha()
    else:
        loaded = sheet

    image = pg.Surface((width, height), pg.SRCALPHA).convert_alpha()
    image.blit(loaded, (0, 0), (x, y, width, height))
    if colorkey is not None:
        image.set_colorkey(colorkey)
    if scale != 1.0:
        size = (int(width * scale), int(height * scale))
        image = pg.transform.scale(image, size)
    return image
