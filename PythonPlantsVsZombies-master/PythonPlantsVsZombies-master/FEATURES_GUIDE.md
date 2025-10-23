# Hướng dẫn sử dụng tính năng mới - Plants vs Zombies

## Các tính năng đã được thêm vào

### 1. Hệ thống đăng nhập/đăng ký
- **Đăng ký tài khoản mới**: Người chơi có thể tạo tài khoản với tên đăng nhập, mật khẩu và email
- **Đăng nhập**: Người chơi có thể đăng nhập bằng tài khoản đã tạo
- **Chơi với tư cách khách**: Người chơi có thể chơi mà không cần đăng ký

### 2. Bảng xếp hạng
- **Xếp hạng theo điểm số**: Hiển thị top 10 người chơi có điểm cao nhất
- **Xếp hạng theo level**: Hiển thị top 10 người chơi đạt level cao nhất
- **Thống kê chi tiết**: Hiển thị số lần thắng, thua, tổng số game

### 3. Hệ thống điểm số
- **Tính điểm tự động**: Điểm được tính dựa trên level và kết quả game
- **Lưu trữ điểm cao nhất**: Tự động lưu điểm cao nhất của mỗi người chơi
- **Theo dõi tiến độ**: Lưu level cao nhất đạt được

## Cách sử dụng

### Khởi động game
1. Chạy file `main.py` hoặc `run_ppvz_local.bat`
2. Tại màn hình chính, bạn sẽ thấy 3 nút mới:
   - **Đăng nhập**: Để đăng nhập với tài khoản có sẵn
   - **Bảng xếp hạng**: Xem bảng xếp hạng
   - **Chơi khách**: Chơi mà không cần đăng ký

### Đăng ký tài khoản mới
1. Click nút "Đăng nhập"
2. Click "Chuyển sang đăng ký"
3. Nhập thông tin:
   - Tên đăng nhập (ít nhất 3 ký tự)
   - Mật khẩu (ít nhất 6 ký tự)
   - Email (tùy chọn)
4. Click "Đăng ký"

### Đăng nhập
1. Click nút "Đăng nhập"
2. Nhập tên đăng nhập và mật khẩu
3. Click "Đăng nhập"

### Xem bảng xếp hạng
1. Click nút "Bảng xếp hạng"
2. Chọn cách sắp xếp:
   - "Theo điểm số": Xếp hạng theo điểm cao nhất
   - "Theo level": Xếp hạng theo level cao nhất
3. Click "Quay lại" để trở về menu chính

## Cấu trúc dữ liệu

### File dữ liệu
- `users.json`: Lưu thông tin người dùng (mật khẩu được mã hóa)
- `scores.json`: Lưu điểm số và thống kê

### Thông tin người dùng
```json
{
  "username": {
    "password": "hashed_password",
    "email": "user@example.com",
    "created_at": "2024-01-01T00:00:00",
    "last_login": "2024-01-01T00:00:00"
  }
}
```

### Thông tin điểm số
```json
{
  "username": {
    "high_score": 5000,
    "total_games": 10,
    "wins": 7,
    "losses": 3,
    "best_level": 5
  }
}
```

## Tính năng bảo mật

- **Mã hóa mật khẩu**: Mật khẩu được mã hóa bằng SHA-256
- **Xác thực đầu vào**: Kiểm tra độ dài tên đăng nhập và mật khẩu
- **Lưu trữ an toàn**: Dữ liệu được lưu trong file JSON local

## Lưu ý

- Dữ liệu được lưu trong thư mục game, không cần kết nối internet
- Có thể chơi với tư cách khách mà không cần đăng ký
- Điểm số được tính tự động khi kết thúc game
- Bảng xếp hạng cập nhật real-time

## Khắc phục sự cố

### Lỗi không thể đăng nhập
- Kiểm tra tên đăng nhập và mật khẩu
- Đảm bảo tài khoản đã được đăng ký

### Lỗi không hiển thị bảng xếp hạng
- Kiểm tra file `scores.json` có tồn tại
- Đảm bảo đã có dữ liệu điểm số

### Lỗi lưu điểm
- Kiểm tra quyền ghi file trong thư mục game
- Đảm bảo đã đăng nhập hoặc chơi với tư cách khách
