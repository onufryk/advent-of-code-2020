import collections

adapters = [0]

with open('input.txt', 'r') as data:
  for line in data:
    adapters.append(int(line.rstrip()))

adapters.sort()

n = len(adapters)
adapters.append(adapters[-1] + 3)

i = len(adapters) - 1

for v in range(len(adapters)):
  print('{:2d} '.format(v), end='')
print()

for v in adapters:
  print('{:2d} '.format(v), end='')
print()

ways = [0] * len(adapters)

ways[0] = 1

while i > 0:
  print('{:-^100}'.format(' ITERATION '))
  diff = adapters[i] - 3
  c = 0
  j = i - 1
  print('{:2d} {:2d} {:2d}'.format(i, adapters[i], diff))

  print(' {:2d} {:2d} {:2d}'.format(j, adapters[j], c))
  while j > 0 and adapters[j] >= diff:
    c += 1
    j -= 1
    print('  {:2d} {:2d} {:2d}'.format(j, adapters[j], c))

  ways[i] = c

  i -= 1

for v in adapters:
  print('{:2d} '.format(v), end='')
print()

for v in ways:
  print('{:2d} '.format(v), end='')
print()

