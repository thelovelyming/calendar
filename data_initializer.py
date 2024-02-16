import data_encrypter
from data_encrypter import generate_key, calculate_hash
from data_encrypter import load_key_from_file
from data_encrypter import save_key_to_file
from data_encrypter import decrypt_data
from data_encrypter import encrypt_data
from data_encrypter import load_encrypted_data
from data_encrypter import save_encrypted_data


def initialize_data():

    # 读取保存的数据文件
    encrypted_data = load_encrypted_data()

    # 检查是否为空
    if len(encrypted_data) == 0:

        data = {}
        name = input("请输入您的姓名：")
        password = input("请输入您的密码：")
        data["user"] = {
            "name": name,
            "password": password,
            "accounts": {},
        }

        # 添加账户和默认日程
        num_accounts = 5  # 假设有5个账户
        for i in range(1, num_accounts + 1):
            account_name = input(f"请输入账户{i}的名称：")
            data["user"]["accounts"][f"account{i}"] = {
                "accountName": account_name,
                "schedules": [{
                    "title": "DEFAULT",
                    "date": "2000-01-01",
                    "start_time": "12:00",
                    "duration": "1 hour",
                    "importance": "1",
                    "content": "DEFAULT"
                }]
            }

    # 若不为空解包并检查hash
    else:
        data = decrypt_data(encrypted_data, load_key_from_file())
        data = data_encrypter.hash_check(data)

    return data


def save_data(data):
    # 将数据保存到文件
    hash_value = calculate_hash(data)
    data["user"]["hash"] = hash_value
    key = generate_key()
    save_key_to_file(key)
    save_encrypted_data(encrypt_data(data, key))
    print("quit")
