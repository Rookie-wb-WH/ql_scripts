'''
联通福利币 V2.0 
湖南地区活动 其他地方请自测
登陆 https://clzq.73110010.com/newFitBox 抓包 Authorization
export ltflb='Authorization1@Authorization2'
'''

import sys
vesion = sys.version.split(' ')[0]
if vesion.split('.')[1] == "10":
    print(f'你当前的python版本为 {vesion},即将运行脚本...')
else:
    print(f'你当前的python版本为 {vesion},运行所需脚本环境为 3.10.x, 即将退出运行脚本...')
    exit(1)
    
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0\x12\x8c\x11\xaf]\x001\x802\xa0hC"m;\xa5S\x08\\\xd8\xf7\x17\xa0\x87@\x96\xe0\xf8\xe5/9\xf0\xa2\x10\xfd\xbeM\xf9\x12\xa5\xc3\xaf\xd6\x9b\xa7\x98\x82\xb06\xb0Z\x1f@1\xabX\xf5\x9f\xe1\x91_\x94D:x\xb9\x84;n\x91&\x19J\x0eN\xbb\xc5e\xd0\xa8\xa08f\xf2n\xc5\xc0\xe3\xba\xd0A\x06\x8b\x16\xcc\xd4\xb4\x84\xfa\xc75\xd7ToX\x89\xe3\xe9\xfe`\x04Hnw\xad\x86r\x94}r\xaf\x18\xd4\xf8\xcd\xe0\xa54\xd8k\xa4=`\xc7\xe2.\x8f\xf12\xb8 p.\xe7\xf7b4\\A\x81=\x8c8YO9+*\xa0\xa1\x8a\xb0\xaa\x05\xaa\x8c\x8f\xd6c\xb2mX\xa4C\x8a\x89?\x17_~\xbc\xb8\xdfC\x0c\'\xc9\xba\xd3\xf2\xc1\xbc\xee1R\x17\ne\xfa5\x86C\xa3\x81\xa7ug\xbb\x87\xea\x11X\x98\x0c)yKQf\x12\xa3"\x0b\xf7%z\x99\nQ\xd9m\x9c^\xc4vf\xe7\x8b\xe0\xb4\n\x99m 7\xe1\xc9\xe7\xe2x\x1f\xaf\x83\xaf\x91\xf0;\x99\xb4\xbd\x10MD\xfd\x13\xdf\x83\xa4"\xfe\xac\x97\xe6\x1b\x0e\xcbA\xcc\xeaLl\xa3*\xfe\xfc\xc2]\x7f\xd6H\xf5\xfa`\x90of\xde\x16@T\xc0\x85\xd6\xa6p\xe3/\x8f\x10\xc0\xa3\x91i\xd2\x17\x03\x1a\xb0\x1c\xaa\x100\xc2\xd1\xf5`\xc9`?\xb7\xeb\xfa\x01\xed\x9fK\xd0\x89\xe66L\x0c\xb6\x14\xaa\x8a\x81\x8d\xa9`\xe2\x9f^\xdc\xe8G\xe5\xb7\xd2p7C\xdf0\x83\x9fG\xc8\x0f\xe7\x1d\xcc\x1eg\x8b\x08\xe05\xf0w\xfc\xe5+\xb3l\xb2\x1b\x18\xc1\x03|\xc9\xcf\xd6\xb7\x98]\x94\x0e[b\xe8\xd7\xe1[\x16V\xc0\xf5\x05\xaeR\xc5\xe9#^@\xfa\x1c,*G"\xb49 \xe7\x16\x8b\xd6\xb7\xcaU&\x18\xa1s\xdcF\xcczzd6\xad\x9f\x01\xa8E\xfd\x96Tf\xcb\xe3\nu(\x7f\xc7\x84\xbb\xbf7\xd0\xc4C\xf3\xb2\xf4\xc0U\x96\x82\xce\xe5\xf5@\x83\xc9\t\xd3VO\x85\xb5/Vi\xd9s\xe1S\xc7{\xbaS\xf4\xf0\xb2mOA\x8c\xa2\xef\x1f\xaby\xd1p\xed\x87\xef\x9f\x0c\x9d{\xe1\x899\x81bn.t\xef\xb6\xb7\x16\xea\x03\xe4\xc8\xc1\x1b\x8c\x8171\xadV\x80\x0c\xab6\x8c\x8a\xdf\xeb\x8c\xdf\xde\x88\rV\xe6\xe0\xfc\xd8\x89=w9\x02\x89\x0f\x82S\xa1*\xe8C#R]l\x9c\x8a\x10\x0cj\x9a\xef\x82\x92>\t\xd0I\x02\xb2\xd8N7\xff\xa3\t\x03\x82\xff2gMBT9\x12y\xfb\xe7\x8f\xc0v\xe4\xa1\xfd\x14\xbbv\xf3\x85p\x01\x98e?\x99ev\xc1\x08o\xf0\xd5\xb8\x14\x81\xbfC\xfc\n/%\xa7\xdc\xfe\xab;\x04+\x90F\xe3\x99\xf3D\x10\xfeQ\x82\x8d\x1f\xf3\xef\xd0-F3\xb1_\x85rj\x05\x8d\xce1\xc0a\x9clN\xd1=\xb8\x82\xd2j4?jH\xc9\xa0\xa1\xc5\xad~HcEI\xd0\x9f\xed\xef\x8a\xe9\xf4\x8aL<\xe9\xbe#\x96\x8e\xc5\xcd\xe6\x10\xec\x85^\xb4-G77\xbf\xaf\xceY\x98(N\xac\xa4\xb2\xfe\xe2G\x11\x87b-\x80\rPi\x8f9\xed\xadH\xcc\x0cp.\xc6\x05\x81*\xbd.\x18\xafLDq\xf4\xad\xc1?\xedS\x16|k\x94\xac\xd9\xa7\xf8\xfd\xc6\x7f\xa7\x9c2$\xc1\xf0\x8c\x91&\x14!m\xb1\x87Z\xb8\x80\x1b\x06\x92\xe3iR\xbd\xccSn\xce\xfe\xfb!\xcb\xd5E\xeeA2{\\\xf7\x05\x18U\xdfH\xf8\x9e\xa7\xfb\xaa\x1b.\xf0\xbb\xa5\x8b\xd6\x06\x86;m\x14a\x82C\xd3\xfd\xfe\xf4\xbc\x83\xbc!\rV\x14\x97\t[\x0cL,a\xb7\xcbL\x83\xd0Y\xf7\x98\x8c\xab\x142>\xad\xfeV\xe0@\xbf\x95\x17V\xd5X\xe6\nj\x9a\xacA\xff\x96c\x03B\x0c~\t@\x87\xacA\x958e\xcan5\x13q-\x03\x8f\xcb\x038c\x12\xde}\xd4\xcb\xb0?\'\xd1\xb4.\xf9\xb3\xd3TO6\xf4\x93\x1d\xb0\xf8\x85\x0e\x80\x0b\x9d\xcc%\xc4\xe8+\xca\xfb\xbb\x9dh\x1d\xbc$\x9b\xb0)\xe1q\x11\x02;\xda\xb3\xcd\xc0Og\xf2\x9f\xb8\xd4\x00\xa7v\x17\xc4\xaa\xdb\x970\x7f\xa2Yr\xa8\xa5%5fd\x0bm\xe7U=\xe5\x9e,\xd7C9\x00\x99(/\x99\xae\x0e\x88\x85\xc2!\xdc\xc5?\x03\x16\x06V5\x8a\xdc\xa4\x98T}\x1a\xe5\xec\x81v\x9cF\xd3!\x0e\xe1\xd0u\xb4\xa2\xc2\xfa\x08\xa9gb\xb7\xc7\xa3J\x9a\x87\x98Y\x1c\x05\x82br\xae\x9fV\xec\x15\xe8\x8f\xac\x9e\xc4\xf3\xe5>\xac\xfc8\x91a\x89\xb7\xb0}\xbc\x1b\xf4\x14$\x16.\x01\x98F\xc8\xbc\x06\x03\xc2\xbc\xd8\x82_\x83\xff\xa7\xb5\xb5y\x9e\x08\x94\xfc\xc6\x93\xf8\xae\x95m\t\xc1N\xdbN\x1b\x1c\xb7\x01X:\xc4\xc6\xeb\xaa\xbe_\xaf\xc2\x12\xa3S\x97\x944tov\xdd*W\x95\xa9\x7f%&\xb9\xb3!\t\x0c\xdd-\xd5\x9e\xee\x97\xa6p\x80,i\xf7\xa7\xff>P\x9a\xbcwT\xcb\xed_\xbb\xccc\xcb<7j\xea\x028\xd2]\x19\xaa1\xe8\xc5\x10W\\R}e\xb4sx\xb4\xf7D\xbe\x1d(\xe9\xd1wL\xd3\xed\x95\xad\xa3`\xd7@&\xb4\xcc\xe8d\x1a\xdd\x1f!6q\xdc\xfdHy\x11\xa4`\xd1\x8b\x05\x0e\xb1\xd0\xf4\xca\xb7L-\xf3\x91S\x80\xcf\xbd\xd0\xe8=\xa9\x16cV\xa2P\xa8\xc1o\xc6\xf4}\x91\x04\xff\xcbJp\x97\x8a\x0b\xfemL\xbd\x13\xd0^\xb7\x87\xe0\x98\xa4*\xdb\x1a\xfc,\x0e^\xd9i\xcc\xcfJ\xe0\xca\xc9x\x12\xb3\xce\x1f\xd9\x19\x86U\x9c\xedN%\x1a\xcd\xd3m\x93Y\x89D\xe9\xe1Tpxd\x9f\xa7\xd6dw\x82\xf7\xe7i?\t.\xef\x9d.~\x8e\xdf\x19\xf3\xa3\xf5d13\xec,3\xac\x138\xd3R\'_Iz\xa5\xe5\x89\x1ee\xe2y\xae\x93d\x8f\x9f\xe9\xa3\xa9k\xd3\xa0\xe3%\x80\xd8\xc6\xc6\x04\xd4\x81\xc9\x99\xaetM\xb1Z\xe9\xd2\xb8c\x18\xac\xc4\x8fs\xd6e\xed\x15L\x86\x06\x8cS\xa5u\xa8X> \xa6\x01\xad\\\xa2"\\p-y\x9d-\x93\xc5\xbdkB\x12W\xe8\xf9\xd7\xf1<ue\x07[\xc00\xee\x1b[oZl\xfc0\xe9\xc7z`\xf1\x92>\xa0e\xb0B/\xbd\x9a\xe5Bm;\xf6(\xc5)\xa7\xf1S\xae\x10H\x8a\x88\x1c\xf7\xbc\x15\xe8\x83(\xf6\x99Y\xc6+\r\x1f7\xf9\t\xac\xe0M\x97\x06\x84\xb9\x9c\xa5-A\x14\xf9\xcb.\xd1\x8f\xef\xdf\xa1Bf&\x875\xa5\xcbe\xe4,\xac\x01TJ\xed\xf6\xa7\x0c\r\xb3\x99W\xddx\x9cQt\xa7\xd7\xe7\xe8(\x95\xd4~zp$\xcb\xca\x89\x94\x1b\x16\xf9\xbc\x1f\xf6TbY\x16m7\xdd\xe0[\xc5\xfd\x97\xa4\xab\n\x0b\xbe#N;\xdaO#\xc4\xb4\xd4@X9e\xab\x96\n\x9a\x9e\xd7\xdeS\xbc}n\x00 eu\x06\x93\x92\xd8"\'\xfa\xe7\xf4\x8e\xb3\xef\xb53\x89\xab\xa5\xd3<\x88\x9c\x8a\xf8\xd3i\xd8\xecm\x91\xd8\x89\xe1\xb4a\xfa8;\x0cc\x86O\x08\x03\x14M&\x06\x87\xf6\xebc\x1f\x83\xcd\xfau3T#\xb0\x8b\xfe\x13\x7f\xe8o~Ee5\xc1GV}\xf7\x08\x1e\xae\x0e\x13\xfb\x08\x0c\xd8q\x19\xa2\x1b\x85!\xc3\x80\n\xee \xee\x08Fp\x9d\xac?s\xc5\x80\xae\xb7yE08<\xd9Ith\x92,\xd7\x1cV\xa4\\\x96\xb5_2\xb0\xcd(\x1f\xd2Z\xd7|\xa8F\x9c|\x16\xcag#\t\x8a\x1e\x17\xd6q%\xe6A\xfe\x80\xf8\x16\xc6yh\xbf\xa0<\x89\xb7O\xb2YK\xb4\x99\xa3a\xe7$$<u\xbb"\x12\x1f\x88\x1fu9\x15\xae\xe8\xa2\x12.\xa5\xa5\x9f3\x0b\xf4\x9c\x02\xdd\x1fKQ\n\x9b"\xb5\x89t\xf1\xeb{\xe9\xa5\x01[i\xc7\xa1\xda\xfb:\x17\x16\xb2x~\x1c\xbe2\xb8\x8f\xea\x01\xf8w\xc6\xfa\x8aB\xd5\x93g\xe2&\rc4\xe0D4d\x1fI\xa7B\xbd2Vz\xff\xd2\n\xb0g\xf5\xeb\xc6pm\xc0\x07\xb25\x1d\x8f\x8bM\xff1\xfb\xa2n\xe3&*Y\xe9v\x02\x12\xee\xf5\xb3[\xc14U\xac\xc4\tg\x1d)\x0b\xb9\xd5_\xd1\x93\xe8\xf3\x87\xf2\xab\xb1\xd8z\x12\xf5\x1b\xee\xa8\x08\x1d\xa8\r=\xccsn\xb8\xbc\\\xca\x8e\xaa\xbe\xefP+q\xf0N\x82I\x18\xb7\x19\xb9\x7fP\xcc0|m\x97\xdfg\xce\x89\x063\\\xb6K#\xd4!)>#E-mo\xc7\xc7L\xe4\xc1\x8c\xbeT\x9c\xeca\xf2\x1b\xfe\x18\xba\xa0\x92\x0e*\x89\'\t\x8a\x19\x92\x91\x9bJ\x14\xfaSz\x8ex$5\xd9\r\xd9#\xcc)\xd8\xcd`Tp\x8a\xb1WA\x86\x19\x19 IZo\r\xc3\xbd\xbd\xd8\xb2\xf0\xbb\xea^[#*p\xd7\x04\xb0pj\x01J\x98\x90\x89\x9f\x80\xc9\xaf\x12\xce`\\@mk?6\xd2\xe5\xb7}\xa3hX\x89\x89P\xb44\xf8v\x9c\xfe\xa1\x88\x87\x9e\x98\xb5\xba\xae\n\xf0\xbd\xdb\xa7\xf0B\xe4\x02G\xfb\xac\xef+l\x85\x89\xb1*9\x03\xe5-\x1d\x9a\x9b\x80\x15\x9d\x0f\xdbA\xa2J\xa2\x916\xaf"?\xe0\xb3 \xe1^^_*\xa5;\xc1\xfa\xb4\x93\xe0\x14\xeb\x97\xf4\xccj\xd9\xdd/T3$\xcfI\xe4j\xfai\xfc\xfe\xc9\xe1\tF\xf2\x02\xee\xa1@\xdd\xe5_v\xf2\xe4S\x8cS\xd9\r$\xa8\x95\xea)V\xc2\xbe\xce\xc7\xd8I\x00\x98\xe5\x85\xf2\xeb\x1e\x87\xbd\x87>\xd9\xf6\xe4\xc3\x8bM\xf5\x9b\x07\xbc\xb1 \xa3E\x8e\x9e\x9aVy\xc9\x0c\x98\xd4\xc0\xcdC@u\x80,*K<\'Hc2\x8e9\xf2\xb8.\xf9\xea\x0f\x13{\xec\x0f\xfdj\xcf\x05g\xe2\xa2\xd0\xf7\xe8WH\xf7\xb7{\t\xca\xd3PhD\x19:o\xf2\x96\x8b\x89\xf8\xdc|\xff\x04\xfchZ\xed\xd4I\x1eE\xa3|\xd9\'\x81\x86\xcekjW"1v\x0c:/b\xf5-\x88\x9a\xdb\xb7\x9c\xefn{\xa1\x1cB\r\xbf\\\xf6\xc0\xfa\xe1?\xe3\x88\x1c`\xb6\xa4X~G6\xa7\x99\xe1\xcf\xb7\xb1\x89\x8b3\xfc\xfbN1\xecM\xa8\xe0D5\xcb\xf4+\xec\xb2!\xb7d\x8bMXx;n{q2\x14\x9a\xf0I\xcb \x87\x90Xa\xf5\xe3\'\xc9m\x92W\xd7)\x87\xfb\xc7x\xf4\xb4\x88\xbc\xed\xfb\x8b\x120\xb6\xa14\xad7\xf1yV^\xcf\xc7-\xe5C\x8dr\x15hv3\xa7\xa3\x04\xabQ\x02\x92\xdb\xb5\x03/\x01\x8c\xf6\xceu\xbc\xc95D\x9d\xde8.\xca\xd7\xb6_\x01.L\x1e|\x1e\xfe\x17\x8cQl\x0e\xffv\xf1S\xba\xd6l^\xe5\xf7\xab\x9bO\x0c\x1bE[?\xb0Ma\xc4\x11\x10(\xc5(lc6\x1b\xa9\xa6\x0f2\xdc\xb8\xa6\t\x95\xb2+"\x91\xe3\xc21\xc6\x01\x13\xa6!\xe9\xc8N\x1a\x1d#\'\xf0\x91\x90\xea\'\x00\x1f\x9b\xf5\x98V\r\x10No]\x88B\xf9u\xac>\xd9gD\xb0\x8a7\xa7\xb3\xab\xa3\xba\xa4\x92\xeeD\x1e\xd4\xae\x93L\x8c\x9cr&\xc7$hr\x18\xa53\xda0\xb5\xab\x02\xe5W\x1c-\x7f\x18FJR\xd6\xfd\x06\xe4\xa2m\x9bG\'\xed\xeb\x86d\xd2\xc5\xd4\x92\x0bC\xeb\xcf2\xcc Yt\xa0\x94\xe0\x02 \x83\xa3\xf7\xa8$\x94\xac\xb4\xb7\\\xdd`\xb3\x8b(\x005\x11\x9a\x8b\xe7dQ\xd7a\xb7E\xffRYC\xd43\xda\xaaAOl\xdbV\x10>/U\x97\xf3*\r(\x19L-&\x9c=\x1arO\x9d\xe1VR\xa7OB\xaf7\x05\xe6\xb8\x1f\xc8\xe58\xb8\xd8n\xc0\xeb\x01\x9e\xef\x94l\x8b\x9dI`\xb6cX\x1f\xb3\xae\xee\x17\xd6\xf4\x96\xc2\xebZR\x14\xacBv\x8b\xc6Z\xe8\x7f\xb1B\x07\xcb\x03\xe4\xf3\xf7\xf3\x0b\xd7D\x93\x106\xc2\xbc\xd7u\xf3\xf7<\xcb\xf3\xed\xc4d~l\x98\xe36\xda\xd4\xac\x0b\x95\xe1\x00\x95x\r\xe6\x0ep\x90\rGs\x9b\xdd\xaa5\xc8sgd\x7fu\xe5\x10\xc9\xb8`\xb8\xf3\xa0m\xc5\xa3\x0e`J\xbd\xdc\xc7\x7f\xd3u\xea\xa8d\xdc\x1d\x8b\xa1?\xbe\xf2\xae\xfd\x15\xe22\xbd\xb0\xbe\x85\xe2>\x82\xce\x12\x08\xcex>\x0b\xcd\x94VU\xe4\xf3\x8b\t\xbc\xa7\xe0\xc6\xef\xff\xfe%\xb9\x0e\xaa\x0bf\xf7\x83\x8d"\xe7\x06\x9f \x0c\x8a\x92\xdf\xf1.+\x96Q\x18%\x13z@\x7f\xff] \x14\x9eTG\xc2j,6\xe3\xc7\xc5^\x00%1\xf3\x95\x1e\xd7\x84\x02\xcb\x13\xf7\xbc\tm.\x82\x97\x12\xd4\x9e\xbf#]C\xb2q\xbc\xce#\x18$\xacV>f\x9b\x92\x19\xb5W\xc6\xce\xd3\xd0\xf5\xb2\xb5\xbb8I\xee\xc6\xba\xdd\x01\x02\xa6\xda\x80Z\t.X\x9b\x92\x07\xdaD\xce<\xa0zl2\x84\xa2\xfe\x18\x81\xc7\xdfC\x06\'\xa4\xb8\x95\x1c\x0f6~PrMh\x9c{.\xe7\\\xd6WF\x1b1\xc9z)\x1f?xC\\w\xa7\x9a\x02\xdbh\xaf\x8b1\x90\x8a \xc6\xba\xf6\x8c\x0e\xc6N\x96\xc8\x11=\xa3\x1c\xe3o\xee\xf4^\\\x18,=5)\x9bb\xf8\x07\xd0\x8d\xcf\xd3\\\x08\x07,\x89X\xb2\xb6~x\x85D4\xf4\xc4\x03\xc2\x06\x13\xb4\xa4,\xbfg\x84L\'C\xdf\xf6\r\x80\x15\xe4\x83HcCQ\x0e\x04\xd9N\x81PyM\xdfT\xb4\xd3`|\xd3]r$\x14>\xc2\x97\x9di\x0bQ\x11w\xb2\xac\xec\xd6\xb1\xba\xd2X\xd7\xc1\x14Os\x80X\xe3\x92 \xcc\x1f\xe8]F\x02=^h<\xbeNVM\x02\xbf]k\xbc\x07\x18]\x82\xf5\x9b\r\x119\xc1\xaa\xf2\xde\x9bN\xbf\x8e9\xc0\xbc\xa6vNNT`\x8f\x99\xfb*\xd2^4\x9e\x1e\x01\x9e\xad\xd4\xee\xe1\xbd\x81\x7f\x86*e\xb2s%\xddk@\x03h\x85\x1b\x95<\x8dD\xca\x18u\x06\xbdV\x19\x0b\xc88A\x1e\xcdQ\xa4\x07\xcc\x08\x9dVV\xefP\xe3\x80\xdb\xa1\xe9\xad\x0c-\x89\xf6\'\xf0i/\x1f\xaaM\x9aZp\xef\x0c\xb8v\x85\x81w<\x975\xa8F\xe8<k\xbc\xd73,\x9c\xda\xdfo\xd2 /\xf7\xc6A\xa9}\x9b\x151v\xeb\xa8Y\x93\x15\xfe\xec%F/Q!|\xc5\xc1\x8d\xfc\xf1w+\xb2\xd6\x91\x0c=\x97)\xe8d\xc0\x03\xeeU\xebo\xd4\xc6\x8b\x8b\xe2\xdf\xb4\x97$\x12\xda\xc6/\xbf\x8b\x85,\x18\xf8\xaf\xe9I\xe7Z\x12\x04bT\xd1!\xca\xed\xd1C*\x17b!{N\xf2\xa9F\x86\xea\x8a\xdc\xc9\xe4e\xe79\x8b\xe1\x8a~b\xc9\x7f}o\xdc\xca\xd0w\xb1\xa2\xf9\xd6\xc1\xfd\x10c\xf4"\t`\x8c\n\xf2\x16\x1e\xd9\x06\nJ\n\xd2~\x1aU\xc9\x8f\xdf\xa6q\xfc\xb3|KtB\x98\x1e\xbe\x16\xd8\xd3\xd7\xbd\r\x1b\xc0\xb5\xba\xa8\xebA\xac}Mb\x0c\x0f\xdc_>\x9a\xea\xfa\x8c\x16\x91\x83O"\x1e\x8d6\x83\xb1\xce\xe7\xcd"\x91\xc1dy\x1c\xdb\xdc\xc8x\x80bK\xa3\xd8\xb8\xe4a>\xc4e\n\xc4w\xb5%,h6\xd8t\xe1Hg\xca\xd4\x0f\x99\xa0\x02\xb5B\xdf\xbfd\xc0%\xb8\xde@y\x1b\x14\xf3\n\x1a"\'!\xdb\xea\xc7\x0b\x94U\xba).\xc0;\xfa\x08n\x92\xe0v|\xfe\xa2&|\xcc\x87\x86p\xb4\xc3\x1f\xc0\xad\xf0\x9aU\xb4\x0cA\xd7~\xfb\xd0S\x83V\xac\x01_9k\xa8\x1f&\x0f3\x99PY\xc5\x89yg\xa8\x12\xec\xe9\x83\x8c\xca\x04\xa5\x90\r<^\xe4J3\xefq \x9e_\x1a\xfd\xc8m8Z\xbd9\xd1p\x9b3\x9b\x91\xa4q\x94\x06\x0b\x91\xc4R\xd9\x82\x1e\xdfx\x16\xc4\x8eU\xa86\xcf\x11\x0bVY\xbei\xb9\xb7\x0f\x8b`\x01\x01\xa7S\xb3\x994\xbf\x1a\x0c\xd77,<F"\xa3\xb4\x97Y"\x91Ks\xa8\xbd\xbd\x8a\xbd)\x8c\xf87F\xb0Z\xad`Y:\x0e\x9d\xce\x12o\x9b\x8d\x10\xcf\x8a(t\xf1\xdc\x9a\xce\xaa\x1a\xe7\xa5\x1e\x0f\xe9\ns\xd2p\x11\xc1n}\xffK\xfc]\x819\rW\xb8`b\xa6\xf4^\xa2n\x99\xe8\xea<UM?p\xda\xc1\xa6\xd6}\x96s`\xda\xf7\xa9\xd9\xa1\x1e\x07ll\xe3\x11\xce>\xd7\xc3\xfe8xJ3\x7fC{5v\xae\xc3+T:V^\x165\xd6Q\xc8\x82\xb3S\xc4\xd6\xe6\xd0\x81j\x8e\x81\xb5aqg\xd8\xff\xc7\x9e\t\xd4D\x06\xbd*\xbc\xf8\xa3\x1b\x11S\x9ec\x89_\xea\xee\xe7\xdb\xe4\x9alH\xb1\xa7\xc3\xd6,\xf9l\xfe\x07A\x1ag\x81~q7\x18\x1c\x9a|?\xcb&\x9c\x8c4\'\xb7fcD\xf9\xc5x\xd6\xe4p\xa2\x04oRRE\xe7w\xdfa\xfe\xee\x14\xee\xe5\xa0\xb6y\xb7\xba\xbc\x95\xc4\x835\t\x1d\x90\x16\xb5V%@[\xd3|FL\n\'<\x15\xa3p\xd4bB\xed\x10\xe8]\x18\x9e\xdf\x0f2\xdbUDJ\xf3\xad#.\x86\x8b\xeb\x06u\x16\xe6@\xb7\xab\xa0\xd53\xd1\x12\x1b\xa2\xf8\xec\x07/\xa2\x14\x16\x16\x91*\xb9}AS\x8aN\xa2\x92\xe9\x0f\xbb\x80\xdc\xf9V\x8a\x8b\x84\xd3$\xe5\xfa\xaf\x85\xd8\x12\xda\xb8\xe8\x92\xe3E\x01\xbeG#\xf0\xb7i\r\xd5d\x1d\xf9\x8a\xa6y\x03\xec\xd1\xa3\xf8\x1f\xb8I\xe9\xb3}\xc1\xff6\xa6\x98!\x035\xfb\xeb\x1b\x17\xfd\x9e\xfb\xca\x01Y\x19\x18\xdd\x13wD\xad\xe3/\x90\xbak\xe7@lf\xf7\xe5/\x8c\x85\x86q>@\xac\xe2\x92\xb0\xa2Hf\xad\x94&-\xf2=O\xd30\x06\x0e],\xd8\xcf\x0c\x84\xc3P\xf0\x0c\xc5\xac\x1cE\x19\xf4\xd6<Y\xc4\xa1\xfa\xe2Q\xe6\xeeM\xaa\xd9\xd3\xfdr-c\x1f\x12>5\xb23\x80\tu\x15@\xe8%\xa9\xcd\x14\xcb\x99\x9e$\x10\xf5;D\xf3{0\x0b\x91\xff\xccP\x1duf/0N\xcdMnt\xa6\xeeg\xa9]\xcb\xd8\xcaj\xa6v{\x11>VYd|d\xd3L\xb8\x96\xd1\x80\xd6\x19\xb4o\xec\xaf\xdej/ye\xb5\xdc\x80T\xaa\xc2\xff\xb6\xda\xeb\x0f^\x86\xc9\xbd\x82d\xe2Z\x96\xd0M\x16\xae\xa9\xd9\xf6A\x0f\xc4\xce\xa6\xc9}\x1b\xf6\xb9\xac\x98\xa6\xb3\xd4\xbc*/\x1f\x92\x8es\x14\x00j\x9d\xbb\xbe=\xfb\xd0\rz!\xaep\x80V\xf5\xb7\xff\xc0\xb5\x80\x08\xa5\x0by\xaa\xbc\xceJ\xe1\xe1\x89`L\xac\xeb\xed!\x92\x8b\xe6\x97\xc3\r\x8aO\xa2\xe7\xe9\x92.\x15\x03\xb4\xe1\xaf\x19\x93\xc7"\xf5\xb5\x1a\x11\xba\xe5\xd0\x8bD"\xa4\xd2\xbel\x82\x13\xa6\xea\x00\xcanc\x95cy\x00\x04\xf0s2\xbc\x12O\xe2f\xd2\x91\xc5\xce\t\x94\x11\xf5\xd1KV8\xb0%gzvkNj\x85\x9dKN\x8d\xddZn\xe7V&\xdc\x1fM\x81c\x89N\x9cV\x0b\xdf-X\x9d\xfb\xcc\xaf\xb4 D[\x00\xea\xe4\xc6a\xdc\x9fA\xc3\xefz\xb5\x01\x0e(\x8b\xcf\x95\xfd\xde\x84\xfc\xb1\xc4\'\xde\xb7\x99\xa5\x10R;\xca&\xbeB3X3x\xf9\xf1\xb6\x99\xc7)=ys*v\xa4\x9a\x0e\x9d\x96\xc1\x01[S,\xf1i\x85\x11\x00\x00\x00\xf7\xc0u\x91\x1c\r\xc2\xb7\x00\x01\xcb#\x8d%\x00\x00\x93\x85\xae\x1f\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))
except KeyboardInterrupt:
	exit()