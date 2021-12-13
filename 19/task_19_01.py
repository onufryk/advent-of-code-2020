import pprint
import re

raw_lines = None
with open('input.txt', 'r') as data:
  raw_lines = [line.rstrip() for line in data.readlines()]

raw_rules = []
messages = []

i = 0
while raw_lines[i] != '':
  raw_rules.append(raw_lines[i])
  i += 1

i += 1
while i < len(raw_lines):
  messages.append(raw_lines[i])
  i += 1

rules = [None] * len(raw_rules)

for raw_rule in raw_rules:
  index, ruledef = raw_rule.split(':')
  disjunction_rules = ruledef.split('|')

  if len(disjunction_rules) > 1:
    rules[int(index)] = {
      'operator': 'OR',
      'arguments':  [[rule.strip(' "') if '"' in rule else int(rule) for rule in disjunction_rule.strip().split(' ')] for disjunction_rule in disjunction_rules]
    }
  else:
    tokens = disjunction_rules[0].strip().split(' ')
    if len(tokens) > 1:
      rules[int(index)] = [rule.strip(' "') if '"' in rule else int(rule) for rule in tokens]
    else:
      rules[int(index)] = tokens[0].strip(' "')

print('{:-^100}'.format(' RULES '))
for i, r in enumerate(rules):
  print('{}: {}'.format(i, r))
print('{:-^100}'.format(''))

# def expand_rule(rule):
#   if isinstance(rule, str):
#     return rule
#   if isinstance(rule, int):
#     return expand_rule(rules[rule])
#   if isinstance(rule, list):
#     return [expand_rule(ruletoken) for ruletoken in rule]

# for i, rule in enumerate(rules[0]):
#   rules[0][i] = expand_rule(rule)


# def flatten(rule):
#   if isinstance(rule, str):
#     return rule
#   if isinstance(rule, list):
#     if all([isinstance(item, str) and len(item) == 1 for item in rule]):
#       return ''.join(rule)
#     return '({})'.format('|'.join([flatten(item) for item in rule]))

# print(rules[0])

# for i, rule in enumerate(rules[0]):
#   rules[0][i] = flatten(rule)
# print(''.join(rules[0]))

# pattern = re.compile('^{}$'.format(''.join(rules[0])))

# print(pattern)

# for msg in messages:
#   print(msg)
#   if pattern.search(msg):
#     print('YEA')

# # ^a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b$
# # ^a(((aa|bb)|(ab|ba))|((ab|ba)|(aa|bb)))b