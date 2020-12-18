import collections
import re

memory = collections.defaultdict(int)
current_mask = None

mem_command_pattern = re.compile(r'mem\[(\d+)\]')

with open('input.txt', 'r') as data:
  for line in data:
    # print(line.rstrip())
    command, argument = line.rstrip().split(' = ')
    if command == 'mask':
      current_mask = argument
      print(argument)
    elif 'mem' in command:
      if not current_mask:
        raise ValueError()
      result = mem_command_pattern.search(command)
      address = int(result.group(1))
      value = int(argument)
      bin_value = format(value, '036b')

      new_value_bits = []
      for i in range(len(current_mask)):
        if current_mask[i] == 'X':
          new_value_bits.append(bin_value[i])
        else:
          new_value_bits.append(current_mask[i])
      new_value = int(''.join(new_value_bits), 2)
      memory[address] = new_value
    else:
      raise ValueError()

print(sum([v for k,v in memory.items()]))