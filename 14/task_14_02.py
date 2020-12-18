import collections
import re

memory = collections.defaultdict(int)
current_mask = None

mem_command_pattern = re.compile(r'mem\[(\d+)\]')

def next_bit(current, index, mask, address, value):
  # print(' ' * (index-1), 'v')
  # print(mask)
  # print(address)
  # print(index, current)
  # print()

  if len(current) == len(mask):
    print(''.join(current), int(''.join(current), 2), value)
    memory[int(''.join(current), 2)] = value
    return

  if mask[index] == 'X':
    next_bit(current + ['0'], index + 1, mask, address, value)
    next_bit(current + ['1'], index + 1, mask, address, value)
  elif mask[index] == '1':
    next_bit(current + ['1'], index + 1, mask, address, value)
  else:
    next_bit(current + [address[index]], index + 1, mask, address, value)

with open('input.txt', 'r') as data:
  for line in data:
    # print(line.rstrip())
    command, argument = line.rstrip().split(' = ')
    if command == 'mask':
      current_mask = argument
    elif 'mem' in command:
      print('{:-^100}'.format(' NEXT '))
      if not current_mask:
        raise ValueError()
      result = mem_command_pattern.search(command)
      address = int(result.group(1))
      value = int(argument)
      bin_address = format(address, '036b')
      bin_value = format(value, '036b')
      print(current_mask)
      print(bin_address)

      next_bit([], 0, current_mask, bin_address, value)

    else:
      raise ValueError()

print(sum([v for k,v in memory.items()]))