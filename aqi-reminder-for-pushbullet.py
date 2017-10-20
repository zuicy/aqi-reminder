#!/user/bin/python
# -*- coding: utf-8 -*


import requests
import json
import demjson
from pushbullet import Pushbullet

r = requests.get('http://www.pm25.in/api/querys/only_aqi.json?city=your_city&token=your_appkey',timeout=5)
#把上面的your_appkey替换为你的appkey,上面的your_city替换为你要选择的城市

s = json.loads(r.text)


a = s[0][ u'aqi']

accesstoken='your_accesstoken'
#将上面的your_accesstoken替换为你的accesstoken

if a<50:
    pb = Pushbullet(accesstoken)
    push = pb.push_note("冻死自己（误", "空气质量不错，开窗通风吧")
#可以自定义自己想想说的话（当空气质量好时），按照push = pb.push_note("这里填标题", "这里输入内容")修改上面
if a>150:
    pb = Pushbullet(accesstoken)
    push = pb.push_note("暴力膜拯救自己", "空气质量很糟糕， 快关窗户为自己续一秒！")
#可以自定义自己想想说的话（当空气质量差时），按照push = pb.push_note("这里填标题", "这里输入内容")修改上面

print u'正常结束'

