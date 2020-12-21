import pprint
import re

rules = {}
my_ticket = []
nearby_tickets = []

rule_pattern = re.compile(r'(\w+): (\d+)-(\d+) or (\d+)-(\d+)')

total = 0

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
      rules[result.group(1)] = [[int(result.group(2)), int(result.group(3))], [int(result.group(4)), int(result.group(5))]]
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

for value in my_ticket:
  valid = False
  for rule, group in rules.items():
    for constraint in group:
      if constraint[0] <= value <= constraint[1]:
        valid = True
  if not valid:
    total += value

for ticket in nearby_tickets:
  for value in ticket:
    valid = False
    for rule, group in rules.items():
      for constraint in group:
        if constraint[0] <= value <= constraint[1]:
          valid = True
    if not valid:
      total += value

print(total)
