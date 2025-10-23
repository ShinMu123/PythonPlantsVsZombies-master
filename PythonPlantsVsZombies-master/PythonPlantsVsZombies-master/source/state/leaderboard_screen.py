__author__ = 'marble_xu'

import pygame as pg
from .. import tool
from .. import constants as c
from ..auth.global_auth import user_manager

class LeaderboardScreen(tool.State):
    def __init__(self):
        tool.State.__init__(self)
        self.sort_by = 'score'  # 'score' hoặc 'level'
        self.font = None
        self.small_font = None
        self.button_rects = {}
        
    def startup(self, current_time, persist):
        self.next = c.MAIN_MENU
        self.persist = persist
        self.game_info = persist
        self.setup_fonts()
        self.setup_ui()
        
    def setup_fonts(self):
        """Thiết lập font chữ"""
        try:
            self.font = pg.font.Font(None, 48)
            self.small_font = pg.font.Font(None, 24)
        except:
            self.font = pg.font.SysFont('arial', 48)
            self.small_font = pg.font.SysFont('arial', 24)
    
    def setup_ui(self):
        """Thiết lập giao diện người dùng"""
        # Vị trí các nút
        self.button_rects = {
            'back': pg.Rect(50, 50, 100, 40),
            'sort_score': pg.Rect(200, 100, 150, 40),
            'sort_level': pg.Rect(400, 100, 150, 40)
        }
    
    def handle_click(self, mouse_pos):
        """Xử lý click chuột"""
        x, y = mouse_pos
        
        # Kiểm tra click vào các nút
        if self.button_rects['back'].collidepoint(x, y):
            self.done = True
        elif self.button_rects['sort_score'].collidepoint(x, y):
            self.sort_by = 'score'
        elif self.button_rects['sort_level'].collidepoint(x, y):
            self.sort_by = 'level'
    
    def update(self, surface, keys, current_time, mouse_pos, mouse_click, events=None):
        """Cập nhật màn hình"""
        self.current_time = self.game_info[c.CURRENT_TIME] = current_time

        # Xử lý sự kiện
        if keys[pg.K_ESCAPE]:
            self.done = True
        if mouse_click[0] and mouse_pos:
            self.handle_click(mouse_pos)

        # Vẽ giao diện
        self.draw(surface)
    
    def draw(self, surface):
        """Vẽ giao diện"""
        # Nền gradient đẹp
        surface.fill(c.BLACK)
        for i in range(0, 800, 40):
            color = (i // 20, i // 30, i // 40)
            pg.draw.rect(surface, color, (i, 0, 40, 600))
        
        # Tiêu đề với hiệu ứng
        title_text = "BẢNG XẾP HẠNG"
        title_surface = self.font.render(title_text, True, c.GOLD)
        title_rect = title_surface.get_rect(center=(400, 80))
        
        # Vẽ bóng cho tiêu đề
        shadow_surface = self.font.render(title_text, True, c.BLACK)
        surface.blit(shadow_surface, (title_rect.x + 2, title_rect.y + 2))
        surface.blit(title_surface, title_rect)
        
        # Nút quay lại
        self.draw_button(surface, "Quay lại", self.button_rects['back'])
        
        # Nút sắp xếp
        self.draw_button(surface, "Theo điểm số", self.button_rects['sort_score'], 
                        self.sort_by == 'score')
        self.draw_button(surface, "Theo level", self.button_rects['sort_level'], 
                        self.sort_by == 'level')
        
        # Vẽ bảng xếp hạng
        self.draw_leaderboard(surface)
    
    def draw_button(self, surface, text, rect, active=False):
        """Vẽ nút"""
        # Màu nút với hiệu ứng
        if active:
            color = c.SKY_BLUE
            border_color = c.WHITE
        else:
            color = c.GREEN
            border_color = c.WHITE
        
        # Vẽ nền nút
        pg.draw.rect(surface, color, rect)
        
        # Vẽ viền nút
        pg.draw.rect(surface, border_color, rect, 2)
        
        # Vẽ hiệu ứng bóng
        shadow_rect = pg.Rect(rect.x + 2, rect.y + 2, rect.width, rect.height)
        pg.draw.rect(surface, (0, 0, 0, 100), shadow_rect)
        
        # Vẽ text với hiệu ứng
        text_surface = self.small_font.render(text, True, c.WHITE)
        text_rect = text_surface.get_rect(center=rect.center)
        
        # Vẽ bóng cho text
        shadow_text = self.small_font.render(text, True, c.BLACK)
        surface.blit(shadow_text, (text_rect.x + 1, text_rect.y + 1))
        surface.blit(text_surface, text_rect)
    
    def draw_leaderboard(self, surface):
        """Vẽ bảng xếp hạng"""
        # Lấy dữ liệu xếp hạng
        if self.sort_by == 'score':
            leaderboard = user_manager.get_leaderboard(10)
            sort_title = "ĐIỂM SỐ"
        else:
            leaderboard = user_manager.get_leaderboard_by_level(10)
            sort_title = "LEVEL"
        
        # Tiêu đề cột
        y_start = 200
        header_y = y_start - 30
        
        # Vẽ header
        headers = ["Hạng", "Tên người dùng", sort_title, "Thắng", "Thua", "Tổng game"]
        header_x = [50, 150, 300, 450, 550, 650]
        
        for i, header in enumerate(headers):
            header_surface = self.small_font.render(header, True, c.GOLD)
            surface.blit(header_surface, (header_x[i], header_y))
        
        # Vẽ dữ liệu
        for i, (username, stats) in enumerate(leaderboard):
            y = y_start + i * 30
            
            # Màu cho top 3
            if i < 3:
                color = c.GOLD if i == 0 else (c.SILVER if i == 1 else c.BRONZE)
            else:
                color = c.WHITE
            
            # Vẽ thông tin
            rank = i + 1
            score_or_level = stats['high_score'] if self.sort_by == 'score' else stats['best_level']
            wins = stats['wins']
            losses = stats['losses']
            total = stats['total_games']
            
            # Cắt tên người dùng nếu quá dài
            display_username = username[:15] + "..." if len(username) > 15 else username
            
            # Vẽ dữ liệu
            data = [str(rank), display_username, str(score_or_level), str(wins), str(losses), str(total)]
            
            for j, text in enumerate(data):
                text_surface = self.small_font.render(text, True, color)
                surface.blit(text_surface, (header_x[j], y))
        
        # Hiển thị thông báo nếu không có dữ liệu
        if not leaderboard:
            no_data_surface = self.small_font.render("Chưa có dữ liệu xếp hạng!", True, c.RED)
            no_data_rect = no_data_surface.get_rect(center=(400, 300))
            surface.blit(no_data_surface, no_data_rect)
