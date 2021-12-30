import collections
import functools
import re

raw_lines = []

with open('input.txt', 'r') as data:
    for input_line in data:
        input_line = input_line.strip()
        raw_lines.append(input_line)

tiles = collections.defaultdict(list)
tiles_metadata = collections.defaultdict(list)

current_tile_id = 0

tile_pattern = re.compile(r"Tile\s(\d+):")

for raw_line in raw_lines:
    match = tile_pattern.match(raw_line)
    if match != None:
        current_tile_id = match.group(1)
    elif raw_line != "":
        tiles[current_tile_id].append(raw_line.replace('.', '0').replace('#', '1'))

frequency = collections.defaultdict(list)
for tile_id, rows in tiles.items():
    # for line in rows:
    #   print(line)
    # print("Building")

    left = []
    right = []
    for col in rows:
        left.append(col[0])
        right.append(col[-1])

    top_1 = int(rows[0], 2)
    right_1 = int(''.join(right), 2)
    bottom_1 = int(rows[-1], 2)
    left_1 = int(''.join(left), 2)

    top_2 = int(rows[0][::-1], 2)
    right_2 = int(''.join(right)[::-1], 2)
    bottom_2 = int(rows[-1][::-1], 2)
    left_2 = int(''.join(left)[::-1], 2)

    tiles_metadata[tile_id].append(top_1)
    tiles_metadata[tile_id].append(right_1)
    tiles_metadata[tile_id].append(bottom_1)
    tiles_metadata[tile_id].append(left_1)
    tiles_metadata[tile_id].append(top_2)
    tiles_metadata[tile_id].append(right_2)
    tiles_metadata[tile_id].append(bottom_2)
    tiles_metadata[tile_id].append(left_2)
    frequency[top_1].append(tile_id)
    frequency[right_1].append(tile_id)
    frequency[bottom_1].append(tile_id)
    frequency[left_1].append(tile_id)
    frequency[top_2].append(tile_id)
    frequency[right_2].append(tile_id)
    frequency[bottom_2].append(tile_id)
    frequency[left_2].append(tile_id)

# for border, amount in frequency.items():
#   print("{}: {}".format(border, amount))

corners = []
for tile_id, metadata in tiles_metadata.items():
    # print(tile_id)
    # print(metadata)
    if sum([len(frequency[border]) == 2 for border in metadata]) == 4:
        corners.append(int(tile_id))

print(corners)
print(functools.reduce(lambda x, y: x * y, corners))
