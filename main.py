import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.new_ved.clicked.connect(self.hello)

    def hello(self):
        text = self.ui.file_name.text()
        if text == "":
            text = "Oo"
        print(f'{text}')


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())