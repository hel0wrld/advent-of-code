import numpy as np
_input=open("input.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
l=np.full(shape=(1500,1500),fill_value=' ',dtype=str)
for line in a:
	x=line.split(',')
	x=[int(i) for i in x]
	l[x[0]][x[1]]='#'
fold=[('x',655)]
z=l.transpose()
for f in fold:
	if f[0]=='x':
		for i in range(0,1500):
			for j in range(f[1],1500):
				if j==f[1]:
					z[i][j]=' '
				elif z[i][j]=='#':
					z[i][j]=' '
					dis=j-f[1]
					z[i][f[1]-dis]='#'
	if f[0]=='y':
		for j in range(0,1500):
			for i in range(f[1],1500):
				if i==f[1]:
					z[i][j]=' '
				elif z[i][j]=='#':
					z[i][j]=' '
					dis=i-f[1]
					z[f[1]-dis][j]='#'
print((z=='#').sum())
