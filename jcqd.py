'''
ikuuu + v2free

v2free注册地址: https://w1.v2free.top/auth/register?code=O9dv
ikuuu注册地址: https://ikuuu.art/auth/register?code=OlHp

两个的用户名和密码都请设置一致的 不一致的话请自行修改代码

变量配置: 
export jcuname='username'
export jcpasswd='password'

需要安装 lxml 依赖: 
    1.进入容器pip install lxml
    2.青龙面板 -> 依赖管理 -> python -> lxml
'''

import requests, json, os, random,urllib3
from lxml import etree
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

def get_ik_domain():
    url = 'https://ikuuu.club/'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=header)
    if res.status_code == 200:
        textname = etree.HTML(res.text)
        links = textname.xpath('//a/@href')
        return links
    else:
        print('ikuuu获取签到域名失败!')
        exit(1)

def checkin():
    url = random.choice(get_ik_domain())
    print('当前签到选择的域名是: ====>  {}'.format(url))
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
    
