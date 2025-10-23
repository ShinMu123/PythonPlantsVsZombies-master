#!/usr/bin/env python3
"""
Demo sử dụng các tính năng mới của Plants vs Zombies
"""

import sys
import os

# Thêm đường dẫn source vào sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'source'))

from auth.user_manager import UserManager

def demo_user_registration():
    """Demo đăng ký người dùng"""
    print("=== Demo đăng ký người dùng ===")
    
    user_manager = UserManager()
    
    # Demo đăng ký một số người dùng
    users = [
        ("player1", "pass123", "player1@game.com"),
        ("player2", "pass456", "player2@game.com"),
        ("gamer", "pass789", "gamer@game.com")
    ]
    
    for username, password, email in users:
        success, message = user_manager.register(username, password, email)
        print(f"Đăng ký {username}: {message}")
    
    print("✅ Demo đăng ký hoàn thành!")

def demo_scoring_system():
    """Demo hệ thống điểm số"""
    print("\n=== Demo hệ thống điểm số ===")
    
    user_manager = UserManager()
    
    # Simulate một số game
    games = [
        ("player1", 5000, 3, True),   # player1 thắng level 3 với 5000 điểm
        ("player1", 3000, 2, False), # player1 thua level 2 với 3000 điểm
        ("player2", 8000, 5, True),  # player2 thắng level 5 với 8000 điểm
        ("gamer", 12000, 6, True),   # gamer thắng level 6 với 12000 điểm
        ("player1", 7000, 4, True),  # player1 thắng level 4 với 7000 điểm
    ]
    
    for username, score, level, won in games:
        user_manager.update_score(score, level, won)
        print(f"{username}: {score} điểm, Level {level}, {'Thắng' if won else 'Thua'}")
    
    print("✅ Demo điểm số hoàn thành!")

def demo_leaderboard():
    """Demo bảng xếp hạng"""
    print("\n=== Demo bảng xếp hạng ===")
    
    user_manager = UserManager()
    
    # Hiển thị bảng xếp hạng theo điểm
    print("🏆 Bảng xếp hạng theo điểm số:")
    leaderboard_score = user_manager.get_leaderboard(5)
    for i, (username, stats) in enumerate(leaderboard_score, 1):
        print(f"  {i}. {username}: {stats['high_score']} điểm")
    
    # Hiển thị bảng xếp hạng theo level
    print("\n🏆 Bảng xếp hạng theo level:")
    leaderboard_level = user_manager.get_leaderboard_by_level(5)
    for i, (username, stats) in enumerate(leaderboard_level, 1):
        print(f"  {i}. {username}: Level {stats['best_level']}")
    
    print("✅ Demo bảng xếp hạng hoàn thành!")

def demo_user_stats():
    """Demo thống kê người dùng"""
    print("\n=== Demo thống kê người dùng ===")
    
    user_manager = UserManager()
    
    # Hiển thị thống kê của từng người dùng
    users = ["player1", "player2", "gamer"]
    
    for username in users:
        stats = user_manager.get_user_stats(username)
        if stats:
            print(f"\n📊 Thống kê của {username}:")
            print(f"  - Điểm cao nhất: {stats['high_score']}")
            print(f"  - Level cao nhất: {stats['best_level']}")
            print(f"  - Tổng số game: {stats['total_games']}")
            print(f"  - Số lần thắng: {stats['wins']}")
            print(f"  - Số lần thua: {stats['losses']}")
            win_rate = (stats['wins'] / stats['total_games'] * 100) if stats['total_games'] > 0 else 0
            print(f"  - Tỷ lệ thắng: {win_rate:.1f}%")
    
    print("✅ Demo thống kê hoàn thành!")

def main():
    """Hàm chính"""
    print("🌱 Demo tính năng Plants vs Zombies 🌱")
    print("=" * 50)
    
    try:
        # Chạy các demo
        demo_user_registration()
        demo_scoring_system()
        demo_leaderboard()
        demo_user_stats()
        
        print("\n🎉 Demo hoàn thành!")
        print("\n📝 Các tính năng đã được thêm vào game:")
        print("1. ✅ Hệ thống đăng nhập/đăng ký")
        print("2. ✅ Bảng xếp hạng")
        print("3. ✅ Hệ thống điểm số")
        print("4. ✅ Thống kê người dùng")
        
        print("\n🚀 Để chạy game:")
        print("python main.py")
        
    except Exception as e:
        print(f"❌ Lỗi trong quá trình demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
