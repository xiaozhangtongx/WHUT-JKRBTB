import yagmail


def sendmail(data):
    try:
        yag = yagmail.SMTP(user='jeremyheung@qq.com', password='phnaacsytkovddea', host='smtp.qq.com')
        yag.send(to='改为自己的邮箱', subject='健康打卡', contents=data)
        print('Email send success')
    except:
        print('Email send fail')
