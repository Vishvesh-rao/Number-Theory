def GCD(a,b):

	#prime_range=int(input("Enter the range till which to generate primes: "))
	gcd=1
	
	
	return gcd

def gen_prime(n):

	for i in range(2, Number + 1):
    if(Number % i == 0):
        isprime = 1
        for j in range(2, (i //2 + 1)):
            if(i % j == 0):
                isprime = 0
                break
            
        if (isprime == 1):
        	prime_facts.append(i)

     return prime_facts

if __name__ == '__main__':

	x=input("Enter the 1 no.: ")
	y=input("Enter the 2 no.: ")
	res=GCD(x,y)
	print("GCD is :",res)