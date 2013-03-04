# coding=utf-8
#a = raw_input('请输入文字')
#print a[2]
#分片操作，类似substring之类
number = [1,2,3,4,5,6,7]
print number[0:3]
#注意，当左边索引比右边"晚"出现时(如3:0,-3:-1)就会返回一个空的序列
print number[-1:0]
print number[-3:-1]
print number[3:0]
#这样就可以拿到从倒数第三个到最后一个的片了。不写表示一"端"。
print number[-3:]
print number[:-3]
print number[:]
#带步长的分片，表示每多少个取一个。
print number[::2]
#与concat类似,但注意列表与字符串不能相加。
number2 = [2,3,4,5]
print number+number2
#序列乘法。。重复n个原来的序列
print number2*3
#in可以检测一个元素是不是在一个序列里
print 1 in number2
#更牛逼的是可以检测一段文字在不在字符串中
a = 'abcaaaccbbb'
print 'abcaa' in a
#跟js的split与join 类似的split与join
b = 'h,e,llo'
d = b.split(',')
print d
print ','.join(d)
#如果字符串每个字母之间是空白的，就需要用list方法
ee= 'hahha'
print list(ee)
#不能给位置不存在的列表赋值
#number[99] = '111' 报错
#删除某元素
print number2
del number2[2]
print number2
#又出现牛逼操作了，分片赋值，会把序列的一部分替换为另一部分，而且长度可以不同。（这里数组跟字符串都是序列）
number2[1:]='dhsjkajkl'
print number2
e= [1,2,3]
f=[4,5,6]
#实现追加的三种方法
#e = e+f
#e.extend(f)
e[len(e):]=f
print e
#count 统计某元素出现的个数
print [1,2,3,22,1,3,2].count(2)
#append 在列表末尾追加元素
#[1,2,3].append(4)
#index()找到元素的索引(第一个这个元素)
print [1,2,3,4,1].index(1)
#pop() 跟js完全类似，移除列表最后一个元素并返回这个元素
print [1,2,3].pop()
#在某个位置插入元素,插入的是一个。注意用分片赋值时，若插入一个元素要写成数组形式
a = [1,2,3]
b=[4,5,6]
a.insert(2,'haha')
b[2:2]=['haha']
print a,b
#remove()方法会删除某个指定值
d = [1,2,3]
d.remove(2)
print d
#reverse()可以反转
#sort与sorted 注意sort只会返回空值，改变原来的数组
#所以不要y = x.sort()，可以把y=x[:] 之后y.sort(),或者
a1 = [3,2,9,2,4]
b1 = sorted(a1)
print b1
#元组，括号括起来的，用逗号分隔的,也就下面几个操作
a= (1,2,3)
print a
print a[2]
print a[0:3]