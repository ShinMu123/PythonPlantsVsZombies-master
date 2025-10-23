__author__ = 'marble_xu'

import json
import os
import hashlib
from datetime import datetime

class UserManager:
    def __init__(self):
        # Đặt đường dẫn file tương đối với thư mục gốc của project
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.users_file = os.path.join(base_dir, 'users.json')
        self.scores_file = os.path.join(base_dir, 'scores.json')
        self.current_user = None
        self.load_users()
        self.load_scores()

    def load_users(self):
        """Tải danh sách người dùng từ file"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    self.users = json.load(f)
            except:
                self.users = {}
        else:
            self.users = {}

    def save_users(self):
        """Lưu danh sách người dùng vào file"""
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)

    def load_scores(self):
        """Tải điểm số từ file"""
        if os.path.exists(self.scores_file):
            try:
                with open(self.scores_file, 'r', encoding='utf-8') as f:
                    self.scores = json.load(f)
            except:
                self.scores = {}
        else:
            self.scores = {}

    def save_scores(self):
        """Lưu điểm số vào file"""
        with open(self.scores_file, 'w', encoding='utf-8') as f:
            json.dump(self.scores, f, ensure_ascii=False, indent=2)

    def hash_password(self, password):
        """Mã hóa mật khẩu"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password, email=""):
        """Đăng ký người dùng mới"""
        if username in self.users:
            return False, "Tên đăng nhập đã tồn tại!"

        if len(password) < 6:
            return False, "Mật khẩu phải có ít nhất 6 ký tự!"

        if len(username) < 3:
            return False, "Tên đăng nhập phải có ít nhất 3 ký tự!"

        hashed_password = self.hash_password(password)
        self.users[username] = {
            'password': hashed_password,
            'email': email,
            'created_at': datetime.now().isoformat(),
            'last_login': None
        }

        # Khởi tạo điểm số cho người dùng mới
        self.scores[username] = {
            'high_score': 0,
            'total_games': 0,
            'wins': 0,
            'losses': 0,
            'best_level': 1
        }

        self.save_users()
        self.save_scores()
        return True, "Đăng ký thành công!"

    def login(self, username, password):
        """Đăng nhập"""
        if username not in self.users:
            return False, "Tên đăng nhập không tồn tại!"

        hashed_password = self.hash_password(password)
        if self.users[username]['password'] != hashed_password:
            return False, "Mật khẩu không đúng!"

        # Cập nhật thời gian đăng nhập cuối
        self.users[username]['last_login'] = datetime.now().isoformat()
        self.current_user = username
        self.save_users()
        return True, "Đăng nhập thành công!"

    def logout(self):
        """Đăng xuất"""
        self.current_user = None

    def is_logged_in(self):
        """Kiểm tra trạng thái đăng nhập"""
        return self.current_user is not None

    def get_current_user(self):
        """Lấy thông tin người dùng hiện tại"""
        return self.current_user

    def update_score(self, score, level_reached, won=False):
        """Cập nhật điểm số"""
        if not self.is_logged_in():
            return

        username = self.current_user
        if username not in self.scores:
            self.scores[username] = {
                'high_score': 0,
                'total_games': 0,
                'wins': 0,
                'losses': 0,
                'best_level': 1
            }

        # Cập nhật điểm cao nhất
        if score > self.scores[username]['high_score']:
            self.scores[username]['high_score'] = score

        # Cập nhật level cao nhất
        if level_reached > self.scores[username]['best_level']:
            self.scores[username]['best_level'] = level_reached

        # Cập nhật thống kê
        self.scores[username]['total_games'] += 1
        if won:
            self.scores[username]['wins'] += 1
        else:
            self.scores[username]['losses'] += 1

        self.save_scores()

    def get_user_stats(self, username=None):
        """Lấy thống kê người dùng"""
        if username is None:
            username = self.current_user

        if username not in self.scores:
            return None

        return self.scores[username]

    def get_leaderboard(self, limit=10):
        """Lấy bảng xếp hạng"""
        sorted_scores = sorted(
            self.scores.items(),
            key=lambda x: x[1]['high_score'],
            reverse=True
        )
        return sorted_scores[:limit]

    def get_leaderboard_by_level(self, limit=10):
        """Lấy bảng xếp hạng theo level"""
        sorted_scores = sorted(
            self.scores.items(),
            key=lambda x: x[1]['best_level'],
            reverse=True
        )
        return sorted_scores[:limit]
