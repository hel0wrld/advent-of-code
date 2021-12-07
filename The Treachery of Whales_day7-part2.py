data=input().split(',')
mean=462
data=[abs(int(x)-mean)*(abs(int(x)-mean)+1)/2 for x in data]
print(sum(data))
