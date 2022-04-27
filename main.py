# -*- coding: utf8 -*-
import json
from urllib import parse
import requests
import datetime
import time
import urllib3

urllib3.disable_warnings()


def main_handler(event, context):
    main()


def send(text):
    pass
    # data = parse.urlencode({'text': text}).encode()
    # headers = {
    #     'Content-Type': 'application/x-www-form-urlencoded',
    #     'Content-Length': str(len(data))
    # }
    # url = "https://api.chanify.net/v1/sender/CICtqJYGEiJBQUxHVDJSS0hEMkJLQlFEQTZOS1dWVkRRWVc3TUNQR1lVIgYIAhoCd3U.JDPlA8aUcFYKYz2vnZNxgGKxzaf1fuDzR_jRalVsdzk"
    # req = requests.post(headers=headers, url=url, data=data)

def get_position(eachvalue, positions, start, end,token,mainid):
    send("开始预约")
    sites = {1: "c7a1e6c77abb48c8b79e5da2bed939c7",
             2: "cc44395619064a2183e06105074a6b02",
             3: "e47431fbfd524876a03a1c5507d85beb",
             4: "9090387ea7b04591a73b1059114c0ab9",
             5: "282cd0b4130949838b7061722e840b56",
             6: "ac85e1a930464d0d8e30f129b661cfea",
             7: "10715133add844669aa2b238791dc65b",
             8: "dd5f9b38bfb645c6a1c7ba1e22d26321",
             9: "a48298dc3c3242c58af5b9c31d0d4795",
             10: "2d3182fed841487caa4b62c677bf8f33",
             11: '7f82a4d546e94a8b9719206a61be842b',
             12: '5e7169c8e2eb49cc9fb4346f4b8c8837',
             13: 'fb82bf61e55a41678942b3675f9c9999',
             14: 'b799f9371f1b4c52ba12ac9faa34c251',
             15: 'ddf1c4bd7a9e41c398f4899b23c94e7c',
             16: '0f2dd393890e4f008122a387bdce7c08',
             17: '648ff49e90ac4c85b729e3eb5a1db7ab',
             18: '48fef4c93cb440748bbd9347ab0dec0f',
             19: '6fc850fca0a146c6b20c7f6ef46a05d7',
             }
    day = (datetime.datetime.now() +
           datetime.timedelta(hours=8)).strftime('%Y-%m-%d')
    time_now = (datetime.datetime.now() + datetime.timedelta(hours=8)
                ).strftime('%Y-%m-%d %H:%M:%S')
    print(time_now)
    print(day)
    # position = sites[position]
    # start_time = day+" "+start+":00"
    # end_time = day+" "+end+":00"
    each_value = eachvalue
    gap = end - start
    detail_list = []
    for i in range(gap):
        for j in range(len(positions)):
            start_time = day + " " + str(start + i) + ":00"
            end_time = day + " " + str(start + i + 1) + ":00"
            position = sites[positions[j]]
            detail = {"venueId": position, "price": each_value, "siteCount": 1,
                      "bookingType": 1, "startDateTime": start_time, "endDateTime": end_time,
                      "payable": each_value, "payment": each_value}
            detail_list.append(detail)
    # detail_list = [{"venueId": position, "price": each_value, "siteCount": 1,
    #                 "bookingType": 1, "startDateTime": start_time, "endDateTime": end_time,
    #                 "payable": each_value, "payment": each_value}]
    total_Amount = payable = payment = each_value*len(detail_list)
    data = {"mainId": mainid, "sportsType": "YuMaoQiu", "identity": "student", "billDateTime": time_now, "totalAmount": total_Amount, "payable": payable, "payment": payment,
            "detailedList": detail_list}
    # start_post_time = datetime.datetime(2022, 4, 18, 14, 24, 0).time()
    end_post_time = datetime.datetime(2022, 4, 18, 7, 0, 59).time()
    # print("start_post_time:", start_post_time)
    print("end_post_time:", end_post_time)
    count = 0
    while True:
        hour = (datetime.datetime.now()+datetime.timedelta(hours=8)).time()
        print("post----------")
        print("hour:", hour)
        order_booking(data,token)
        count += 1
        print("count:", count)
        if hour >= end_post_time or count > 250:
            print('end------------')
            break

    pass


def order_booking(data,token):
    start = time.time()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type': 'application/json',
        'Authorization': token,
        'Referer': 'https://servicewechat.com/wxb9a7dd05206565ec/8/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    url = 'https://wltyzx.cug.edu.cn/api/app/WeixinOrder/CreateOrder'
    r = requests.session().post(url, json=data, headers=headers, verify=False)
    print("posttime:", time.time() - start)
    print(r.text)
    if("成功" in r.text):

        send("成功预约！")
    r = r.json()
    data = r['data']
    url1 = 'https://wltyzx.cug.edu.cn/api/app/WeixinOrder/GetUnpaidOrderInfo/' + \
           str(data)
    url2 = 'https://wltyzx.cug.edu.cn/api/app/WeixinOrder/GetMemberPaymentType/' + \
           str(data)
    r1 = requests.get(url1, headers=headers, verify=False)
    r2 = requests.get(url2, headers=headers, verify=False)
    print(r1.text)
    print(r2.text)


def main():
    start = time.time()
    value = 10
    start_time = 19
    end_time = 22
    position = [5]
    mainid = "填写你的mainid"
    token = '填写你的token'
    get_position(value, position, start_time, end_time,token,mainid)
    print("totaltime:", time.time()-start)


main()

