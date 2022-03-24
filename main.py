import json
import random

import mail
import requests

temperature = ["36\"C~36.5°C", "36.5°C~36.9°C"]

useragentlist = [
    "Mozilla/5.0 (Linux; U; Android 7.1.2; zh-cn; MI 6 Build/NXTHUAWEI) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/9.9 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 baiduboxapp/0_01.5.2.8_enohpi_6311_046/5.3.9_1C2%8enohPi/1099a/7D4BD508A31C4692ACC31489A6AA6FAA3D5694CC7OCARCEMSHG/1",
    "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; vivo X5Max Build/KTU84P) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/1.0.0.100 U3/0.8.0 Mobile Safari/534.30 AliApp(TB/6.5.0) WindVane/8.0.0 1080X1920 GCanvas/1.4.2.21",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92 baiduboxapp/0_01.5.2.8_enohpi_8022_2421/2.01_2C2%8enohPi/1099a/05D5623EBB692D46C9C9659B23D68FBD5C7FEB228ORMNJBQOHM/1",
    "Mozilla/5.0 (Linux; Android 8.0.0; BKL-AL00 Build/HUAWEIBKL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.0.0)",
    "Mozilla/5.0 (Linux; Android 8.1.0; vivo X20 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 8.1.0)",
    "Mozilla/5.0 (Linux; Android 9; DUK-AL20 Build/HUAWEIDUK-AL20; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/11.19 SP-engine/2.15.0 baiduboxapp/11.19.5.10 (Baidu; P1 9)"
]


def request_sessionId(json_data):
    url = "https://yjsxx.whut.edu.cn/wx/api/login/checkBind"
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",

        "Referer": "https://servicewechat.com/wx225eb50c34f6f98e/13/page-frame.html",
        "X-Tag": "flyio",
        "Content-Length": "100",
        "Accept-Language": "zh-cn",
        "Connection": "keep - alive",
        "Host": "yjsxx.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    r = requests.post(url=url, headers=headers, json=json_data)
    print(r)
    result = json.loads(r.text)
    print("request_sessionId", result)
    sessionId = result['data']['sessionId']
    f = open("sessionId.txt",'a')
    f.write("\n")
    f.write(sessionId)
    f.close()
    return str(sessionId)


def request_bindUserInfo(sessionId, json_data):
    url = "https://yjsxx.whut.edu.cn/wx/api/login/bindUserInfo"
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wx225eb50c34f6f98e/13/page-frame.html",
        "Cookie": "JSESSIONID=%s" % (sessionId),
        "Accept": "*/*",
        "X-Tag": "flyio",
        "Content-Length": "2",
        "Accept-Language": "zh-cn",
        "Connection": "keep - alive",
        "Host": "yjsxx.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    print(json_data)
    r = requests.post(url=url, headers=headers, json=json_data)
    result = json.loads(r.text)
    print("request_bindUserInfo", result)


def request_monitorRegister(sessionId, province, city, county, street):
    currentAddress = str(province) + str(city) + str(county) + str(street)
    url = "https://yjsxx.whut.edu.cn/wx/./monitorRegister"
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wx225eb50c34f6f98e/13/page-frame.html",
        "Cookie": "JSESSIONID=%s" % (sessionId),
        "Accept": "*/*",
        "X-Tag": "flyio",
        "Content-Length": "203",
        "Accept-Language": "zh-cn",
        "Connection": "keep - alive",
        "Host": "yjsxx.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    json_data = {
        "diagnosisName": "",
        "relationWithOwn": "",
        "currentAddress": currentAddress,
        "remark": "无",
        "healthInfo": "正常",
        "isDiagnosis": 0,
        "isFever": 0,
        "isInSchool": "0",  # 如果在学校，修改为1
        "isLeaveChengdu": 0,
        "isSymptom": "0",
        "temperature": random.choice(temperature),
        "province": province,
        "city": city,
        "county": county
    }
    r = requests.post(url=url, headers=headers, json=json_data)
    result = json.loads(r.text)
    print("request_monitorRegister", result)
    return result


def cancelBind(sessionId):
    url = "https://yjsxx.whut.edu.cn/wx/api/login/cancelBind"
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wx225eb50c34f6f98e/13/page-frame.html",
        "Cookie": "JSESSIONID=%s" % (sessionId),
        "Connection": "keep - alive",
        "Host": "yjsxx.whut.edu.cn"
    }
    headers['User-Agent'] = random.choice(useragentlist)
    r = requests.post(url=url, headers=headers)
    result = json.loads(r.text)
    print("cancelBind", result)


if __name__ == '__main__':
    data = {'sn': '修改为学号', 'idCard': '修改为身份证后六位'}
    sessionId = request_sessionId(data)
    request_bindUserInfo(sessionId, data)
    res = request_monitorRegister(sessionId, "湖北省", "武汉市", "洪山区", "工大路")
    if res['code'] == 0:
       mail.sendmail(["success", "今日打卡成功"])
    else:
       mail.sendmail(["error", res['message']])
    cancelBind(sessionId)
