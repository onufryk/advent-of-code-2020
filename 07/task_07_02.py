import re
import json

rules = {}

pattern_no_bags = re.compile(r'^(.+) bags contain no other bags\.$')
pattern_one_bag = re.compile(r'^(.+) bags contain 1 ([^,]+) bag\.$')
pattern_many_bags = re.compile('([^\\s]+\\s[^\\s]+) bags contain ([^\\.]+)\\.')
pattern_many_bags_sub = re.compile('\s*(\d*)\s(.*)\sbags?\s*')

with open('input.txt', 'r') as data:
  for line in data:
    # print(line.rstrip())

    result1 = pattern_no_bags.search(line)
    if result1:
      rules[result1.group(1)] = {}
      continue

    result2 = pattern_one_bag.search(line)
    if result2:
      rules[result2.group(1)] = {result2.group(2) : 1}
      continue

    result3 = pattern_many_bags.search(line)
    if result3:
      subrules = result3.group(2)
      rules[result3.group(1)] = {pattern_many_bags_sub.search(subrule).group(2):int(pattern_many_bags_sub.search(subrule).group(1)) for subrule in subrules.split(',')}
      continue

  print(json.dumps(rules, indent=2))

def bags_count(rule):
  if rule not in rules or not rules[rule]:
    return 0
  return sum([number for color, number in rules[rule].items()]) + sum([number*bags_count(color) for color, number in rules[rule].items()])

print(bags_count('shiny gold'))