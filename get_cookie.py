from selenium import webdriver
import time
import json

# 填写webdriver的保存目录
driver = webdriver.Chrome()

# 记得写完整的url 包括http和https
driver.get('https://cc.163.com/24/6924324/?actiontype=1&actid=9670&actidpos=activity-entry-con')

# 程序打开网页后20秒内 “手动登陆账户”
time.sleep(30)

with open('cookies.txt','w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()
