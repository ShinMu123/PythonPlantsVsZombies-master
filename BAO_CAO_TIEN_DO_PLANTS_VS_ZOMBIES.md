# BÁO CÁO TIẾN ĐỘ DỰ ÁN: PLANTS VS ZOMBIES GAME

**Sinh viên:** [Tên của bạn]  
**Lớp:** [Tên lớp]  
**Giảng viên hướng dẫn:** [Tên giáo viên]  
**Ngày báo cáo:** [Ngày tháng năm]  

## 📋 TỔNG QUAN DỰ ÁN

### Mục tiêu dự án
- Phát triển một game Plants vs Zombies đơn giản bằng ngôn ngữ Python
- Sử dụng thư viện Pygame để xử lý đồ họa và tương tác
- Mô phỏng cơ chế gameplay cơ bản của trò chơi gốc
- Áp dụng kiến thức lập trình hướng đối tượng và thiết kế game

### Phạm vi dự án
- **Ngôn ngữ:** Python 3.7+
- **Thư viện chính:** Pygame 1.9
- **Thời gian phát triển:** [Thời gian bạn đã làm]
- **Mục đích:** Học thuật, không thương mại

## 🎯 TÍNH NĂNG ĐÃ TRIỂN KHAI

### ✅ Các loại cây (Plants)
- **SunFlower:** Sản xuất ánh sáng mặt trời
- **PeaShooter:** Bắn đạn đậu thường
- **SnowPeaShooter:** Bắn đạn băng làm chậm zombie
- **WallNut:** Cây chắn đường với giáp cao
- **CherryBomb:** Bom nổ phạm vi lớn
- **ThreePeaShooter:** Bắn 3 hướng
- **Chomper:** Cây ăn thịt zombie
- **PuffShroom:** Nấm bắn đạn (đêm)
- **PotatoMine:** Mìn khoai tây
- **Spikeweed:** Gai đâm zombie
- **Jalapeno:** Nổ theo hàng
- **IceShroom:** Đóng băng tất cả zombie
- **HypnoShroom:** Thôi miên zombie

### ✅ Các loại zombie
- **Normal Zombie:** Zombie thường
- **ConeHead Zombie:** Zombie đội nón (giáp)
- **BucketHead Zombie:** Zombie đội xô (giáp mạnh)
- **Flag Zombie:** Zombie cầm cờ
- **Newspaper Zombie:** Zombie cầm báo

### ✅ Cơ chế gameplay
- **Hệ thống bản đồ:** Lưới 9x5 với 5 hàng
- **Thu thập ánh sáng:** Click để thu thập, tự động sản xuất
- **Đặt cây:** Kéo thả cây từ card vào vị trí
- **Tấn công:** Cây tự động tấn công zombie trong hàng
- **Va chạm:** Hệ thống collision detection
- **Hiệu ứng đặc biệt:** Băng, nổ, thôi miên

### ✅ Các màn chơi
- **Level 1-2:** Ngày (day level)
- **Level 3:** Đêm (night level)
- **Level 4:** Chọn card di chuyển (moving card select)
- **Level 5:** Bowling với WallNut

## 🏗️ KIẾN TRÚC CODE

### Cấu trúc thư mục
```
PythonPlantsVsZombies/
├── main.py                 # Điểm khởi đầu
├── README.md              # Tài liệu tổng quan
├── CODE_ANALYSIS.md       # Phân tích code
├── DETAILED_MECHANICS.md  # Cơ chế chi tiết
├── source/
│   ├── main.py           # Hàm main chính
│   ├── constants.py      # Hằng số và cấu hình
│   ├── tool.py           # Công cụ tiện ích
│   ├── component/        # Các thành phần game
│   │   ├── map.py        # Quản lý bản đồ
│   │   ├── plant.py      # Logic cây
│   │   ├── zombie.py     # Logic zombie
│   │   └── menubar.py    # Thanh menu
│   ├── state/            # Các trạng thái game
│   │   ├── mainmenu.py   # Màn hình chính
│   │   ├── level.py      # Màn chơi
│   │   └── screen.py     # Màn thắng/thua
│   └── data/             # Dữ liệu cấu hình
│       ├── entity/       # Thông tin thực thể
│       └── map/          # Cấu hình level
├── resources/            # Hình ảnh, âm thanh
└── demo/                 # Ảnh demo
```

### Pattern thiết kế
- **State Machine:** Quản lý các màn hình game
- **Sprite Groups:** Tối ưu hóa render và collision
- **Component-based:** Tách biệt logic từng thành phần
- **Data-driven:** Cấu hình level qua JSON

## 🔧 CÔNG NGHỆ SỬ DỤNG

### Thư viện chính
- **Pygame:** Xử lý đồ họa, âm thanh, input
- **JSON:** Lưu trữ cấu hình level và thực thể
- **Python built-in:** OS, sys, random, time

### Tính năng kỹ thuật
- **Game Loop:** 60 FPS với đồng bộ thời gian
- **Event Handling:** Xử lý chuột và bàn phím
- **Animation:** Hệ thống frame-based animation
- **Memory Management:** Tự động dọn dẹp sprite
- **Collision Detection:** Sprite collision với tỷ lệ tùy chỉnh

## 📊 TIẾN ĐỘ HOÀN THÀNH

### ✅ Đã hoàn thành (100%)
- [x] Cài đặt Pygame và môi trường phát triển
- [x] Thiết kế kiến trúc tổng thể
- [x] Implement hệ thống State Machine
- [x] Tạo các class cơ bản (Plant, Zombie, Bullet)
- [x] Hệ thống bản đồ và lưới
- [x] Logic tấn công và va chạm
- [x] Hệ thống tài nguyên (ánh sáng mặt trời)
- [x] Menu chính và chọn level
- [x] Tất cả 5 level với cấu hình khác nhau
- [x] Hiệu ứng đặc biệt (băng, nổ, thôi miên)
- [x] Điều kiện thắng/thua
- [x] Tối ưu hóa hiệu suất
- [x] Tài liệu chi tiết (README, CODE_ANALYSIS, DETAILED_MECHANICS)

### 🔄 Đang phát triển
- [ ] Thêm âm thanh nền và hiệu ứng âm thanh
- [ ] Cải thiện giao diện người dùng
- [ ] Thêm nhiều level mới
- [ ] Hệ thống lưu điểm cao


## 🎮 HƯỚNG DẪN CHẠY GAME

### Yêu cầu hệ thống
- Python 3.7+
- Pygame 1.9+
- Windows/Linux/MacOS

### Cách chạy
```bash
# Cài đặt thư viện
pip install pygame

# Chạy game
python main.py

# Hoặc dùng file batch (Windows)
run_ppvz_local.bat
```

### Cách chơi
1. **Menu chính:** Click "Adventure" để bắt đầu
2. **Chọn cây:** Chọn các card cây ở thanh bên phải
3. **Đặt cây:** Kéo thả cây vào vị trí trên bản đồ
4. **Thu thập ánh sáng:** Click vào các icon mặt trời
5. **Chống zombie:** Cây sẽ tự động tấn công zombie
6. **Thắng level:** Tiêu diệt tất cả zombie trước khi chúng vào nhà

## 📈 THỰC HIỆN DEMO

Game đã chạy thành công trên máy tính của sinh viên. Các tính năng chính hoạt động ổn định:
- Menu chính và chuyển đổi level
- Đặt cây và thu thập ánh sáng
- Tấn công và va chạm
- Hiệu ứng đặc biệt
- Điều kiện thắng/thua

## 🎯 KHÓ KHĂN GẶP PHẢI

### Kỹ thuật
1. **Collision Detection:** Khó khăn trong việc tối ưu hóa va chạm giữa nhiều sprite
2. **State Management:** Quản lý chuyển đổi giữa các trạng thái game
3. **Animation Timing:** Đồng bộ animation với game loop
4. **Memory Optimization:** Tránh rò rỉ bộ nhớ với sprite groups

### Giải pháp
1. Sử dụng `pygame.sprite.collide_circle_ratio()` với tỷ lệ tùy chỉnh
2. Implement State Machine pattern với `startup()`, `update()`, `cleanup()`
3. Sử dụng timer-based updates thay vì frame-based
4. Tự động `kill()` sprite khi không cần thiết

## 📚 KẾT LUẬN

### Đánh giá chung
Dự án đã hoàn thành đầy đủ các yêu cầu đề ra với:
- **Chức năng:** 100% các tính năng cơ bản đã hoạt động
- **Code quality:** Kiến trúc rõ ràng, dễ bảo trì và mở rộng
- **Tài liệu:** Chi tiết và đầy đủ
- **Demo:** Chạy ổn định trên nhiều môi trường

### Học được
- **Lập trình hướng đối tượng:** Áp dụng OOP trong thiết kế game
- **Game development:** Hiểu về game loop, state management, collision detection
- **Python advanced:** Sử dụng thư viện bên thứ 3, JSON, file I/O
- **Optimization:** Tối ưu hóa hiệu suất cho game real-time

### Hướng phát triển tương lai
- Thêm chế độ multiplayer
- Cải thiện đồ họa và âm thanh
- Port sang mobile platforms
- Thêm nhiều level và chế độ chơi mới

---

**Tài liệu tham khảo:**
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Plants vs Zombies Wiki](https://plantsvszombies.fandom.com/)
- [Game Development Patterns](https://gameprogrammingpatterns.com/)

**Liên hệ:** [Email của bạn] | [GitHub repository nếu có]
