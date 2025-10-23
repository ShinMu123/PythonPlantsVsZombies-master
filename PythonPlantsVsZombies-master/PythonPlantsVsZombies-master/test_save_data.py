#!/usr/bin/env python3
"""
Test script để kiểm tra việc lưu dữ liệu đăng nhập/đăng ký
"""

import json
import os
from source.auth.user_manager import UserManager

def test_save_data():
    """Test việc lưu dữ liệu"""
    print("🧪 Test lưu dữ liệu đăng nhập/đăng ký")
    print("=" * 50)

    # Khởi tạo UserManager
    user_manager = UserManager()

    print("📁 Đường dẫn file:")
    print(f"   users.json: {user_manager.users_file}")
    print(f"   scores.json: {user_manager.scores_file}")
    print()

    # Hiển thị dữ liệu hiện tại
    print("📊 Dữ liệu hiện tại:")
    print(f"   Số người dùng: {len(user_manager.users)}")
    print(f"   Số bản ghi điểm: {len(user_manager.scores)}")
    print("   Người dùng:", list(user_manager.users.keys()))
    print()

    # Test đăng ký người dùng mới
    test_username = "test_user_" + str(hash(os.urandom(4)) % 10000)
    test_password = "testpass123"
    test_email = "test@example.com"

    print(f"🔐 Đăng ký người dùng mới: {test_username}")
    success, message = user_manager.register(test_username, test_password, test_email)
    print(f"   Kết quả: {message}")

    if success:
        print("✅ Đăng ký thành công!")

        # Kiểm tra file đã được lưu
        print("\n🔍 Kiểm tra file sau khi đăng ký:")
        if os.path.exists(user_manager.users_file):
            with open(user_manager.users_file, 'r', encoding='utf-8') as f:
                saved_users = json.load(f)
            if test_username in saved_users:
                print("✅ File users.json đã được cập nhật")
                print(f"   Thông tin: {saved_users[test_username]}")
            else:
                print("❌ File users.json chưa được cập nhật")
        else:
            print("❌ File users.json không tồn tại")

        if os.path.exists(user_manager.scores_file):
            with open(user_manager.scores_file, 'r', encoding='utf-8') as f:
                saved_scores = json.load(f)
            if test_username in saved_scores:
                print("✅ File scores.json đã được cập nhật")
                print(f"   Thông tin: {saved_scores[test_username]}")
            else:
                print("❌ File scores.json chưa được cập nhật")
        else:
            print("❌ File scores.json không tồn tại")

        # Test đăng nhập
        print(f"\n🔑 Test đăng nhập với {test_username}")
        login_success, login_message = user_manager.login(test_username, test_password)
        print(f"   Kết quả: {login_message}")

        if login_success:
            print("✅ Đăng nhập thành công!")

            # Test cập nhật điểm
            print(f"\n🏆 Test cập nhật điểm cho {test_username}")
            user_manager.update_score(2500, 3, True)
            print("   Đã cập nhật điểm: 2500, level 3, thắng")

            # Kiểm tra điểm đã được lưu
            if os.path.exists(user_manager.scores_file):
                with open(user_manager.scores_file, 'r', encoding='utf-8') as f:
                    updated_scores = json.load(f)
                if test_username in updated_scores:
                    print("✅ Điểm đã được lưu")
                    print(f"   Thông tin cập nhật: {updated_scores[test_username]}")
                else:
                    print("❌ Điểm chưa được lưu")
        else:
            print("❌ Đăng nhập thất bại!")
    else:
        print("❌ Đăng ký thất bại!")

    print("\n🎉 Test hoàn thành!")

if __name__ == "__main__":
    test_save_data()
