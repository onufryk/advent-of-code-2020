import re

latitude = 0  # N or S
longitude = 0  # E or W
direction =  0  # L, R, F

command_pattern = re.compile(r'(\w)(\d+)')

with open('input.txt', 'r') as data:
  for line in data:
    result = command_pattern.search(line.rstrip())
    if not result:
      raise ValueError(line)
    command = result.group(1)
    argument = int(result.group(2))
    print('{} {}'.format(command, argument))
    if command == 'N':
      latitude += argument
    elif command == 'S':
      latitude -= argument
    elif command == 'E':
      longitude += argument
    elif command == 'W':
      longitude -= argument
    elif command == 'L':
      direction = (direction + argument) % 360
    elif command == 'R':
      direction = (direction - argument) % 360
    elif command == 'F':
      if direction == 0:
        longitude += argument
      elif direction == 90:
        latitude += argument
      elif direction == 180:
        longitude -= argument
      elif direction == 270:
        latitude -= argument
      else:
        raise ValueError(direction)

    else:
      raise ValueError(command)
    # if command in ['L', 'R']:
    print(latitude, longitude, direction)


print(abs(latitude) + abs(longitude))
