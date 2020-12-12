def print_generation(generation):
  for row in generation:
    print(''.join(row))

def print_line(title=''):
  print('{:-^100}'.format(' {} '.format(title)))

def deep_copy(generation):
  new_generation = []
  for row in range(len(generation)):
    new_generation.append(['.'] * len(generation[row]))

  for row in range(len(generation)):
    for col in range(len(generation[row])):
      new_generation[row][col] = generation[row][col]

  return new_generation

def occupied_seats(generation, row, column):
  nrows = len(generation)
  ncols = len(generation[0])

  n = 0
  i = row - 1
  while i >= 0:
    if generation[i][column] == 'L':
      break
    if generation[i][column] == '#':
      n += 1
      break
    i -= 1

  i = row + 1
  while i < nrows:
    if generation[i][column] == 'L':
      break
    if generation[i][column] == '#':
      n += 1
      break
    i += 1

  i = column - 1
  while i >= 0:
    if generation[row][i] == 'L':
      break
    if generation[row][i] == '#':
      n += 1
      break
    i -= 1

  i = column + 1
  while i < ncols:
    if generation[row][i] == 'L':
      break
    if generation[row][i] == '#':
      n += 1
      break
    i += 1

  i = row - 1
  j = column - 1
  while i >= 0 and j >= 0:
    if generation[i][j] == 'L':
      break
    if generation[i][j] == '#':
      n += 1
      break
    i -= 1
    j -= 1

  i = row + 1
  j = column + 1
  while i < nrows and j < ncols:
    if generation[i][j] == 'L':
      break
    if generation[i][j] == '#':
      n += 1
      break
    i += 1
    j += 1

  i = row - 1
  j = column + 1
  while i >= 0 and j < ncols:
    if generation[i][j] == 'L':
      break
    if generation[i][j] == '#':
      n += 1
      break
    i -= 1
    j += 1

  i = row + 1
  j = column - 1
  while i < nrows and j >= 0:
    if generation[i][j] == 'L':
      break
    if generation[i][j] == '#':
      n += 1
      break
    i += 1
    j -= 1

  return n

origin = []

with open('input.txt', 'r') as data:
  for line in data:
    origin.append(list(line.rstrip()))

print_generation(origin)
print_line(' START ')

current_generation_number = 0
any_seat_changed = True
number_of_occupied_seats = 0
generations = [origin]

nrows = len(origin)
ncols = len(origin[0])

while any_seat_changed:
  current_generation_number += 1

  print_line(current_generation_number)

  previous_generation = generations[current_generation_number-1]

  generations.append(deep_copy(previous_generation))

  current_generation = generations[current_generation_number]

  any_seat_changed = False
  number_of_occupied_seats = 0
  for row in range(0, nrows):
    for col in range(0, ncols):
      # print(row, col, previous_generation[row][col])
      # print(occupied_seats(previous_generation, row, col))
      if previous_generation[row][col] == '#':
        number_of_occupied_seats += 1
      if previous_generation[row][col] == '.':
        continue
      elif previous_generation[row][col] == 'L':
        nseats = occupied_seats(previous_generation, row, col)
        if nseats == 0:
          current_generation[row][col] = '#'
          number_of_occupied_seats += 1
          any_seat_changed = True
          # print('change to #')
      elif previous_generation[row][col] == '#':
        nseats = occupied_seats(previous_generation, row, col)
        if nseats >= 5:
          # print('change to L')
          current_generation[row][col] = 'L'
          number_of_occupied_seats -= 1
          any_seat_changed = True
      else:
        raise ValueError('Invalid character!')

      # print()
      # print_line('previous')
      # print_generation(previous_generation)
      # print_line('current')
      # print_generation(current_generation)

  print_generation(generations[current_generation_number])
  # break

print(number_of_occupied_seats)