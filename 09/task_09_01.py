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
    print(numbers[i])
    break
