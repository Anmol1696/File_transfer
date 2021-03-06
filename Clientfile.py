import socket
from chunks import *

def Main():
	host = '127.0.1.1'
	port = 5005
	
	s = socket.socket()
	s.connect((host,port))

	inp = raw_input('Enter Upload and Download : ')
	s.send(inp)
	
	while not inp == 'q':
		if inp == 'u':
			print 'U - Starting'
			addr = raw_input('Enter the location of the file : ')
			r = open(addr,'r')
			name = raw_input('Enter the name of the file : ')
			name = str(name) + '\n'*(100-len(name)) 
			s.send(name)
			al = r.readlines()
			r.close()
			data = ''
			for x in range(len(al)):
				data = data + al[x]
			len_1 = str(len(chunks(data)[0])-4)
			len_1 = '0'*(4-(len(len_1))) + len_1
			s.send(str(len_1))
			for x in chunks(data):
				s.send(str(x))
			print 'U - Done'
		elif inp == 'd':
			print 'D - Starting'
			addr = raw_input('Enter the location wher you want to download it of the file : ')
			temp = open(addr,'w')
			name = raw_input('Enter the name of the file : ')
			name = str(name) + '\n'*(100-len(name))
			s.send(name)
			len_1 = s.recv(4)
			while True:
				data = s.recv(int(len_1)+4)
				for x in range(int(len_1)): temp.write(str(data[x]))
				len_2 = ''
				for x in range(4): len_2 += str(data[int(len_1)+x])
				len_1 = len_2
				
				if len_1 == '0000':
					break
				data = ''
			temp.close()
			print 'D - Done'
		inp = raw_input('U or D : ')
		s.send(inp)
	s.close()
if __name__ == "__main__":
	Main()
