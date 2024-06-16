# Cursor/DynamicCursor.py

import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QTimer, QPointF
from PyQt5.QtGui import QPixmap, QTransform, QCursor

# Function to rotate an image around a pivot point
def rotate_on_pivot(image, angle, pivot, origin):
    transform = QTransform()
    transform.translate(pivot.x(), pivot.y())
    transform.rotate(-angle)
    transform.translate(-pivot.x(), -pivot.y())
    
    rotated_image = image.transformed(transform, Qt.SmoothTransformation)
    
    origin_vector = origin - pivot
    rotation_transform = QTransform().rotate(-angle)
    rotated_vector = rotation_transform.map(origin_vector)
    offset = pivot + rotated_vector
    
    rect = rotated_image.rect()
    rect.moveCenter(offset.toPoint())
    
    return rotated_image, rect

class Weapon:
    def __init__(self, pivot, image):
        self.pivot = pivot
        self.pos = pivot + QPointF(20, 0)
        
        self.image_orig = image
        self.image_unflipped = self.image_orig
        self.image_flipped = self.image_orig.transformed(QTransform().scale(-1, 1))
        
        self.image = self.image_orig
        self.rect = self.image.rect()
        self.rect.moveCenter(self.pos.toPoint())
        
    def update(self, dt, mouse_pos):
        self.image_orig = self.image_unflipped
        mouse_offset = mouse_pos - self.pivot
        mouse_angle = -math.degrees(math.atan2(mouse_offset.y(), mouse_offset.x()))
        
        self.image, self.rect = rotate_on_pivot(self.image_orig, mouse_angle, self.pivot, self.pos)
    
    def draw(self, scene):
        weapon_item = QGraphicsPixmapItem(self.image)
        weapon_item.setPos(self.rect.topLeft())
        scene.addItem(weapon_item)

class DynamicCursor(QMainWindow):
    reference_dict = {}  # Class attribute to hold loaded images

    def __init__(self, image_filename):
        super().__init__()
        
        self.image_filename = image_filename

        # Set up the screen size dynamically
        screen = QApplication.primaryScreen().availableGeometry()
        self.screen_width = screen.width()
        self.screen_height = screen.height()
        
        self.setWindowTitle('Dynamic Cursor')
        self.setGeometry(100, 100, self.screen_width, self.screen_height)
        
        self.scene = QGraphicsScene()
        
        # Set the scene's background to transparent
        self.scene.setBackgroundBrush(Qt.transparent)
        
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, self.screen_width, self.screen_height)
        
        # Set the view's background to transparent and no frame
        self.view.setStyleSheet("background: transparent; border: none;")
        
        self.load_image(self.image_filename)
        
        global screen_center
        screen_center = QPointF(self.screen_width / 2, self.screen_height / 2)
        
        self.weapon = Weapon(screen_center, self.reference_dict[self.image_filename])
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        self.timer.start(16)
        
        self.setMouseTracking(True)
        
        # Make the window frameless and transparent
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Make the window always on top
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        
        # Make the window transparent for input events
        self.setWindowFlag(Qt.WindowTransparentForInput)
        
        self.showFullScreen()
    
    def load_image(self, image_name):
        image = QPixmap(image_name)
        self.reference_dict[image_name] = image
  
    def update_game(self):
        dt = 1 / 60.0
        
        global_mouse_pos = QCursor.pos()
        
        mouse_pos = self.view.mapToScene(self.view.mapFromGlobal(global_mouse_pos))
        
        self.weapon.update(dt, mouse_pos)
        
        self.scene.clear()
        
        self.weapon.draw(self.scene)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
