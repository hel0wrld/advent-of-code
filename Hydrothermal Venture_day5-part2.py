import numpy as np
_input=open("input.txt","r");
a=_input.readlines();
m=np.zeros(shape=(1000,1000),dtype=int)
for line in a:
	sn=line[:-1].replace(" -> ",",")
	v=sn.split(',')
	v=[int(i) for i in v]
	#print(type(v[0]))
	print(v)
	if v[0]==v[2]: 				#x is same so iterate y
		print("x same")
		if(v[1]>v[3]):
			v[1],v[3]=v[3],v[1]
		for i in range(v[1],v[3]+1):
			m[v[0]][i]+=1
			#print("x,y",v[0],i)
		continue
	if v[1]==v[3]: 				#y is same so iterate x
		print("y same")
		if(v[0]>v[2]):
			v[0],v[2]=v[2],v[0]
		for i in range(v[0],v[2]+1):
			m[i][v[1]]+=1
			#print("x,y",i,v[1])
		continue
	if v[0]+v[1]==v[2]+v[3]:	#right diagonal syntactically but left as transposed
		print("left diagonal")
		if v[0]>v[2]:
			v[0],v[2]=v[2],v[0]
			v[1],v[3]=v[3],v[1]
		for i in range(v[0],v[2]+1):
			m[i][v[0]+v[1]-i]+=1
	if v[2]-v[0]==v[3]-v[1]:	#left diagonal syntactically but right as transposed
		print('right diagonal')
		if v[0]>v[2]:
			v[0],v[2]=v[2],v[0]
			v[1],v[3]=v[3],v[1]
		for i in range(v[0],v[2]+1):
			m[i][i-v[0]+v[1]]+=1
print(m.transpose())
count=0
for row in m:
	for x in row:
		if(x>=2):
			count+=1
print(count)
