import json


def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)


def add_schedule(account_name, schedule):
    data = load_data()
    if account_name in data["user"]["accounts"]:
        data["user"]["accounts"][account_name]["schedules"].append(schedule)
    save_data(data)


def delete_schedule(account_name, index):
    data = load_data()
    if account_name in data["user"]["accounts"]:
        schedules = data["user"]["accounts"][account_name]["schedules"]
        if 0 <= index < len(schedules):
            del schedules[index]
    save_data(data)


def update_schedule(account_name, index, updated_schedule):
    data = load_data()
    if account_name in data["user"]["accounts"]:
        schedules = data["user"]["accounts"][account_name]["schedules"]
        if 0 <= index < len(schedules):
            schedules[index] = updated_schedule
    save_data(data)


def add_account(account_name):
    data = load_data()
    if account_name not in data["user"]["accounts"]:
        data["user"]["accounts"][account_name] = {
            "accountName": account_name,
            "schedules": []
        }
    save_data(data)


def delete_account(account_name):
    data = load_data()
    if account_name in data["user"]["accounts"]:
        del data["user"]["accounts"][account_name]
    save_data(data)


def rename_account(old_name, new_name):
    data = load_data()
    if old_name in data["user"]["accounts"]:
        data["user"]["accounts"][new_name] = data["user"]["accounts"].pop(old_name)
    save_data(data)
