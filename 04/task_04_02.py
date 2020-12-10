import re

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def is_passport_valid(passport):
  if len(required_fields - set(passport.keys())) > 0:
    return False
  return validate_byr(passport.get('byr', None)) and validate_iyr(passport.get('iyr', None)) and validate_eyr(passport.get('eyr', None)) and validate_hgt(passport.get('hgt', None)) and validate_hcl(passport.get('hcl', None)) and validate_ecl(passport.get('ecl', None)) and validate_pid(passport.get('pid', None)) and validate_cid(passport.get('cid', None))


def validate_byr(value):
  # byr (Birth Year) - four digits; at least 1920 and at most 2002.
  if value is None:
    return False
  result = re.compile(r'^(\d{4})$').search(value)
  if not result:
    return False
  return  1920 <= int(result.group(1)) <= 2002

def validate_iyr(value):
  # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  if value is None:
    return False
  result = re.compile(r'^(\d{4})$').search(value)
  if not result:
    return False
  return  2010 <= int(result.group(1)) <= 2020

def validate_eyr(value):
  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  if value is None:
    return False
  result = re.compile(r'^(\d{4})$').search(value)
  if not result:
    return False
  return  2020 <= int(result.group(1)) <= 2030

def validate_hgt(value):
  # hgt (Height) - a number followed by either cm or in:
  # If cm, the number must be at least 150 and at most 193.
  # If in, the number must be at least 59 and at most 76.
  if value is None:
    return False
  result = re.compile(r'^(\d+)(\w\w)$').search(value)
  if not result:
    return False
  if result.group(2) == 'cm':
    return  150 <= int(result.group(1)) <= 193
  else:
    return  59 <= int(result.group(1)) <= 76

def validate_hcl(value):
  # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  if value is None:
    return False
  return re.compile(r'^#[\dabcdef]{6}$').search(value)

def validate_ecl(value):
  # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  if value is None:
    return False
  return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def validate_pid(value):
  # pid (Passport ID) - a nine-digit number, including leading zeroes.
  if value is None:
    return False

  return re.compile(r'^\d{9}$').search(value)

def validate_cid(value):
  # cid (Country ID) - ignored, missing or not.
  return True


current_passport = {}
valid_count = 0
with open('input.txt', 'r') as data:
  for line in data:

    if line == '\n':
      if is_passport_valid(current_passport):
        valid_count += 1

      current_passport.clear()
      continue

    current_passport.update({item.split(':')[0]:item.split(':')[1] for item in line[:-1].split(' ')})

print(valid_count)