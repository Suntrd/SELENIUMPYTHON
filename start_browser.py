#coding=utf-8
from selenium import webdriver
#判断页面元素是否存在
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
#判断元素是否包含
print(EC.title_contains("注册"))
#判断元素是否存在
element = driver.find_element_by_class_name("controls")
EC.visibility_of_element_located(element)



driver.find_element_by_id("register_email").send_keys("szq@qq.com")

user_name_element_node = driver.find_elements_by_class_name("controls")[1]
user_name_element = user_name_element_node.find_element_by_class_name("form-control")
user_name_element.send_keys("szq")

driver.find_element_by_name("password").send_keys("111111")
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("1234")

#driver.close()