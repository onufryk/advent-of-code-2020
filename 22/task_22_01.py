import collections

decks = collections.defaultdict(list)
with open("input.txt", "r") as input_file:
    current_player = None
    for input_line in input_file:
        input_line = input_line.strip()
        if input_line.startswith("Player "):
            current_player = input_line
        elif input_line != "":
            decks[current_player].append(int(input_line))


def has_winner():
    for player, deck in decks.items():
        if len(deck) == 0:
            return True
    return False


round = 0
while not has_winner():
    round += 1
    print("{:-^100}".format(" Round {} ".format(round)))
    print("Player 1 deck: {}".format(decks['Player 1:']))
    print("Player 2 deck: {}".format(decks['Player 2:']))
    player_1_move = decks['Player 1:'].pop(0)
    player_2_move = decks['Player 2:'].pop(0)
    if player_1_move > player_2_move:
        decks['Player 1:'].append(player_1_move)
        decks['Player 1:'].append(player_2_move)
    else:
        decks['Player 2:'].append(player_2_move)
        decks['Player 2:'].append(player_1_move)

winner = None
for player, deck in decks.items():
    if len(deck) != 0:
        winner = deck

mult = len(winner)
score = 0
for card in winner:
    score += mult * card
    mult -= 1

print(score)
