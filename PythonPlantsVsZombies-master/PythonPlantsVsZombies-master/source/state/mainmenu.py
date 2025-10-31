__author__ = 'marble_xu'

import os
import pygame as pg
from .. import tool
from .. import constants as c

class Menu(tool.State):
    def __init__(self):
        tool.State.__init__(self)
        self.bg_image = None
        self.font = None
        self.option_frames = []
        self.option_clicked = False
    
    def startup(self, current_time, persist):
        self.next = c.LEVEL
        self.persist = persist
        self.game_info = persist
        self.setupBackground()
        self.setupOption()

    def setupBackground(self):
        try:
            frame_rect = [80, 0, 800, 600]
            bg_path = c.GFX[c.MAIN_MENU_IMAGE]
            
            if not os.path.exists(bg_path):
                print(f"[ERROR] Không tìm thấy file hình nền: {bg_path}")
                self.bg_image = pg.Surface((800, 600))
                self.bg_image.fill(c.BLACK)
            else:
                self.bg_image = tool.get_image(bg_path, *frame_rect)
                
            self.bg_rect = self.bg_image.get_rect()
            self.bg_rect.x = 0
            self.bg_rect.y = 0
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi tải hình nền: {e}")
            self.bg_image = pg.Surface((800, 600))
            self.bg_image.fill(c.BLACK)
        
    def setupOption(self):
        try:
            self.option_frames = []
            frame_names = [c.OPTION_ADVENTURE + '_0', c.OPTION_ADVENTURE + '_1']
            frame_rect = [0, 0, 165, 77]
            
            for name in frame_names:
                if os.path.exists(c.GFX[name]):
                    self.option_frames.append(tool.get_image(c.GFX[name], *frame_rect, c.BLACK, 1.7))
                else:
                    print(f"[ERROR] Không tìm thấy file: {c.GFX[name]}")
                    # Tạo surface trống thay thế
                    empty = pg.Surface((165, 77))
                    empty.fill(c.GREEN)
                    self.option_frames.append(empty)
            
            self.option_frame_index = 0
            self.option_image = self.option_frames[self.option_frame_index]
            self.option_rect = self.option_image.get_rect()
            self.option_rect.x = 435
            self.option_rect.y = 75
            
            self.option_start = 0
            self.option_timer = 0
            self.option_clicked = False
            
            self.setupButtons()
            
        except Exception as e:
            print(f"[ERROR] Lỗi khi tải option frames: {e}")
    
    def setupButtons(self):
        """Thiết lập các nút mới"""
        font_paths = [
            "C:/Windows/Fonts/times.ttf",
            "C:/Windows/Fonts/arial.ttf", 
            "C:/Windows/Fonts/tahoma.ttf",
            "C:/Windows/Fonts/segoeui.ttf"
        ]
        
        loaded = False
        for f in font_paths:
            if os.path.exists(f):
                try:
                    self.font = pg.font.Font(f, 26)
                    print(f"[FONT] Đã nạp font: {f}")
                    loaded = True
                    break
                except Exception as e:
                    print(f"[FONT] Lỗi nạp font {f}: {e}")
                    continue

        if not loaded:
            print("[FONT] Dùng font mặc định")
            self.font = pg.font.SysFont("arial", 26)

        self.button_rects = {
            'login': pg.Rect(50, 200, 180, 50),
            'leaderboard': pg.Rect(50, 270, 180, 50),
            'guest': pg.Rect(50, 340, 180, 50)
        }
    
    def checkOptionClick(self, mouse_pos):
        if not mouse_pos:
            return False
            
        x, y = mouse_pos
        if self.option_rect and self.option_rect.collidepoint(x, y):
            self.option_clicked = True
            self.option_timer = self.option_start = self.current_time
        return False
    
    def checkButtonClick(self, mouse_pos):
        """Kiểm tra click vào các nút mới"""
        if not mouse_pos:
            return False
            
        x, y = mouse_pos
        for button_name, rect in self.button_rects.items():
            if rect.collidepoint(x, y):
                if button_name == 'login':
                    self.next = c.AUTH_SCREEN
                    self.done = True
                elif button_name == 'leaderboard':
                    self.next = c.LEADERBOARD_SCREEN
                    self.done = True
                elif button_name == 'guest':
                    self.next = c.LEVEL
                    self.done = True
                return True
        return False
        
    def update(self, surface, keys, current_time, mouse_pos, mouse_click, events=None):
        self.current_time = self.game_info[c.CURRENT_TIME] = current_time

        if mouse_click and mouse_pos is not None:
            if not self.option_clicked:
                if not self.checkButtonClick(mouse_pos):
                    self.checkOptionClick(mouse_pos)

        if self.option_clicked:
            if (self.current_time - self.option_timer) > 200:
                self.option_frame_index = (self.option_frame_index + 1) % 2
                self.option_timer = self.current_time
                self.option_image = self.option_frames[self.option_frame_index]
            if (self.current_time - self.option_start) > 1300:
                self.done = True

        self.draw(surface)
    
    def draw(self, surface):
        """Vẽ toàn bộ giao diện"""
        # Vẽ background
        if self.bg_image and self.bg_rect:
            surface.blit(self.bg_image, self.bg_rect)
            
        # Vẽ nút option
        if self.option_image and self.option_rect:
            surface.blit(self.option_image, self.option_rect)
            
        # Vẽ các nút
        self.drawButtons(surface)
    
    def drawButtons(self, surface):
        """Vẽ các nút mới"""
        if not self.font:
            return
            
        button_texts = {
            'login': 'Đăng nhập',
            'leaderboard': 'Bảng xếp hạng', 
            'guest': 'Chơi khách'
        }
        
        for button_name, rect in self.button_rects.items():
            # Vẽ nền nút
            pg.draw.rect(surface, c.GREEN, rect)
            pg.draw.rect(surface, c.WHITE, rect, 2)
            
            # Vẽ text
            try:
                text = button_texts[button_name]
                text_surface = self.font.render(text, True, c.WHITE)
                text_rect = text_surface.get_rect(center=rect.center)
                surface.blit(text_surface, text_rect)
            except Exception as e:
                print(f"[ERROR] Lỗi vẽ text nút {button_name}: {e}")