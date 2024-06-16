import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPixmap, QDragEnterEvent, QDropEvent
from PyQt5.QtCore import Qt
from PIL import Image
import os

class ImageSpaceAdder(QWidget):
    def __init__(self, space_width=200, desired_height=400):
        super().__init__()
        self.space_width = space_width
        self.desired_height = desired_height
        self.initUI()
        self.image_path = None

    def initUI(self):
        self.setWindowTitle('Image Space Adder')
        self.setGeometry(100, 100, 500, 400)  # Smaller window size

        # Set up the layout
        main_layout = QVBoxLayout()

        # Label to display instructions for drag-and-drop
        self.instructions_label = QLabel('Drag and drop an image file here:', self)
        self.instructions_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.instructions_label)

        # Horizontal layout for image preview and status
        preview_status_layout = QHBoxLayout()

        # Label to show the loaded image
        self.image_display = QLabel(self)
        self.image_display.setFixedSize(300, 200)  # Smaller preview area
        self.image_display.setAlignment(Qt.AlignCenter)
        preview_status_layout.addWidget(self.image_display)

        # Label to show the save status
        self.status_label = QLabel('', self)
        self.status_label.setAlignment(Qt.AlignCenter)
        preview_status_layout.addWidget(self.status_label)

        main_layout.addLayout(preview_status_layout)
        self.setLayout(main_layout)

        # Enable drag and drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        # Accept the drag event if it contains image files
        if event.mimeData().hasUrls() and any(url.toLocalFile().lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')) for url in event.mimeData().urls()):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        # Process the dropped image files
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    self.image_path = file_path
                    pixmap = QPixmap(file_path)
                    self.image_display.setPixmap(pixmap.scaled(self.image_display.size(), Qt.KeepAspectRatio))
                    self.status_label.setText(f"Image loaded: {file_path}")
                    self.status_label.setStyleSheet("color: blue;")
                    self.add_space_resize_and_save_image(file_path)  # Automatically add space and save the image
                else:
                    self.status_label.setText("Invalid file type. Please drop an image file.")
                    self.status_label.setStyleSheet("color: red;")
            event.acceptProposedAction()
        else:
            event.ignore()

    def add_space_resize_and_save_image(self, file_path):
        if not file_path:
            return
        
        # Load the original image
        arrow_image = Image.open(file_path)
        
        # Convert image to RGBA (supports transparency and ensures consistency for PNG)
        arrow_image = arrow_image.convert('RGBA')

        # Get the size of the original image
        arrow_width, arrow_height = arrow_image.size

        # Define the width of the new image (space width + arrow width)
        new_width = arrow_width + self.space_width

        # Create a new image with the combined width and original height
        new_image_with_space_first = Image.new("RGBA", (new_width, arrow_height), (255, 255, 255, 0))

        # Paste the arrow onto the new image after the specified space width
        new_image_with_space_first.paste(arrow_image, (self.space_width, 0))

        # Calculate the new width to maintain the aspect ratio
        aspect_ratio = new_width / arrow_height
        new_width_resized = int(self.desired_height * aspect_ratio)

        # Resize the image to the desired height while maintaining aspect ratio
        resized_image = new_image_with_space_first.resize((new_width_resized, self.desired_height), Image.Resampling.LANCZOS)

        # Save the updated image with a new name
        base_name = os.path.splitext(file_path)[0]
        new_file_name = f"{base_name}_spaced.png"
        resized_image.save(new_file_name, format='PNG')

        # Update the status label
        self.status_label.setText(f"Image saved as: {new_file_name}")
        self.status_label.setStyleSheet("color: green;")

if __name__ == '__main__':
    # Define the space width and desired height here
    space_width = 500  # Width of the space to add before the arrow
    desired_height = 100  # Desired height for the resized image

    app = QApplication(sys.argv)
    ex = ImageSpaceAdder(space_width, desired_height)
    ex.show()
    sys.exit(app.exec_())
