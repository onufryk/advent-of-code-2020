import re
import json

rules = {}

pattern_no_bags = re.compile(r'^(.+) bags contain no other bags\.$')
pattern_one_bag = re.compile(r'^(.+) bags contain 1 ([^,]+) bag\.$')
pattern_many_bags = re.compile('([^\\s]+\\s[^\\s]+) bags contain ([^\\.]+)\\.')
pattern_many_bags_sub = re.compile('\s*\d\s(.*)\sbags?\s*')

with open('input.txt', 'r') as data:
  for line in data:
    # print(line.rstrip())

    result1 = pattern_no_bags.search(line)
    if result1:
      rules[result1.group(1)] = []
      continue

    result2 = pattern_one_bag.search(line)
    if result2:
      rules[result2.group(1)] = [result2.group(2)]
      continue

    result3 = pattern_many_bags.search(line)
    if result3:
      subrules = result3.group(2)
      rules[result3.group(1)] = [pattern_many_bags_sub.search(subrule).group(1) for subrule in subrules.split(',')]
      continue

  print(json.dumps(rules, indent=2))

  solutions = 0

  def can_have_shiny_gold(subrules):
    if not subrules:
      return False
    if 'shiny gold' in subrules:
      return True

    return any([can_have_shiny_gold(rules[subrule]) for subrule in subrules])

  for color, ruleset in rules.items():
    if color == 'shiny gold':
      continue
    if can_have_shiny_gold(ruleset):
      solutions += 1

  print(solutions)