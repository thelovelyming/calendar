from datetime import datetime


def get_days_difference(date_str):
    # 将日期字符串转换为 datetime 对象
    date = datetime.strptime(date_str, "%Y-%m-%d")
    # 获取当前时间
    now = datetime.now()
    # 计算时间差
    time_difference = now - date
    # 获取时间差的天数部分
    days_difference = time_difference.days
    # 返回天数差
    return days_difference


def calculate_weight(days_difference, importance):
    # 计算权重
    if days_difference <= 7:
        weight_days = 5 - (days_difference / 7) * 5  # 使用时间差的百分比
    else:
        weight_days = 0

    # 计算权重，将时间差权重和重要性相加
    weight = weight_days + int(importance)

    return weight


def get_schedules(data):
    all_schedules = []
    # 获取账户中的所有日程
    for account in data["user"]["accounts"].values():
        for schedule in account["schedules"]:
            # 计算天数差并替换日期到日程字典中
            schedule["days"] = get_days_difference(schedule["date"])
            schedule["weights"] = calculate_weight(get_days_difference(schedule["date"]), schedule["importance"])
            all_schedules.append(schedule)
    return all_schedules


def get_sort_key_by_importance(schedule):
    # 获取重要性、日期和时间
    importance = int(schedule["importance"])
    days = schedule["days"]
    time = schedule["start_time"]

    # 返回一个元组，包含了多个排序键
    return -importance, days, time


def get_sort_key_by_days(schedule):
    importance = int(schedule["importance"])
    days = schedule["days"]
    time = schedule["start_time"]

    # 修改了排序顺序
    return days, time, -importance


def sort_schedules_by_importance(all_schedules):
    # 对日程列表按照重要性进行排序
    all_schedules_sorted = sorted(all_schedules, key=get_sort_key_by_importance)
    return all_schedules_sorted


def sort_schedules_by_days(all_schedules):
    # 对日程列表按照日期进行排序
    all_schedules_sorted = sorted(all_schedules, key=get_sort_key_by_days)
    return all_schedules_sorted


def sort_schedules_by_weight(all_schedules):
    all_schedules_sorted = sorted(all_schedules, key=lambda x: x["weights"], reverse=True)
    return all_schedules_sorted


def print_schedules(all_schedules):
    for schedule in all_schedules:
        print(schedule)
