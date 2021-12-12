import yagmail


def sendmail(data):
    try:
        yag = yagmail.SMTP(user='256037838@qq.com', password='axauuihsfdspcadd', host='smtp.qq.com')
        yag.send(to='你的邮箱', subject='健康打卡', contents=data)
        print('Email send success')
    except:
        print('Email send fail')
