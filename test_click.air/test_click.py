# -*- encoding=utf8 -*-
__author__ = "hulu"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android import adb
poco=AndroidUiautomationPoco(use_airtest_input=True,screenshot_each_action=False)
size = poco.get_screen_size()
# size2 = device.get_current_resolution()
print(size)
x = size[0]
y = size[1]

# position = poco(text="").get_position()
# poco(text="").click()

# offspring 遍历父级下面的元素，知道找到
# position = poco(name="__next").offspring("android.view.View")[9].get_position() #  [2].get_position()
# position = poco(name="__next").child().child()[10].get_position() #  [2].get_position()
# position = poco(text="立即抢购").get_position()
position=poco("myDomScroll").child()[9].child().child().child().get_position()


print(position)
# position = [x*position[0],y*position[1]]
# touch(position)









