from main_window import MainWindow
from PyQt6.QtWidgets import QApplication, QWidget

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()