## Plants vs Zombies (Python/Pygame) – Hướng dẫn chạy & Phân tích mã

### 1) Giới thiệu
Trò chơi Plants vs Zombies viết bằng Python sử dụng Pygame, có màn đăng nhập/đăng ký, bảng xếp hạng và nhiều màn chơi. Repo đã kèm sẵn tài nguyên hình ảnh.

### 2) Yêu cầu hệ thống
- Python 3.9+ (đã chạy tốt với 3.13.0)
- Pygame 2.6+
- Windows (đã test) hoặc hệ điều hành khác có hỗ trợ SDL/Pygame

### 3) Cài đặt nhanh
1. Mở terminal tại thư mục dự án (chứa file `main.py`, `run_game.py`):
   - Ví dụ: `D:\Thư mục mới (4)\PythonPlantsVsZombies-master\PythonPlantsVsZombies-master`
2. (Khuyến nghị) Tạo môi trường ảo và kích hoạt:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
3. Cài thư viện:
   ```bash
   pip install pygame
   ```

### 4) Cách chạy
- Cách 1 (khuyến nghị, có tạo dữ liệu mẫu):
  ```bash
  python run_game.py
  ```
  Script sẽ tạo `users.json`, `scores.json` mẫu và khởi chạy game.

- Cách 2 (chạy trực tiếp game):
  ```bash
  python main.py
  ```

- Cách 3 (file .bat tiện lợi trên Windows):
  - Double‑click `run_ppvz_local.bat` hoặc chạy trong terminal:
    ```bash
    .\run_ppvz_local.bat
    ```

- VS Code (Debug): tạo `launch.json` với cấu hình:
  ```json
  {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Run PvZ main.py",
        "type": "python",
        "request": "launch",
        "program": "${workspaceFolder}/main.py",
        "console": "integratedTerminal",
        "cwd": "${workspaceFolder}"
      }
    ]
  }
  ```

### 5) Cấu trúc thư mục chính
- `main.py`: Điểm vào chính; khởi tạo game, đăng ký state, chạy vòng lặp.
- `run_game.py`: Script chạy tiện lợi, tạo dữ liệu mẫu rồi gọi `main.py`.
- `source/`
  - `main.py`: Điểm vào dạng module (`python -m source.main`), không khuyến nghị chạy trực tiếp.
  - `tool.py`: Engine lõi (vòng lặp game, quản lý state, input, nạp ảnh `GFX`).
  - `constants.py`: Hằng số cho gameplay, màu sắc, tên state, đường dẫn tài nguyên.
  - `state/`: Các màn hình (menu, level, thắng/thua, auth, leaderboard).
  - `component/`: Thành phần gameplay (map, menubar, plant, zombie…).
  - `data/`: JSON cấu hình level, entity.
- `resources/graphics/`: Tài nguyên hình ảnh (Screen, Cards, Items, Plants, Zombies…).
- `users.json`, `scores.json`: Dữ liệu người dùng và điểm số (tạo bởi `run_game.py`).

### 6) Phân tích code (tổng quan)
- Vòng lặp game – `source/tool.py`:
  - Lớp `Control` nắm `screen`, `clock`, `state_dict`, `state_name`, `state` hiện tại.
  - `setup_states(state_dict, start_state)`: gán state và gọi `startup` state đầu tiên.
  - `main()`: vòng lặp: lấy sự kiện → `event_loop()` → `update()` state → vẽ FPS → `display.flip()`.
  - Chuyển state qua `flip_state()`: gọi `cleanup()` state cũ (trả `game_info`) → `startup()` state mới.

- Quản lý state – `source/state/*`:
  - `mainmenu.Menu`: màn hình chính, hiển thị nút đăng nhập, bảng xếp hạng, chơi khách.
  - `level.Level`: nạp map JSON (`source/data/map/level_*.json`), thiết lập background, menubar, nhóm sprite; xử lý chơi, thắng/thua.
  - `screen.py`: màn thắng (`GameVictoryScreen`) và thua (`GameLoseScreen`).
  - `auth_screen_fixed.py`: màn đăng nhập/đăng ký; dùng `source/auth/*` quản lý user.
  - `leaderboard_screen.py`: hiển thị điểm cao.

- Tài nguyên – `source/tool.py` / `source/constants.py`:
  - `constants.GRAPHICS_PATH` trỏ tới `resources/graphics`.
  - `tool.GFX`: dictionary chứa Surface đã nạp. Có loader nạp folder `Screen`, `Cards` và danh sách background từ `Items/Background`.
  - Một số state lấy ảnh bằng key (ví dụ `ChooserBackground`, `MoveBackground`, `PanelBackground`, `StartButton`, `MainMenu`, `Adventure_0/1`).

- UI chọn cây & gameplay – `source/component/menubar.py`:
  - `Panel` (chế độ chọn thẻ) + `MenuBar`/`MoveBar` (hiển thị thẻ khi chơi).
  - `Card` xử lý logic cooldown, chi phí mặt trời; vẽ đè hiệu ứng cooldown/disabled.

- Dữ liệu – `source/data/`:
  - `map/level_*.json`: mô tả background, danh sách zombie, cấu hình menubar.
  - `entity/plant.json`, `entity/zombie.json`: khai báo thông tin hình ảnh/khung cắt.

### 7) Cách mở rộng/sửa lỗi nhanh
- Nếu thiếu ảnh (KeyError tên ảnh): kiểm tra tồn tại file đúng tên trong `resources/graphics/...` và loader đã nạp thư mục đó.
- Nếu chạy không hiện cửa sổ: thử `Alt+Tab`, hoặc chạy `python -X dev main.py` để xem log chi tiết.
- Nếu import lỗi khi chạy `source/main.py`: chạy ở root `python main.py` hoặc `python -m source.main` (từ root). 

### 8) Tài khoản mẫu (khi dùng `run_game.py`)
- `admin` / `password`
- `test` / `123456`

### 9) Giấy phép
Chỉ dùng cho mục đích học tập/tham khảo. Tài nguyên đồ họa thuộc về chủ sở hữu gốc.

### PHÂN TÍCH CODE (chi tiết)

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

# CƠ CHẾ CHI TIẾT CỦA CODE PLANTS VS ZOMBIES

## 🎮 **LUỒNG HOẠT ĐỘNG CHÍNH**

### **1. Khởi động Game (main.py)**
```python
def main():
    # Tạo đối tượng Control - bộ não của game
    game = tool.Control()
    
    # Đăng ký các trạng thái game
    state_dict = {
        c.MAIN_MENU: mainmenu.Menu(),      # Màn hình chính
        c.GAME_VICTORY: screen.GameVictoryScreen(),  # Màn thắng
        c.GAME_LOSE: screen.GameLoseScreen(),        # Màn thua
        c.LEVEL: level.Level()             # Màn chơi
    }
    
    # Thiết lập state ban đầu và bắt đầu game
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()  # Vòng lặp chính
```

### **2. Vòng lặp chính (Control.main)**
```python
def main(self):
    while not self.done:  # Chạy đến khi game kết thúc
        self.event_loop()    # 1. Xử lý sự kiện (click, keyboard)
        self.update()        # 2. Cập nhật logic game
        pg.display.update()  # 3. Vẽ lên màn hình
        self.clock.tick(self.fps)  # 4. Đồng bộ 60 FPS
```

## 🏗️ **KIẾN TRÚC HỆ THỐNG**

### **1. State Machine (Máy trạng thái)**
```python
class State():
    def startup(self, current_time, persist):  # Khởi tạo state
    def update(self, surface, current_time, mouse_pos, mouse_click):  # Cập nhật
    def cleanup(self):  # Dọn dẹp khi chuyển state
```

**Cách hoạt động:**
- Mỗi state quản lý một màn hình riêng
- Chuyển đổi state thông qua `self.done = True` và `self.next = 'state_name'`
- Dữ liệu được truyền qua `persist` dictionary

### **2. Sprite Groups (Nhóm đối tượng)**
```python
# Mỗi hàng có các group riêng để tối ưu hiệu suất
self.plant_groups = []      # [Group(), Group(), Group(), Group(), Group()]
self.zombie_groups = []    # [Group(), Group(), Group(), Group(), Group()]
self.bullet_groups = []    # [Group(), Group(), Group(), Group(), Group()]
self.hypno_zombie_groups = [] # Zombie bị thôi miên
```

## 🎯 **HỆ THỐNG ĐIỀU KHIỂN CHUỘT**

### **1. Xử lý sự kiện chuột**
```python
def event_loop(self):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            self.mouse_pos = pg.mouse.get_pos()  # Lưu vị trí chuột
            self.mouse_click[0], _, self.mouse_click[1] = pg.mouse.get_pressed()
            # [0] = click trái, [1] = click phải
```

### **2. Cơ chế kéo thả cây**
```python
def setupMouseImage(self, plant_name, select_plant):
    # Ẩn con trỏ chuột
    pg.mouse.set_visible(False)
    
    # Tạo hình ảnh cây theo chuột
    self.mouse_image = tool.get_image(frame_list[0], x, y, width, height)
    self.drag_plant = True  # Bật chế độ kéo thả
```

### **3. Hiển thị preview cây**
```python
def setupHintImage(self):
    # Tạo hình ảnh mờ để hiển thị vị trí đặt cây
    image = pg.Surface([width, height])
    image.blit(self.mouse_image, (0, 0))
    image.set_alpha(128)  # Độ trong suốt 50%
```

## 🌱 **HỆ THỐNG CÂY CHI TIẾT**

### **1. Cấu trúc cây cơ bản**
```python
class Plant(pg.sprite.Sprite):
    def __init__(self, x, y, name, health, cost):
        self.name = name           # Tên cây
        self.health = health       # Máu
        self.cost = cost          # Giá mua
        self.state = c.IDLE       # Trạng thái hiện tại
        self.attack_timer = 0      # Timer tấn công
        self.animate_timer = 0    # Timer animation
```

### **2. Hệ thống trạng thái cây**
```python
def handleState(self):
    if self.state == c.IDLE:
        self.idling()      # Nghỉ ngơi
    elif self.state == c.ATTACK:
        self.attacking()   # Tấn công
    elif self.state == c.SLEEP:
        self.sleeping()    # Ngủ (nấm)
    elif self.state == c.DIE:
        self.dying()       # Chết
```

### **3. Cơ chế tấn công**
```python
def setAttack(self):
    self.state = c.ATTACK
    self.attack_timer = self.current_time
    
def attacking(self):
    # Kiểm tra cooldown tấn công
    if (self.current_time - self.attack_timer) > self.attack_interval:
        self.shootBullet()  # Bắn đạn
        self.attack_timer = self.current_time
```

### **4. Các loại cây đặc biệt**

**SunFlower (Hoa hướng dương):**
```python
def setAttack(self):
    # Sản xuất ánh sáng mặt trời
    if (self.current_time - self.attack_timer) > self.attack_interval:
        self.sun_group.add(Sun(x, y, x, y))
```

**CherryBomb (Bom anh đào):**
```python
def setAttack(self):
    # Nổ phạm vi lớn
    self.state = c.EXPLODE
    # Gây sát thương cho tất cả zombie trong phạm vi
```

**Chomper (Cây ăn thịt):**
```python
def setAttack(self, zombie, zombie_group):
    # Nuốt zombie
    zombie.setDie()
    self.state = c.DIGEST  # Chuyển sang trạng thái tiêu hóa
```

## 🧟 **HỆ THỐNG ZOMBIE CHI TIẾT**

### **1. Cấu trúc zombie**
```python
class Zombie(pg.sprite.Sprite):
    def __init__(self, x, y, name, health, head_group=None):
        self.health = health       # Máu
        self.damage = 1           # Sát thương
        self.speed = 1            # Tốc độ di chuyển
        self.state = c.WALK       # Trạng thái
        self.is_hypno = False     # Bị thôi miên
```

### **2. Hệ thống di chuyển**
```python
def walking(self):
    # Di chuyển từ phải sang trái
    if (self.current_time - self.walk_timer) > interval:
        if self.is_hypno:
            self.rect.x += self.speed  # Thôi miên: đi ngược lại
        else:
            self.rect.x -= self.speed  # Bình thường: đi về phía trái
```

### **3. Hệ thống máu và giáp**
```python
def setDamage(self, damage, ice=False):
    self.health -= damage
    
    # Kiểm tra mất đầu
    if self.health <= c.LOSTHEAD_HEALTH and not self.losHead:
        self.changeFrames(self.losthead_walk_frames)
        self.setLostHead()
    
    # Hiệu ứng băng
    if ice:
        self.setIceSlow()
```

### **4. Các loại zombie đặc biệt**

**ConeHeadZombie (Zombie đội nón):**
```python
def __init__(self):
    self.health = c.CONEHEAD_HEALTH  # 20 máu
    self.helmet = True               # Có giáp
```

**BucketHeadZombie (Zombie đội xô):**
```python
def __init__(self):
    self.health = c.BUCKETHEAD_HEALTH  # 30 máu
    self.helmet = True                # Giáp mạnh hơn
```

## 🎯 **HỆ THỐNG ĐẠN VÀ VA CHẠM**

### **1. Cấu trúc đạn**
```python
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, start_y, dest_y, name, damage, ice):
        self.damage = damage    # Sát thương
        self.ice = ice         # Hiệu ứng băng
        self.state = c.FLY     # Trạng thái bay
        self.x_vel = 4        # Tốc độ ngang
        self.y_vel = 4        # Tốc độ dọc
```

### **2. Cơ chế bay của đạn**
```python
def update(self, game_info):
    if self.state == c.FLY:
        # Điều chỉnh vị trí Y để bay thẳng
        if self.rect.y != self.dest_y:
            self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        
        # Xóa đạn khi ra khỏi màn hình
        if self.rect.x > c.SCREEN_WIDTH:
            self.kill()
```

### **3. Hệ thống va chạm**
```python
def checkBulletCollisions(self):
    # Sử dụng collision detection với tỷ lệ 0.7
    collided_func = pg.sprite.collide_circle_ratio(0.7)
    
    for bullet in self.bullet_groups[i]:
        zombie = pg.sprite.spritecollideany(bullet, self.zombie_groups[i], collided_func)
        if zombie and zombie.state != c.DIE:
            zombie.setDamage(bullet.damage, bullet.ice)
            bullet.setExplode()
```

## 🗺️ **HỆ THỐNG BẢN ĐỒ**

### **1. Lưới 9x5**
```python
GRID_X_LEN = 9  # 9 cột
GRID_Y_LEN = 5  # 5 hàng
GRID_X_SIZE = 80   # Kích thước ô ngang
GRID_Y_SIZE = 100  # Kích thước ô dọc
```

### **2. Chuyển đổi tọa độ**
```python
def getMapIndex(self, x, y):
    # Chuyển từ pixel sang tọa độ lưới
    x -= c.MAP_OFFSET_X
    y -= c.MAP_OFFSET_Y
    return (x // c.GRID_X_SIZE, y // c.GRID_Y_SIZE)

def getMapGridPos(self, map_x, map_y):
    # Chuyển từ tọa độ lưới sang pixel
    return (map_x * c.GRID_X_SIZE + c.GRID_X_SIZE//2 + c.MAP_OFFSET_X,
            map_y * c.GRID_Y_SIZE + c.GRID_Y_SIZE//5 * 3 + c.MAP_OFFSET_Y)
```

### **3. Quản lý vị trí cây**
```python
def showPlant(self, x, y):
    map_x, map_y = self.getMapIndex(x, y)
    if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
        return self.getMapGridPos(map_x, map_y)  # Trả về vị trí đặt cây
    return None
```

## 💰 **HỆ THỐNG TÀI NGUYÊN**

### **1. Ánh sáng mặt trời**
```python
class Sun(pg.sprite.Sprite):
    def __init__(self, x, y, dest_x, dest_y):
        self.sun_value = c.SUN_VALUE  # 25 điểm
        self.live_time = c.SUN_LIVE_TIME  # 7 giây
        self.fall_speed = 2
```

### **2. Sản xuất ánh sáng**
```python
def play(self, mouse_pos, mouse_click):
    # Sản xuất tự động mỗi 7 giây
    if (self.current_time - self.sun_timer) > c.PRODUCE_SUN_INTERVAL:
        self.sun_timer = self.current_time
        map_x, map_y = self.map.getRandomMapIndex()
        x, y = self.map.getMapGridPos(map_x, map_y)
        self.sun_group.add(plant.Sun(x, 0, x, y))
```

### **3. Thu thập ánh sáng**
```python
# Kiểm tra click vào ánh sáng
for sun in self.sun_group:
    if sun.checkCollision(mouse_pos[0], mouse_pos[1]):
        self.menubar.increaseSunValue(sun.sun_value)
        sun.kill()
```

## 🎮 **HỆ THỐNG MENU VÀ CARD**

### **1. Cấu trúc Card**
```python
class Card():
    def __init__(self, x, y, name_index, scale=0.78):
        self.sun_cost = plant_sun_list[name_index]      # Giá mua
        self.frozen_time = plant_frozen_time_list[name_index]  # Thời gian cooldown
        self.frozen_timer = -self.frozen_time         # Timer cooldown
        self.select = True                             # Có thể chọn
```

### **2. Kiểm tra có thể mua**
```python
def canClick(self, sun_value, current_time):
    # Đủ tiền và hết cooldown
    if self.sun_cost <= sun_value and (current_time - self.frozen_timer) > self.frozen_time:
        return True
    return False
```

### **3. Hiển thị trạng thái card**
```python
def createShowImage(self, sun_value, current_time):
    time = current_time - self.frozen_timer
    if time < self.frozen_time:  # Đang cooldown
        # Hiển thị thanh cooldown
        frozen_height = (self.frozen_time - time)/self.frozen_time * self.rect.h
    elif self.sun_cost > sun_value:  # Không đủ tiền
        image.set_alpha(192)  # Làm mờ
```

## 🎯 **HỆ THỐNG LEVEL VÀ SPAWN**

### **1. File cấu hình level**
```json
{
    "background_type": 0,           // Loại nền (ngày/đêm)
    "init_sun_value": 50,           // Ánh sáng ban đầu
    "zombie_list": [                // Danh sách zombie
        {"time": 1000, "name": "Zombie", "map_y": 0},
        {"time": 5000, "name": "ConeheadZombie", "map_y": 1}
    ]
}
```

### **2. Spawn zombie theo thời gian**
```python
def play(self, mouse_pos, mouse_click):
    if len(self.zombie_list) > 0:
        data = self.zombie_list[0]
        if data[0] <= (self.current_time - self.zombie_start_time):
            self.createZombie(data[1], data[2])  # Tạo zombie
            self.zombie_list.remove(data)         # Xóa khỏi danh sách
```

### **3. Tạo zombie**
```python
def createZombie(self, name, map_y):
    x, y = self.map.getMapGridPos(0, map_y)
    if name == c.NORMAL_ZOMBIE:
        self.zombie_groups[map_y].add(zombie.NormalZombie(c.ZOMBIE_START_X, y, self.head_group))
    elif name == c.CONEHEAD_ZOMBIE:
        self.zombie_groups[map_y].add(zombie.ConeHeadZombie(c.ZOMBIE_START_X, y, self.head_group))
```

## 🏆 **ĐIỀU KIỆN THẮNG THUA**

### **1. Kiểm tra thắng**
```python
def checkVictory(self):
    # Không còn zombie trong danh sách
    if len(self.zombie_list) > 0:
        return False
    
    # Không còn zombie trên màn hình
    for i in range(self.map_y_len):
        if len(self.zombie_groups[i]) > 0:
            return False
    return True
```

### **2. Kiểm tra thua**
```python
def checkLose(self):
    # Zombie đi qua màn hình
    for i in range(self.map_y_len):
        for zombie in self.zombie_groups[i]:
            if zombie.rect.right < 0:  # Zombie ra khỏi màn hình trái
                return True
    return False
```

## 🎨 **HỆ THỐNG ĐỒ HỌA**

### **1. Tải hình ảnh**
```python
def load_all_gfx(directory):
    # Tự động tải tất cả hình ảnh từ thư mục
    # Hỗ trợ .png, .jpg, .bmp, .gif
    # Tự động phát hiện thư mục graphics
```

### **2. Animation**
```python
def animation(self):
    # Chuyển frame theo thời gian
    if (self.current_time - self.animate_timer) > self.animate_interval:
        self.frame_index = (self.frame_index + 1) % self.frame_num
        self.image = self.frames[self.frame_index]
        self.animate_timer = self.current_time
```

### **3. Hiển thị**
```python
def draw(self, surface):
    # Vẽ background
    surface.blit(self.background, self.bg_rect)
    
    # Vẽ các sprite groups
    for i in range(self.map_y_len):
        self.plant_groups[i].draw(surface)
        self.zombie_groups[i].draw(surface)
        self.bullet_groups[i].draw(surface)
```

## 🔧 **TỐI ƯU HÓA**

### **1. Sprite Groups theo hàng**
- Mỗi hàng có group riêng → giảm collision detection
- Chỉ kiểm tra va chạm trong cùng hàng

### **2. Timer-based updates**
- Cập nhật animation mỗi 150ms
- Cập nhật card mỗi 250ms
- Tránh cập nhật quá thường xuyên

### **3. Memory management**
- Tự động xóa sprite khi `kill()`
- Sử dụng `set_colorkey()` để tối ưu hiển thị

## 🚀 **CÁCH CHẠY**

1. **Cài đặt pygame:**
```bash
pip install pygame
```

2. **Chạy game:**
```bash
python run_game.py

```

3. **Hoặc dùng batch file:**
```bash
run_ppvz_local.bat
```




