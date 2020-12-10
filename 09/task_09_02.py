preamble_size = 25

numbers = []

with open('input.txt') as data:
  for line in data:
    numbers.append(int(line.rstrip()))

for i in range(preamble_size, len(numbers)):
  preamble = numbers[i-preamble_size:i]
  sums = set()
  for j in preamble:
    for k in preamble:
      if j != k:
        sums.add(j+k)
  if numbers[i] not in sums:
    break

weak_number = numbers[i]

print('Weak Number {} at position {}.'.format(weak_number, i))

range_size = 2

filtered_numbers = numbers[:i]
sum_found = False

cracked = 0

while range_size < len(filtered_numbers) and not sum_found:
  print('{:-^100}'.format(' RANGE {} '.format(range_size-1)))
  print('Range size {}.'.format(range_size))

  for i in range(len(filtered_numbers)-range_size+1):
    print('Range start {}'.format(i))
    irange = filtered_numbers[i:i+range_size]
    range_sum = sum(irange)
    print('Range {}'.format(irange))
    print('Range Sum {}'.format(range_sum))

    if range_sum == weak_number:
      sum_found = True
      cracked = sum([min(irange), max(irange)])
      break

  range_size += 1

print('Found {}'.format(cracked))