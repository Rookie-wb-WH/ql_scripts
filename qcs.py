'''
vx小程序 -- 屈臣氏
抓包 mystore-01api.watsonsvip.com.cn 下的 Authorization openId uniionId
多账号使用 @ 分隔 账号之间使用 # 分隔
变量填写： export qcs='Authorization1#openId1#uniionId1@Authorization2#openId2#uniionId2'
cron: 3 3 * * *
'''

import sys
vesion = sys.version.split(' ')[0]
if vesion.split('.')[1] == "10":
    print(f'你当前的python版本为 {vesion},即将运行脚本...')
else:
    print(f'你当前的python版本为 {vesion},运行所需脚本环境为 3.10.x, 即将退出运行脚本...')
    exit(1)
    
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(bz2.decompress(b'BZh91AY&SY>\x06w%\x00\x03e\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe0\x0b\x9f/v\xde\xde\xd4\xef\xb7\xd6\xcf\xb7}\xdaO\xbe\xf79\xf7\xdeKU\xbe\xd6\xbb\xedk\xdd[\xda\xfb}\xde\xfb\xba{w\xcf}\xf3{\xc8S\xc5=OSO\x03F\xa9\xb2z(~\xa9\xe1\xa3B\x9e\nm\x11\xe4\x9bF\xd5<FOD\xf4\xa3\xf41\x0cT\xf5=\xa23B4\x9eQ\xfa\x93\xc9\xe9\x13z\t\xa9\xe9?T\xf20)\xbc\xa6\x9e\x94\xf2dO\xd0\x8c\x89\xb4OQ\xe4OOI\xb2S\xf56SS\xf5<S\xd3S\xd5=\xe85S\x1e\x8c\xa9\xec\xa7\xa9\xe9\xa5\x0e\xa9\xe0$\xfdS\xd3jzFSi\x1f\xa9\x9aS\xf4Fi\x18S\xf4jzS\xf5O)\xfaSj6\x8dM\xb5=M2z\x89\x86\x8d\'\xe8\x13\xd3M\'\xa2\x9e&\x9bF\x86\x88\xc91\xa1<\x8d\x0fT\xd3mS\xfdB=\r1L\xdaS\xc9\xa3L\x93\xc8\xc4Lj\x9eSj{J1=L\xf5OhS\x1bSj6\xa1\xd4\xc9\x8c\x92l\xa7\xa9\xfa\xa6\x1e\xa9\xe4\x9e2OD\xda\x9e\xa6Q\xed4\x1aS\xf4A\x92z\x996SO&\x98\xc2\x9e\xa9\x98\xd4\xf2MG\x86\xa8oP\xccJ~\x8fSM=Q\xe20\x89\xb2\x18\x80\x8d1\xa2\x8c\xf4\x9bT\xf2b\x9f\xa5<\xa3\xcd$\xf2\x9bL\x89\xea~\xa9\x9e\x8a=O\nz\x04\xf2i\xe8\x83\xa9\xea\x19\x1a\x07\x94zL\x81\x9a\x8f)\xe5\x19=\x13@\xd1\x93\xd14c\xd5\x1eSjz\x9b\x1a\ni\x93\xcai\x99G\xa2mO\xd4j1\xa4\xf4\x81\xa1\xa6\x9a3H=M\xa9\xa3\xd4\xf2\x98LC\xd1\x06C@\xd3\xca\x1eSi\xa8\xf54\x06\x8c\x9e\xa7\xa9\xa7\xa84d\x1b$\xc6\xa0\x93\t\xa6i10L\x86\xd3A\x19\xa9\xa6\xd0\'\xa3#M1Cd\xd3&\x86\x89\xa7\x94\xd3j3I\x89\xea\x1e\xa3M=OI\x9a\x8d4\r4\xc2d\xc4b0\xd4\xda51=44\x13F\x99\x1eBmL\x9a4\xc4\xc8\xc8\x18L\x9ai\x9a2\x9a4h\xd0\xaa\xa7\xe8\x02i6\x04\xf5Fd\xd1\x94\xf4I\xe5<\xa7\x88\xc85<\xa7\xb4j\x9e\x91\xe5<\xd2m\x14\xfdS\xd3Q\xedSmS\xf5OQ\xe4x\xa9\xbdQ\xa7\x93Q\xa7\x91\xa4m\xa6\xa9\xb2y4)\xe9<F\x93z\x9e\x94\xf4bba=S\xd2~\x88\x9e\x9a=)\xfaS\xd4\xf2jy=5\x1a\x1amSM=\xa2i=\xa2\x01\xea\x9f\xe2A\x00\x1c,D\x86\xaci\xe1\x02\x80\x00;\x84\x0fw-\xecL0@L\xe8!\x11\x0f\x90\x1a\xae`\xa0\x03g\xefN9\x9bT2I\xd2\x91^\xda!\xd8\x99!\x00\xd5K\xe9CY\xaf\xdap\x84I/\xf0Qow\xa4H\xf4\xfc\x06t\xbcE\xae\xaa1d\xdd\xf0\x1a\xdci\xab\xe8`\x15i\x03\x98\x18\xff>\xb8\x8aB\xabYd\x91\x86\xb7\xe7o\x17\x89\x84\x12\xbd3\xef\xf3\xb5|\xf5\x8aF\xb8_g\x80q<x\x0e\xae\xae\xbe\xd4\x14}X\xa8\x8c\xe2I\x98\x90\xb65\xb7*h\xef\xf9\xcc\x10\x85a\xdc\xfd\x106H\x9b_\xa0\xcd=\x14\xa7\xbe5\xcf\x1ef\x8f\x83\x1e\xd9\xbd\xa8\x19Q\x01\x84\x84\xbc\xfb\xe4\xc1\xe7X\xbb\xdd\xe92R>\xae\x9e\xe4"\xa6\x7f+[\xdc\x8d8U\x8fL\xbb\n\xc5\xba\x13%j\x18Df\x1b\xafI\xc3)i[f\xb3\xc0r\xf7N!eO\xd1p\xae.\x8ch\x9a\x8b\x1d\x9d\xc1\xd9\x8d\x81\x93\xbe,}PH{\x7fu\xfb-\xde\xb3\x10\x87C\xa8\x89,\xebT\xd2\xc7`\xac\xa0\x10i\xcb\xee}4 K\tp\x10\x1fF\xf7\xf2\x98I\x99\xa7ZE\x95\x05\x1ci\x97\xf7&\xdd\\\x08/\x19~\xd9\xe5\x84\x0c\xdc\xb1\xb3\x1f\xc1\xac\x1bj;\x16&\xaa\x0f\x9e\x86\x19\x91v\xce\xadhr\xa9bbJ~\x12\xb1\r\xf0\x7feD\xe2\xc8,\xfd\x81\xce\x05+\xa7\xeev\xa4&\x07j9\xdb\x93\xc6\xef\t\x1bo\xa2\xa6\xa2\x93\xc2Y\xc7\x9fHG\xb5\x89[\x00x\x89\xf6\x06\n\x08\xfe\xd4\x8axL=`V\xec\xd9\xfbZ\xda\x8e\xb7\xbd\x15\x06\\\xcb10\x98/-\xfb\x99\x88\xf0\xb5\xc5\xfb\xcb $4}E\x8f\xe2\xcf\xe9!\xf3pb\xec\x10\xbb\x17\xed\xca\xff^\x89\x99\xc1\xf3Y<\xb6s\xc9\x0f\x10-\xdb\xdfP\xd2JK7V\xa7Z+\xf5A\x16\x17D\xe3j\xde\xa7\x14\xc1D\xaeu\xe3n\xd5\xd0\xb5\xf0\xb1\x84%y\x001\xa8-m\x8fEs\xf1\xc2\xc1"]\n\x18n\xbf(0\xa4\xc8\x90\xc7a-"\n\xaf<\x1d#\xaf\xfa\xdas\x033\xfc\xee-~\xdd\xe0\xc0\xf4\xb3\xab\x9c\xf5TU\xc6\x96U\x91k\xe5 I\x92\xbd(\x998\x86A\xb8a\xc15\x8co:\xfa\xbb\x13\x97K&\x9d\xd3\xaeO\xc8\x97YB4\xbb\xcf\xa5\xf7t\xff\xd7\xddj\xb1\x10v\xf9)W\xb4\x06De\x15\x9b\x92\xeb8m\xe8\x8e\x99kN\xd3ZR\x14\x06\xfe2\x97+\x946J\xa8\xf7\x1d\x0egt\xb3@ur\xa5\xb7\xdb8\r\x11\x04\x9b\x86\x9c\x02~\xe2X"\x9c?\xee9&\x94\xc1\xecKWXE8r,\xecGw\xa7\xb5U\xa2{\xf8\xc2\xa8\xed\xae>B\x94$<\xda\x99\xb4.\xd22Ue\xbc\x95\xd3\xa2\xa1-\x16\x03~\xba,\x11\xa3{\xc4.\xde\xeaG@^\xd9\xad \x8aB\x86\x9a\xae\x92{\x11\xad\xdfD*T^\x86Q\x8a@\x88)\x19BQ\xd1v\xdf\x9b\xe3\x12\xbd\xd7\x95?\x8f\xa1m\x8d\x95_\x84\xa1\xbct\x1b\xe1\x03m,N.\x8e\xe7\xa4\x19\x80!\x9f\xe1=\xea\x92;q\xca\x1e\x8f?\x96\xc5-\x00\xcc\x9f^L|\xd5kc(\x12\xd7\xf3\xf1q\xd0\xc0O\xaaK\x199\x98{\xd3\x88\xab\xcd\x16\xd2\xa0<\x8ds\x88[<\xb4\x94\xf0\xc7\xab\xf5\xa5\xdf\xf4\xc7Qu\xb4\x1d\x86\xe4\xb0\x82,\x91\x08\xd0\x08C\xea\x83\xf7\xdaU\xca6\x9d\xae\xa6;\x87tx\xea\xb9\x9d\xb6F\x04p\x1a<|\xf22\x9c\xd0f\'a`\xcdf\x076\xcc\x0e\xa3\xfcNX\x98s\xfe\x07\xd3\x1b~G\xf0s \xefw\x8a\x9d\xd2\xf6\x86\xaeR\xd7#,b:l"\xfa\x1e4<Q\xf5\xc7g\x05tJ^\xab\xfbC\x83\xa7\xdf\xf9\'L4Z\x84y\x89s +\x04\xa8\x0b\x9a\x87\x94QY\xb7\x1ct\x97\xab\x13\x8f\x00\xb2\x8d\x89\xd7K\xb4r\xd3\xf3Y\xfd\x8d\x92\xb8p\xca\xb2\\i\xf6\xf8\xc6\xc8\xfb\xb1\x1cOF}\x90\xa5\x08<\xb5q3\xe1#\xecl\xf7/\xa5\xa6\xf0i\x1aT/\x03\x80)\xa11\xdc\xbc)\xedG\xecU\x9e\x08\x97\x97G\x1f\x19\xf1\xf2u\xeb\xe5_\xd9-1\x8c\x82\x965\x8a\xdd$\x96\x8a+q?\xcbw,\xbd\xf0\x99\xa0\x14u\x0eGY\xdb\xe7i\x1c\xa9L\xea\xa4\xfb\xdc\xb8K0F+/\xb5\x11\xb8\xc0\x06\xa0B[c\xfaWY%e\xf0=\xfeY@3\xbe/9^u\x028>\xc6$\x81h\xb7\xaa\x0b\x82G\xee\xf6\xff!\xb4j\xa4\xa9\x08\x0f\x85\xb6\xcc\x9d\xf0_\x13\x00\x14\xf4\x9brx\x1a\xdb8\x8aA\x82\x1c\xc2\xb3\xa4\xdd\x86\xba\xc4P\xa7\xe8Cm\x11\x16\xf5\x11\x1b9T+\nz\x17\x07\x9c\xd4\xeb$\xe4)\x95\xbaj\xb7\xd2\x04\xf5\t\xdbO\x86r[[\xa7\xcb\xcf\x03ftO3I<\x99\x8b\x1e\x0b\x0e%\x8by\xb7F\xb6\xb6/\xcaaw\x9c\x11V\x94\x15\xff\x11hE\xb4\t\x93\xce\xdd\x93\xe3/\x87\xd9\x17\xe6M}*!p\xfbU\xedo\x90\xd8\x0bb\x01\xfa\xc7\x94\xc7\xc5\xc7\x1c\xb0\xe24\xa5\xa4\xacL8\xde)t\xab/\x0b\xd6\x1e\x89`\x17-\t\xd5\x1c\xd8\xf3\x15\xd7\xaf\xb6t\x82\xd1r\xf5\xefN\xb1\x8e\xd8h\x00\xa5\xb9\xe6\xa8\x0b\x13\xc2\xbb\xc1xK\x94\xf5\xdf\xee k\xf6y=\xcaDW"\xf3\x91\xa5\xdc\xca\x07H\x16\x18\x92\xa8:\x95\x82\xf7\xe5\x17<F\x1fO N\xc2\xfb@6C\x17K\xfd\xa4\xb5\xff\xe3\xcd$\xee\xca\xaa\xb3\x1b\x97\x87\xcfk_\xdc\xd0t\xa5\n\xfcH\x00\xca\xe9\xb5\xc9\xd1\xaf.\xb7\xd1+S\xc0\xa5#\xa4\xa1\x1b?\xfa\xc4hn\x87<\xa5\x9cn\x1c\xea\x91\xc7\x1af\xecM\x87\xd9\xb4\xf2j\x90~\xf0\xf9\x06\xc0jJ\xcd\x7f\x18\xe0\xf3\x0chI\xcf\x19\x9f=\xbb\x15>\xf2*G|\x07\xfb\x15\xc4z\x93\xef\xb0,y\x10\xc2\xa9\xd8_4\xb6><%\xb3\t\xef\xbc\x0e\x1a\x15\xce\x19\xadg\x05\x91:\xa1X\xe1\xb7y3U\x96\xe8-\xcf\x9amG\xac\xbe\xaf\xc6\xbf\x8cp\xc29\x8c\x99X\xc6~\x1e\x9a\xde\xfa\x86| \xca\xeb/F\xb8>{\xf9\xff<\x91\x9e\x03\x97\xd3\xa8\t[\x08\xdeV\xc5.>O\xdax9K\x08\xfcu\xb8\xea\xb99S\xd3\xa3\xa2\xe2F\xd3\xa9\x1e#\x16\xbe\xda}q\xdf=\x838\xd7\xd8\xadq\xc4_%v\xbe\xc9\'t\\\xca\x90\x11\xc3w\x03\xc9\x8b\x83\xad\xdd&\xac\xa5I\xf5\xb1\x9f[\x058M\xc6R\x94\xbe\xd9\xb5\xee\x94\xa9}\xa7\n\xd5\x0ff\xb8\xdc\xce/\xe4\xf1^\xbcK\'\xa3X\xdcU\xce\xf4\xbd1]\x00\x13\xca\x13\x84\xfd\x83]\x91(\x9b\x1e\x07p\th\xf4\xfe\xeb\x97\xc1\xbe:\xd9\xfeUR\x89\x9f6y\xbb(.\xf5\xcd\x93\xd5\xd4:\x06\x90uK0;\x8a\xba\xfa\xe4\x87\xee\x16\x03Q%]\xe7xA\x91Y\x8d\x9d\x80\xb5k\xe2F\xed\x96\xc8WD\x8c\xd4\x85\xe2\x83QI\xf5\x88\xf9jK\xb2`"\x9a\xf4\xa8I\xd1\x94&\xb6\x98:M\x00Q\xe2\xab\x8f\xec\x9b\x03m\xc4\x01\xf3;\x9d\xfaw!\x87\xf3\xa4{\xf4\x08\xb5\xaa\x82\x1f\xe4]\x17\x88\x8c\xa2\xbda\x89\xb9N\xcb!\xdb"\x91C\xc8\xed\x82\xc8\x11\x1b\xe3\xe6\xd2\xd9\xfe\xacJH\xda\t\xedb\x99-P\x05|,\xbb\x1fY!hc\x924\x021\x0f\xdc\xef}+\x90\xc4g\x05[\xdc\xd3\x1bK\xa2\x1d\x08\xe9Yg\xb2)2\x14T:z\xfbE\xf2\xa1\xb0^\xf2\xa1\xdd\xea\xf9\x02T\xa1 8\xf9H\t\xabx\x86\xee\x91\x86\x18\x05m\x02\xbe\xc1\xa8.\x90|\xa0\xc2\xf2\xc1<\xa5\x97d~Yw\xf7\xca\x04\xc4\xe5\xdcO\x86\xeb\xe7|}\x0bfH\x84Z\x08#@\x04-j\xc9$D\xe8P\x8d\x08\xe4\x13~X\x83f6h\xa9\xd1A\xc5\xaex\xa3\xe7\x0ba\xb5\xa2\x02\x95\xd4K\x14\x9c\xe0\xb9\xeb\xab\x1f\x1df\xc7E+Me\xe8|J\xd3P\xf4\xfc\xdc\r>\x9bw\x8e\x893xwg0\xd0\\\xd6[\x89\x8f\xa3\xf6\xf48\xb7\xa2d\x12n\xfe{\xd7=U\xa1\xd9\xeb\x0f\xdc\x91$\x8e<W\xd1\x8d\x04\xb2\xf0\xec\xc4\xac\xbc\xdfg\x9b\xb3\xd1Y\x03cb\xc02\xd1OP\xb7\x8abk\xdc\xcc\x0f\xb7_\x92\x02\xb3\xd3Y\xfa\xde\xef\xee\xb5\x89p\xa8\x1d;\x84\xd2\xc6\xe5\x1d\x1c\xd8\t\x8d\x1c\xca\xba<\xf3ch\xde\x16e\x12<\xda3\xb4\xd9\xa5\xfe\xbe\x05\x03,gz\xf0Z\xf9\xd9\x05]\x05\xda\t5\x94\x94t]k\x85\xd3-\xd3&\xd3[kK\xf7Y\xc1M\xd7\x9a\xa3\xberK\xd0\xe10\x0f\x13\x9d\xd1\xf6\xf4\xb05\x1aQ\xd1C\x06\x1e-\xae\x0c\xcfw$\xe7I\xea\xec\x9bg:\x9d\xdb\x97Z@>\xd9\x1b2\xc9I\xcb\x9d\xd6\x9c\xc1?\xf7\xce\xac\x85\x07P\xd1\xff\xd7\x13\x86\xcf\x95(o\xc0a\xd9\xc9t\xcci\xc6\xc7\xf4\xd7!u2\x12_XV\xc6#\x17\xe1\x0fL\xa7\xa3\xd5\xe0\xa7{U\x14/q\xe5\xb5[ t\xe8n\x1c\x0b\xe0p\x9e\x113o\xbf~\x8e\xdc\xd5Irb\xc5\\\x01\xb2\x14GvS\xed~/\xb1I\x80\x917\x0f\xb5 \x1c\xb2D\xc0\xdc\xae\xd6AH\xf6o3\xf1\xdb\xfc\xbc\xa9\nU*Ty06C2WF\xdc\xe8\xb3]\xef\xc7Cm[\xb2\xc6X\x9c\x8c]\xecV\x83\xc0\xcf\x0f\x10)\x8b\x19\xbaP\xfa\xd4\n\xc3>\x9e0m\xc6.9&\x85i\xa9\xd3e\xcbaY\xb43EG\xc4?\xd3\x11\xfe\xacpJp\xe3\xdc\xe9\xb6\xde\xe4\x94\xf1P\xe6Xmt\x9a\x80\x8d\x1e\x99\x13J\xb6*\xa5\x8a\xfd\xb3\xeb\xd4Ay\x15\xf3V\x17t\xef\x1a\x81\xbf.&\xebS"\xfd~\x87\xa7\x01\x8e\xe2\xee\xd8/\x13\xa3\xfb\xac\x14_\xdd\xf2\x97\xc8E:\xc2\x03W\xfa\x11\xc2@\xbf\x8d\xdf\x80\xb5\xc8\'fa\xfd\xe7#\xa8\xd6\x12\x1b\xc0\x9e\xd0\x7fQ\x03>\xb8\x11+\xa1x\xcay]\xd8R\xdbB\xd1\x90=\xbd\x98u\xd6\xc0\xdb\xfb \x1c9\x10\x8d=\x8at\xcf\xe3#\x0bYa\xce\\:H\xb9\xdd\xcc\x95\x86\xd68\xb3U\xac\xb2\xdd\x08\xeb\xe7\x011\xfc^\x1e\xb1\xf3\xf08\xcd\xb0{u\xa6T\x1bv\xa1\xf7Zz\xbfZ`\xc6+\xd2\x9fuG\xa0\x16X\xe5\x19\xcf_\xe0\xa9\xc0\xac7\x92P8\xcf\xefm+)lW6\xa3w\xaf{b\xe5\x9e\x15\x0f\xd4sQ\x01*`l\x14\x96?\xedv\x95\x0e\xb6\xbf\x12\xc7\xa5\xf3ZaS\x83C\xccv\xfb7\xe9=\x90\x11&q\xc3\xbe%\x92\xba\t\xdfk\xc1B-B\xa96\xf2\x1fr\xb2T\x0e_\x9c\rn\xac\x89\x0f\xf8I\'N\xe5F\x1c\xe3\'\x1e\xc1s(\xbf;YA/u\xa8\xddq\xdbTD+\xe2\xb9|\x1f\n_>a\xd8\x10,\x10{\x90c\x15\xea\xe6E\xd7\xc8\xe3\x0c\xaa\xd0\xcfs\xd0\xfcT\xda\xbd\xb0\xdb\xffS\\\xdf:\xc0\xefej\x92\xfe\x81\xad\xd3X&)p\x88[I9\xcb\xe5\xb7\x86\x82U\xc0E\xc0\xf0M1\x07\xc8\xa4\x84\xf5\x05\x1b\xd6\x12\xd7q\xe2Dx\xd42]\xa6\x93?\xafG\x89\x99\xfb[\xb0v\x94\x98\xaa4\xe1zJ%Mm-\xd3\x18rx\xfd\'&P<\xcf\x90\xd4\xb63a\x89\x1b\xa5\x1a$\x8dt#^\x80>\xa1WG\xb8\xe6\x90\x03mU\x05\xd7\xa0$cM\xf5\x9d\xe6\xfb\x15\x1c\x96e\xd3dk\x88\xaa41\x05|\x1b\x8e\xab\xd3\x1a\xc1\x80Lv\xc8uw\x98\x05\xcfi[\x0e\xd3\x88K\xbcs\xefou\xa4\xef\xf8~\x98\x0c\xb5\xe3\xc5\x9a\xb0\x02\t\x10`\xb8\x9b\xb1n\x026\x1a\x06\x86\x01\xcaU\nQ\xbb\xc31G\xdbG\n\xeeh\xe7\x03\xfey\x93L\x1fI\xb1\x04i\xa4}-z\xa6\x98\x1dk\xeaV\xbc?_\x9d3\xb1\xb1\xfd\x8e\x16-\xb3E\x88\xc2\xe6\xee\xadRH\xcb\xec9\x06\xa6\xfe\x18\x13\r\x85\x1a\x7f\x90\rp\x14\xd7A\x9d|\x15\xca\xa5U\xd4\xdb\n\x14\xd4\x0e\xec\x10\xba\x14a\xa4\xdc\x10^\x16O2\x1ebX\xc0\xe67\x14\xed\xd4\xcc\xa5\xc2`>@>\'\x9c% \xee\xb1\xda\xbf\\\x1d?\xe9/\xc9\xa1\x86W\xb2\x87\x1a\xd4ez\xb0\xa2\xf2\x8d\xc4\xf3iU:\t~\x87\xf2\xeaY\xfe\xce\xce\xf6TQC;\xa3\xd4}\xb4\xba\x0c\xb6\x12\x91\x92\xfc\x89}D,\x91\xc8\x10a[\xe6PKvh\x98U"a\xde\x85\xaeI\xbe\x16\xb9]\x96\x0f&\xddV\xdd\xfc\xe3j*/\xdeD9\xf0\x96*\xb1W_Cx=\xbc:\x85|\xf3+\x93\x86:<\xf6\xbfy\xd1o~\x17\xce\xe8\xf5}c7\xa9\x9b\x80SLdk\x1b&\x05\xe4\x91\t\x91a%\x9f\xb4!\xcfQ\xa2\x10.xg!9\xe7%\xb3\x91\xbb]\xde\xc8\xe3\xef6\xaf\x083g\'a\x86O\xc5\x04\x8f\x0e\x0e\xf7R\x91\xc0\xbc\x1ev\xdc\xcc\xc6\xe3v\xb7\x88\xfa0z\xcf\xed)\xbfOLj\xeb\x98\xe1\xd9s\xb2\xac\x96VZ*\xfa\x06\x1f\x90\xf4F\x078\x9f\n\x91\x19Dt#2nH\xbfo\xd5\xfc)(^\x1b\xb7\xba\x19\xb3\xda\xb7K\xfc\x97\x16\x80\xa6m\x81\xd1f\n\x15w~\x85M\x04\xc8HI\xd9aG&B[\xd5\xf4.a\x9f2\xc6Tm02ov\xaf\x8d\x19\xf3\x18\xb7x\xa3\x1f\xf6V\xd5?\xd1\xf6nN\xa5K\xc2\xde\xd8_&\x1d\x85S\'\xc2\x05\xde9\x16\xf0\xdf\x1b!\xdd\xff,\xad\x9c\x8a\x98\xebG\x9da\xa3\x13?_|\x82^v(h\n\x99\xaa\xcdT\xa0\xbf\xda\x95-\xdc\xeeFU\xec\x16\x8c\x81\x12@\x90\xb8\xdfB\n\xcd7\xa9\x02\xb9\x85r\x0b\x1f\xff\\%\xed\xc0{n\x1d\x07\x86\xe1r\x13\x06\xe3+\xde\x1a\xa0\xf2\xaa\xa1\x89=&\xceo\xab\xe9\xfd8\xb9\x08\xe5N\xc2\x88q\xb3\x94\x91g\x10\xaa\x9b2s\x93\xf4\xe3\xd5\xf5\xfc\xb4\x88\xb1V^\x07\xbe\xed\xb9\x96\x14\r\x14\xbf"\xa7\xc3W\\v\xa3L\x83\x12\xad\xf2L;H\xf0N\xaa}\x89\xd5\x1f\xa2\xe2\xf6a_\xe0r\xf3c\x07\xd1-\xf8\xbfx\xa1\xc2\x82\xb6\x9e)\xe4\xa3\x1d\x93@\xa3\xf4\r\xcd3\xcc\xb3\x8f{\xc4\xbc\x04\x12\xb3r4\xe6\xdei\x1b>$\xec"\xb8\xeel^,5O\xb7\xc4\xdb\x89f\x8f.Fo\x16\xe7\x00\xc1x\xfa\xcd5\xa2\xd5u!\x08G\xc6}.\x93\x1cz\x99t\xad\xaa%\xdee\xf8\xe8\x8c\xfa\x82\xe2\x00\xadZqk\n\x88D\x16\x9e\xc3 \xfb\xb3\x00d\xbaL{Oj\x05\xd3\xd3\x84V\xe9\x9b\xa25\x87l#\x90\x8b\xf1\xca\xab\xb2\x88\xca\xac\x86\xe3\xa8\x94\xdf\xf1\xf1\x9a\xe2\x83\x85\xa8~\x1c\xa7\xcbN=}\x92\xec\xda#%\xdeC\xe31\'^\x0b\xa9\xd9yU\x82\xe8\xf6\xaf\xfe\x8a\x92\x0f\xeb\xf3\xbft\r\xb1fG\x13\x8ce;\xe6q_\xe2\xb3\xf9\xba\x96\x05\xee\x0f\xef;\x1c:\xf6\x12"\xb9M\xf2T\xd5\xfah#b\xf6F\x16\xe0\xc0\xf1\xd0b\x0e5\x99\xd8\x89+\xa4\xb9\xc3\x13\xa9/\xda\x187\xf9\x1c{-\xecO\x0cw\x9e\x84\xe4\xcc\xb4\xfb\xfc\xd8t\x9a\th\x1d\xf1\xef\xdd_\x8dow-\xc6m \x16\xea\xf2\x82Z+\xd1\xf8l\xe5\xd6\x19\xc7\x8b&L\x837\x8bt\xa1^\xd5\xc8\xd4\x14"\xc6\xbd\xcb"!\xa7Z\xe3S@\x05H\x0c\xcaq\xff\xd4\xb1r\x1f\x80"\xdfr>\xe7\xc4\x8biw\xeb\x1b\xec\xa5g\xa2\xb2\xb90\'1Tn\xa9\xf1S\xde\x1b\x1d?\t*n\x1fX\x81\xechZ\x15U\x064\x90\xbfe\xcdm\x96I0@W\xc2C\xbf\x068uurQ\x1e[\xb3i\xc1\xe5\xechr\xd6\\\xfc\x88\x8fg\xc7W \x83^\x063\xcff\xf9\xf4x\xd9\xcb\xb8\xbe\x8al\xe2\x88j\xa8\xb7\xa2;\x14\x8eU\x82\xa3\xd0\xb5S\x8d\x9f"\xeb-@\xfe\x11yR8\xa6\x1c\xd4\xbf \xa8\xf7\xa8\xa2\xcf\xf4\xae\xe6d\xbb\xaf\x11\xa2\xaf\xf2\xab\xe8F\x03\xf3\xf3\xb6\x95(z\x8ae\xe3{\xcb\x13\x16\xbfr\x8b\x9f^J)\xff\xd9\xca\x96\xfb\xc6\x88\xda\xf3\xcc\x1e4\xcc\x83\x1b\x84\x04\xfb\xc2R6|\x14\xbb5\xe4\x81\xe9j,m\xa7\x12\xac\xcb\xcc\xfb\x11\xbb\xe9\x9e\xcd\xda\xdb\x9a\xf0:\xa54\xcc\x81\x7f$c=y!\x84i\xdc\xff\xc9\x1fz\xa6<\x8f\x87\xb1*0\xff\xd3d\xfc|S%_\xb2:\x06\x9eD\xcf\xe5!\xae\xb0\xe7\x14\xa2!\xc73F\xf8\xa7\x9b\xb1\xdd\x0c\x9fkY4z\x1b6;c\xc7p\xc8\xf1ZD\xf2\x04\xc3\xa8\x01\xe3~G\x9aa\x00\xf6\xa6\x1ar\xcb\xb3@\x92z\xf8Ff;\x1a\x03\x1b\xc5Eo\x17\x03ksQ\x0f\xd5\xbafs\xf6\xd7G2$f\x00\xe6%\xb8\x05K#\x14\xf4\x89R9\xbe\x1bG\x8d:;iL\x85HAM%N\xdc\x14{\x90\xc6\x8a(Y%d\x01+\x82\x83\x86M\x13U\x0b1A\x18E\xf5\xba\x12o\xcf\xa3}\xa3\xae\r\x90\xfa\x94s\xfbx\xba\xc1~\xe4\xd4\xd5\x87|\xa7l\'\xf2%:\xb5y\xb0\xc6m!\x94\xa3\x1e\x9c\xf9/M\xce7\xe5\x08oi\xf6\xc9\xceL\xe5%~\x8f{s\x9exI;\xf5]\x9e\xe9\x93PX\\\x18\xce\xc2\xcd\xfaFW\xd8:wp\xb3-&\xc8\x070\xc1\x02\xb3K\xa2\xff\x1cD\x8a\xd5f\x19r\xac\xd9\x0b\xb6\xbfs\xce|\xa8\xa3/\xe6\xb5\xf53k\xf1\xe7\xc1\xed\xcc\xbb\xc55\xd4\xfaN3\x1e\x81\x01\xd9\xc67,3=q\x88v\xc2j\xed\xe1\x13\xe4\xe4\xddV\'\xc0C\xa2\x1eN\r\x17\x90\xec\xbdSya\x9dU/\x0bb1\xf6\xb2\r\xb0\xdfh\x84T\xcf\xec%\xb5\xd0\xdcv2\xa8\xff\x0b\x85\x9a\xbe\xbf\xd2r8\xd5\xec\xb9\xc3\x8c\xbdEl\x86\t\xdef\x81\xb8\x16\'\x8cX\x1bX\x99\x8c]B\x04\xbe1*\xd4@\xca\xd9\xf2s\x8f\xd2n:6\xe42\xe0\xda\xdaj\x08\xf9\xc1\xf8"\x8fO\x9c\xd3\x08\x1d#\xb5z1\x92%-;\xf4|\x81\xfb\x81\x0b\xa9\xd9\x8bx\xbc\xd0\x0e.\xe6\xfb2=\xf6P\x13\x15FT\x02:w\xfe.\xe4\x8ap\xa1 |\x0c\xeeJ')))
except KeyboardInterrupt:
	exit()