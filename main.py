# -*- coding: utf8 -*-
import json
from urllib import parse
import requests
import datetime
def main_handler(event, context):
    main()


def get_position(eachvalue, position, start, end):
    sites = {1: "c7a1e6c77abb48c8b79e5da2bed939c7",
             2: "",
             3: "e47431fbfd524876a03a1c5507d85beb",
             4: "9090387ea7b04591a73b1059114c0ab9",
             5: "ac85e1a930464d0d8e30f129b661cfea", }
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(day)
    position = sites[position]
    # start_time = day+" "+start+":00"
    # end_time = day+" "+end+":00"
    each_value = eachvalue
    gap = end-start
    detail_list = []
    for i in range(gap):
        start_time = day+" "+str(start+i)+":00"
        end_time = day+" "+str(start+i+1)+":00"
        detail = {"venueId": position, "price": each_value, "siteCount": 1,
                  "bookingType": 1, "startDateTime": start_time, "endDateTime": end_time,
                  "payable": each_value, "payment": each_value}
        detail_list.append(detail)
    print(detail_list)
    # detail_list = [{"venueId": position, "price": each_value, "siteCount": 1,
    #                 "bookingType": 1, "startDateTime": start_time, "endDateTime": end_time,
    #                 "payable": each_value, "payment": each_value}]
    total_Amount = payable = payment = each_value*len(detail_list)
    data = {"mainId": "09bcd2404fcb4af9951b38f03c2837db", "sportsType": "YuMaoQiu", "identity": "student", "billDateTime": time_now, "totalAmount": total_Amount, "payable": payable, "payment": payment,
            "detailedList": detail_list}
    print(data)
    order_booking(data)
    pass


def order_booking(data):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjA5YmNkMjQwNGZjYjRhZjk5NTFiMzhmMDNjMjgzN2RiIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6IuWPtuWuh-a2myIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjE2NTA0NDM4MTYiLCJyZWZyZXNoX3RpbWUiOiIxNjUwMjI3ODE2IiwianRpIjoiMDliY2QyNDA0ZmNiNGFmOTk1MWIzOGYwM2MyODM3ZGIiLCJBcHBfUGVybWlzc2lvbnMiOiJBcHAiLCJuYmYiOjE2NTAwMTE4MTYsImV4cCI6MTY1MDQ0MzgxNiwiaXNzIjoic2VpbiIsImF1ZCI6InNlaW4ifQ.wXjiwePZzQX1dBRu2ZzhuiGXkTJ0l_YdPsu70DvDiww',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wxb9a7dd05206565ec/8/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    url = 'https://wltyzx.cug.edu.cn/api/app/WeixinOrder/CreateOrder'
    r = requests.post(url, json=data, headers=headers, verify=False)
    print(r.text)
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
    get_position(20, 1, 18, 19)
