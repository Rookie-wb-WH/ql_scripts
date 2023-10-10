'''
ikuuu + v2free

v2free注册地址: https://w1.v2free.top/auth/register?code=O9dv
ikuuu注册地址: https://ikuuu.art/auth/register?code=OlHp

两个的用户名和密码都请设置一致的 不一致的话请自行修改代码

变量配置: 
export jcuname='username'
export jcpasswd='password'

'''


import requests, json, re, os, random
from notify import send

def v2checkin():
    url = 'https://w1.v2free.top'
    login_url = '{}/auth/login'.format(url)
    check_url = '{}/user/checkin'.format(url)
    header = {
        'origin': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    data = {
        'email': EMAIL,
        'passwd': PASSWD
    }
    response = json.loads(session.post(url=login_url, headers=header, data=data, verify=False).text)
    # 进行签到
    result = json.loads(session.post(url=check_url, headers=header, verify=False).text)
    content = result['msg']
    send('v2free', content)


def checkin():
    url = random.choice(['https://ikuuu.art/', 'https://ikuuu.uk/'])
    login_url = '{}/auth/login'.format(url)
    check_url = '{}/user/checkin'.format(url)
    header = {
        'origin': url,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    data = {
        'email': EMAIL,
        'passwd': PASSWD
    }
    response = json.loads(session.post(url=login_url, headers=header, data=data).text)
    # 进行签到
    result = json.loads(session.post(url=check_url, headers=header).text)
    content = result['msg']
    send('ikuuu签到', content)

if __name__ == "__main__":
    session = requests.session()
    # ikuuu用户名
    EMAIL = os.environ.get('jcuname')
    # ikuuu密码
    PASSWD = os.environ.get('jcpasswd')
    v2checkin()
    checkin()
    