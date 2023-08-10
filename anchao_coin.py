from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import json

'''使浏览器静音'''
options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
# 填写webdriver的保存目录
driver = webdriver.Chrome(options=options)

# 记得写完整的url 包括http和https
driver.get('https://cc.163.com/24/6924324/?actiontype=1&actid=9670&actidpos=activity-entry-con')

# 首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies.txt','r') as f:
    # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookies_list = json.load(f)

    # 方法1 将expiry类型变为int
    for cookie in cookies_list:
        # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)
driver.refresh()
driver.implicitly_wait(10)   # 隐式等待
p1  = driver.find_element(By.CLASS_NAME,'btn-close-today').click()  # 关闭弹窗
driver.implicitly_wait(20)
'''定位第一个iframe'''
iframe = driver.find_element(By.XPATH,"(//iframe[@name='webcc_4000'])[4]")
driver.switch_to.frame(iframe)  # 切换到iframe
driver.implicitly_wait(10)
p2 = driver.find_element(By.XPATH,'/html/body/div/div[3]/div/div[5]').click()  #点击立即加速升级
driver.implicitly_wait(20)
'''定位第二个iframe'''''
driver.switch_to.default_content()  # 切换到默认页面
driver.implicitly_wait(10)
iframe_1 = driver.find_element(By.XPATH,"(//iframe[@name='webcc_4000'])[5]")
driver.switch_to.frame(iframe_1)  # 切换到iframe
driver.implicitly_wait(10)
shouqu = driver.find_element(By.XPATH,"(//div[@class='btn'])[1]").click()
time.sleep(5)
driver.quit()