# find the number of divisor
def divisor(n):
	divisor=0
	for i in range(1, n//2+1):
		if n%i==0:
			divisor+=1
			
	return divisor+1

n=int(input())
print(divisor(n))