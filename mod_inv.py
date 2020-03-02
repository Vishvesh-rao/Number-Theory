def modular_inverse(a,m):

	t=1
	inverse=1
	while(t):

		if (a*inverse)%m==1:
			t=0
		inverse+=1

	return inverse-1

def GCD(a,b):
    
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

if __name__ == '__main__':

	t=1
	while(t):
		t=0
		m=input("Enter the modulo m.: ")
		a=input("Enter a no.: ")
		if GCD(a,m)!=1:
			t=1

	res=modular_inverse(a,m)
	print("modular inverse :",res)
