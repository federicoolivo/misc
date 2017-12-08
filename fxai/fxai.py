# you can use metatrader4 to export data from the past
# I tested this program with the closing values of the daily chart of EUR/JPY
# values_to_confront is the lenght of the pattern. (x)
# the program will take the last x values and compare them with each block of x values in the past
# for each block of values, we calculate it's average value and place in an array the difference between that average and the values of the block
# we compare the difference of the last block with that of each other block
# when we find the block with the least difference, we can say that that's the most similar pattern to the recent price movements
# we then use the value that follows it to predict the next value, which should be similar

# the program does not correspond exactly to this description. 
# instead of confronting the last block with all the previous ones, it confronts all blocks with all the other ones
# this was done to allow me to test the program properly

# after testing the program with different values, i found out that the success rate it always around 50%
# this means that the market behaves in a random way and it's therefore unpredictable

values_str = []
values = []
values_to_confront = 20
filename = 'eurjpy'
good_results = 0
bad_results = 0

fin = open(filename)

# create array of strings
for value in fin:
	values_str.append(value.strip('\n'))

# remove terminator of text file
values_str.pop() 

# create array of floats
for value in values_str:
	values.append(float(value))

# array lenght
total_values = len(values)

#total_values = 20

for i in range(0, total_values - values_to_confront):
	print 'blocco ',
	print i,
	print '\t\trisultato: ',
	risultato = values[i + values_to_confront] - values[i + values_to_confront - 1]
	print risultato,
	#print '\tmedia: ',
	average = 0
	for l in range(i, i + values_to_confront):
		average += values[l]
	average = average / values_to_confront
	#print average,
	print ''
	#print 'valori:\t\t',
	#for l in range(i, i + values_to_confront):
	#	print values[l],
	#print ''
	difference = []
	for l in range(i, i + values_to_confront):
		difference.append(values[l] - average)
	print 'scostamenti:\t',
	for l in range(0, values_to_confront):
		print '%.3f' % difference[l],
	print ''

	minimum_difference = 1000000
	similar_block = -1

	for j in range(0, total_values - values_to_confront):
		if j != i:
			average2 = 0
			for p in range(j, j + values_to_confront):
				average2 += values[p]
			average2 = average2 / values_to_confront
			difference2 = []
			for p in range(j, j + values_to_confront):
				difference2.append(values[p] - average2)

			total_difference = 0
			for q in range (0, values_to_confront):
				a = difference[q]
				b = difference2[q]

				if a >= b:
					total_difference += a - b
				else:
					total_difference += b - a
			if total_difference < minimum_difference:
				minimum_difference = total_difference
				similar_block = j

			

	print 'similar_block: ',
	print similar_block,
	print '\trisultato: ',
	risultato2 = values[similar_block + values_to_confront] - values[similar_block + values_to_confront - 1]
	print risultato2
	if (risultato >= 0 and risultato2 >= 0) or (risultato < 0 and risultato2 < 0):
		good_results += 1
	else:
		bad_results += 1

	print 'scostamenti:\t',

	average3 = 0
	for c in range(similar_block, similar_block + values_to_confront):
		average3 += values[c]
	average3 = average3 / values_to_confront
	for c in range(similar_block, similar_block + values_to_confront):
		print '%.3f' % (values[c] - average3),

	print '\nminimum difference: ',
	print minimum_difference,
	print '\n'

print 'good results: %d' % good_results
print 'bad results: %d' % bad_results
print 'result: %.3f' % (100 * float(good_results) / (float(good_results) + float(bad_results)))




	













