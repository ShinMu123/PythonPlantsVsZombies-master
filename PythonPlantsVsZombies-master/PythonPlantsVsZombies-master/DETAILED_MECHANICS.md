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
python main.py
```

3. **Hoặc dùng batch file:**
```bash
run_ppvz_local.bat
```

Code này được thiết kế rất tốt với kiến trúc modular, dễ hiểu và mở rộng!
