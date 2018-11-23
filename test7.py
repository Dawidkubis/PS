def generate_primes(lim):
	nums = list(range(2,lim))
	primes = []
	while nums != []:
		primes.append(nums[0])
		nums = [i for i in nums if i % primes[-1] != 0]
	return primes


primes = generate_primes(1000000)
print(primes[0])