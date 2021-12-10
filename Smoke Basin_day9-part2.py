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
					ans.append((i,j))
			elif j==(len(y)-1):
				if l[i][j]<l[1][j] and l[i][j]<l[i][j-1]:
					ans.append((i,j))
			else:
				if l[i][j]<l[i+1][j] and l[i][j]<l[i][j-1] and l[i][j]<l[i][j+1]:
					ans.append((i,j))
		elif i==(len(l)-1):
			if j==0:
				if l[i][j]<l[i-1][j] and l[i][j]<l[i][j+1]:
					ans.append((i,j))
			elif j==(len(y)-1):
				if l[i][j]<l[i-1][j] and l[i][j]<l[i][j-1]:
					ans.append((i,j))
			else:
				if l[i][j]<l[i-1][j] and l[i][j]<l[i][j-1] and l[i][j]<l[i][j+1]:
					ans.append((i,j))
		elif j==0:
			if l[i][j]<l[i-1][j] and l[i][j]<l[i+1][j] and l[i][j]<l[i][j+1]:
				ans.append((i,j))
		elif j==(len(y)-1):
			if l[i][j]<l[i-1][j] and l[i][j]<l[i+1][j] and l[i][j]<l[i][j-1]:
				ans.append((i,j))
		else:
			if l[i][j]<l[i-1][j] and l[i][j]<l[i+1][j] and l[i][j]<l[i][j-1] and l[i][j]<l[i][j+1]:
				ans.append((i,j))
def explore(i,j):
	if (i>len(l)-1 or i<0) or (j>len(l[0])-1 or j<0) or l[i][j]==9 or l[i][j]==-1:
		return 0
	print(l[i][j],i,j)
	l[i][j]=-1
	return 1+explore(i,j+1)+explore(i,j-1)+explore(i+1,j)+explore(i-1,j)
print(ans)
last=[]
for pit in ans:
	last.append(explore(pit[0],pit[1]))
last.sort()
print(last[-1]*last[-2]*last[-3])
