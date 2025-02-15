
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt App")
        self.setGeometry(100, 100, 800, 600)  # Window size (x, y, width, height)

        # Set the background color
        self.setStyleSheet("background-color: black;")

        # Create a label
        self.label = QLabel("Insert app name", self)
        self.label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")

        # Set the position of the label (x, y)
        self.label.move(200, 200)  # Adjust these values as needed

        # Fullscreen mode
        self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
