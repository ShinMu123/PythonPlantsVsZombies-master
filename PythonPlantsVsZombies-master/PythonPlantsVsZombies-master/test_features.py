#!/usr/bin/env python3
"""
Script test cho các tính năng mới của Plants vs Zombies
"""

import sys
import os

# Thêm đường dẫn source vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))

from auth.user_manager import UserManager

def test_user_management():
    """Test hệ thống quản lý người dùng"""
    print("=== Test hệ thống quản lý người dùng ===")
    
    # Tạo user manager mới
    user_manager = UserManager()
    
    # Test đăng ký
    print("1. Test đăng ký người dùng mới...")
    success, message = user_manager.register("testuser", "password123", "test@example.com")
    print(f"   Kết quả: {success}, Thông báo: {message}")
    
    # Test đăng nhập
    print("2. Test đăng nhập...")
    success, message = user_manager.login("testuser", "password123")
    print(f"   Kết quả: {success}, Thông báo: {message}")
    
    # Test cập nhật điểm
    print("3. Test cập nhật điểm số...")
    user_manager.update_score(5000, 3, True)
    user_manager.update_score(3000, 2, False)
    user_manager.update_score(8000, 5, True)
    
    # Test lấy thống kê
    print("4. Test lấy thống kê người dùng...")
    stats = user_manager.get_user_stats("testuser")
    print(f"   Thống kê: {stats}")
    
    # Test bảng xếp hạng
    print("5. Test bảng xếp hạng...")
    leaderboard = user_manager.get_leaderboard(5)
    print(f"   Top 5 điểm cao: {leaderboard}")
    
    leaderboard_level = user_manager.get_leaderboard_by_level(5)
    print(f"   Top 5 level cao: {leaderboard_level}")
    
    print("✅ Test hoàn thành!")

def test_data_files():
    """Test file dữ liệu"""
    print("\n=== Test file dữ liệu ===")
    
    # Kiểm tra file users.json
    if os.path.exists("users.json"):
        print("✅ File users.json đã được tạo")
        with open("users.json", "r", encoding="utf-8") as f:
            import json
            data = json.load(f)
            print(f"   Số người dùng: {len(data)}")
    else:
        print("❌ File users.json chưa được tạo")
    
    # Kiểm tra file scores.json
    if os.path.exists("scores.json"):
        print("✅ File scores.json đã được tạo")
        with open("scores.json", "r", encoding="utf-8") as f:
            import json
            data = json.load(f)
            print(f"   Số bản ghi điểm: {len(data)}")
    else:
        print("❌ File scores.json chưa được tạo")

def main():
    """Hàm chính"""
    print("🌱 Test tính năng Plants vs Zombies 🌱")
    print("=" * 50)
    
    try:
        test_user_management()
        test_data_files()
        
        print("\n🎉 Tất cả test đã hoàn thành thành công!")
        print("\nĐể chạy game với tính năng mới:")
        print("1. Chạy: python main.py")
        print("2. Hoặc chạy: run_ppvz_local.bat")
        print("\nTính năng mới:")
        print("- Đăng nhập/Đăng ký")
        print("- Bảng xếp hạng")
        print("- Hệ thống điểm số")
        
    except Exception as e:
        print(f"❌ Lỗi trong quá trình test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
