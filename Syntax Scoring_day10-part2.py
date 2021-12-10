_input=open("input.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
bruh,close=[],[')',']','>','}']
new=[]
error=[]
for line in a:
	flag=0
	for c in line:
		if c in close:
			if bruh[-1]=='{' and c=='}':
				bruh.pop()
			elif bruh[-1]=='<' and c=='>':
				bruh.pop()
			elif bruh[-1]=='(' and c==')':
				bruh.pop()
			elif bruh[-1]=='[' and c==']':
				bruh.pop()
			else:
				flag=1
				break
		else:
			bruh.append(c)
	if flag==0:
		new.append(line)
		bruh.reverse()
		nooberror=0
		for x in bruh:
			if x=='(':
				nooberror=nooberror*5+1
			elif x=='[':
				nooberror=nooberror*5+2
			elif x=='{':
				nooberror=nooberror*5+3
			else:
				nooberror=nooberror*5+4
		error.append(nooberror)
	bruh.clear()
error.sort()
print(error[int(len(error)/2)])
