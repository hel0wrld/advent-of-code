import numpy as np
_input=open("input.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
row,col=1500,1500
l=np.full(shape=(row,col),fill_value=' ',dtype=str)
for line in a:
	x=line.split(',')
	x=[int(i) for i in x]
	l[x[0]][x[1]]='#'
fold=[('x',655),('y',447),('x',327),('y',223),('x',163),('y',111),('x',81),('y',55),('x',40),('y',27),('y',13),('y',6)]
z=l.transpose()
for f in fold:
	if f[0]=='x':
		for i in range(0,row):
			for j in range(f[1],col):
				if j==f[1]:
					z[i][j]=' '
				elif z[i][j]=='#':
					z[i][j]=' '
					dis=j-f[1]
					z[i][f[1]-dis]='#'
		col=f[1]
	if f[0]=='y':
		for j in range(0,col):
			for i in range(f[1],row):
				if i==f[1]:
					z[i][j]=' '
				elif z[i][j]=='#':
					z[i][j]=' '
					dis=i-f[1]
					z[f[1]-dis][j]='#'
		row=f[1]
z=z[:row,:col]
for x in z:
	for m in x:
		print(m,end='')
	print()
