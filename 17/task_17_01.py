import copy
import pprint
import numpy

EXTRA_POS = 7

def print_level(matrix):
  for row in matrix:
    print(''.join('X' if col != 0 else '.' for col in row))

def print_levels(scene):
  for i, level in enumerate(scene):
    print('{:-^80}'.format(' LEVEL {} '.format(i - EXTRA_POS)))
    print_level(level)

original = []
with open('input.txt', 'r') as data:
  for line in data:
    original.append([1 if c == '#' else 0 for c in line.rstrip()])

print('{:-^80}'.format(' ORIGINAL '))
print_level(original)

N = len(original)
M = len(original[0])

ROWS = N + EXTRA_POS * 2
COLS = M + EXTRA_POS * 2
LEVELS = 1 + EXTRA_POS * 2

field = numpy.zeros((LEVELS, ROWS, COLS), dtype=numpy.int16)

for i in range(N):
  for j in range(M):
    field[EXTRA_POS][i+EXTRA_POS][j+EXTRA_POS] = original[i][j]

print_levels(field)

for i in range(EXTRA_POS - 1):
  new_field = copy.deepcopy(field)
  for z in range(LEVELS):
    for x in range(ROWS):
      for y in range(COLS):
        # print('POINT', z, x, y, field[z][x][y])
        active = 0
        inactive = 0
        for zn in [z-1, z, z+1]:
          if zn < 0 or zn >= LEVELS:
            continue
          for xn in [x-1, x, x+1]:
            if xn < 0 or xn >= ROWS:
              continue
            for yn in [y-1, y, y+1]:
              if yn < 0 or yn >= COLS:
                continue
              if zn == z and xn == x and yn == y:
                continue
              if field[zn][xn][yn] == 1:
                active += 1
              else:
                inactive += 1

              # print(' NGHBR', zn, xn, yn, field[zn][xn][yn])
        # print('Active {}, Inactive {}'.format(active, inactive))
        if field[z][x][y] == 1:
          if active != 2 and active != 3:
            new_field[z][x][y] = 0
        else:
          if active == 3:
            new_field[z][x][y] = 1
  field = new_field
  print('{:-^80}'.format(' ITERATION {} '.format(i)))
  print_levels(field)

total_active = 0
for z in range(LEVELS):
  for x in range(ROWS):
    for y in range(COLS):
      total_active += field[z][x][y]

print('Total Active {}'.format(total_active))