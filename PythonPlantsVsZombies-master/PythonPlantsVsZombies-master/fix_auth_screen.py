#!/usr/bin/env python3
"""
Sửa lỗi màn hình đăng nhập
"""

import json
import os

def create_users_json():
    """Tạo file users.json"""
    users = {
        "admin": {
            "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
            "email": "admin@game.com",
            "created_at": "2024-01-01T00:00:00",
            "last_login": None
        },
        "test": {
            "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
            "email": "test@game.com",
            "created_at": "2024-01-01T00:00:00",
            "last_login": None
        }
    }
    
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)
    print("✅ Đã tạo users.json")

def create_scores_json():
    """Tạo file scores.json"""
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
    print("✅ Đã tạo scores.json")

def main():
    print("🔧 Sửa lỗi màn hình đăng nhập")
    print("=" * 40)
    
    try:
        create_users_json()
        create_scores_json()
        
        print("\n🎉 Đã tạo dữ liệu mẫu!")
        print("\n📝 Tài khoản test:")
        print("- admin / password")
        print("- test / 123456")
        
        print("\n🚀 Chạy game:")
        print("python main.py")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    main()
