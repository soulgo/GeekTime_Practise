#!/usr/bin/env python
#encoding:UTF-8

# from __future__ import print_function
import sys,os
'''
#判断文件是否存在
def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + 'does not exists')
    elif not os.access(filename,os.R_OK):
        raise SystemExit(filename + 'is not accessible')
    else:
        print(filename + 'is accessible')

if __name__ == '__main__':
    main()
'''
#通过cat /etc/passwd |python test_argv.py 将调用的内容输出到列表里
'''
def get_content():
    return sys.stdin.readlines()

print(get_content())
'''
'''
1、filename 前正在读取的文件名；
2、fileno ：文件的描述符；
3、filelineno ：正在读取的行是当前文件的第几行；
4、isfirstline ：正在读取的行是否当前文件的第 行；
5、isstdin fileinput：正在读取文件还是直接从标准输入读取内容
'''
'''
import fileinput
for line in fileinput.input():
    # print(line,end='')
    meta = [fileinput.filename(),fileinput.filelineno(),fileinput.fileno(),fileinput.isfirstline(),fileinput.isstdin()]
    print(*meta,end="")
    print(line,end="")
'''
#使用 getpass 库读取密码
'''
import getpass
#主要包含 getuser 函数和 getpass 函数 前者用来从环境变 中获取用户名'后者用来等待用户输入密码
user = getpass.getuser()
passwd = getpass.getpass('your password:')
print(user,passwd)
'''
#################################################
#使用 ConfigParse 解析配置文件
# python3更改成了小写
'''
1、configparser 中有很多的方法'其中与读取配置文件'判断配置项相关的方法有
2、sections ：返回一个包含所有章节的列表；
3、has_section ：判断章节是否存在；
4、items ：以元组的形式返回所有选项；
5、options ：返回一个包含章节下所有选项的列表；
6、has_option ：判断某个选项是否存在；
7、get、getboolean、getinit、getfloat ：获取选项的值
'''
'''
import configparser
cf = configparser.ConfigParser(allow_no_value=True)
cf.read('my.cnf')
print(cf.sections())
print(cf.has_section('client'))
print(cf.options('mysqld'))
print(cf.get('client','host'))
'''
'''
1、remove_section ：删除一个章节；
2、add_section ：添加一个章节；
3、remote_option ：删除一个选项；
4、set ：添加一个选项；
5、write ：将ConfigParser对象中的数据保存到文件中
'''
'''
cf.remove_section('client')
cf.add_section('lxj')
cf.set('lxj','host','127.0.0.1')
cf.set('lxj','port','3306')
#必须要写入才会生效
cf.write(open('my.cnf','w'))
print(cf.remove_section('DEFAULT'))
#清空除[DEFAULT]之外所有内容
cf.clear()
cf.write(open('my.cnf','w'))
print('DEFAULT' in cf)
cf.remove_option('DEFAULT', 'ForwardX11')
cf.set('DEFAULT', 'ForwardX11', 'no')
print(cf['DEFAULT']['ForwardX11'])
cf.write(open('my.cnf','w'))
'''
#################################################
#使用 argparse 解析命令行参数
'''
使用argparse模块、模仿MySQL 客户端、解析命令行的例子在这个例子中，
我们添加了5个选项，分别是 host、user、password、port、version 其中，
host、user、password 都是必传的参数，因为我们没有指定参数的类型，
所以这几个参数的取值都以字符串的形式保存。对于user、password、port选项，
为了提供易用性，可以使用"-u"、"-P"和"-p"的方式指定参数,port 取值是一个端口号，
因此，我们通过type项告诉 ArgumentParser, port 数的数据类型为整数。
'''
'''
import argparse
def _argparse():
	parser = argparse.ArgumentParser(description='Python-MySQL client')
	parser.add_argument ('--host',action='store',dest='host',required=True, help='connect to host')
	parser.add_argument ('-u','--user', action= 'store',dest='user ',required=True, help=' user for login' )
	parser.add_argument ('-p','--password',action= 'store',dest='password',required=True, help='password to use when connecting to server')
	parser.add_argument ('-P','--port', action='store', dest='port',default=3306,type=int,help='port number to use for connection or 3306 for default ' )
	parser.add_argument ('-v','--version', action='version',version='%(prog)s 0.1')
	return parser.parse_args()
def main() :
	parser = _argparse()
	conn_args = dict(host=parser.host, user=parser.user,password=parser.password, port=parser.port)
	print(conn_args)
if __name__ == '__main__':
	main()
'''
#logging模块
'''
import logging
import logging.config
#配置日志格式
# logging.basicConfig(filename='app.log',level=logging.INFO)
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename='app.log'
# )
#引用配置文件的方式
logging.config.fileConfig('logging.cnf')
logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
'''
#########################################################
#使用 click 解析命令行参数
'''
1、command ：使函数 hello 成为命令行接口；
2、option ：增加命令行选项；
3、echo ：输出结果，使用 echo 进行输出是为了获得更好的兼容性，因为 Python2中print是一个语句， Python3中 print是一个函数
'''
'''
1、default ：设置命令行参数的默认值；
2、help ：参数说明；
3、type ：参数类型，可以是 string、int、float 等；
4、prompt ：当在命令行中没有输入相应的参数时，会根据 prompt 提示用户输入；
5、nargs ：指定命令行参数接受的值的个数。
'''
'''
import click
@click.command()
@click.option('--count',default=1,help='Number of greetings')
@click.option('--name',prompt='Your name',help='The person to greet')
def hello(count,name):
    for x in range(count):
        click.echo('Hello %s!' %name)

if __name__ == '__main__':
    hello()
######
'''
#设置 prompt为True,就能够交互式地输入密码，设置 hide_input为True ，就可以隐藏我们的命令行输入，设置confirmation_prompt为True，就可以进行密码的两次验证
'''
@click.command()
@click.option('--password',prompt=True,hide_input=True,confirmation_prompt=True)
def encrypt(password):
    click.echo('Encrypting password to %s' % password.encode('rot13'))

if __name__ == '__main__':
    encrypt()
######
#执行程序，系统会自动进入编辑器
import click
message = click.edit()
print(message,end="")
'''
#####################################
# from prompt_toolkit import prompt
# while True:
#     user_input = prompt('>')
#     print(user_input)




































