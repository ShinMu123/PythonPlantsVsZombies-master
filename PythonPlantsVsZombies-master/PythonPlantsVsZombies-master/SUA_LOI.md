# Hướng dẫn sửa lỗi màn hình đăng nhập

## 🔧 Các bước sửa lỗi

### 1. Tạo dữ liệu mẫu
```bash
python fix_auth_screen.py
```

### 2. Chạy game với script mới
```bash
python run_game.py
```

### 3. Hoặc chạy game bình thường
```bash
python main.py
```

## 📝 Tài khoản mẫu

Sau khi chạy `fix_auth_screen.py`, bạn sẽ có 2 tài khoản:

1. **admin / password**
2. **test / 123456**

## 🎮 Cách sử dụng

### Màn hình chính:
- **Đăng nhập**: Click để đăng nhập/đăng ký
- **Bảng xếp hạng**: Click để xem xếp hạng
- **Chơi khách**: Click để chơi mà không cần đăng ký

### Màn hình đăng nhập:
- **Click vào ô nhập liệu** để chọn
- **Click nút** để thực hiện hành động
- **ESC** để thoát

## 🐛 Khắc phục sự cố

### Lỗi "không cho bấm gì":
1. Đảm bảo đã chạy `fix_auth_screen.py`
2. Kiểm tra file `users.json` và `scores.json` có tồn tại
3. Thử chạy `python run_game.py`

### Lỗi import:
1. Đảm bảo đang ở thư mục đúng
2. Kiểm tra file `source/auth/global_auth.py` có tồn tại

### Lỗi pygame:
1. Cài đặt pygame: `pip install pygame`
2. Kiểm tra phiên bản Python (khuyến nghị 3.7+)

## 📁 Cấu trúc file

```
PythonPlantsVsZombies-master/
├── source/
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── user_manager.py
│   │   └── global_auth.py
│   ├── state/
│   │   ├── auth_screen_simple.py  # Phiên bản đơn giản
│   │   └── leaderboard_screen.py
│   └── main.py
├── users.json          # Dữ liệu người dùng
├── scores.json         # Dữ liệu điểm số
├── fix_auth_screen.py  # Script tạo dữ liệu
└── run_game.py         # Script chạy game
```

## ✅ Kiểm tra hoạt động

1. Chạy `python fix_auth_screen.py`
2. Chạy `python run_game.py`
3. Click "Đăng nhập"
4. Thử đăng nhập với `admin / password`
5. Click "Bảng xếp hạng" để xem xếp hạng

## 🎉 Thành công!

Nếu mọi thứ hoạt động, bạn sẽ thấy:
- Màn hình đăng nhập đẹp
- Có thể click vào các ô nhập liệu
- Có thể click các nút
- Có thể đăng nhập với tài khoản mẫu
- Có thể xem bảng xếp hạng
