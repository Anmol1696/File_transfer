def chunks(data):
	msg = ['' for x in range(len(data)/1020 + 1)]
	for x in range(0,len(data)/1020 + 1):
		if x == len(data)/1020:	rep = len(data) - (x*1020)
		else: rep = 1020
		for y in range(rep):
			msg[x] += data[(x*1020)+y]
	for x in range(len(msg)):
		if x != len(msg) - 1:
			l = '0'*(4-len(str(len(msg[x+1])))) + str(len(msg[x+1]))
			msg[x] += l
		else :
			msg[x] += '0000'
	return msg
