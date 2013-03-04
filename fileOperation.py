# coding=utf-8
#open读取文件，记得文件路径前面加r,模式可以选择 r 读模式  w写模式  a追加模式 b 二进制模式 + 读写模式。如果是图像，声音，或者跨平台的记得选择rb
txt = open(r'test2','rb')
#read可以指定读取多少个字符
print txt.read(1)
#注意readline与read方法，是读出的意思，也就是说有个游标，读完了游标向后移动了。
print txt.readline()
print txt.readline()
print txt.readline()
#记得操作完了把文件关掉
txt.close()
#牛逼操作来了，文件迭代器。可以直接像操作对象一样操作文件
txt = open(r'test2','rb')
for line in txt:
    print line
txt.close()
#可以计算行数
txt = open(r'test2','rb')
l = len(txt.readlines())
print l
txt.close()
#可以计算单词数目
txt = open(r'test2','rb')
text=''
while True:
    char = txt.read(1)
    if not char:
        break
    text+=char
words = len(text.split())
print words
txt.close()
#删除指定行,从0开始
def deleteLine(file,num):
    temp = open(file,'rb')
    text = temp.readlines()
    del(text[num])
    temp = open(file,'w');
    temp.write(''.join(text))
    temp.close()
deleteLine(r'test.txt',4)
