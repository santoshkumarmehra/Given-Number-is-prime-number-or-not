n=int(input("enter the number = "))
count=0
for i in range(1,n+1):
	if n%i==0:
		count=count+1
if count==2:
	print("this is a prime number = ",True)
else:
	print("this is not a prime number = ",False)
		
				