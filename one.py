#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2

url = "http://www.95598.cn/95598/outageNotice/queryOutageNoticeList"

headers = {
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

"""
orgNo=11401&outageStartTime=2018-01-29&outageEndTime=2018-02-05&
scope=&provinceNo=11102&typeCode=&lineName=&anHui=02
"""
formdata = {
"orgNo" : "41416",
"outageStartTime" : "2018-01-29",
"outageEndTime" : "2018-02-05",
"scope" : "",
"provinceNo" : "41101",
"typeCode" : "",
"lineName" : "",
"anHui" : "02"
}

# 经过urlencode转码
data = urllib.urlencode(formdata)

# 如果Request()方法里的data参数有值，那么这个请求就是POST
# 如果没有，就是Get
request = urllib2.Request(url, data = data, headers = headers)

print urllib2.urlopen(request).read()