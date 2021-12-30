from copy import deepcopy
required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid = 0
passports = []

with open('input.txt', 'r') as data:
  current_passport = set()
  for input_line in data:
    input_line = input_line.strip()
    if input_line == '':
      passports.append(current_passport)
      current_passport = set()
    else:
      current_passport |= {item.split(':')[0] for item in input_line.split(' ')}

  if len(current_passport) > 0:
    passports.append(current_passport)
    current_passport = set()

for passport in passports:
  print(passport)
  if len(required_fields - passport) == 0:
    valid += 1

  print(required_fields - passport)
  print(passport - required_fields)

print(valid)
