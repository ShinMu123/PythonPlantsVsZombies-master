#!/usr/bin/env python3
"""
Kiểm tra cơ sở dữ liệu
"""

import json
import os

def check_database():
    """Kiểm tra cơ sở dữ liệu"""
    print("🔍 Kiểm tra cơ sở dữ liệu...")
    print("=" * 40)
    
    # Kiểm tra file users.json
    if os.path.exists("users.json"):
        print("✅ File users.json tồn tại")
        try:
            with open("users.json", "r", encoding="utf-8") as f:
                users = json.load(f)
            print(f"   📊 Số người dùng: {len(users)}")
            print("   👥 Danh sách người dùng:")
            for username in users.keys():
                print(f"      - {username}")
        except Exception as e:
            print(f"   ❌ Lỗi đọc file: {e}")
    else:
        print("❌ File users.json không tồn tại")
    
    # Kiểm tra file scores.json
    if os.path.exists("scores.json"):
        print("\n✅ File scores.json tồn tại")
        try:
            with open("scores.json", "r", encoding="utf-8") as f:
                scores = json.load(f)
            print(f"   📊 Số bản ghi điểm: {len(scores)}")
            print("   🏆 Bảng xếp hạng:")
            sorted_scores = sorted(scores.items(), key=lambda x: x[1]['high_score'], reverse=True)
            for i, (username, stats) in enumerate(sorted_scores, 1):
                print(f"      {i}. {username}: {stats['high_score']} điểm")
        except Exception as e:
            print(f"   ❌ Lỗi đọc file: {e}")
    else:
        print("\n❌ File scores.json không tồn tại")
    
    print("\n🎮 Tài khoản để test:")
    print("1. admin / password")
    print("2. test / 123456") 
    print("3. player1 / 123456")
    
    print("\n🚀 Để chạy game:")
    print("python main.py")

def main():
    """Hàm chính"""
    print("🌱 Kiểm tra cơ sở dữ liệu Plants vs Zombies 🌱")
    print("=" * 50)
    
    try:
        check_database()
        print("\n🎉 Kiểm tra hoàn thành!")
    except Exception as e:
        print(f"\n❌ Lỗi: {e}")

if __name__ == "__main__":
    main()
