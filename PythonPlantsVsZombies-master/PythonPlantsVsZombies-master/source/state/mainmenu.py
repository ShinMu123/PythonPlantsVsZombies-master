__author__ = 'marble_xu'

import pygame as pg
from .. import tool
from .. import constants as c

class Menu(tool.State):
    def __init__(self):
        tool.State.__init__(self)
    
    def startup(self, current_time, persist):
        self.next = c.LEVEL
        self.persist = persist
        self.game_info = persist
        # Chuẩn bị background và nút chọn (Adventure)
        self.setupBackground()
        self.setupOption()

    def setupBackground(self):
        frame_rect = [80, 0, 800, 600]
        self.bg_image = tool.get_image(tool.GFX[c.MAIN_MENU_IMAGE], *frame_rect)
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.x = 0
        self.bg_rect.y = 0
        
    def setupOption(self):
        self.option_frames = []
        frame_names = [c.OPTION_ADVENTURE + '_0', c.OPTION_ADVENTURE + '_1']
        frame_rect = [0, 0, 165, 77]
        
        for name in frame_names:
            self.option_frames.append(tool.get_image(tool.GFX[name], *frame_rect, c.BLACK, 1.7))
        
        self.option_frame_index = 0
        self.option_image = self.option_frames[self.option_frame_index]
        self.option_rect = self.option_image.get_rect()
        self.option_rect.x = 435
        self.option_rect.y = 75
        
        self.option_start = 0
        self.option_timer = 0
        self.option_clicked = False
        
        # Thiết lập các nút mới
        self.setupButtons()
    
    def setupButtons(self):
        """Thiết lập các nút mới"""
        self.font = pg.font.Font(None, 24)
        self.button_rects = {
            'login': pg.Rect(50, 200, 120, 40),
            'leaderboard': pg.Rect(50, 260, 120, 40),
            'guest': pg.Rect(50, 320, 120, 40)
        }
    
    def checkOptionClick(self, mouse_pos):
        x, y = mouse_pos
        if(x >= self.option_rect.x and x <= self.option_rect.right and
           y >= self.option_rect.y and y <= self.option_rect.bottom):
            self.option_clicked = True
            self.option_timer = self.option_start = self.current_time
        return False
    
    def checkButtonClick(self, mouse_pos):
        """Kiểm tra click vào các nút mới"""
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
                    # Chơi với tư cách khách
                    self.next = c.LEVEL
                    self.done = True
                return True
        return False
        
    def update(self, surface, keys, current_time, mouse_pos, mouse_click, events=None):
        self.current_time = self.game_info[c.CURRENT_TIME] = current_time
        
        if not self.option_clicked:
            if mouse_pos:
                # Kiểm tra click vào các nút mới trước
                if not self.checkButtonClick(mouse_pos):
                    self.checkOptionClick(mouse_pos)
        else:
            if(self.current_time - self.option_timer) > 200:
                self.option_frame_index += 1
                if self.option_frame_index >= 2:
                    self.option_frame_index = 0
                self.option_timer = self.current_time
                self.option_image = self.option_frames[self.option_frame_index]
            if(self.current_time - self.option_start) > 1300:
                self.done = True

        surface.blit(self.bg_image, self.bg_rect)
        surface.blit(self.option_image, self.option_rect)
        
        # Vẽ các nút mới
        self.drawButtons(surface)
    
    def drawButtons(self, surface):
        """Vẽ các nút mới"""
        button_texts = {
            'login': 'Đăng nhập',
            'leaderboard': 'Bảng xếp hạng',
            'guest': 'Chơi khách'
        }
        
        for button_name, rect in self.button_rects.items():
            # Vẽ nút
            pg.draw.rect(surface, c.GREEN, rect)
            pg.draw.rect(surface, c.WHITE, rect, 2)
            
            # Vẽ text
            text = button_texts[button_name]
            text_surface = self.font.render(text, True, c.WHITE)
            text_rect = text_surface.get_rect(center=rect.center)
            surface.blit(text_surface, text_rect)