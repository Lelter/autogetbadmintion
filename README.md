# 微信小程序：地大体育的预约工具，提供羽毛球场地1-8号场地预约。  

可在服务器上部署，每天7点自动抢场地，采用暴力post方式确保抢到。  

如果抢到场地，将发送至channify提示成功预约。  

---
## 使用方法：

1.利用fiddler抓取返回头部的mainId和请求头部中的Token。 

2.设置参数，几号场地，从几点到几点。

3.放置在服务器上，定时七点启动，默认抢250次，大约90秒。   

---
## 示例
**如果需要在早上7点抢19点至22点场，参数设置如下：**

    value = 10 #表示每个场地所用价钱，在周六日为20 
    start_time = 19 #表示开始时间
    end_time = 22 #表示结束时间
    position = [5] #表示场地，默认为5号，最多约240分钟
    mainid=''#输入在fiddler中抓取的mainid
    token=''#输入在fiddler中抓取的token  
**fiddler使用方法：**  
打开电脑端微信小程序，打开fiddler，登录进入地大体育。  
预约一个场地，查看抓包获得的请求头和返回头中的mainid和token。 
![token](.\Snipaste_2022-04-21_11-18-12.png)
token在Security中的Authorization。  
mainid位于抓包中的如下地址的最后一个后缀：
https://wltyzx.cug.edu.cn/api/app/WeixinReserve/GetFieldArea/YuMaoQiu/student/09b233333333  
其中，09b开头的信息就是我的mainid，每个人都不一样，我的已打码。  
抓完包之后，就可以部署在云服务器或者腾讯云函数上使用了.   
**channify使用方法**  
可用可不用。不用把send()函数注释掉就行。

---
## 遇到问题
1.token会过期，大约一周时间，每次都需要重新抓取，比较麻烦，目前无解，需要手动更新。  