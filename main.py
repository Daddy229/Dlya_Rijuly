import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow
import excel_pars
import darwing


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.new_ved.clicked.connect(self.create_xl)
        self.ui.clear_all.clicked.connect(self.clear_table)
        self.ui.calculate.clicked.connect(self.only_calculate)
        self.ui.draw_profile.clicked.connect(self.draw_me)

    def create_xl(self):
        name = self.ui.file_name.text()
        if name == "":
            name = "no_name"
        name += '.xlsx'
        excel_pars.make_title(f'{name}')
        excel_pars.clear_table(f'{name}')

    def clear_table(self):
        name = self.ui.file_name.text()
        if name == "":
            name = "no_name"
        name += '.xlsx'
        excel_pars.clear_table(f'{name}')

    def only_calculate(self):
        name = self.ui.file_name.text()
        if name == "":
            name = "no_name"
        name += '.xlsx'
        excel_pars.read_info(f_name=name)

    def draw_me(self):
        prof_name = self.ui.file_name.text()
        m_x = int(self.ui.x_scale.text())
        m_y = int(self.ui.y_scale.text())

        darwing.draw_profile(m_x_scale=m_x, m_y_scale=m_y, profile_name=prof_name)


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())