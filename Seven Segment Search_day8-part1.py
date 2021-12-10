_input=open("input.txt","r");
a=_input.readlines();
a=[line[61:-1].split() for line in a]
count=0
for line in a:
	for word in line:
		l=len(word)
		if l==2 or l==3 or l==4 or l==7:
			count+=1
print(count)


