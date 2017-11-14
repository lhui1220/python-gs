f = None
try:
#	print str(1/0)
	f = open('error.log','r')
	
except ZeroDivisionError as e:
	print str(e)
except IOError as e:
	print str(e)
finally:
	if f:
		print 'close file'
		f.close()
