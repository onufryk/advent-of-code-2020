required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

passports = []
current_passport = set()
valid_count = 0
with open('input.txt', 'r') as data:
  for line in data:
    if line == '\n':
      passports.append(current_passport)
      if len(required_fields - current_passport) == 0:
        valid_count += 1

      current_passport.clear()
      continue
    current_passport |= {item.split(':')[0] for item in line.split(' ')}

print(valid_count)
