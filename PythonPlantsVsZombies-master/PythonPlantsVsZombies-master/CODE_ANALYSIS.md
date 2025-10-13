# PHÂN TÍCH CODE PLANTS VS ZOMBIES

## 🎮 TỔNG QUAN GAME
Đây là một game Plants vs Zombies được viết bằng Python sử dụng thư viện Pygame. Game mô phỏng trò chơi gốc với cơ chế đặt cây để chống lại zombie.

## 🏗️ KIẾN TRÚC TỔNG THỂ

### 1. **Cấu trúc thư mục chính:**
```
source/
├── main.py          # Điểm khởi đầu của game
├── constants.py     # Các hằng số và cấu hình
├── tool.py         # Các công cụ và hàm tiện ích
├── component/      # Các thành phần game
│   ├── map.py      # Quản lý bản đồ
│   ├── plant.py    # Logic cây
│   ├── zombie.py   # Logic zombie
│   └── menubar.py  # Thanh menu
└── state/          # Các trạng thái game
    ├── mainmenu.py # Màn hình chính
    ├── level.py    # Màn chơi
    └── screen.py   # Màn hình kết thúc
```

## 🔧 CƠ CHẾ HOẠT ĐỘNG

### 1. **Hệ thống State Machine (Máy trạng thái)**
```python
# Các trạng thái chính:
MAIN_MENU = 'main menu'      # Màn hình chính
LEVEL = 'level'              # Màn chơi
GAME_VICTORY = 'game victory' # Thắng
GAME_LOSE = 'game los'       # Thua
```

**Cách hoạt động:**
- Game sử dụng pattern State Machine để quản lý các màn hình
- Mỗi state có các phương thức: `startup()`, `update()`, `cleanup()`
- Chuyển đổi state thông qua `flip_state()`

### 2. **Vòng lặp chính (Game Loop)**
```python
def main():
    # 1. Tạo Control object (quản lý game)
    game = tool.Control()
    
    # 2. Đăng ký các state
    state_dict = {
        c.MAIN_MENU: mainmenu.Menu(),
        c.GAME_VICTORY: screen.GameVictoryScreen(),
        c.GAME_LOSE: screen.GameLoseScreen(),
        c.LEVEL: level.Level()
    }
    
    # 3. Bắt đầu vòng lặp chính
    game.main()
```

**Vòng lặp chính hoạt động:**
1. **Event Loop**: Xử lý sự kiện (click chuột, bàn phím)
2. **Update**: Cập nhật logic game
3. **Render**: Vẽ lên màn hình
4. **Clock**: Đồng bộ FPS (60 FPS)

### 3. **Hệ thống Sprite Groups**
Game sử dụng pygame.sprite.Group để quản lý các đối tượng:

```python
# Mỗi hàng có các group riêng:
self.plant_groups = []      # Nhóm cây theo hàng
self.zombie_groups = []    # Nhóm zombie theo hàng  
self.bullet_groups = []    # Nhóm đạn theo hàng
self.hypno_zombie_groups = [] # Zombie bị thôi miên
```

## 🌱 HỆ THỐNG CÂY (PLANTS)

### 1. **Các loại cây chính:**
- **SunFlower**: Sản xuất ánh sáng mặt trời
- **PeaShooter**: Bắn đạn đậu
- **WallNut**: Cây hạt dẻ chắn đường
- **CherryBomb**: Bom anh đào nổ
- **Chomper**: Cây ăn thịt
- **SnowPea**: Đậu tuyết làm chậm zombie

### 2. **Cơ chế hoạt động:**
```python
class Plant(pg.sprite.Sprite):
    def __init__(self, x, y, name, health, cost):
        # Khởi tạo cây với vị trí, tên, máu, giá
        
    def update(self, game_info):
        # Cập nhật trạng thái cây mỗi frame
        
    def setAttack(self):
        # Chuyển sang trạng thái tấn công
        
    def setDamage(self, damage):
        # Nhận sát thương
```

### 3. **Hệ thống trạng thái cây:**
- `IDLE`: Nghỉ ngơi
- `ATTACK`: Tấn công
- `SLEEP`: Ngủ (một số cây nấm)
- `DIE`: Chết

## 🧟 HỆ THỐNG ZOMBIE

### 1. **Các loại zombie:**
- **NormalZombie**: Zombie thường
- **ConeHeadZombie**: Zombie đội nón
- **BucketHeadZombie**: Zombie đội xô
- **FlagZombie**: Zombie cầm cờ
- **NewspaperZombie**: Zombie cầm báo

### 2. **Cơ chế di chuyển và tấn công:**
```python
def walking(self):
    # Di chuyển từ phải sang trái
    if (self.current_time - self.walk_timer) > interval:
        self.rect.x -= self.speed
        
def attacking(self):
    # Tấn công cây khi va chạm
    if self.prey.health > 0:
        self.prey.setDamage(self.damage)
```

### 3. **Hệ thống máu và giáp:**
- Mỗi zombie có máu khác nhau
- Một số có giáp (nón, xô) giảm sát thương
- Khi mất đầu, zombie vẫn di chuyển nhưng chậm hơn

## 🎯 HỆ THỐNG ĐẠN VÀ VA CHẠM

### 1. **Các loại đạn:**
- **PeaNormal**: Đạn đậu thường
- **PeaIce**: Đạn đậu băng
- **BulletMushRoom**: Đạn nấm

### 2. **Cơ chế va chạm:**
```python
def checkBulletCollisions(self):
    # Kiểm tra va chạm đạn với zombie
    for bullet in self.bullet_groups[i]:
        zombie = pg.sprite.spritecollideany(bullet, self.zombie_groups[i])
        if zombie:
            zombie.setDamage(bullet.damage, bullet.ice)
            bullet.setExplode()
```

## 🗺️ HỆ THỐNG BẢN ĐỒ

### 1. **Lưới 9x5:**
```python
GRID_X_LEN = 9  # 9 cột
GRID_Y_LEN = 5  # 5 hàng
```

### 2. **Quản lý vị trí:**
```python
def getMapGridPos(self, map_x, map_y):
    # Chuyển đổi tọa độ lưới thành pixel
    
def getMapIndex(self, x, y):
    # Chuyển đổi pixel thành tọa độ lưới
```

## 🎮 HỆ THỐNG ĐIỀU KHIỂN

### 1. **Chuột:**
- **Click trái**: Chọn cây, đặt cây, thu thập ánh sáng
- **Click phải**: Hủy chọn cây
- **Di chuyển**: Hiển thị preview cây

### 2. **Kéo thả cây:**
```python
def setupMouseImage(self, plant_name, select_plant):
    # Hiển thị hình ảnh cây theo chuột
    pg.mouse.set_visible(False)
    self.drag_plant = True
```

## 💰 HỆ THỐNG TÀI NGUYÊN

### 1. **Ánh sáng mặt trời:**
- Sản xuất tự động mỗi 7 giây
- Thu thập bằng cách click
- Mỗi ánh sáng = 25 điểm

### 2. **Chi phí cây:**
- Mỗi cây có giá khác nhau
- Kiểm tra đủ tiền trước khi mua

## 🎨 HỆ THỐNG ĐỒ HỌA

### 1. **Tải hình ảnh:**
```python
def load_all_gfx(directory):
    # Tải tất cả hình ảnh từ thư mục resources/graphics
    # Tự động phát hiện thư mục graphics
```

### 2. **Animation:**
```python
def animation(self):
    # Chuyển đổi frame theo thời gian
    if (self.current_time - self.animate_timer) > self.animate_interval:
        self.frame_index = (self.frame_index + 1) % self.frame_num
        self.image = self.frames[self.frame_index]
```

## 🎯 HỆ THỐNG LEVEL

### 1. **File cấu hình level:**
```json
{
    "background_type": 0,
    "init_sun_value": 50,
    "zombie_list": [
        {"time": 1000, "name": "Zombie", "map_y": 0},
        {"time": 5000, "name": "ConeheadZombie", "map_y": 1}
    ]
}
```

### 2. **Spawn zombie:**
```python
def createZombie(self, name, map_y):
    # Tạo zombie theo thời gian định sẵn
    if name == c.NORMAL_ZOMBIE:
        self.zombie_groups[map_y].add(zombie.NormalZombie(...))
```

## 🏆 ĐIỀU KIỆN THẮNG THUA

### 1. **Thắng:**
- Không còn zombie nào trong danh sách
- Không còn zombie nào trên màn hình

### 2. **Thua:**
- Zombie đi qua màn hình (rect.right < 0)

## 🔧 CÁC TÍNH NĂNG ĐẶC BIỆT

### 1. **Cây đặc biệt:**
- **CherryBomb**: Nổ phạm vi lớn
- **IceShroom**: Đóng băng tất cả zombie
- **HypnoShroom**: Thôi miên zombie
- **Chomper**: Ăn zombie

### 2. **Hiệu ứng:**
- Đóng băng làm chậm zombie
- Nổ phạm vi
- Thôi miên zombie tấn công lẫn nhau

## 🚀 CÁCH CHẠY GAME

1. **Cài đặt pygame:**
```bash
pip install pygame
```

2. **Chạy game:**
```bash
python main.py
```

3. **Hoặc sử dụng file batch:**
```bash
run_ppvz_local.bat
```

## 📝 GHI CHÚ QUAN TRỌNG

1. **FPS**: Game chạy ở 60 FPS
2. **Tọa độ**: Hệ tọa độ pixel với gốc (0,0) ở góc trên trái
3. **Collision**: Sử dụng pygame.sprite.collide_circle_ratio()
4. **Memory**: Tự động quản lý bộ nhớ với sprite groups
5. **Extensibility**: Dễ dàng thêm cây/zombie mới bằng cách tạo class mới

## 🎮 LUỒNG GAME CHÍNH

1. **Khởi động** → Main Menu
2. **Click Adventure** → Chọn cây
3. **Click Start** → Bắt đầu chơi
4. **Đặt cây** → Chống zombie
5. **Thu thập ánh sáng** → Mua cây mới
6. **Kết thúc** → Victory/Lose Screen

Game sử dụng kiến trúc modular, dễ mở rộng và bảo trì!
