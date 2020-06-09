non_prime_list = []
prime_list = []

def Generate_primes(number): 
	
	for num in range(2,number+1):
		if num not in non_prime_list:
			prime_list.append(num)

			for non_prime in range(num*num , number+1 , num):
				non_prime_list.append(non_prime)		


if __name__ == '__main__':

	number = int(input("Please enter the upper limit for prime no. generaion: "))

	Generate_primes(number)
	
	print("list of primes from 2 to {} is--> {} ".format(number,prime_list))

