data=input().split(',')
median=309
data=[abs(int(x)-median) for x in data]
print(sum(data))
