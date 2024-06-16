import sys
import os
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox, QHBoxLayout, QMenu, QAction, QSystemTrayIcon, QGraphicsDropShadowEffect, QFrame
from PyQt5.QtGui import QPixmap, QIcon, QColor
from PyQt5.QtCore import Qt, QPoint, QProcess, QMetaObject, Q_ARG, pyqtSlot
from pynput import keyboard
import threading

# Importing classes and functions from MouseRestrict.py located in the subdirectory MouseRestrict
from MouseRestrict.MouseRestrict import MouseRestrictor
# Importing DynamicCursor class
from Cursor.DynamicCursor import DynamicCursor

def resource_path(relative_path):
    """ Convert relative resource paths to absolute paths for both development and bundled application. """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class GlobalKeyListener(threading.Thread):
    def __init__(self, app):
        super(GlobalKeyListener, self).__init__()
        self.app = app
        self.listener = keyboard.Listener(on_press=self.on_press)

    def run(self):
        self.listener.start()
        self.listener.join()

    def on_press(self, key):
        try:
            if key == keyboard.Key.esc:
                self.app.exit_app()
            elif key.char == '1':
                self.app.toggle_pause()
            elif key.char == '2':
                self.app.toggle_dynamic_cursor()
        except AttributeError:
            pass

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super(CustomTitleBar, self).__init__(parent)
        self.setFixedHeight(30)  # Set height for the title bar
        self.setStyleSheet("background-color: #333333; color: white; border-bottom: 2px solid #555555;")  # Style the title bar with a bottom border

        # Apply a shadow effect to create a visual separation
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setOffset(0, 3)  # Shadow offset
        self.setGraphicsEffect(shadow)

        # Layout for the title bar
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Window icon
        self.window_icon = QLabel()
        self.window_icon.setPixmap(QPixmap(resource_path('app_logo.ico')).scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(self.window_icon, alignment=Qt.AlignLeft)

        # Window title
        self.title_label = QLabel("SlitherAssist")
        self.title_label.setStyleSheet("padding-left: 10px;")
        layout.addWidget(self.title_label, alignment=Qt.AlignLeft)

        # Spacer to push buttons to the right
        layout.addStretch()

        # Minimize button
        self.minimize_button = QPushButton("-")
        self.minimize_button.setFixedSize(30, 30)
        self.minimize_button.setStyleSheet("background-color: #555555; border: none; color: white;")
        self.minimize_button.clicked.connect(self.minimize_to_tray)
        layout.addWidget(self.minimize_button)

        # Close button
        self.close_button = QPushButton("X")
        self.close_button.setFixedSize(30, 30)
        self.close_button.setStyleSheet("background-color: #E81123; border: none; color: white;")
        self.close_button.clicked.connect(self.close_window)
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def minimize_to_tray(self):
        self.window().hide()
        self.window().tray_icon.showMessage(
            "SlitherAssist",
            "The application has been minimized to the system tray.",
            QSystemTrayIcon.Information,
            2000
        )

    def close_window(self):
        self.window().close()

    # Enable dragging the window
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging_position = event.globalPos() - self.parent().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.dragging_position:
            self.parent().move(event.globalPos() - self.dragging_position)
            event.accept()

class App(QWidget):
    def __init__(self):
        super().__init__()
        print("Starting App initialization...")
        self.show_initial_alert()  # Show the alert before initializing the UI
        self.initUI()
        print("UI initialized.")
        self.mouse_restrictor = MouseRestrictor(resource_path('MouseRestrict/invisible_cursor.cur'), 
                                                resource_path('MouseRestrict/original_cursor.cur'))
        self.mouse_restrictor.start()

        self.dynamic_cursor = None  # Placeholder for the DynamicCursor instance

        self.global_key_listener = GlobalKeyListener(self)
        self.global_key_listener.start()

        self.first_click = True
        self.last_toggle_time = time.time()

    def show_initial_alert(self):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Information)
        alert.setWindowTitle('Important!!!!')
        alert.setText('Use full screen for slither.io (REQUIRED)')
        alert.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        alert.setDefaultButton(QMessageBox.Ok)

        response = alert.exec_()

        if response == QMessageBox.Cancel:
            self.exit_app()

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)  # Remove the default title bar
        self.setWindowIcon(QIcon(resource_path('app_logo.ico')))

        # Main frame that acts as a border
        self.frame = QFrame(self)
        self.frame.setStyleSheet("background-color: white; border: 5px solid #333333; border-radius: 10px;")
        self.frame.setGeometry(10, 10, 380, 430)  # Adjust size according to your need

        # Main layout inside the frame
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.setContentsMargins(0, 0, 0, 0)
        frame_layout.setSpacing(0)

        # Custom title bar
        self.title_bar = CustomTitleBar(self)
        self.title_bar.setFixedHeight(30)
        frame_layout.addWidget(self.title_bar)

        # System tray setup
        self.tray_icon = QSystemTrayIcon(QIcon(resource_path('app_logo.ico')), self)
        self.tray_icon.setToolTip("SlitherAssist")
        self.tray_icon.activated.connect(self.on_tray_icon_activated)

        # Context menu for the tray icon
        self.tray_menu = QMenu(self)
        restore_action = QAction("Restore", self)
        restore_action.triggered.connect(self.show)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)
        self.tray_menu.addAction(restore_action)
        self.tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.show()

        # Add a semi-transparent overlay behind the text
        self.overlay = QLabel(self.frame)
        self.overlay.setStyleSheet("background-color: rgba(0, 0, 0, 0.6); border-radius: 15px;")

        # Create a background label with a background image
        self.background_label = QLabel(self.frame)
        pixmap = QPixmap(resource_path('background.webp'))
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(self.frame.rect())

        # Set up the info label with enhanced styling
        self.info_label = QLabel('''
            <div style="text-align: center; font-size: 20px; color: #FFFFFF;">
                <p style="margin-bottom: 0;">
                    <b>Instructions:</b><br>
                    <span>Press <b>"1"</b> to toggle start/stop</span><br>
                    <span>Press <b>"2"</b> to display extra cursor</span><br>
                    <span>Press <b>"Esc"</b> to exit</span>
                </p>
            </div>
        ''', self.frame)
        self.info_label.setStyleSheet("padding: 15px; background-color: rgba(0, 0, 0, 0.8); border-radius: 10px; margin: 20px;")

        # Button styles
        button_style = """
            QPushButton {
                font-size: 18px;
                padding: 15px;
                border-radius: 10px;
                color: white;
                background-color: #4CAF50;  /* Default color */
                margin: 5px;
                min-width: 150px;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #39733A;
            }
        """

        self.start_stop_button = QPushButton('Start', self.frame)
        self.start_stop_button.setIcon(QIcon(resource_path('start_icon.webp')))
        self.start_stop_button.setStyleSheet(button_style)

        self.extra_cursor_button = QPushButton('Display Extra Cursor', self.frame)
        self.extra_cursor_button.setStyleSheet(button_style + "background-color: #FF9800;")

        self.exit_button = QPushButton('Exit', self.frame)
        self.exit_button.setIcon(QIcon(resource_path('exit_icon.webp')))
        self.exit_button.setStyleSheet(button_style + "background-color: #f44336;")

        self.start_stop_button.clicked.connect(self.toggle_pause)
        self.extra_cursor_button.clicked.connect(self.toggle_dynamic_cursor)
        self.exit_button.clicked.connect(self.exit_app)

        # Layout for buttons
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.start_stop_button)
        button_layout.addWidget(self.extra_cursor_button)
        button_layout.addWidget(self.exit_button)
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setSpacing(15)  # Add space between buttons

        frame_layout.addWidget(self.info_label, alignment=Qt.AlignCenter)
        frame_layout.addLayout(button_layout)

        self.setLayout(frame_layout)
        self.setGeometry(300, 300, 400, 450)
        self.setFixedSize(400, 450)
        self.background_label.setGeometry(self.frame.rect())
        self.overlay.setGeometry(self.frame.rect())

        # Ensure background label stays at the bottom
        self.background_label.lower()
        self.overlay.lower()
        self.info_label.raise_()
        self.start_stop_button.raise_()
        self.extra_cursor_button.raise_()
        self.exit_button.raise_()
        print("UI setup complete.")

    def closeEvent(self, event):
        """Allow the application to exit normally when the close button is clicked."""
        self.exit_app()

    def on_tray_icon_activated(self, reason):
        """Restore the window when the tray icon is clicked."""
        if reason == QSystemTrayIcon.Trigger:
            self.show()

    def toggle_pause(self):
        if self.first_click:
            self.start_stop_button.setText('Pause')
            self.first_click = False
            self.mouse_restrictor.set_cursor_invisible()
        else:
            if self.mouse_restrictor.paused:
                self.start_stop_button.setText('Pause')
                self.mouse_restrictor.set_cursor_invisible()
            else:
                self.start_stop_button.setText('Resume')
                self.mouse_restrictor.set_cursor_visible()
        self.mouse_restrictor.toggle_pause()

    def toggle_dynamic_cursor(self):
        current_time = time.time()
        if current_time - self.last_toggle_time < 0.5:
            print("Debouncing, please wait...")
            return
        self.last_toggle_time = current_time

        if self.dynamic_cursor is None:
            print("Starting dynamic cursor...")
            QMetaObject.invokeMethod(self, "start_dynamic_cursor", Qt.QueuedConnection)
            self.extra_cursor_button.setText('Stop Extra Cursor')
        else:
            print("Stopping dynamic cursor...")
            self.terminate_dynamic_cursor()

    @pyqtSlot()
    def start_dynamic_cursor(self):
        # This method is called in the main GUI thread
        self.dynamic_cursor = DynamicCursor(resource_path('Cursor/arrow_spaced.png'))
        self.dynamic_cursor.show()

    def terminate_dynamic_cursor(self):
        if self.dynamic_cursor:
            self.dynamic_cursor.close()
            self.dynamic_cursor = None
            self.extra_cursor_button.setText('Display Extra Cursor')

    def exit_app(self):
        self.mouse_restrictor.stop()
        self.mouse_restrictor.join()

        if self.dynamic_cursor:
            self.dynamic_cursor.close()

        QApplication.instance().quit()
        os._exit(0)

if __name__ == "__main__":
    print("Starting the application...")
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
