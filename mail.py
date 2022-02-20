import yagmail


def sendmail(data):
    try:
        yag = yagmail.SMTP(user='你的一个用于发送邮件的工具邮箱', password='工具邮箱密码', host='smtp.qq.com')
        yag.send(to='你的邮箱', subject='健康打卡', contents=data)
        print('Email send success')
    except:
        print('Email send fail')
