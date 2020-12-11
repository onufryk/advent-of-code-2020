import collections

adapters = [0]

with open('input.txt', 'r') as data:
  for line in data:
    adapters.append(int(line.rstrip()))

adapters.sort()

n = len(adapters)
adapters.append(adapters[-1] + 3)

diffs = collections.defaultdict(int)

for i in range(n):
  diffs[adapters[i+1] - adapters[i]] += 1

print(diffs[1]*diffs[3])