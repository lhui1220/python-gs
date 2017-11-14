# encoding=utf-8

import time
import json

def fread(filename):
	f = open(filename,'r')
	for line in f:
		print line
	f.close()

def fwrite(filename):
	f = open(filename,'a')
	now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	val = ('zhangsan',42)
	f.write('[%s] 你好, %s!\n' % (now, str(val)))
	f.close()

def serialize(obj,filename):
	f = open(filename,'w')
	json.dump(obj, f)
	f.close()

def unserialize(filename):
	f = open(filename, 'r')
	obj = json.load(f)
	print str(obj)

# test file rw

filename = 'rw.txt'

fwrite(filename)

fread(filename)

# test json serialize

filename = 'serial.txt'

obj = {'id':1,'name':'张三','age':28}

serialize(obj,filename)

unserialize(filename)
