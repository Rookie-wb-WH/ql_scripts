'''
ikuuu + v2free

v2free注册地址: https://w1.v2free.top/auth/register?code=O9dv
ikuuu注册地址: https://ikuuu.art/auth/register?code=OlHp

两个的用户名和密码都请设置一致的 不一致的话请自行修改代码

变量配置: 
export jcuname='username'
export jcpasswd='password'

'''

import requests, json, os, random,urllib3
from notify import send
import urllib3

# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 发起请求时忽略证书验证警告
requests.packages.urllib3.disable_warnings()

# 发起请求
response = requests.get('https://example.com', verify=False)



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
    print('v2free' + content)
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
    print('ikuuu' + content)
    send('ikuuu', content)

if __name__ == "__main__":
    session = requests.session()
    # ikuuu用户名
    EMAIL = os.getenv('jcuname')
    # ikuuu密码
    PASSWD = os.getenv('jcpasswd')
    v2checkin()
    checkin()
    
