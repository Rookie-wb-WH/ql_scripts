'''
ikuuu机场签到

变量配置: 
export ikusername='username'
export ikpassword='password'

'''


import requests, json, re, os, random
from notify import send


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
    EMAIL = os.environ.get('ikusername')
    # ikuuu密码
    PASSWD = os.environ.get('ikpassword')
    checkin()