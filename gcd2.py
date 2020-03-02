
def GCD(a,b):
    
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

if __name__ == '__main__':
	
	x=input("Enter the 1 no.: ")
	y=input("Enter the 2 no.: ")
	res=GCD(x,y)
	print("GCD is :",res)

