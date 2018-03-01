#encoding: utf-8 -*-
import urllib2
import json
import re
import sys
from city import city

proxy_info = {'host':'cnproxy.int.nokia-sbell.com','port':8080}
proxy_support = urllib2.ProxyHandler({"http":"http://%(host)s:%(port)d"%proxy_info})

opener=urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

reload(sys)
sys.setdefaultencoding('utf-8')
s=u'城市名称:\n'
cityname = raw_input(s.encode('gb2312'))
#cityname = raw_input(s)
#cityname1=cityname.encode("gb2312")
print(cityname.decode('gbk').encode('utf-8'))
#print(cityname.encode('utf-8'))
#citycode = city.get(cityname.decode('gb2312').encode('gb2312'))
citycode = city.get(cityname.decode('gbk').encode('utf-8'))
print(citycode)

#html=urllib2.urlopen("http://172.24.208.168/#", timeout=60).read()
#print(html)

if citycode:
    url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content = urllib2.urlopen(url,timeout=30).read()
    print content


#print city
raw_input()
#data=json.loads(content)
#re=data['weatherinfo']
