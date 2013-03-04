# coding=utf-8
def show(arg):
    print arg
#字符串格式化，用元组来格式化
a = 'this is me: %s ,my age is: %s'
b = a % ('jty',22)
print b
#使用string模块的模板方法。注意若使用模板匹配后的结果，使用substitute的返回值。
from string import Template
s = Template('hello $x ,this is ${y}\'s son')
d = s.substitute(x='jty',y='tsp')
print d
#字符串格式化   %字符+转换标志(-左对齐，+加上符号  空白表示正数前保留空格 0表示位数不够填充0)+最小字符宽度+
# 点+精度(数字表示小数位数，字符串表示最大字符个数)+转换类型
print 'hello %d' % 10
print 'hello %.4f' % 10
import math
print 'hello %8.2f' % math.pi
print 'hello %2.8f' % math.pi
print 'hello %08.2f' % math.pi
print 'hello %+8.2f' % math.pi
print 'hello %+8.2f' % -math.pi
print 'hello %+8.2s' % 'helloworld!!!'
#字符串位置查找 find
print 'helloworld'.find('world')
print 'helloworld'.find('w43orld')
#还可以提供起始点与结束点
print '123456123'.find('123',1)
print '123456123'.find('123',1,5)
#lower 返回小写版本
show('12TWEWERWdsd3456'.lower())
#replace 替换某部分
show('123ldjka44123'.replace('123','999'))
#strip 去字符串两侧空格
show('   312321jkdajl  '.strip())