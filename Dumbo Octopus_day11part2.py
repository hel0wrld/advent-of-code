_input=open("input.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
l=[]
for line in a:
	x=list(line)
	x=[int(i) for i in x]
	l.append(x)
print(l)
flash=0
c_flash=0
for day in range(10000):
	for i in range(10):
		for j in range(10):
			l[i][j]+=1
	count=0
	aa=15
	while aa>0:
		aa-=1
		for i in range(10):
			for j in range(10):
				if l[i][j]>9:
					count+=1
					l[i][j]=-10
					if i==0:
						if j==0:
							l[1][0]+=1 
							l[0][1]+=1
							l[1][1]+=1
						elif j==9:
							l[1][j]+=1 
							l[i][j-1]+=1
							l[1][j-1]+=1
						else:
						 	l[i+1][j]+=1  
						 	l[i+1][j+1]+=1  
						 	l[i+1][j-1]+=1  
						 	l[i][j-1]+=1  
						 	l[i][j+1]+=1
					elif i==9:
						if j==0:
							l[i-1][j]+=1 
							l[i][j+1]+=1
							l[i-1][j+1]+=1
						elif j==9:
							l[i-1][j]+=1	
							l[i][j-1]+=1
							l[i-1][j-1]+=1					
						else:
							l[i-1][j]+=1	
							l[i-1][j+1]+=1	
							l[i-1][j-1]+=1	
							l[i][j-1]+=1	
							l[i][j+1]+=1
					elif j==0:
						l[i-1][j]+=1	
						l[i+1][j]+=1	
						l[i][j+1]+=1
						l[i+1][j+1]+=1
						l[i-1][j+1]+=1
					elif j==9:
						l[i-1][j]+=1	
						l[i+1][j]+=1	
						l[i][j-1]+=1
						l[i+1][j-1]+=1
						l[i-1][j-1]+=1
					else:
						l[i-1][j]+=1
						l[i-1][j-1]+=1
						l[i-1][j+1]+=1
						l[i+1][j]+=1
						l[i+1][j-1]+=1
						l[i+1][j+1]+=1
						l[i][j-1]+=1
						l[i][j+1]+=1
		if count==0:
			break
	for i in range(10):
		for j in range(10):
			if l[i][j]<0:
				c_flash+=1
				l[i][j]=0
	if c_flash==100:
		flash=day
		break
	c_flash=0
	for line in l:
		print(line)
	print()
print(flash+1)
