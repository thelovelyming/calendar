from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtWidgets import QMainWindow, QCalendarWidget
from PySide6.QtCore import QDate, Qt


class CalendarApp(QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.setWindowTitle("Calendar App")

        self.calendar = QCalendarWidget(self)
        self.setCentralWidget(self.calendar)

        self.calendar.clicked.connect(self.on_date_clicked)
        self.calendar.activated.connect(self.on_date_double_clicked)

        # 将日期与调度关联的示例字典
        self.schedules = {}

        for account in data["user"]["accounts"].values():
            for schedule in account["schedules"]:
                date_string = schedule["date"]
                year, month, day = map(int, date_string.split("-"))
                title = schedule["title"]
                date = QDate(year, month, day)
                # 将日期对象作为字典的键
                self.schedules[date] = title

        self.update_calendar()

    def update_calendar(self):
        for date, title in self.schedules.items():
            date_format = QTextCharFormat()
            date_format.setForeground(QColor(Qt.black))  # 设置日期文本的前景色为黑色
            date_format.setBackground(QColor(Qt.white))  # 设置日期文本的背景色为白色
            date_format.setToolTip(title)  # 设置日期的工具提示为日程标题
            self.calendar.setDateTextFormat(date, date_format)
            self.calendar.setDateToolTip(date, title)  # 将日期的工具提示设置为日程标题，以在日历上直接显示标题


    def get_date_format(self, date):
        # 获取给定日期的文本格式
        return self.calendar.dateTextFormat(date)

    def on_date_clicked(self, date):
        schedule = self.schedules.get(date)
        if schedule:
            print(f"Schedule for {date.toString(Qt.ISODate)}: {schedule}")
            self.calendar.setSelectedDate(date)

    def on_date_double_clicked(self, date):
        print("1")
       # schedule = self.schedules.get(date)
       # new_schedule, ok = QInputDialog.getText(self, "Edit Schedule", f"Edit Schedule for {date.toString(Qt.ISODate)}", text=schedule)
       # if ok:
        #    self.schedules[date] = new_schedule

         #   self.update_calendar()
          #  return data




