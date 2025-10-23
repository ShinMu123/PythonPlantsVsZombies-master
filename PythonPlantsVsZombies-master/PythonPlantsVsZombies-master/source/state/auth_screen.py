__author__ = 'marble_xu'

import pygame as pg
from .. import tool
from .. import constants as c
from ..auth.global_auth import user_manager

class AuthScreen(tool.State):
    def __init__(self):
        tool.State.__init__(self)
        self.mode = 'login'  # 'login' hoặc 'register'
        self.input_username = ''
        self.input_password = ''
        self.input_email = ''
        self.active_input = 'username'  # 'username', 'password', 'email'
        self.message = ''
        self.message_timer = 0
        self.font = None
        self.small_font = None
        self.input_rects = {}
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
            self.font = pg.font.Font(None, 36)
            self.small_font = pg.font.Font(None, 24)
        except:
            self.font = pg.font.SysFont('arial', 36)
            self.small_font = pg.font.SysFont('arial', 24)
    
    def setup_ui(self):
        """Thiết lập giao diện người dùng"""
        # Vị trí các input field (cải thiện vị trí)
        self.input_rects = {
            'username': pg.Rect(300, 200, 250, 35),
            'password': pg.Rect(300, 250, 250, 35),
            'email': pg.Rect(300, 300, 250, 35)
        }
        
        # Vị trí các nút (cải thiện vị trí và kích thước)
        self.button_rects = {
            'login': pg.Rect(200, 400, 120, 45),
            'register': pg.Rect(480, 400, 120, 45),
            'switch_mode': pg.Rect(300, 480, 200, 35),
            'guest': pg.Rect(300, 530, 200, 35)
        }
    
    
    def handle_click(self, mouse_pos):
        """Xử lý click chuột"""
        x, y = mouse_pos
        
        # Kiểm tra click vào input fields
        for input_name, rect in self.input_rects.items():
            if rect.collidepoint(x, y):
                self.active_input = input_name
                return
        
        # Kiểm tra click vào các nút
        if self.button_rects['login'].collidepoint(x, y):
            self.login()
        elif self.button_rects['register'].collidepoint(x, y):
            self.register()
        elif self.button_rects['switch_mode'].collidepoint(x, y):
            self.switch_mode()
        elif self.button_rects['guest'].collidepoint(x, y):
            self.play_as_guest()
    
    def login(self):
        """Xử lý đăng nhập"""
        if not self.input_username or not self.input_password:
            self.show_message("Vui lòng nhập đầy đủ thông tin!")
            return
        
        success, message = user_manager.login(self.input_username, self.input_password)
        self.show_message(message)
        
        if success:
            self.done = True
    
    def register(self):
        """Xử lý đăng ký"""
        if not self.input_username or not self.input_password:
            self.show_message("Vui lòng nhập đầy đủ thông tin!")
            return
        
        success, message = user_manager.register(
            self.input_username, 
            self.input_password, 
            self.input_email
        )
        self.show_message(message)
        
        if success:
            self.mode = 'login'
            self.input_username = ''
            self.input_password = ''
            self.input_email = ''
    
    def switch_mode(self):
        """Chuyển đổi giữa đăng nhập và đăng ký"""
        self.mode = 'register' if self.mode == 'login' else 'login'
        self.input_username = ''
        self.input_password = ''
        self.input_email = ''
        self.active_input = 'username'
        self.message = ''
    
    def play_as_guest(self):
        """Chơi với tư cách khách"""
        user_manager.logout()
        self.done = True
    
    def show_message(self, message):
        """Hiển thị thông báo"""
        self.message = message
        self.message_timer = pg.time.get_ticks()
    
    def update(self, surface, current_time, mouse_pos, mouse_click):
        """Cập nhật màn hình"""
        self.current_time = self.game_info[c.CURRENT_TIME] = current_time
        
        # Xử lý sự kiện
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.handle_keyboard_event(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                if mouse_pos:
                    self.handle_click(mouse_pos)
        
        # Vẽ giao diện
        self.draw(surface)
    
    def handle_keyboard_event(self, event):
        """Xử lý sự kiện bàn phím"""
        if event.key == pg.K_ESCAPE:
            self.done = True
        elif event.key == pg.K_RETURN:
            if self.mode == 'login':
                self.login()
            else:
                self.register()
        elif event.key == pg.K_TAB:
            # Chuyển đổi giữa các input field
            if self.active_input == 'username':
                self.active_input = 'password'
            elif self.active_input == 'password':
                if self.mode == 'register':
                    self.active_input = 'email'
                else:
                    self.active_input = 'username'
            elif self.active_input == 'email':
                self.active_input = 'username'
        elif event.key == pg.K_BACKSPACE:
            # Xóa ký tự cuối
            if self.active_input == 'username':
                self.input_username = self.input_username[:-1]
            elif self.active_input == 'password':
                self.input_password = self.input_password[:-1]
            elif self.active_input == 'email':
                self.input_email = self.input_email[:-1]
        else:
            # Thêm ký tự mới
            char = event.unicode
            if char and char.isprintable():
                if self.active_input == 'username' and len(self.input_username) < 20:
                    self.input_username += char
                elif self.active_input == 'password' and len(self.input_password) < 30:
                    self.input_password += char
                elif self.active_input == 'email' and len(self.input_email) < 50:
                    self.input_email += char
    
    def draw(self, surface):
        """Vẽ giao diện"""
        # Nền gradient (từ đen đến xanh đậm)
        surface.fill(c.BLACK)
        # Vẽ một số hình chữ nhật để tạo hiệu ứng nền
        for i in range(0, 800, 50):
            color = (i // 10, i // 20, i // 30)
            pg.draw.rect(surface, color, (i, 0, 50, 600))
        
        # Tiêu đề với hiệu ứng
        title_text = "ĐĂNG NHẬP" if self.mode == 'login' else "ĐĂNG KÝ"
        title_surface = self.font.render(title_text, True, c.GOLD)
        title_rect = title_surface.get_rect(center=(400, 100))
        
        # Vẽ bóng cho tiêu đề
        shadow_surface = self.font.render(title_text, True, c.BLACK)
        surface.blit(shadow_surface, (title_rect.x + 2, title_rect.y + 2))
        surface.blit(title_surface, title_rect)
        
        # Vẽ input fields
        self.draw_input_field(surface, "Tên đăng nhập:", self.input_username, 
                             self.input_rects['username'], self.active_input == 'username')
        
        self.draw_input_field(surface, "Mật khẩu:", self.input_password, 
                             self.input_rects['password'], self.active_input == 'password', True)
        
        if self.mode == 'register':
            self.draw_input_field(surface, "Email (tùy chọn):", self.input_email, 
                                 self.input_rects['email'], self.active_input == 'email')
        
        # Vẽ các nút
        self.draw_button(surface, "Đăng nhập", self.button_rects['login'], 
                        self.mode == 'login')
        
        self.draw_button(surface, "Đăng ký", self.button_rects['register'], 
                        self.mode == 'register')
        
        # Nút chuyển đổi
        switch_text = "Chuyển sang đăng ký" if self.mode == 'login' else "Chuyển sang đăng nhập"
        self.draw_button(surface, switch_text, self.button_rects['switch_mode'])
        
        # Nút chơi với tư cách khách
        self.draw_button(surface, "Chơi với tư cách khách", self.button_rects['guest'])
        
        # Hiển thị thông báo
        if self.message and (self.current_time - self.message_timer) < 3000:
            message_surface = self.small_font.render(self.message, True, c.RED)
            message_rect = message_surface.get_rect(center=(400, 450))
            surface.blit(message_surface, message_rect)
    
    def draw_input_field(self, surface, label, text, rect, active, password=False):
        """Vẽ input field"""
        # Vẽ label với màu sắc đẹp
        label_surface = self.small_font.render(label, True, c.LIGHTYELLOW)
        surface.blit(label_surface, (rect.x - 150, rect.y + 5))
        
        # Vẽ khung input với hiệu ứng
        if active:
            # Hiệu ứng nhấp nháy cho input đang active
            if (self.current_time // 500) % 2:
                pg.draw.rect(surface, c.SKY_BLUE, rect, 3)
            else:
                pg.draw.rect(surface, c.WHITE, rect, 3)
        else:
            pg.draw.rect(surface, c.WHITE, rect, 2)
        
        # Vẽ nền input
        pg.draw.rect(surface, (30, 30, 30), rect)
        
        # Vẽ text
        display_text = text
        if password:
            display_text = '*' * len(text)
        
        text_surface = self.small_font.render(display_text, True, c.WHITE)
        surface.blit(text_surface, (rect.x + 5, rect.y + 8))
        
        # Vẽ con trỏ nếu đang active
        if active and (self.current_time // 300) % 2:
            cursor_x = rect.x + 5 + text_surface.get_width()
            pg.draw.line(surface, c.WHITE, (cursor_x, rect.y + 8), (cursor_x, rect.y + 28))
    
    def draw_button(self, surface, text, rect, active=False):
        """Vẽ nút"""
        # Màu nút với hiệu ứng
        if active:
            color = c.SKY_BLUE
            border_color = c.WHITE
        else:
            color = c.GREEN
            border_color = c.WHITE
        
        # Vẽ nền nút với gradient
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
