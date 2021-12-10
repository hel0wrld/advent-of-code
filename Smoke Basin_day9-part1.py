import numpy as np
_input=open("input.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
l=[]
for line in a:
	x=list(line)
	x=[int(i) for i in x]
	l.append(x)
ans=[]
for i,y in enumerate(l):
	for j,x in enumerate(y):
		if i==0:
			if j==0:
				if l[0][0]<l[1][0] and l[0][0]<l[0][1]:
					ans.append(l[0][0])
			elif j==(len(y)-1):
				if l[i][j]<l[1][j] and l[i][j]<l[i][j-1]:
					ans.append(l[i][j])
			else:
				if l[i][j]<l[i+1][j] and l[i][j]<l[i][j-1] and l[i][j]<l[i][j+1]:
					ans.append(l[i][j])
		elif i==(len(l)-1):
			if j==0:
				if l[i][j]<l[i-1][j] and l[i][j]<l[i][j+1]:
					ans.append(l[i][j])
			elif j==(len(y)-1):
				if l[i][j]<l[i-1][j] and l[i][j]<l[i][j-1]:
					ans.append(l[i][j])
			else:
				if l[i][j]<l[i-1][j] and l[i][j]<l[i][j-1] and l[i][j]<l[i][j+1]:
					ans.append(l[i][j])
		elif j==0:
			if l[i][j]<l[i-1][j] and l[i][j]<l[i+1][j] and l[i][j]<l[i][j+1]:
				ans.append(l[i][j])
		elif j==(len(y)-1):
			if l[i][j]<l[i-1][j] and l[i][j]<l[i+1][j] and l[i][j]<l[i][j-1]:
				ans.append(l[i][j])
		else:
			if l[i][j]<l[i-1][j] and l[i][j]<l[i+1][j] and l[i][j]<l[i][j-1] and l[i][j]<l[i][j+1]:
				ans.append(l[i][j])
#ans=[i+1 for i in ans]
print(sum(ans)+len(ans))

