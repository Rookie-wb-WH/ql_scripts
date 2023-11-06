'''
ikuuu + v2free + gw树洞

v2free注册地址: https://w1.v2free.top/auth/register?code=O9dv
ikuuu注册地址: https://ikuuu.art/auth/register?code=OlHp
gw树洞注册地址: https://kkone.io/auth/register?code=4fMxiN

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



def v2checkin():
    print('==========[当前正在进行v2free签到]==========')
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
    try:
        res = requests.get(url, headers=header)
        if res.status_code == 200:
            textname = etree.HTML(res.text)
            links = textname.xpath('//a/@href')
            return links
        else:
            print('ikuuu获取签到域名失败!')
            exit(1)
    except Exception as e:
        print(e)

def checkin():
    print('==========[当前正在进行ikuuu签到]==========')
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

def sign_in(email, passwd):
    print('==========[当前正在进行gw树洞签到]==========')
    body = {"email" : email,"passwd" : passwd,}
    headers = {'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    resp = requests.session()
    resp.post(f'https://kkone.io/auth/login', headers=headers, data=body, verify=False)
    ss = resp.post(f'https://kkone.io/user/checkin').json()
    if 'msg' in ss:
        print(ss['msg'])
        print('gw树洞' + ss['msg'])
        send('gw树洞', ss['msg'])

if __name__ == "__main__":
    session = requests.session()
    # ikuuu用户名
    EMAIL = os.getenv('jcuname')
    # ikuuu密码
    PASSWD = os.getenv('jcpasswd')
    # v2Free
    v2checkin()
    # ikuuu
    checkin()
    # gw树洞
    sign_in(EMAIL, PASSWD)
