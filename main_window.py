from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(701, 389)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Roboto Mono"])
        font.setPointSize(10)
        font.setBold(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_6 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Roboto Mono Medium"])
        font1.setPointSize(17)
        font1.setBold(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"Roboto Mono Medium"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.file_name = QLineEdit(self.centralwidget)
        self.file_name.setObjectName(u"file_name")

        self.horizontalLayout_4.addWidget(self.file_name)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.new_ved = QPushButton(self.centralwidget)
        self.new_ved.setObjectName(u"new_ved")
        self.new_ved.setFont(font)
        self.new_ved.setStyleSheet(u"background-color: rgb(41, 137, 255);\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_3.addWidget(self.new_ved)

        self.clear_all = QPushButton(self.centralwidget)
        self.clear_all.setObjectName(u"clear_all")
        self.clear_all.setFont(font)
        self.clear_all.setStyleSheet(u"background-color: rgb(41, 137, 255);\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_3.addWidget(self.clear_all)

        self.calculate = QPushButton(self.centralwidget)
        self.calculate.setObjectName(u"calculate")
        self.calculate.setFont(font)
        self.calculate.setStyleSheet(u"background-color: rgb(41, 137, 255);\n"
"color: rgb(255,255,255);")

        self.horizontalLayout_3.addWidget(self.calculate)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(109, 0))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(16, 0))
        font3 = QFont()
        font3.setFamilies([u"Roboto Mono Medium"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")

        self.horizontalLayout.addWidget(self.label_4)

        self.x_scale = QLineEdit(self.centralwidget)
        self.x_scale.setObjectName(u"x_scale")
        sizePolicy.setHeightForWidth(self.x_scale.sizePolicy().hasHeightForWidth())
        self.x_scale.setSizePolicy(sizePolicy)
        self.x_scale.setMinimumSize(QSize(0, 0))
        self.x_scale.setMaximumSize(QSize(100, 26))
        self.x_scale.setBaseSize(QSize(20, 26))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.x_scale.setFont(font4)

        self.horizontalLayout.addWidget(self.x_scale)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(15, 0))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0,0,0);")

        self.horizontalLayout.addWidget(self.label_5)

        self.y_scale = QLineEdit(self.centralwidget)
        self.y_scale.setObjectName(u"y_scale")
        sizePolicy.setHeightForWidth(self.y_scale.sizePolicy().hasHeightForWidth())
        self.y_scale.setSizePolicy(sizePolicy)
        self.y_scale.setMinimumSize(QSize(0, 0))
        self.y_scale.setMaximumSize(QSize(100, 26))
        self.y_scale.setBaseSize(QSize(20, 26))
        self.y_scale.setFont(font4)

        self.horizontalLayout.addWidget(self.y_scale)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.draw_profile = QPushButton(self.centralwidget)
        self.draw_profile.setObjectName(u"draw_profile")
        self.draw_profile.setMinimumSize(QSize(254, 0))
        self.draw_profile.setFont(font)
        self.draw_profile.setStyleSheet(u"background-color: rgb(41, 137, 255);\n"
"color: rgb(255,255,255);")

        self.verticalLayout_3.addWidget(self.draw_profile)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u0440\u044b\u0436\u0443\u043b\u0438", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0434\u043e\u043c\u043e\u0441\u0442\u044c \u0442\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043d\u0438\u0432\u0435\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430", None))
        self.new_ved.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.clear_all.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.calculate.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0451\u0442", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0434\u043e\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0441\u0448\u0442\u0430\u0431", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.draw_profile.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043f\u0440\u043e\u0444\u0438\u043b\u044c", None))
    # retranslateUi

