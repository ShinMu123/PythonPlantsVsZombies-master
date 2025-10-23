# Vị trí lưu trữ cơ sở dữ liệu - Plants vs Zombies

## 📁 Vị trí file dữ liệu:

### 🎯 **Thư mục chính:**
```
PythonPlantsVsZombies-master/PythonPlantsVsZombies-master/
├── users.json          ← Thông tin người dùng
├── scores.json         ← Điểm số và thống kê
└── source/
    └── auth/
        └── user_manager.py  ← Code quản lý dữ liệu
```

### 📍 **Đường dẫn đầy đủ:**
- **users.json**: `D:\Thư mục mới (4)\PythonPlantsVsZombies-master\PythonPlantsVsZombies-master\users.json`
- **scores.json**: `D:\Thư mục mới (4)\PythonPlantsVsZombies-master\PythonPlantsVsZombies-master\scores.json`

## 🔍 **Cách kiểm tra:**

### 1. Kiểm tra bằng file explorer:
- Mở thư mục: `D:\Thư mục mới (4)\PythonPlantsVsZombies-master\PythonPlantsVsZombies-master\`
- Tìm file `users.json` và `scores.json`

### 2. Kiểm tra bằng command line:
```bash
cd "D:\Thư mục mới (4)\PythonPlantsVsZombies-master\PythonPlantsVsZombies-master"
dir *.json
```

### 3. Kiểm tra bằng Python:
```bash
python check_database.py
```

## 📊 **Nội dung file:**

### users.json:
```json
{
  "admin": {
    "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    "email": "admin@game.com",
    "created_at": "2024-01-01T00:00:00",
    "last_login": null
  },
  "test": {
    "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
    "email": "test@game.com",
    "created_at": "2024-01-01T00:00:00",
    "last_login": null
  }
}
```

### scores.json:
```json
{
  "admin": {
    "high_score": 15000,
    "total_games": 25,
    "wins": 20,
    "losses": 5,
    "best_level": 8
  },
  "test": {
    "high_score": 8000,
    "total_games": 15,
    "wins": 12,
    "losses": 3,
    "best_level": 6
  }
}
```

## 🔧 **Cách thay đổi vị trí lưu trữ:**

Nếu muốn thay đổi vị trí lưu trữ, sửa trong file `source/auth/user_manager.py`:

```python
class UserManager:
    def __init__(self):
        # Thay đổi đường dẫn ở đây
        self.users_file = 'C:/MyData/users.json'  # Đường dẫn mới
        self.scores_file = 'C:/MyData/scores.json'  # Đường dẫn mới
```

## 💾 **Sao lưu dữ liệu:**

### 1. Sao lưu thủ công:
- Copy file `users.json` và `scores.json`
- Lưu vào thư mục khác

### 2. Sao lưu tự động:
```python
import shutil
import datetime

# Tạo bản sao lưu
backup_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
shutil.copy('users.json', f'backup_users_{backup_time}.json')
shutil.copy('scores.json', f'backup_scores_{backup_time}.json')
```

## 🚨 **Lưu ý quan trọng:**

1. **Không xóa file** `users.json` và `scores.json`
2. **Không di chuyển** file ra khỏi thư mục game
3. **Sao lưu thường xuyên** để tránh mất dữ liệu
4. **Không chỉnh sửa** file JSON trực tiếp (có thể gây lỗi)

## 📱 **Truy cập dữ liệu:**

### Từ game:
- Đăng nhập → Tự động tải dữ liệu
- Chơi game → Tự động lưu điểm
- Xem bảng xếp hạng → Tự động cập nhật

### Từ code:
```python
import json

# Đọc dữ liệu
with open('users.json', 'r', encoding='utf-8') as f:
    users = json.load(f)

# Ghi dữ liệu
with open('users.json', 'w', encoding='utf-8') as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
```

## 🎯 **Tóm tắt:**

- **Vị trí**: Thư mục game chính
- **File**: `users.json`, `scores.json`
- **Định dạng**: JSON
- **Mã hóa**: Mật khẩu SHA-256
- **Tự động**: Lưu/tải khi chơi game
