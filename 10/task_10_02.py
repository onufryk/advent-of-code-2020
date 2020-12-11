import collections

adapters = {0}
max_jolts = 0

with open('input.txt', 'r') as data:
  for line in data:
    val = int(line.rstrip())
    adapters.add(val)
    if max_jolts < val:
      max_jolts = val

max_jolts += 3

n = len(adapters)
adapters.add(max_jolts)

for v in range(len(adapters)):
  print('{:2d} '.format(v), end='')
print()

for v in adapters:
  print('{:2d} '.format(v), end='')
print()

ways = [0] * (max_jolts + 1)

ways[0] = 1

for i in range(1, len(ways)):
  ways[i] = 0
  if (i - 1) >= 0 and (i - 1) in adapters:
    ways[i] += ways[i-1]
  if (i - 2) >= 0 and (i - 2) in adapters:
    ways[i] += ways[i-2]
  if (i - 3) >= 0 and (i - 3) in adapters:
    ways[i] += ways[i-3]

print(ways[-1])

