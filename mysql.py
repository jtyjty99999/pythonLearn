# coding=utf-8
import MySQLdb

try:
    conn=MySQLdb.connect(host='192.168.1.7',user='root',passwd='abc123',port=3306)
    cur=conn.cursor()
#建立数据库
    cur.execute('drop database python')
    cur.execute('create database if not exists python')
#选择数据库
    conn.select_db('python')
#建表,execute执行sql语句
    cur.execute('create table test(id int,info varchar(20))')
    values=[]
    for i in range(20):
            values.append((i,'hi rollen'+str(i)))
#批量插入，速度非常快
    cur.executemany('insert into test values(%s,%s)',values)
#更新单个数据
    cur.execute('update test set info="I am rollen" where id=3')
    count=cur.execute('select * from test')
    print 'there has %s rows record' % count
#cursor用来执行命令的方法:
#callproc(self, procname, args):用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
#execute(self, query, args):执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
#executemany(self, query, args):执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
#nextset(self):移动到下一个结果集

#cursor用来接收返回值的方法:
#fetchall(self):接收全部的返回结果行.
#fetchmany(self, size=None):接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
#fetchone(self):返回一条结果行.
#scroll(self, value, mode='relative'):移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果 mode='absolute',则表示从结果集的第一行移动value条.
#hi rollen0  初始游标,也是设置cur.scroll(0,mode='absolute')后的游标。执行fetchone后，会返回这条记录，同时游标下移
#hi rollen1 从初始游标fetchone后的游标
#hi rollen2 设置cur.scroll(2,mode='absolute')处的游标
#I am rollen
#hi rollen4
#hi rollen5
#hi rollen6
    result=cur.fetchone()
    print result
    print 'ID: %s info %s' % result
    results=cur.fetchmany(5)
    for r in results:
        print r
    print '=='*10
    cur.scroll(2,mode='absolute')
    result=cur.fetchone()
    print result
    cur.scroll(0,mode='absolute')
    results=cur.fetchall()
    for r in results:
        print r[1]

#提交事务，必须！
    conn.commit()
    cur.close()
    conn.close()

except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])