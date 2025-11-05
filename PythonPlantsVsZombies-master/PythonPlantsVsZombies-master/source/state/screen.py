__author__ = 'marble_xu'

import pygame as pg
from .. import tool
from .. import constants as c

class Screen(tool.State):
    def __init__(self):
        tool.State.__init__(self)
        self.end_time = 3000

    def startup(self, current_time, persist):
        self.start_time = current_time
        self.next = c.LEVEL
        self.persist = persist
        self.game_info = persist
        name = self.getImageName()
        self.setupImage(name)
        self.next = self.set_next_state()

    # Lớp cơ sở cho màn hình kết thúc (thắng/thua)
    # Hiển thị một hình lớn trong một khoảng thời gian, sau đó chuyển state
    
    def getImageName(self):
        pass

    def set_next_state(self):
        pass

    def setupImage(self, name):
        frame_rect = [0, 0, 800, 600]
        self.image = tool.get_image(tool.GFX[name], *frame_rect)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, surface, keys, current_time, mouse_pos, mouse_click, events=None):
        if(current_time - self.start_time) < self.end_time:
            surface.fill(c.WHITE)
            surface.blit(self.image, self.rect)
        else:
            self.done = True

class GameVictoryScreen(Screen):
    def __init__(self):
        Screen.__init__(self)

    def getImageName(self):
        return c.GAME_VICTORY_IMAGE

    def set_next_state(self):
        return c.LEVEL

    def update(self, surface, keys, current_time, mouse_pos, mouse_click, events=None):
        if mouse_click and mouse_click[0]:  # left click to continue
            self.done = True
        super().update(surface, keys, current_time, mouse_pos, mouse_click, events)

class GameLoseScreen(Screen):
    def __init__(self):
        Screen.__init__(self)
    
    def getImageName(self):
        return c.GAME_LOOSE_IMAGE
    
    def set_next_state(self):
        return c.MAIN_MENU