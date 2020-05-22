# Even/Odd
num = int(input("Enter a number : "))
if num%2 == 0 :
	print("%d number is an Even number"%(num))
else:
	print("%d number is an Odd number"%(num))

#Prime no.

if num > 0 :
	flag = 0 
	for x in range(1,num+1):
		if num%x == 0 :
			flag+=1	
			
	if flag == 2 :
		print("%d is a Prime number"%(num))
	else:
		print("%d is not a Prime number"%(num))

    
#Palindrome
sum1=0
count=0      
rev=num
while rev>0 :        
	r = rev % 10
	sum1 = sum1 * 10 + r
	rev = rev // 10 
	count+=1              #counting number of digit 
if num==sum1 :
	pass
	print("%d is a Palindome number"%(num))
else:
	print("%d number is not a Palindome number"%(num)) 	
		
#Armstrong no.
arm=num
sum2=0
while arm >0 :
	pass
	l = arm % 10
	c = l**count
	sum2 = sum2 + c
	arm = arm//10
if sum2==num:
	print("%d number is an Armstrong number"%(num))
else:
	print("%d number is an Armstrong number"%(num))