import sys
import os

# Thêm đường dẫn thư mục source vào sys.path
project_path = os.path.join(os.path.dirname(__file__), 'PythonPlantsVsZombies-master', 'PythonPlantsVsZombies-master')
sys.path.insert(0, project_path)

import pygame as pg
from source.main import main

if __name__ == '__main__':
    main()
    pg.quit()
