from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("SELECT")
        button.setMinimumSize(120, 40)
        button.setMaximumSize(200, 50)
        button.setStyleSheet("padding: 12px 24px; font-size: 14px;")

        self.setWindowTitle("CSV cleaner")
        self.setMinimumSize(QSize(512, 384))
        self.setWindowIcon(QIcon("resources/app_icon.png"))
        self.setCentralWidget(button)

    def file_selection(self):
        pass