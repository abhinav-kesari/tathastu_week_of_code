# Fabonacci Series
num = int(input("Enter limit : "))
a,b=0,1
for x in range(1,num+1):
	print(a,end=",")
	c=a+b
	a,b=b,c
	
	