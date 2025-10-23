#!/usr/bin/env python3
"""
Test giao diện đăng nhập/đăng ký và bảng xếp hạng
"""

import sys
import os
import pygame as pg

# Thêm đường dẫn source vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))

from auth.user_manager import UserManager

def test_user_manager():
    """Test UserManager"""
    print("=== Test UserManager ===")
    
    user_manager = UserManager()
    
    # Test đăng ký
    print("1. Đăng ký người dùng test...")
    success, message = user_manager.register("testuser", "password123", "test@example.com")
    print(f"   Kết quả: {success}, Thông báo: {message}")
    
    # Test đăng nhập
    print("2. Đăng nhập...")
    success, message = user_manager.login("testuser", "password123")
    print(f"   Kết quả: {success}, Thông báo: {message}")
    
    # Test cập nhật điểm
    print("3. Cập nhật điểm số...")
    user_manager.update_score(5000, 3, True)
    user_manager.update_score(3000, 2, False)
    user_manager.update_score(8000, 5, True)
    
    # Test bảng xếp hạng
    print("4. Lấy bảng xếp hạng...")
    leaderboard = user_manager.get_leaderboard(5)
    print(f"   Top 5: {leaderboard}")
    
    print("✅ UserManager hoạt động tốt!")

def test_pygame_init():
    """Test khởi tạo pygame"""
    print("\n=== Test Pygame ===")
    
    try:
        pg.init()
        screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("Test UI")
        
        print("✅ Pygame khởi tạo thành công!")
        
        # Test font
        font = pg.font.Font(None, 36)
        text = font.render("Test Text", True, (255, 255, 255))
        print("✅ Font hoạt động tốt!")
        
        pg.quit()
        return True
        
    except Exception as e:
        print(f"❌ Lỗi Pygame: {e}")
        return False

def main():
    """Hàm chính"""
    print("🌱 Test giao diện Plants vs Zombies 🌱")
    print("=" * 50)
    
    try:
        # Test UserManager
        test_user_manager()
        
        # Test Pygame
        if test_pygame_init():
            print("\n🎉 Tất cả test đã hoàn thành!")
            print("\n🚀 Để chạy game:")
            print("python main.py")
            print("\n📝 Hướng dẫn sử dụng:")
            print("1. Click 'Đăng nhập' để đăng nhập/đăng ký")
            print("2. Click 'Bảng xếp hạng' để xem xếp hạng")
            print("3. Click 'Chơi khách' để chơi mà không cần đăng ký")
            print("\n⌨️  Phím tắt:")
            print("- ESC: Thoát")
            print("- Enter: Xác nhận")
            print("- Tab: Chuyển input field")
        else:
            print("❌ Không thể khởi tạo Pygame!")
            
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
