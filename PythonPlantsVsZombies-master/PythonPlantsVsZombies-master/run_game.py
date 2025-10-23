#!/usr/bin/env python3
"""
Script chạy game Plants vs Zombies với tính năng mới
"""

import os
import sys
import json

def create_sample_data():
    """Tạo dữ liệu mẫu"""
    print("🔧 Tạo dữ liệu mẫu...")
    
    # Tạo users.json
    users = {
        "admin": {
            "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
            "email": "admin@game.com",
            "created_at": "2024-01-01T00:00:00",
            "last_login": None
        },
        "test": {
            "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",  # "123456"
            "email": "test@game.com",
            "created_at": "2024-01-01T00:00:00",
            "last_login": None
        }
    }
    
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)
    
    # Tạo scores.json
    scores = {
        "admin": {
            "high_score": 10000,
            "total_games": 10,
            "wins": 8,
            "losses": 2,
            "best_level": 5
        },
        "test": {
            "high_score": 5000,
            "total_games": 5,
            "wins": 3,
            "losses": 2,
            "best_level": 3
        }
    }
    
    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)
    
    print("✅ Đã tạo dữ liệu mẫu!")

def main():
    """Hàm chính"""
    print("🌱 Plants vs Zombies - Phiên bản có đăng nhập và bảng xếp hạng 🌱")
    print("=" * 70)
    
    try:
        # Tạo dữ liệu mẫu
        create_sample_data()
        
        print("\n📝 Tài khoản mẫu:")
        print("1. admin / password")
        print("2. test / 123456")
        
        print("\n🎮 Hướng dẫn sử dụng:")
        print("1. Click 'Đăng nhập' để đăng nhập/đăng ký")
        print("2. Click 'Bảng xếp hạng' để xem xếp hạng")
        print("3. Click 'Chơi khách' để chơi mà không cần đăng ký")
        
        print("\n🚀 Đang khởi động game...")
        
        # Chạy game
        import main
        main.main()
        
    except KeyboardInterrupt:
        print("\n👋 Tạm biệt!")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
