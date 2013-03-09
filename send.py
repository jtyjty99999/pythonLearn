# coding:utf-8
import httplib,urllib #加载模块
#urllib可以打开网站去拿
#res = urllib.urlopen('http://baidu.com');
#print res.headers
#定义需要进行发送的数据     
params = urllib.urlencode({'param':'6'});
#定义一些文件头     
headers = {"Content-Type":"application/x-www-form-urlencoded",
           "Connection":"Keep-Alive",'Content-length':'200'};
#与网站构建一个连接
conn = httplib.HTTPConnection("localhost:8765");
#开始进行数据提交   同时也可以使用get进行
conn.request(method="POST",url="/",body=params,headers=headers);
#返回处理后的数据
response = conn.getresponse();
print response.read()
#判断是否提交成功
if response.status == 200:
    print "发布成功!^_^!";
else:
    print "发布失败\^0^/";
#关闭连接
conn.close();