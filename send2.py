# coding:utf-8
import httplib,urllib,time #加载模块
#定义一些文件头
headers = {"Content-Type":"application/x-www-form-urlencoded",
           "Connection":"Keep-Alive"};
#与网站构建一个连接
#开始进行数据提交   同时也可以使用get进行
start = time.time()
i=10000
while(i>1):
    conn = httplib.HTTPConnection("192.168.1.3:7379");
    conn.request(method="GET",url="/INCR/count",body='',headers=headers);
    print i;
    i-=1
print time.time()-start