_input=open("input.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
bruh,close=[],[')',']','>','}']
error=[]
for line in a:
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
				print("error in line",line)
				if(c==')'):
					error.append(3)
				elif (c==']'):
					error.append(57)
				elif (c=='}'):
					error.append(1197)
				else:
					error.append(25137)
				break
		else:
			bruh.append(c)
	bruh.clear()
print(error)
print(sum(error))


