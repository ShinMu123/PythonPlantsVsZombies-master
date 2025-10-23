#!/usr/bin/env python3
"""
Test màn hình đăng nhập/đăng ký
"""

import sys
import os
import pygame as pg

# Thêm đường dẫn source vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))

def test_auth_screen():
    """Test màn hình đăng nhập"""
    print("=== Test màn hình đăng nhập ===")
    
    try:
        # Khởi tạo pygame
        pg.init()
        screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Test Auth Screen")
        
        # Import và tạo auth screen
        from state.auth_screen import AuthScreen
        from constants import constants as c
        
        auth_screen = AuthScreen()
        auth_screen.startup(0, {c.CURRENT_TIME: 0})
        
        print("✅ Auth screen khởi tạo thành công!")
        
        # Test vẽ màn hình
        auth_screen.draw(screen)
        pg.display.flip()
        print("✅ Vẽ màn hình thành công!")
        
        # Test xử lý click
        mouse_pos = (400, 300)
        mouse_click = [True, False]
        auth_screen.update(screen, 1000, mouse_pos, mouse_click)
        print("✅ Xử lý click thành công!")
        
        # Test xử lý bàn phím
        event = pg.event.Event(pg.KEYDOWN, key=pg.K_a, unicode='a')
        auth_screen.handle_keyboard_event(event)
        print("✅ Xử lý bàn phím thành công!")
        
        pg.quit()
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Hàm chính"""
    print("🌱 Test màn hình đăng nhập 🌱")
    print("=" * 50)
    
    if test_auth_screen():
        print("\n🎉 Test thành công!")
        print("\n🚀 Bây giờ bạn có thể chạy game:")
        print("python main.py")
    else:
        print("\n❌ Test thất bại!")

if __name__ == "__main__":
    main()
