#!/usr/bin/env python3
"""
Test nhập tiếng Việt có dấu
"""

import sys
import os
import pygame as pg

# Thêm đường dẫn source vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))

def test_vietnamese_input():
    """Test nhập tiếng Việt có dấu"""
    print("🔤 Test nhập tiếng Việt có dấu...")
    
    try:
        # Khởi tạo pygame
        pg.init()
        screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Test Vietnamese Input")
        
        # Import và tạo auth screen
        from state.auth_screen_fixed import AuthScreen
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
        
        # Test xử lý bàn phím tiếng Việt
        vietnamese_chars = ['ă', 'â', 'ê', 'ô', 'ơ', 'ư', 'đ']
        for char in vietnamese_chars:
            event = pg.event.Event(pg.KEYDOWN, key=pg.K_a, unicode=char)
            auth_screen.handle_keyboard(event)
            print(f"✅ Nhập ký tự '{char}' thành công!")
        
        pg.quit()
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Hàm chính"""
    print("🌱 Test nhập tiếng Việt có dấu 🌱")
    print("=" * 50)
    
    if test_vietnamese_input():
        print("\n🎉 Test thành công!")
        print("\n📝 Hướng dẫn sử dụng:")
        print("1. Click vào ô nhập liệu để chọn")
        print("2. Gõ tiếng Việt có dấu: ă, â, ê, ô, ơ, ư, đ")
        print("3. Click nút 'Đăng nhập' hoặc nhấn Enter")
        print("4. Nhấn Tab để chuyển giữa các ô")
        print("5. Nhấn ESC để thoát")
        
        print("\n🚀 Chạy game:")
        print("python main.py")
    else:
        print("\n❌ Test thất bại!")

if __name__ == "__main__":
    main()
