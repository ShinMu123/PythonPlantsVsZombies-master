import pygame as pg
import os
from .state import State

class AuthScreen(State):
    def __init__(self):
        State.__init__(self)
        self.font = None
        self.small_font = None
        self.setup_fonts()
        self.username = ""
        self.password = ""
        self.error_message = ""
        self.active_input = None
        self.button_rect = pg.Rect(250, 350, 200, 50)
        self.username_rect = pg.Rect(200, 200, 300, 40)
        self.password_rect = pg.Rect(200, 260, 300, 40)
        self.show_password = False

    def setup_fonts(self):
        """Thiết lập font Times New Roman có hỗ trợ tiếng Việt"""
        try:
            font_path = r"C:\WINDOWS\Fonts\TIMES.TTF"
            if not pg.font.get_init():
                pg.font.init()

            if os.path.exists(font_path):
                self.font = pg.font.Font(font_path, 36)
                self.small_font = pg.font.Font(font_path, 24)
                print("Đã load font Times từ Windows:", font_path)
            else:
                # fallback sang font hệ thống nếu không có file
                self.font = pg.font.SysFont('timesnewroman', 36)
                self.small_font = pg.font.SysFont('timesnewroman', 24)
                print("Không tìm thấy file TIMES.TTF, dùng SysFont('timesnewroman')")
        except Exception as e:
            print("Lỗi khi load font:", e)
            self.font = pg.font.SysFont('arial', 36)
            self.small_font = pg.font.SysFont('arial', 24)

    def draw_text(self, surface, text, pos, color=(255, 255, 255)):
        text_surface = self.small_font.render(text, True, color)
        surface.blit(text_surface, pos)

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.username_rect.collidepoint(event.pos):
                self.active_input = "username"
            elif self.password_rect.collidepoint(event.pos):
                self.active_input = "password"
            elif self.button_rect.collidepoint(event.pos):
                self.authenticate()
            else:
                self.active_input = None

        if event.type == pg.KEYDOWN:
            if self.active_input == "username":
                if event.key == pg.K_BACKSPACE:
                    self.username = self.username[:-1]
                else:
                    self.username += event.unicode
            elif self.active_input == "password":
                if event.key == pg.K_BACKSPACE:
                    self.password = self.password[:-1]
                else:
                    self.password += event.unicode

    def authenticate(self):
        if self.username == "admin" and self.password == "123":
            print("Đăng nhập thành công!")
            self.done = True
            self.next = "GAMEPLAY"
        else:
            self.error_message = "Sai tên đăng nhập hoặc mật khẩu!"

    def update(self, surface, keys, dt):
        surface.fill((0, 0, 0))

        # Tiêu đề
        title_surface = self.font.render("ĐĂNG NHẬP", True, (255, 255, 0))
        surface.blit(title_surface, (200, 100))

        # Username box
        pg.draw.rect(surface, (255, 255, 255), self.username_rect, 2)
        username_display = self.username if self.username else "Tên đăng nhập"
        self.draw_text(surface, username_display, (self.username_rect.x + 10, self.username_rect.y + 10))

        # Password box
        pg.draw.rect(surface, (255, 255, 255), self.password_rect, 2)
        display_pass = self.password if self.show_password else "*" * len(self.password)
        password_display = display_pass if display_pass else "Mật khẩu"
        self.draw_text(surface, password_display, (self.password_rect.x + 10, self.password_rect.y + 10))

        # Nút đăng nhập
        pg.draw.rect(surface, (0, 200, 0), self.button_rect)
        self.draw_text(surface, "Đăng nhập", (self.button_rect.x + 50, self.button_rect.y + 10))

        # Hiển thị lỗi
        if self.error_message:
            error_surface = self.small_font.render(self.error_message, True, (255, 0, 0))
            surface.blit(error_surface, (200, 420))
