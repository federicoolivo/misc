# once I wrote a similar program that generated random formulas and checked how many primes they could find consecutively
# I noticed that these formulas were ofter parabolas like ax^2 + bx + c
# this program only generates these formulas
# primes_to_find is the minimum number of primes that your formulas must be able to generate
# by default the program will create 10 of these formulas

# analising the data I optimised the program and found a formula that generates 80 primes
# x^2 - 79x + 1601
# later I found out that Euler already found it 300 years ago and apparently there's no formula to generate more primes than that

import random
import math

def sign():
	if(random.randint(0,1) == 0):
		return -1
	else:
		return 1


def is_prime(x):

	if x < 0:
		x *= -1

	for i in range(int(math.sqrt(x)),x):
		if x % i == 0:
			return False
		else:
			i += 1
	return True


def print_equation(a,b,c):
	equation = ''
	if a > 0:
		equation += '+'
	equation += str(a) + 'x^\t'
	if b > 0:
		equation += '+'
	equation += str(b) + 'x\t'
	if c > 0:
		equation += '+'
	equation += str(c)

	print equation,

def check_if_x_numbers_are_prime(a,b,c, primes_to_find):

	maximum_primes_to_find = 1000
	prime_count = 0

	for i in range (1, maximum_primes_to_find):
		if is_prime(a*i*i + b*i + c) == True:
			prime_count += 1
		else: 
			break

	return prime_count


primes_to_find = 10

runs = 0

for i in range(0,10):

	found_equation = False

	while found_equation == False:

		runs += 1

		# the sign are always in the order + - +

		a = 1 		# 'a' is always 1 or -1

		# 'b' is always odd
		# 'b' will create an equation that will find at least 'b' primes

		b = random.randint(primes_to_find * 2, 300) / 2 * -1

		# 'c' is always a prime
		c = 2
		while is_prime(c) == False:
			# 'c' is always higher than 10 * 'b'
			c = random.randint(1,5000)


		prime_count = check_if_x_numbers_are_prime(a,b,c, primes_to_find)

		if prime_count >= primes_to_find:

			print_equation(a,b,c)

			print '\tcount: ' + str(prime_count)

			#for i in range (1, prime_count+1):
			#	print a*i*i + b*i + c

			found_equation = True

		if runs % 10000 == 0:
			print runs

print 'total runs = ' + str(runs)
			

