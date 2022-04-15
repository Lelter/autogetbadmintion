import requests
import datetime
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjA5YmNkMjQwNGZjYjRhZjk5NTFiMzhmMDNjMjgzN2RiIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvbmFtZSI6IuWPtuWuh-a2myIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjE2NTA0NDM4MTYiLCJyZWZyZXNoX3RpbWUiOiIxNjUwMjI3ODE2IiwianRpIjoiMDliY2QyNDA0ZmNiNGFmOTk1MWIzOGYwM2MyODM3ZGIiLCJBcHBfUGVybWlzc2lvbnMiOiJBcHAiLCJuYmYiOjE2NTAwMTE4MTYsImV4cCI6MTY1MDQ0MzgxNiwiaXNzIjoic2VpbiIsImF1ZCI6InNlaW4ifQ.wXjiwePZzQX1dBRu2ZzhuiGXkTJ0l_YdPsu70DvDiww',
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wxb9a7dd05206565ec/8/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'
}
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time)
'''
badminton
{"mainId":"09bcd2404fcb4af9951b38f03c2837db","sportsType":"YuMaoQiu","identity":"student","billDateTime":"2022-04-15 17:30:00","totalAmount":10,"payable":10,"payment":10,"detailedList":[{"venueId":"7f82a4d546e94a8b9719206a61be842b","price":10,"siteCount":1,"bookingType":1,"startDateTime":"2022-04-15 18:00","endDateTime":"2022-04-15 19:00","payable":10,"payment":10}]}
3:venueId=e47431fbfd524876a03a1c5507d85beb
4号：venueId=9090387ea7b04591a73b1059114c0ab9
'''
url = 'https://wltyzx.cug.edu.cn/api/app/WeixinOrder/CreateOrder'
data = {"mainId": "09bcd2404fcb4af9951b38f03c2837db", "sportsType": "YuMaoQiu", "identity": "student", "billDateTime": time, "totalAmount": 10, "payable": 10, "payment": 10,
        "detailedList": [{"venueId": "9090387ea7b04591a73b1059114c0ab9", "price": 10, "siteCount": 1, "bookingType": 1, "startDateTime": "2022-04-15 18:00", "endDateTime": "2022-04-15 19:00", "payable": 10, "payment": 10}]}
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
