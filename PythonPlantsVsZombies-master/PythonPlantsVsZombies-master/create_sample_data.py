#!/usr/bin/env python3
"""
Tạo dữ liệu mẫu cho game Plants vs Zombies
"""

import json
import os
from datetime import datetime

def create_sample_users():
    """Tạo dữ liệu người dùng mẫu"""
    users = {
        "admin": {
            "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # "password"
            "email": "admin@game.com",
            "created_at": "2024-01-01T00:00:00",
            "last_login": None
        },
        "player1": {
            "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",  # "123456"
            "email": "player1@game.com",
            "created_at": "2024-01-01T00:00:00",
            "last_login": None
        },
        "gamer": {
            "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",  # "123456"
            "email": "gamer@game.com",
            "created_at": "2024-01-01T00:00:00",
            "last_login": None
        }
    }
    
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)
    
    print("✅ Đã tạo file users.json với dữ liệu mẫu")

def create_sample_scores():
    """Tạo dữ liệu điểm số mẫu"""
    scores = {
        "admin": {
            "high_score": 15000,
            "total_games": 25,
            "wins": 20,
            "losses": 5,
            "best_level": 8
        },
        "player1": {
            "high_score": 12000,
            "total_games": 15,
            "wins": 12,
            "losses": 3,
            "best_level": 6
        },
        "gamer": {
            "high_score": 18000,
            "total_games": 30,
            "wins": 25,
            "losses": 5,
            "best_level": 10
        }
    }
    
    with open("scores.json", "w", encoding="utf-8") as f:
        json.dump(scores, f, ensure_ascii=False, indent=2)
    
    print("✅ Đã tạo file scores.json với dữ liệu mẫu")

def main():
    """Hàm chính"""
    print("🌱 Tạo dữ liệu mẫu cho Plants vs Zombies 🌱")
    print("=" * 50)
    
    try:
        # Tạo dữ liệu mẫu
        create_sample_users()
        create_sample_scores()
        
        print("\n🎉 Đã tạo dữ liệu mẫu thành công!")
        print("\n📝 Tài khoản mẫu:")
        print("1. admin / password")
        print("2. player1 / 123456")
        print("3. gamer / 123456")
        
        print("\n🚀 Bây giờ bạn có thể chạy game:")
        print("python main.py")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
