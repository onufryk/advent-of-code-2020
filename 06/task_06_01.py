total = 0

with open('input.txt', 'r') as data:
  current_group = ''
  for line in data:
    if line == '\n':
      total += len(set(current_group))
      current_group = ''
      print(total)
    else:
      print(line, end='')
      current_group = current_group + line[:-1]
      print(current_group)
      print(set(current_group))
      print(len(set(current_group)))

print(total)