def GCD(a,b):

	while(b):
		a,b=a,a/b

	return a 

if __name__ == '__main__':

	x=input("Enter the 1 no.: ")
	y=input("Enter the 2 no.: ")
	res=GCD(x,y)
	print("GCD is :",res)