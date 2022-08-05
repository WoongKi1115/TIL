x = int(input())
count = 1

a,b = 1,1
while True:
	if count==x:
		print(str(a)+"/"+str(b))
		break
	else:
		if a==1 and b==2:
			a,b=b,a
		elif a == 1:
			if (a+b)%2==0:
				b=b+1
				count+=1
				b=b-1
				a=a+1
				count+=1
			else:
				a=a+1
				count+=1
		elif b==1:
			if (a+b)%2==0:
				b=b+1
				count+=1
				b=b-1
				a=a+1
				count+=1
			else:
				a=a+1
				count+=1
				a=a-1
				b=b+1
				count+=1
		else:
			if (a+b)%2==0:
				b=b-1
				a=a+1
				count+=1
			else:
				a=a-1
				b=b+1
				count+=1
