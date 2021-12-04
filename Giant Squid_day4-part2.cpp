import numpy as np
_input=open("input.txt","r");
_output=open("output.txt","w");
a=_input.readlines();
data=a[0][:-1].split(',')
print(data)
num=(len(a)-1)/6
board=[[0]*5]*5
#boards=[board]*int(num)
n=0
_matrices=open("matrices.txt","w");
for lines in a[2:]:
	_matrices.write(lines)
_matrices.close()
m=np.loadtxt("matrices.txt", dtype="int")
#print(m)
boards=np.array_split(m,num)
inz=[]
for board in boards:
	inz.append(board)
print(inz)
flag,final,num_done=(0,0,0)
board_done = [0]*int(num)
for number in data:
	for idx, board in enumerate(inz):
		for row in board:
			for index, item in enumerate(row):
				if item.item()==int(number):
					row[index]=-1;
		row_total=[sum(x) for x in board]
		col_total=[sum(x) for x in zip(*board)]
		print("row_total=",row_total," col_total=",col_total)
		if -5 in row_total or -5 in col_total:
			board_done[idx]=1
		if not 0 in board_done:
			flag=1
			final_sum=0
			for row in board:
				for x in row:
					if x==-1:
						continue
					else:
						final_sum+=x
			final=final_sum*int(number)
			print("final_sum",final_sum,"number",number)
			break
	if flag==1:
		break


print(final)#the final answer
      

print(type(inz[0][0][0].item()))
print(type(int(data[0])))
'''print(boards)
print(data)
print(type(data))
data2=a[2][:-1].split(',')
print(data)
print(type(data))
_output.write(a[0])
_output.write(a[1])
_output.write(a[2])
print(type(a[0]))'''
_input.close()
_output.close()
