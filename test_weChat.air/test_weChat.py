# -*- encoding=utf8 -*-
__author__ = "hulu"
from multiprocessing import Process
from airtest.core.api import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android import adb
def action1():
    device = connect_device('Android://127.0.0.1:5037/3EP7N18B16035167')
    poco=AndroidUiautomationPoco(use_airtest_input=True,screenshot_each_action=False)
    size = poco.get_screen_size()
    x = size[0]
    y = size[1]
    keyevent("KEYCODE_HOME")
    device.shell("am force-stop com.tencent.mm")
    pkg_list = shell("pm list packages")
    if "com.tencent.mm" in str(pkg_list):
        print("已安装微信")
        start_app("com.tencent.mm")
        print("打开APP成功")
    else:
        print("未安装微信")
    sleep(20)
    touch(Template(r"tpl1579071596755.png", record_pos=(-0.422, -0.781), resolution=(1440, 3120)))


    touch(Template(r"tpl1579062543075.png", record_pos=(0.142, 0.492), resolution=(1440, 3120)))
    touch(Template(r"tpl1579062693000.png", record_pos=(0.082, 0.069), resolution=(1440, 3120)))
    touch(Template(r"tpl1579062887728.png", record_pos=(-0.122, -0.198), resolution=(1440, 3120)))


    touch(Template(r"tpl1579062753662.png", record_pos=(-0.251, 0.198), resolution=(1440, 3120)))
    sleep(2)
    swipe((0.5*x,0.6*y),(0.5*x,0.3*y),duration=0.2)
    sleep(2)
    device.shell("/system/bin/screencap -p /sdcard/screenshot1.png")
    swipe((0.9*x,0.3*y),(0.42*x,0.3*y),duration=0.2)
    sleep(2)
    device.shell("/system/bin/screencap -p /sdcard/screenshot2.png")
    swipe((0.9*x,0.3*y),(0.42*x,0.3*y),duration=0.2)
    sleep(2)
    device.shell("/system/bin/screencap -p /sdcard/screenshot3.png")


    
action1()

os.system(r"del D:\Users\hulu\PycharmProjects\my_airtest\pic\screenshot1.png")
os.system(r"del D:\Users\hulu\PycharmProjects\my_airtest\pic\screenshot2.png")
os.system(r"del D:\Users\hulu\PycharmProjects\my_airtest\pic\screenshot3.png")
#     adb.ADB.pull('/sdcard/screenshot1.png','D:\Users\hulu\PycharmProjects\my_airtest\pic\screenshot1.png')
os.system(r"adb pull /sdcard/screenshot1.png D:\Users\hulu\PycharmProjects\my_airtest\pic\screenshot1.png")
os.system(r"adb pull /sdcard/screenshot2.png D:\Users\hulu\PycharmProjects\my_airtest\pic\screenshot2.png")
os.system(r"adb pull /sdcard/screenshot3.png D:\Users\hulu\PycharmProjects\my_airtest\pic\screenshot3.png")


