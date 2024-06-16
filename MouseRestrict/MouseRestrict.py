# MouseRestrict/MouseRestrict.py

import ctypes
import threading
import time
import math
import random
from screeninfo import get_monitors

# Function to load the custom cursor from file
def load_custom_cursor(cursor_path):
    handle = ctypes.windll.user32.LoadCursorFromFileW(cursor_path)
    return handle

# Function to set the system cursor
def set_system_cursor(cursor_handle, cursor_name):
    ctypes.windll.user32.SetSystemCursor(cursor_handle, 32512)  # IDC_ARROW (Normal Select)

class MouseRestrictor(threading.Thread):
    def __init__(self, invisible_cursor_path, original_cursor_path):
        super(MouseRestrictor, self).__init__()
        self.invisible_cursor_file = invisible_cursor_path
        self.original_cursor_file = original_cursor_path

        # Load the cursors
        self.INVISIBLE_CURSOR = load_custom_cursor(self.invisible_cursor_file)
        self.ORIGINAL_CURSOR = load_custom_cursor(self.original_cursor_file)

        # Ensure the custom invisible cursor is loaded correctly
        if not self.INVISIBLE_CURSOR or not self.ORIGINAL_CURSOR:
            print("Failed to load cursors.")
            exit(1)

        self.paused = True  # Start in a paused state
        self.running = True

    def run(self):
        self.restrict_mouse_within_circle()

    def restrict_mouse_within_circle(self):
        monitor = get_monitors()[0]
        screen_width = monitor.width
        screen_height = monitor.height

        x0, y0, N, boundary_margin = screen_width // 2, screen_height // 2, 50, 10
        while self.running:
            if not self.paused:
                x, y = self.get_mouse_pos()
                dx, dy = x - x0, y - y0
                d = math.sqrt(dx**2 + dy**2)

                if d > N - boundary_margin:
                    angle = math.atan2(dy, dx)
                    nearest_x = x0 + (N - boundary_margin) * math.cos(angle)
                    nearest_y = y0 + (N - boundary_margin) * math.sin(angle)
                    self.set_mouse_pos(nearest_x, nearest_y)
                time.sleep(0.02 + random.uniform(0, 0.01))
            else:
                time.sleep(0.1)

    def toggle_pause(self):
        self.paused = not self.paused

    def stop(self):
        self.running = False
        self.set_cursor_visible()

    def set_cursor_invisible(self):
        if self.reset_invisible_cursor():
            set_system_cursor(self.INVISIBLE_CURSOR, "invisible")

    def set_cursor_visible(self):
        if self.reset_original_cursor():
            set_system_cursor(self.ORIGINAL_CURSOR, "original")

    def reset_invisible_cursor(self):
        self.INVISIBLE_CURSOR = load_custom_cursor(self.invisible_cursor_file)
        return bool(self.INVISIBLE_CURSOR)

    def reset_original_cursor(self):
        self.ORIGINAL_CURSOR = load_custom_cursor(self.original_cursor_file)
        return bool(self.ORIGINAL_CURSOR)

    def set_mouse_pos(self, x, y):
        ctypes.windll.user32.SetCursorPos(int(x), int(y))

    def get_mouse_pos(self):
        point = ctypes.wintypes.POINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
        return point.x, point.y
