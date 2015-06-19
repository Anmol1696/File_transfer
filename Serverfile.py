import socket
from chunks import *

def Main():
	host = '10.3.192.50'
	port = 5005
	
	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	
	c,addr = s.accept()
	print 'Connection From : ' + str(addr)
	
	load = 0
	while True:
		if load == 0:
			dor = c.recv(1)		# Upload file for download
			
		else: load = 0
		if  str(dor)=='u':
			print 'U - Starting'
			r = str(c.recv(100))
			name = ''
			for x in r:
				if x == '\n': break
				name = name + x
			print 'Name.type -> ' + str(name)
			temp = open('/home/anmol/Documents/Python/Server/%s' % (str(name)),'w')
			print 'nice'
			len_1 = c.recv(4)
			while True:
				data = c.recv(int(len_1)+4)
				for x in range(int(len_1)): temp.write(str(data[x]))
				len_2 = ''
				for x in range(4): len_2 += str(data[int(len_1)+x])
				len_1 = len_2
				
				if len_1 == '0000':
					break
				data = ''
			temp.close()
			print 'U - Done'
		
		elif str(dor)=='d':
			print 'D - Staring'
			r = c.recv(100)
			name = ''
			for x in str(r):
				if x == '\n': break
				name = name + x
			print 'Name-> ' + name
			temp = open('/home/anmol/Documents/Python/Server/%s' % (str(name)),'r')
			al = temp.readlines()
			temp.close()
			data = ''
			for x in range(len(al)):
				data = data + al[x]
			len_1 = str(len(chunks(data)[0])-4)
			len_1 = '0'*(4-(len(len_1))) + len_1
			c.send(str(len_1))
			for x in chunks(data):
				c.send(str(x))
			
			print 'D - Done'
		elif str(dor) == 'q':
			break
	s.close()
	
if __name__ == "__main__":
	Main()
