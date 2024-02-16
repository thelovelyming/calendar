from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation, QEasingCurve
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QDesktopWidget
from calendar_main_page import calendar_main_page

animation = None  # 将动画定义为全局变量


def on_text_changed(input_password):
    input_password.setStyleSheet("")  # 恢复默认样式


def on_button_clicked(password, input_password, data):
    if password == input_password.text():
        print("successful")
        input_password.window().close()
        calendar_main_page(data)
    else:
        input_password.setStyleSheet("color: red;")
        input_password.setPlaceholderText("try again")


def on_enter_event(event):
    if animation.state() != QPropertyAnimation.Running:
        animation.start()
        print(animation.state())


def on_leave_event(event):
    if animation.state() == QPropertyAnimation.Running:
        animation.stop()
        print(animation.state())


def calculate_center(window_width, width):
    return window_width // 2 - width // 2


def quit_app(app):
    app.quit()


def login_main(data):

    password = data["user"]["password"]
    app = QApplication([])

    window = QMainWindow()
    window_width = 300
    window_height = 400
    window.resize(window_width, window_height)
    window.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    desktop = QDesktopWidget().screenGeometry()
    screen_width = desktop.width()
    screen_height = desktop.height()

    window_x = (screen_width - window_width) // 2
    window_y = (screen_height - window_height) // 2
    window.move(window_x, window_y)

    quit_button = QPushButton(window)
    quit_button.setIcon(QIcon("image/exit.png"))
    quit_button.setFlat(True)
    quit_button.clicked.connect(lambda: quit_app(app))
    quit_button.resize(25, 25)
    quit_button.move(window_width - quit_button.width(), 0)

    global animation
    animation = QPropertyAnimation(quit_button, b"rotation")
    animation.setDuration(1000)
    animation.setStartValue(0)
    animation.setEndValue(360)
    animation.setEasingCurve(QEasingCurve.Linear)
    animation.setLoopCount(-1)

    quit_button.enterEvent = on_enter_event
    quit_button.leaveEvent = on_leave_event

    label = QLabel(window)
    pixmap = QPixmap("image/login.png")
    scaled_pixmap = pixmap.scaled(100, 100)
    label.setPixmap(scaled_pixmap)
    label.resize(pixmap.width(), pixmap.height())
    label.move(100, 25)

    input_password = QLineEdit(window)
    input_password.setPlaceholderText("password")
    input_password.resize(200, 30)
    input_password.move(calculate_center(window_width, input_password.width()), 200)
    input_password.textChanged.connect(lambda: on_text_changed(input_password))

    button = QPushButton('login', window)
    button.resize(100, 30)
    button.move(calculate_center(window_width, button.width()), 300)
    button.clicked.connect(lambda: on_button_clicked(password, input_password, data))

    window.show()

    app.exec_()
