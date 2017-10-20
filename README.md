# aqi-reminder-for-pushbullet
## 介绍
一个可以根据你当前所在城市的AQI值来向你的pushbullet上推送提醒的脚本。基于python2.6。
##前提
要想使用，你必须  
1.申请一个你自己的[appkey](http://pm25.in/api_doc)  
2.确保你已经安装[requests](https://pypi.python.org/pypi/requests/2.7.0)  
3.确保你已经安装[pushbullet.py](https://pypi.python.org/pypi/pushbullet.py)  
4.取得自己pushbullet的[access tokens](https://www.pushbullet.com/)
##下载
```git clone https://github.com/zuicy/aqi-reminder-for-pushbullet.git```  
##配置
######由于本人很懒，代码很短，所以没有将所有要修改的内容放在开头，带来的不便（你来打我啊，逃
在下载的文件中找到**aqi-reminder-for-pushbullet.py**进行编辑  
###修改appkey，选择你所在的城市
```r = requests.get('http://www.pm25.in/api/querys/only_aqi.json?city=your_city&token=your_appkey',timeout=5)```  
在文档中把上面的**your_appkey**替换为你的**appkey**,上面的**your_city**替换为你要选择的城市
####城市规则：
请使用城市的**拼音**  
例如： "city=guangzhou"  
**重名情况**：泰州的拼音为"taizhoushi"，台州的拼音为"taizhou"
###修改access tokens
```accesstoken='your_accesstoken'```  
在文档中将上面的**your_accesstoken**替换为你的**accesstoken**
###自定义推文
下面的为默认推文  
`push = pb.push_note("冻死自己（误", "空气质量不错，开窗通风吧")`  
`push = pb.push_note("暴力膜拯救自己", "空气质量很糟糕， 快关窗户为自己续一秒！")`  
可以自定义自己想想说的话，在文档中按照**push = pb.push_note("这里填标题", "这里输入内容")**修改上面
##测试
我们应该先测试一下以防出现未知的错误，使用python运行一下到**aqi-reminder-for-pushbullet.py**吧。  
如果输出**’正常结束‘**，那么恭喜你，你马上就能使用上aqi-reminder-for-pushbullet了。  
如果程序报错，**请检查配置是否正确或重新下载**（别想了，不会有常见错误解析的

##设置定时任务
最后一步，设置定时任务来使程序定时执行。  
如果你用的是Linux系统，我推荐你使用cronjob。  
不会使用？[教程](https://linux.cn/article-4924-1.html)接好。
##完成，好好享受吧
##意见与反馈
**人生处女座，要是将来出现了偏差，我是不会负泽任的。**  
**但还是欢迎向我提出各种建议，邮箱：zuicy@foxmail.com**
##感谢
1.pm2.5提供的数据  
2.request开发者  
3.pushbullet.py开发者
