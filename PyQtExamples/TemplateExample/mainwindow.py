from PyQt5.QtWidgets import \
    QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("This is my template example")
        print("Hello world!!")