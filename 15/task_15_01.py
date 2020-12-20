import collections
import pprint


nums = []
with open('input.txt', 'r') as data:
  for line in data:
    nums = [int(i) for i in line.rstrip().split(',')]

print(nums)

memo = collections.defaultdict(list)

turn = 0
turns = []

for i, n in enumerate(nums):
  turn += 1
  turns.append(n)
  memo[n].append(turn)

print(turn)
print(turns)
pprint.pprint(memo)

while turn != 2020:
  turn += 1
  last_number_spoken = turns[-1]
  if len(memo[last_number_spoken]) == 1:
    turns.append(0)
    memo[0].append(turn)
  else:
    new_number = memo[last_number_spoken][-1] - memo[last_number_spoken][-2]
    turns.append(new_number)
    memo[new_number].append(turn)

print(turns[-1])
