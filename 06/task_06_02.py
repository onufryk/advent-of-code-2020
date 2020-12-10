total = 0

with open('input.txt', 'r') as data:
  current_group = set('abcdefghijklmnopqrstuvwxyz')
  for line in data:
    print(line, end='')
    if line == '\n':
      total += len(current_group)
      current_group = set('abcdefghijklmnopqrstuvwxyz')
      print('Total', total)
    else:
      current_group &= set(line[:-1])
      print(current_group)

print(total)