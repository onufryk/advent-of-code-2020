field = []

with open('input.txt', 'r') as data:
  for line in data:
    print(line, end='')
    field.append(list(line)[:-1])

tree_count = 0
i = 0
j = 0

while i < len(field):
  n = len(field[i])
  symbol = field[i][j % n]
  print(i, j, symbol)
  if symbol == '#':
    tree_count += 1

  i += 1
  j += 3

print(tree_count)

