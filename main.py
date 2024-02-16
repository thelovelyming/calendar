from data_initializer import initialize_data, save_data
from login import login_main

# 初始化
data = initialize_data()

login_main(data)

# 保存
save_data(data)
