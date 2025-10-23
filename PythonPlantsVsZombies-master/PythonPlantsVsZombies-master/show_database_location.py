#!/usr/bin/env python3
"""
Hiển thị vị trí cơ sở dữ liệu
"""

import os
import json

def show_database_location():
    """Hiển thị vị trí cơ sở dữ liệu"""
    print("🗂️ Vị trí cơ sở dữ liệu Plants vs Zombies")
    print("=" * 50)
    
    # Lấy thư mục hiện tại
    current_dir = os.getcwd()
    print(f"📁 Thư mục hiện tại: {current_dir}")
    
    # Kiểm tra file users.json
    users_file = os.path.join(current_dir, "users.json")
    if os.path.exists(users_file):
        print(f"✅ users.json: {users_file}")
        try:
            with open(users_file, "r", encoding="utf-8") as f:
                users = json.load(f)
            print(f"   👥 Số người dùng: {len(users)}")
            for username in users.keys():
                print(f"      - {username}")
        except Exception as e:
            print(f"   ❌ Lỗi đọc file: {e}")
    else:
        print(f"❌ users.json: Không tìm thấy")
    
    # Kiểm tra file scores.json
    scores_file = os.path.join(current_dir, "scores.json")
    if os.path.exists(scores_file):
        print(f"✅ scores.json: {scores_file}")
        try:
            with open(scores_file, "r", encoding="utf-8") as f:
                scores = json.load(f)
            print(f"   📊 Số bản ghi điểm: {len(scores)}")
            # Hiển thị top 3
            sorted_scores = sorted(scores.items(), key=lambda x: x[1]['high_score'], reverse=True)
            print("   🏆 Top 3 điểm cao:")
            for i, (username, stats) in enumerate(sorted_scores[:3], 1):
                print(f"      {i}. {username}: {stats['high_score']} điểm")
        except Exception as e:
            print(f"   ❌ Lỗi đọc file: {e}")
    else:
        print(f"❌ scores.json: Không tìm thấy")
    
    print(f"\n📂 Đường dẫn đầy đủ:")
    print(f"   users.json:  {os.path.abspath(users_file)}")
    print(f"   scores.json: {os.path.abspath(scores_file)}")
    
    print(f"\n🔍 Cách mở thư mục:")
    print(f"   Windows: explorer \"{current_dir}\"")
    print(f"   Command: cd \"{current_dir}\"")

def main():
    """Hàm chính"""
    try:
        show_database_location()
        print(f"\n🎮 Để chạy game:")
        print(f"   python main.py")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    main()
