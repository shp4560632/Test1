#encoding=utf-8
import urllib2
import urllib
import re

proxy_info = {'host':'cnproxy.int.nokia-sbell.com','port':8080}
proxy_support = urllib2.ProxyHandler({"http":"http://%(host)s:%(port)d"%proxy_info})

opener=urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

html=urllib2.urlopen("http://www.baidu.com/",timeout=120).read()
print html
