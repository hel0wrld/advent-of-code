from collections import Counter
_input=open("output.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
import random
_input=open("input.txt","r");
a=_input.readlines();
a=[line[:-1] for line in a]
ops=[]
word='SCSCSKKVVBKVFKSCCSOV'
for line in a:
    x=line.split(' -> ')
    ops.append(x)
dw=''
for i in range(10):
	for k in range(len(word)-1):
		tw=word[k:k+2]
		for inst in ops:
			if inst[0]==tw:
				if word[k+1]==inst[0][1]:
					dw+=inst[0][0]+inst[1]
				else:
					dw+=inst[0][0]+inst[1]+inst[0][1]
	dw+=word[-1]
	word=dw
	dw=''
num=list(Counter(word).values())
num.sort()
print(num[-1]-num[0])
