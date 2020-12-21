import pprint
import re

rules = {}
my_ticket = []
nearby_tickets = []

rule_pattern = re.compile(r'([^\:]+): (\d+)-(\d+) or (\d+)-(\d+)')

mode = 'fields'
with open('input.txt', 'r') as data:
  for line in data:
    if 'your ticket:' in line:
      mode = 'my_ticket'
    elif 'nearby tickets:' in line:
      mode = 'nearby_tickets'
    elif mode == 'fields':
      if line.rstrip() == '':
        continue
      result = rule_pattern.search(line)
      if not result:
        raise ValueError(line)
      rules[result.group(1)] = (int(result.group(2)), int(result.group(3)), int(result.group(4)), int(result.group(5)))
    elif mode == 'my_ticket':
      if line.rstrip() == '':
        continue
      my_ticket = [int(num) for num in line.rstrip().split(',')]
    elif mode == 'nearby_tickets':
      if line.rstrip() == '':
        continue
      nearby_tickets.append([int(num) for num in line.rstrip().split(',')])
    else:
      raise ValueError(line)

# print('{:-^100}'.format(' FIELDS '))
# pprint.pprint(rules)

# print('Total tickets {}.'.format(len(nearby_tickets)))

valid_tickets = []

for ticket in nearby_tickets:
  is_ticket_valid = True
  for position, value in enumerate(ticket):
    is_value_valid = False
    for rule, constraints in rules.items():
      min1, max1, min2, max2 = constraints
      if (min1 <= value and value <= max1) or (min2 <= value and value <= max2):
        is_value_valid = True
    if not is_value_valid:
      is_ticket_valid = False

  if is_ticket_valid:
    valid_tickets.append(ticket)

# print('Valid tickets {}.'.format(len(valid_tickets)))

positions = [set(rules.keys())] * len(my_ticket)

for index, ticket in enumerate(valid_tickets):
  # print('{:-^100}'.format(' TICKET {} '.format(index + 1)))
  # print(ticket)
  for position, value in enumerate(ticket):
    # print('{:-^100}'.format(position))
    # print('Position {:2d}. Value: {}.'.format(position, value))
    candidates = set()
    for rule, constraints in rules.items():
      min1, max1, min2, max2 = constraints
      # print(rule, min1, max1, min2, max2)
      if (min1 <= value and value <= max1) or (min2 <= value and value <= max2):
        candidates.add(rule)
    positions[position] = positions[position] & candidates

# print('{:-^100}'.format(' POSITIONS '))
# for position, fields in enumerate(positions):
#   print(position, len(fields))
#   print(fields)

field_map = {}
detected_fields = set()
for i in range(1, len(my_ticket) + 1):
  for position, fields in enumerate(positions):
    if len(fields) == i:
      possible_fields = fields - detected_fields
      if len(possible_fields) > 1:
        raise ValueError()
      field = possible_fields.pop()
      detected_fields.add(field)
      field_map[field] = position

# pprint.pprint(field_map)

product = 1
for field, position in field_map.items():
  if 'departure' in field:
    product = product * my_ticket[position]

print(product)