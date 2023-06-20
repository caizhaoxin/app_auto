# -*- encoding=utf8 -*-
__author__ = "HP"

from airtest.core.api import *
import os
import random

auto_setup(__file__)

# 获取设备的高度和宽度
width, height = device().get_current_resolution()
# 校准滑动的起点和终点
start_pt = (width * 0.9, height / 2)
end_pt = (width * 0.1, height / 2)


def slide():
    swipe((1014, 1279), (1014, -500), duration=0.03)


def run():
    main_botton_tab = [[934, 62], [60, 510], [108, 165], [614, 244], [494, 759]]
    i = random.randint(0, 6)
    if i < 5:
        touch(main_botton_tab[i])
    elif i == 5:
        slide()
    else:
        swipe(start_pt, end_pt)
    sleep(2)


# 运行一个app
def run_app(app, i):
    stop_app(app)
    start_app(app)
    sleep(8)
    print(shell("mkdir -p " + filePath + app + "/"))
    for j in range(50):
        filename = str(i) + "_" + str(j)
        run()
        s = None
        s = (shell("uiautomator dump " + filePath + app + "/" + filename + ".xml"))
        while s is None:
            sleep(5)

        print(shell("screencap -p " + filePath + app + "/" + filename + ".png"))


# 所有数据存放手机存储卡的111文件夹下，可更改
filePath = "/sdcard/111/"
print(shell("mkdir -p " + filePath))

# app列表
app_list = ['com.sup.android.superb', 'com.tencent.mtt', 'com.sohu.sohuvideo', 'com.ss.android.auto',
            'com.ximalaya.ting.android', 'com.zhihu.android', 'com.qiyi.video.lite', 'com.dragon.read', 'com.xs.fm',
            'com.jingdong.app.mall', 'com.kmxs.reader', 'com.smile.gifmaker', 'com.fenbi.android.solar',
            'com.greenpoint.android.mc10086.activity', 'com.ss.android.article.video', 'com.achievo.vipshop',
            'com.kuaishou.nebula']
# 逐一运行app
for i in range(3):
    for app in app_list:
        run_app(app, i)
        sleep(2)
        stop_app(app)

# 将数据从收集移到电脑的文件夹
os.system("adb pull /sdcard/111 E:/test")
