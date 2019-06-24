def erastotenes_sieve(n):

 	natural_nums = [x for x in range(2, n+1)]
 	selected_nums = {natural_nums[x]:False for x in range(len(natural_nums))}

 	for i in range(2, int(n**0.5)):
 		if selected_nums[i]==False:
 			for j in range(i, int(n/i)):
 				selected_nums[i*j]=True
 	return [k for k,x in selected_nums.items() if x==False]

def find_next_prime(n):
	x, y = n, 2*n
	for p in range(x, y):
		for i in range(2, p):
			if p % i == 0:
				break
		else:
			return p
	return None 

def find_4_primes(n):
	if n/4>max_primes:
		prime_div_4 = find_next_prime(int(n/4))
		ctr = 1
		primes_to_sum = []
		while prime_div_4 > int(n/4):
			prime_div_4 = find_next_prime(int(n/4)-ctr)
			ctr += 1
		primes_to_sum.append(prime_div_4)
		total_sum = n - primes_to_sum[-1]
		if (total_sum-primes[0])%2 == 0:
			primes_to_sum.append(primes[0])
			total_sum -= primes[0]
		elif (total_sum-primes[1])%2 == 0:
			primes_to_sum.append(primes[1])
			total_sum -= primes[1]
		for x in range(len(primes)-1, -1, -1):
			next_prime = find_next_prime(total_sum-primes[x])
			if primes[x] + next_prime == total_sum:
				primes_to_sum += [primes[x], next_prime]
				return primes_to_sum
		return None
	else:	
		primes_div_4 = [2]
		primes_div_4 += [x for x in primes if x < n/4]
		if primes_div_4[-1] * 4 == n:
			return [primes_div_4[-1], primes_div_4[-1], primes_div_4[-1], primes_div_4[-1]]
		primes_to_sum = [primes_div_4[-1]]
		total_sum = n - primes_to_sum[-1]
		if (total_sum-primes[0]) % 2 == 0:
			primes_to_sum.append(primes[0])
			total_sum -= primes[0]
		elif (total_sum-primes[1]) % 2 == 0:
			primes_to_sum.append(primes[1])
			total_sum -= primes[1]

		for x in primes:
			for y in primes:
				if x + y == total_sum:
					primes_to_sum += [x,y]
					return primes_to_sum
		return None






def read_input():
	numbers = []
	try:
		while (True):
			number = int(input().strip())
			numbers.append(number)
	except EOFError:
		pass
	return numbers

max_primes = 1000000 
numbers = read_input()
primes = erastotenes_sieve(max_primes)


for number in numbers:
	if number<8:
		print ("Impossible.")
	else:
		prime_sum = find_4_primes(number)
		if prime_sum != None:
			print ("{} {} {} {}".format(prime_sum[0], prime_sum[1], prime_sum[2], prime_sum[3]))
		else:
			print ("Impossible.")

