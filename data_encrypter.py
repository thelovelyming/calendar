import json
import hashlib
from cryptography.fernet import Fernet


def generate_key():
    # 生成密钥
    key = Fernet.generate_key()
    return key


def encrypt_data(data, key):
    # 使用密钥对数据进行加密
    data_str = json.dumps(data)

    f = Fernet(key)
    encrypted_data = f.encrypt(data_str.encode())
    return encrypted_data


def decrypt_data(encrypted_data, key):
    # 使用密钥对加密数据进行解密
    f = Fernet(key)
    data_str = f.decrypt(encrypted_data).decode()
    data_str = data_str.replace("\\", "")

    # print(data_str)

    data = json.loads(data_str)

    print(type(data))
    print(data)

    return data


def save_encrypted_data(encrypted_data):
    # 将加密数据保存到文件
    with open("data.json", "wb") as file:
        file.write(encrypted_data)


def load_encrypted_data():
    # 从文件中加载加密数据
    try:
        with open("data.json", "rb") as file:
            encrypted_data = file.read()
    except FileNotFoundError:
        encrypted_data = {}
    return encrypted_data


def save_key_to_file(key):
    # 将密钥保存到文件
    with open("key.txt", "w") as key_file:
        key_file.write(key.decode())


def load_key_from_file():
    # 从文件中加载密钥
    with open("key.txt", "r") as key_file:
        key = key_file.read().strip()
    return key


def calculate_hash(data):
    # 将数据转换为 JSON 字符串
    data_json = json.dumps(data, sort_keys=True)

    # 创建 SHA-256 哈希对象
    hash_object = hashlib.sha256()

    # 更新哈希对象
    hash_object.update(data_json.encode('utf-8'))

    # 计算哈希摘要并转换为十六进制字符串
    hash_value = hash_object.hexdigest()

    # 返回哈希值
    return hash_value


def hash_check(data):
    pre_hash_value = data["user"]["hash"]
    del data["user"]["hash"]
    hash_value = calculate_hash(data)
    print("hash_value is : " + hash_value)
    print("pre_hash_value is : " + pre_hash_value)
    if hash_value == pre_hash_value:
        print("hash correct")
    else:
        print("hash not correct")
    return data
