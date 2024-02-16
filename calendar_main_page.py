from PySide6.QtWidgets import QMainWindow, QListWidget, QListWidgetItem, QApplication

from data_sort import get_schedules


class ScheduleWindow(QMainWindow):
    def __init__(self, schedules):
        super().__init__()

        self.setWindowTitle("Schedules")
        self.setGeometry(100, 100, 400, 300)

        self.schedules_list = QListWidget(self)
        self.schedules_list.setGeometry(10, 10, 380, 280)

        for schedule in schedules:
            item_text = (f"Title: {schedule['title']}, Date: {schedule['date']}, "
                         f"Start Time: {schedule['start_time']}, Duration: {schedule['duration']}, "
                         f"Importance: {schedule['importance']}, Content: {schedule['content']}")
            item = QListWidgetItem(item_text)
            self.schedules_list.addItem(item)

    def closeEvent(self, event):
        QApplication.quit()


def creat_list(schedules):
    window = ScheduleWindow(schedules)
    window.show()
    return window


def calendar_main_page(data):
    app = QApplication([])
    all_schedules = get_schedules(data)
    window = creat_list(all_schedules)
    window.show()
    app.exec_()
