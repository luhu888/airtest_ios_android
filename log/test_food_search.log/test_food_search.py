# -*- encoding=utf8 -*-
__author__ = "hulu"

from airtest.core.api import *

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android import adb
device = connect_device('Android://127.0.0.1:5037/3EP7N18B16035167')
# device = connect_device('Android://127.0.0.1:5037/MQS0219909005465')
poco=AndroidUiautomationPoco(use_airtest_input=True,screenshot_each_action=False)
# size = poco.get_screen_size()
# x = size[0]
# y = size[1]
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
sleep(5)
poco("ctrip.android.publicproduct:id/home_tab_bar_icon_iv").click() # 找到待测商品名称对应的元素
# print([i for i in item_text_obj])

# poco(type='android.widget.ImageView',name='ctrip.android.publicproduct:id/home_tab_bar_icon_iv').click()


# touch(Template(r"tpl1613812838293.png", record_pos=(-0.281, 0.472), resolution=(1440, 3120)))




