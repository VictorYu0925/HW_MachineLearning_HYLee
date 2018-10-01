filename = '/words.txt'
file1 = open(filename, 'r', encoding='UTF-8')
content = file1.read()
file1.close()


ordercount = 0
dicwordorder = []
dicwordcount = {}

for words in content.split():
	if(dicwordcount.get(words) == None):
		dicwordorder.append(words)	
		ordercount = ordercount + 1
		dicwordcount[words] = 1

	else:
		dicwordcount[words] = dicwordcount[words]+1
#		print(words, dicwordcount[words])		

writename = '/hw0answer.txt'
file2 = open(writename, 'w', encoding='UTF-8')
num = 0
for words in dicwordorder:
	num = num + 1	
	file2.write(str(num) + ' ' + words + ' ' + str(dicwordcount[words]) + '\r\n')
