'''
沪上阿姨抢券
抓包 webapi.qmai.cn 下的 Qm-User-Token
单账号变量填写: export hsayqq='Qm-User-Token'
多账号变量填写: export hsayqq='Qm-User-Token1#Qm-User-Token2' 请使用 # 隔开
抢券次数变量填写: export hsayqqcs=100 默认次数为 35 次

活动时间: 10月16日 - 10月31日 每日1000张免单券
'''

try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(zlib.decompress(b'x\x9c\x01*\x0b\xd5\xf4c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00@\x00\x00\x00sH\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x01l\x03Z\x03d\x00d\x01l\x04Z\x04d\x00d\x01l\x05Z\x05e\x06e\x00\xa0\x07e\x05\xa0\x08d\x02\xa1\x01\xa1\x01\x83\x01\x01\x00d\x01S\x00)\x03\xe9\x00\x00\x00\x00NsE\n\x00\x00x\x9c\x85\x96k8\x13\x0c\x1f\xc67\x9bY\x98C\xa8\x84\xa9\x18C\xa4\x19\n\xd3\xb0$l\xc6HF\xc26m\x0e\x919\xae\x9cr\x1c&\xa1r\xa81i\x0e\xf1>D9tB(\xa4\xc8\x14\xe3\x11:\xd0$)CE==\xbd\xdf\xde/\xef}]\xf7\xfd\xfbp_\xd7\xff\xff\xf5\xa6\x00\xfeG\x90\xdf\xc6\xfe6\xd3\xe1wP\x01T`\x08\x80\xfc_\x02\xc9\xc0?\x94 K\xfc!\x88\x0c\xfaC0\x19\xfc\x87\x92dI\x1a\x84\x06(\x97\xa2\x81\xca\xa1T\t\x1e\x90\x07L\x01\x02\x7f7$\x80\x1e\xe8\xc3\xbf\xb7\t\xcc\xf0-\x00\x80-\x99~p\xbf\x8d\x97\x0e\xc9+\xf1\x1ae\x19\x00L\xfa\xf5\x7f5$im8\x11\xfc,\xe6\xfe\xe2R\xf4\xd9\xe8%\xdf\xaf\xcf\x8c\x8e\x16()\xd1!\x99&\xf6|<z\x10\x8c\x16\xd2\xd3\x05\xbd\xbc\xdbh\xbf"\x05\x06/\xbd\x00_\xdd\xdd\x89\xd1)\xb2\xdf]r\x81\xc4\xa8\xa6\xb2\x9c\x8b\xd1\xb2A\x18-<\xc6\xb9\x88\xcb/\xdd\x8a\xfeB\xc7[\xa5W\xe5\xa1\x87\x04\x81\x05TFu\xea\x10\x8bK\x0ca\xa7\xe8\xdd\xa9\x94w\xa0\x8ba5\x05\xc3p\xd2\x08q\x04\x0f3\xab\xaa\x0e\xb5WX\xe1\xa0X\x1c4#\xf3\xf7\x1b\x17\xa2\xfcQ\x11F\xab\x1fcs\x9daE\xd2\xe5;\x8c\xf4\x1cr_9\xc2+d\xe1+w$\xd1G\\\xb4QV|n\xb1N\t\x06\x07\x16\x9b\xe0\x1e\xd7\x86*\xd9\x01\xd1 \x81\x90\xa3Z\x0e\xed\xeeK\xe7\x17\x01Fp\x83vG\xaeC\xd1v\xba5\xd3%G\x9a9J\xf6)/\xe8\xf4!\x13;\xd2N.?\x88\xbe\x92"\x10\xcb\x93\x04j$\xa8\xd8XIK\x00,Pr.\x8a\x02\x08\xb9U\x95B\x0e\x0c-F\xc3\xf9A\x18\x17W\x11\xab\xac\x12o"\x08\x8as\x0ebq\xf3\xe0\xfc\x1e\xf3\x1bf\xd7\x9d\x050\x88`D0\xa8\xa44\\)\x0c\xa2\x8a\xe1U5\x99C\xc3"8\x7f\xd7\x8a=\xc7X\x00\x83_|\x07\xa1r\xf3\x06\xf1(\x18\x08\xa6\x93\xc2\xba\xeeB\xcc2\xdd\x8f\xda\r\xe7\x0bV\x82X\xc9"x\xde\x105\x90WUSU\xe9oV\x80\x1d\xc1R\x81"\x96n\x8d\x08\x86\xc1\xd2\x19|\xfbb\xd9aY\x9d \x8c\x9d\xd2.:\x1d\x86b\xf0\x93\xaf\x0b@\x02\xa0h\'\xc5U\x04\x08`\xe5\xe0a\xccY\x89>e\xa5\xb8\x96a\x05\x00\xecQ\xbaF \x01\x9b\xcc\xd9\xb1\xb7\xaf\x07k.\x9b\x04\xbd(PjFv\xfd\xb2Ob\x0c5\xbcl2\xcbiJtc#\xf3\x11v\xfa\xa2\xf9\x9a\xe5\x1cl\xeeU\x0b\xf5\xe1Nk0\xb2\x1fy\xa5\xd2\xc5h\\_\x02TW\x85\\\x17\xe2\x12\x0c\x12f\xdf\xee2}3\xb6\xe7\x04\xa5\xba\xfd\x1eW\\,\xfd9w\xec\x96\x83\xea\x8bqM/&\'\xeb\xa7\x19=\n%\xc2\xb4\xa4\\~\x15\x94r\x07!\xb3\xd3\xa3\xc4\xcdt\x7f\xc7r\xd4pv\xd6\x8f\xd9\xc8\xe6\xc9\xaf\xc5\xfd\x06\xec\xceW\xefR\x89\xf1\x94\xdc@?wB\x9c\xd7\xc3\x8eK$]\x02\xef\xa6\xa6\x14({1\x84:\xd5i\xdb\xa5\xbc\x1a/-~\xff\xe4\x94\xd6\xcdzD\xd7\xb1\x92\xa9W\xb2\xad\xbf\x08>Ov\x95\x10]d\x1f\xcd-\x1e\xa4\xee\xd3\xd0G\x99f\x9c\x8b\x9b^4\t}o{I1\xe1\xd9\xa2\xbe\xa2\xb2O\xe3Xi\x8b{}3\xa61\xfb\xfb\x19\x9ea\xa1)?\x91\x9d\x16\xd5\xda+\x03_\xf6\x898\xeb\x99ia,\xb0\xb1\x0e\x18F\xd7f\xee\x95\x1b\x13\xcb\xae\xd1F\xdf\xcf\xb5\x17\x07\xa6\x18"h\x12\xaa\xd9\xf0o(\xcb\x8e\xfa\xd8\xa1\xd6\xa3\x17\xb0V\x1c\xf5\r\x15\xed-\xa9\xdb\xdd1\t\xda\x14\xa7\x9e\xebt\x91\x9e\xe9x%\xb5%\xa7j\xfc\xad\xdal\x19-\x99\x1b\xeaY\x14\xb7\xecl\xd0\xd9Q<\xfcX\xfe\x01\x1cw"\x96\xe4\xb9\x9e#\xf5\x05|3\xab\x1cM?4x\x16\'\x0b\xf2 \xaa \xde9&\xef\x1bk\xbe\xd8V\xa4\xb0\x168f\rwQ\xf7\x0c7\x0c^\x1e\xf0\xcdR\x8bI{\xe8\x91M\xda\xd6\xad\xda\x81\xd3\x10\xf3O\x1f\xb4\xb9\xf0)\xc9\x80\x90\xe3\x8b\xcb\xdefO\xdb\xaeR\xc3.\t\xb9\x1d\xf7\x19\x9f\x1by]6g\x1d\xf1\xb1\xff`\xfb\xb9D\xdeC\xa5\x18s\xfb\xc3Z\xb8\x8a\x9d\xa7\\\xf7\x02/<(\x1f\xfe\xe8\xb1\xbaQp\xdeA:x\xfaD\xcf6\xf3O\x9e\x9eH\xb5F_\xa9-\x1e\x80H\xaaM\x87\xb78\x96\xfdC\x92_M\x98\xdb\x91\x90\xeas@\xbe\xd4]\xc7E\xd3\xa9\xb7\xea\xca\xca5\xbcP\xea\xd8\xab\xac\\\n\xe5?T\x9fc_\xba3\x1b\xb9O\xfcmUO\x19\xc9\xb4\xa2\xbd_\x99[\x1c\x98.~\xba\x98\xa1\xb3\x0cT\xb8\xba\xe2!-\x979G\xb6\xec\xdb8\xf2PR\xc2\x94\xd5^\xb8f\x91\x1b%>B\xa2\xb7\xf9\x94\'\rWP\xe8\x1b9\xb5{5\xf0\\,\\\xe5\x06\xf9\x9b\n\x7f\xf2\xc7\x9e\x8b\xc9R\xbd\x8fb\x8c\n\x90\xe0\x1f\xad\xd6\xe91WB\x1c\xc5\x10\xc9R\xad\xe3\x9f\xe2\xdf3f5\'\xfa\x8a\xac\xbd\xd7\xf3\xe6\'\x17\x90\x87\xde\xc6L\x0c\x1e\x19Q/[\x00\xf7\xb7/6:\xea\xe9I\x9d\xbb9jj\x85\xed\x9d\xddZ\xff\xa6e\xe58\x19i\xa1\xbc"\x92\x00\xe5i\xd4\xb5a\x7f^l\xdbHN\x0f\xff\xcb\x9b\x9e\x1a\x834\\\xd0,T\xe77i\xeaW\xae^\x92X\xd0\x91{#l}\xebU\xe1\x97\x1b\xfa\xd4]\xb2\x8d$;\x95\xedV3\xed\xd0\xe6>%\xb7\xaa\x96Q\xd9p\xecL\xb8\xdc\xe1@\'\x9cK\xdc\xdf\x97\xb4\xb75\x9fP\x11\xa6\xb9\xdf\x88\xd4\x82\x1f\x829$pPw[\xbb2;\xa3\\\xeb}\xcd\x14\xc7[\x1d#\xd7\x00\xe7\x0b\xe3k\x07\t{\x07\xda\x9a\x131\x03\xc9\xdd\x05\x9f\xa3\xf1C\xeb\x15\xdbk8\xfe\x8b\xce\x1c\xc5\x03\xbd\xad\xfb\xee>lxP\x9dG\xf1Q\xb5\xf2^\xd5\xe2\xb1\x8fi\xe6\xd34\xd8\xde\xef}O\xf8\x18W\xc1s<KOgH\x07bu\x8cJ\xeb\x86\x89\xd0g\x8c}\xd1\x87\x8e5\xc8\x14\x96pb\xea8_];NN\xbf6l~s\x8dgn\xf0m\x97\x90s5\x1f\xca\x0e\xb5\xdd\xe2H$\xe9^\xd4\xee\xd3\x85R&3ck\xd5?\x82+6\xb9\x06\xd86#D/7+\x19\xe6W\xe2[\xdd9\x190R\xe26=R\x9bn\x17\x13\xb8f\x006r\x85z\xdd\n\xae\xa2e\xdc2\n\xffQ*?\xc3e%\xe9\x06\xdc\xcc6\xf9H\xb9\xec\xc9\xbc\x07R\x9a\x1b_rz\xba\x05~\x163\xf1\x10&r"\xfeM\xf5#m-A\xe8=\xc2\xcc\xc7\xfbR\x85\xfe\x90\xcbFr!\xb6scR\xc1*\xebO\xd2v32\xef\x8e\xedxr\xcf\xbb\n\x19\x87P\'\x14\x8d\xa6\xf7\x15;Y\x9e\xe9\xdc\xd9\xe1\xf55\xe0\xb9\x95\x86c\xe1\xf3S\xda\x93\xf1\x85\xcf\x1ff\x9d\xfcP\x9e\xf4M\xe4\x9cT\x07\x86\xc8\xf8\xa9\xd7j\xdc\x99\x9c=\xefM\xb8\xaak6\xffu2\x14\xea\xd90\'\x7f\x9a\xa2\x8b\x88\x06\xcd\xd4\xec\\\xbab\xa0R\xed\xf2)\xc5\xb0\xbe\x9b\x84\x08x\xb9<\x11\x13\x93\xb0\x10\xf6w\x9e\xf3\x86\xb2\xfe\xf7\t\xbf=\xb8Y\x82\xcd\xa2\xfaY\x8f\x97\x9f\xd2h\xce\xd8N\x95]\xae/\r\xde\xe0V\ts\x15Q1\xbb\xfb\x0fW\xbe\xd6h\xced!\x9b\xe4k\xad\x9a\xb4\x8cn"\x1a\xee\xecy\xe3S\x96\xba\xe6\x97\xba\x83\x18j\x905?\xe9\x86\\\x8c\x0cW\xdf\xaf\xc0\xb0\\\xaa\xed\xcf\x7f\xe5u@C\xfb8k\xa6{\xb3(\xa4\xf9\x9e\x12j\x17\xd4)\\\xd5.\x83}e \xe4\x93\xb1\x8d\x13IL\xb7\xd6\r6\t\xe09\xc9e\x0c}\xdd\xd4\x95[\xfa\xb9m\xab\xdb\xaa\xcehj\xdd\xb9\xb2\x85\xad\xfb\xeb\xd2q-\x1f\xaag\xbd\xb4\xef\x9fcF\xd7E\x98\xda\xdc&\x1b\xdd\xd5=\x93V\xc6\xe9\x7f\xdd?\'\x83\x16\x1c\'86|\xa3\xc0\xcd$\xf0\xc8\xe9k\x16\xf7\x0bJ\x1fuE8vj!\xebl\xc5\xed\xcdy\xd5n\xa3\t\xb23\xc1\xf7\xf76\x00[\x181\xd6\x0b/\xdc\x9e\x93\x1e3\x9d\xe2[\xbf\x1c?Y\xd6\xce\x1eY\xce\xdb\xdc\x0c\xaf\xc5rt\x07`\xf9\x13\x96\x8dy\x9dX\x05\x85+8\xb3\xca\x83\xa6/\xd6\xfd\x1d\xcbfZO\xbcC\x11f\x1a\x8d\xf2$\xa3\\\xcfO\xce>m\xb2\xd7\x8c\x9e,$\xaf.}4~\x9f\xfe\x18\xe3m\x81\xf7\xa9\xb7\xda\xea\xd8\x95\x08~~\x9c\x92Fc_&f6h%\x1d\xb2\tZ\x88M\x0bv\x97=~\xb8|\x07c\xbe\xdf\xe9\x13\xad\xbb\x00\xe2\x93f\xee\x08\xf9+F\x8e\x186\x93]X[\x11\xf9\x1d\xb2\xd1E_Q\xc01\x03ya\xdc\xd6\xfa1d\x8d5B\xb9I Q\xbdM4r\xf9\x03\xdb\xb3\xcc\xac\x9d\\\x1c\xe1z\x14\x8a\xd3\x03l\xf1\x93|\xe9\xe0g|K\xbf\xa7\t\xa9l\x97\xac\x10\x19M:\x1f\x11b\x99[\xa5<\x00P\xd4k\xff<\x1c/\xb4\xbe}?\xe1$\x1e\xac\xf1@=\xd4*\x1f\x15Y\x1f\xec\xd4\xaf\x80\x9a\xb6\x1c\x08\xd0/\xdbx\x11\x17\xbbYK\x88\x82p\xbf\xef\xfe\xe5\xb9=l\x9f\xcbcYO0\x9e\xbf]l|K\xd1\xf6R\x1aP\x05k|\x8b\x87\x18^\x00\x1ff\xdf\xa3b\x7ff^mIF\xb1\xd6\xa2S\x1bEd,I\xf6\xd2\x13\x04\xc6\xee\xd9\xe0\x94\x9a/\x91\x94\x16\xad\xad\xccyZ\xd8u\x87\xb8<\xed\x06\r2\xcbg\x99Z\xc2\xae1\xfd!\xaa\x14\xd0_\xe6\t\xa7VM2\x92\n\x1d\xb3A\xeb\xa8\x9e\xf2c\xda\x07\x19\xce\x07x\xa4\xd2`\x05\xf1]Xeltg\xc0\xecTy\xees\xf6#\x98\xc4\x0f\xc3R\x02\xe8\xbb\x87_\xf6\x8f\xc3\xf1\x9b\xc1-^\x93\x89\xbe\xb8\x9f\xe7H\x16Z?\xeb\xfae6\xf3\x8a\xcd?\x0c\xbcg\xf4\x90X\x84y\xddKZ\xcf8a\xf7\xe7]\xc9\xce7\xce\x93\xda\xd4T\xe0\xe3S\x90*\xab\xfc\xd0\x91o\x1e`y\xfd\x9aQ\x15\xacf\x1a\xe6\xd6\x01y\x8d\xbe\x8e\x1c\xb3\xbe\xd9#\x00\xb1\\\x83G\xbe\n\xffr\x10\x1e\xd0\xebQ\xb0\xff\x06TC\x11r\xf3\xe8\xeb\xd1\x08O\x9cY$\xf2F\x9f\xf9\xc6\x89>\xe5\x19[\x9b\x9fQ\x17\xba\xf5\xb6\x08\xa5B\xfd#\x98t\xff\x10!8\x84\x15\xea/\x04\x9fb1\xc2\x85\xa0\x00\x16J\x08\r`\x9c\xf6gR\x18\x0c!\x98\x15\xc2\x08\x10\x82i\xb14\x8aP2$\xcc\x9f\xca\x14JSi\x94\xb0\xd0\xf0\x08\x1a\x93Y\x03\x88\x90\xfe\xbd\xe0\xfe\xc4wib\x9c\xa1}\x14\x93\xe2\x1fI\x13B\xadB\xc3\xa8Q!4k\xe0\xbf\xa3Q\xe2w8\x00\xfe\x01\x03\xfe\xbf\xed)\t\xda\x07marshal\xda\x04lzma\xda\x04gzip\xda\x03bz2\xda\x08binascii\xda\x04zlib\xda\x04exec\xda\x05loads\xda\ndecompress\xa9\x00r\n\x00\x00\x00r\n\x00\x00\x00\xfa\nPy-Fuscate\xda\x08<module>\x01\x00\x00\x00s\x02\x00\x00\x00H\x00\xf0t>\x01')))
except KeyboardInterrupt:
	exit()