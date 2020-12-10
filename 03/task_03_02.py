import operator
from itertools import accumulate
from functools import reduce

field = []

with open('input.txt', 'r') as data:
  for line in data:
    print(line, end='')
    field.append(list(line)[:-1])

deltas = [(1,1), (1, 3), (1, 5), (1, 7), (2, 1)]
tree_counts = []

for step_i, step_j in deltas:
  tree_count = 0
  i = 0
  j = 0

  while i < len(field):
    n = len(field[i])
    symbol = field[i][j % n]
    print(i, j, symbol)
    if symbol == '#':
      tree_count += 1

    i += step_i
    j += step_j

  tree_counts.append(tree_count)

print(tree_counts)
print(list(accumulate(tree_counts, operator.mul)))
print(reduce(lambda x,y: x * y, tree_counts, 1))
