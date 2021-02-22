# -*- encoding=utf8 -*-
__author__ = "hulu"

from airtest.core.api import *

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android import adb
device = connect_device('Android://127.0.0.1:5037/88Y5T19C26013755')
# device = connect_device('Android://127.0.0.1:5037/MQS0219909005465')
poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
size = poco.get_screen_size()
device.unlock()
# size2 = device.get_current_resolution()
x = size[0]
y = size[1]
keyevent("KEYCODE_HOME")
device.shell("am force-stop ctrip.android.view")
pkg_list = shell("pm list packages")
if "ctrip.android.view" in str(pkg_list):
    print("已安装携程")
    start_app("ctrip.android.view" )
    print("打开APP成功")
else:
    print("未安装携程")
print("打开美食林成功")
sleep(6)
# position=poco("ctrip.android.publicproduct:id/home_tab_bar_icon_iv")[1].get_position()
# # print(position)
# position = [x*position[0],y*position[1]]
# touch(position)
# sleep(3)
position_food=poco("ctrip.android.publicproduct:id/home_index_food").get_position()
position_food = [x*position_food[0], y*position_food[1]]
touch(position_food)
