#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 21:50
# @Author  : Liz
# @File    : basics.py

import uiautomator2 as u2
import time,os
from appium import webdriver
'''
华为 p30    8KE5T19C26000133
华为 mate7  5LM0215C28005351
vivo x21    ea6e291e
'''
#import sys
#sys.path.append('E:\\python\\Lib\\site-packages\\uiautomator2')
rolltimes = 200

class P30(object):

    def init(self):
        self.d = u2.connect('8KE5T19C26000133')
        #self.d = u2.connect('ea6e291e')
    #     cap = {
    #        'deviceName':' 8KE5T19C26000133',
    #        ' platformName': 'Android',
    #         'platformVersion': '10',
    #         'appPackage':' com.duowan.mobile',
    #         'appActivity': 'com.yy.mobile.plugin.homepage.ui.home.HomeActivity',
    #         'noReset': True
    # }
    #     d = webdriver.Remote('http://127.0.0.1:4723/wd/hub',cap)

    def in_out(self):
        # 进出直播间1000次
        for j in range(1, 200):
            time.sleep(0.5)
            # 点击进入直播间
            if j % 2 != 0:  # 分左右两边点击
                self.d.click(0.239, 0.238)

            #elif j % 2 ==0:
                #self.d.click(0.742, 0.256)
            time.sleep(0.5)
            if self.d(resourceId="com.yy.mobile.plugin.main:id/phoneNumLoginNumberTv").exists:  # 如果未登录进某些直播间会弹登录框，关掉
                self.d(resourceId="com.yy.mobile.plugin.main:id/closeLoginBtn").click()
                time.sleep(0.5)
                # d(resourceId="com.yy.mobile.plugin.livebasebiz:id/btn_exit_layout").click()
            else:
                # 设置元素查找等待时间
                # d.implicitly_wait(5.0)
                self.d.press("back")
                # time.sleep(0.5)
                if self.d(text="狠心退出").exists:  # 首次退出直播间会有个关注离开的弹窗
                    self.d(text="狠心退出").click()
            #if j % 2 == 0:
                #self.d.swipe(0.825, 0.377,0.789, 0.181)
            print("***执行到第{0}次***".format(j))

    def up_down_live(self):
        for roll in range(1,rolltimes):
            self.d.swipe(0.565, 0.714,0.557, 0.243)
            data = time.strftime('%H:%M:%S', time.localtime())
            print(f"{data} 第{roll}次执行")

    def up_down_video(self):
        for roll in range(1,rolltimes):
            self.d.swipe(0.606, 0.507,0.614, 0.341)
            time.sleep(0.5)
            data = time.strftime('%H:%M:%S', time.localtime())
            print(f"{data} 第{roll}次执行")


class Vivo_Y73S(object):

    def init(self):
        self.d = u2.connect('NRUWX48HHIKFW4KF')

    def in_out(self):

        for j in range(1,200):
            time.sleep(0.5)
            # 点击进入直播间
            if j % 2 == 0:  # 分左右两边点击
                self.d.click(0.262, 0.504)

            else:
                self.d.click(0.773, 0.507)
            time.sleep(0.5)
            if  self.d(resourceId="com.yy.mobile.plugin.main:id/phoneNumLoginNumberTv").exists:  # 如果未登录进某些直播间会弹登录框，关掉
                self.d(resourceId="com.yy.mobile.plugin.main:id/closeLoginBtn").click()
                time.sleep(0.5)
                # d(resourceId="com.yy.mobile.plugin.livebasebiz:id/btn_exit_layout").click()
            else:
                # 设置元素查找等待时间
                # d.implicitly_wait(5.0)
                self.d.press("back")
                # time.sleep(0.5)
                if  self.d(text="狠心退出").exists:  # 首次退出直播间会有个关注离开的弹窗
                    self.d(text="狠心退出").click()
            if j % 2==0:
                self.d.swipe(0.756, 0.539, 0.754, 0.241)
            print("***执行到第{0}次***".format(j))


    def up_down_live(self):
        for roll in range(1,rolltimes):
            self.d.swipe(0.73, 0.681,0.681, 0.148)
            time.sleep(0.3)
            data = time.strftime('%H:%M:%S', time.localtime())
            print(f"{data} 第{roll}次执行")



    def up_down_video(self):
        for roll in range(1,rolltimes):
            self.d.swipe(0.45, 0.661, 0.468, 0.344)
            time.sleep(0.5)
            data = time.strftime('%H:%M:%S', time.localtime())
            print(f"{data} 第{roll}次执行")




d2 = Vivo_Y73S()
d2.init()
d2.up_down_live()
