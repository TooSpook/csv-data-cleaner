from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV cleaner")
        self.setFixedSize(QSize(512, 384))
        self.setWindowIcon(QIcon("resources/app_icon.png"))