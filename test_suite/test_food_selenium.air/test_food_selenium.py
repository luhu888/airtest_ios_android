# -*- encoding=utf8 -*-
__author__ = "hulu"

from airtest.core.api import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
options = Options()
options.add_argument(r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
# chrome_options.add_argument('detach=True')
options.add_argument('--no-sandbox')   # 解决DevToolsActivePort文件不存在的报错
# chrome_options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--start-maximized') #指定浏览器分辨率
options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
# options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
# chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
# chromedriver = "C:\Program Files\Python35\Scripts\chromedriver.exe"
driver=webdriver.Chrome(chrome_options=options)  # executable_path驱动路径
driver.set_window_size(411,823)
# driver.get("https://m.ctrip.com/webapp/you/foods/address.html?new=1&ishideheader=true")
driver.get("https://m.ctrip.com")
driver.find_element_by_id('HOMEPAGE_TO_MYCTRIP').click()
# driver.find_element_by_class_name('home-btn').click()
# driver.find_element_by_link_text('账号密码登录').click()
# driver.execute_script("document.getElementsByClassName('nofastclick')[0].value='15856691310';")
# driver.execute_script("document.getElementsByClassName('nofastclick')[1].value='luhu199515lbh';")
# driver.execute_script("document.getElementsByClassName('nofastclick')[2].click()")
driver.get('https://m.ctrip.com/webapp/gourmet/food/homeList/address.html?new=1&isHideNavBar=YES&ishideheader=true&seo=0&from=https%3A%2F%2Fm.ctrip.com%2Fhtml5%2F')
get_food_text="""var a=document.getElementsByClassName('res_name')[0].innerText;
var o = document.body; 
function createDIV(text) 
{ 
var div = document.createElement("div"); 
div.className = 'result';
div.innerHTML = text; 
div.style.zIndex='999999';
o.appendChild(div); 
} 
createDIV(a); """
# assert_equal(result1,result2,msg="%s不等于%s"%(result1,result2))
# doc = driver.find_element_by_class_name('res_name').text
sleep(4)
driver.execute_script(get_food_text)
result1 = driver.find_element_by_class_name('result').text
result2 = '生煎'
click_food = "document.getElementsByClassName('res_name')[0].click()"
driver.execute_script(click_food)
sleep(4)
driver.close()
assert_equal(result1, result2, msg="%s不等于%s"%(result1,result2))


