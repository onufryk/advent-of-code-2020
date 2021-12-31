import copy
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

game_id = 1


def has_winner(deck1, deck2):
    if len(deck1) == 0 or len(deck2) == 0:
        return True
    return False


def play_game(current_game_id, deck1, deck2):
    round = 0
    global game_id

    game_decks = []

    while not has_winner(deck1, deck2):
        round += 1
        print("{:-^100}".format(" Round {} (Game {}) ".format(round, current_game_id)))
        print("Player 1 deck: {}".format(deck1))
        print("Player 2 deck: {}".format(deck2))

        for game_deck in game_decks:
            if deck1 == game_deck or deck2 == game_deck:
                return 'Player 1:'

        game_decks.append(copy.deepcopy(deck1))
        game_decks.append(copy.deepcopy(deck2))

        player_1_draw = deck1.pop(0)
        player_2_draw = deck2.pop(0)

        print("Player 1 plays: {}".format(player_1_draw))
        print("Player 2 plays: {}".format(player_2_draw))

        winner = None
        if len(deck1) >= player_1_draw and len(deck2) >= player_2_draw:
            print("Playing a sub-game to determine the winner...")
            winner = play_game(game_id + 1,deck1[:player_1_draw], deck2[:player_2_draw])
        else:
            if player_1_draw > player_2_draw:
                winner = 'Player 1:'
            else:
                winner = 'Player 2:'

        print("{} wins round {} of game {}!".format(winner, round, current_game_id))

        if winner == 'Player 1:':
            deck1.append(player_1_draw)
            deck1.append(player_2_draw)
        elif winner == 'Player 2:':
            deck2.append(player_2_draw)
            deck2.append(player_1_draw)

    game_id += 1
    if len(deck2) == 0:
        print("The winner of game {} is player 1!".format(current_game_id))
        return 'Player 1:'
    elif len(deck1) == 0:
        print("The winner of game {} is player 2!".format(current_game_id))
        return 'Player 2:'



play_game(game_id, decks['Player 1:'], decks['Player 2:'])

winner = decks['Player 1:'] if len(decks['Player 2:']) == 0 else decks['Player 2:']
mult = len(winner)
score = 0
for card in winner:
    score += mult * card
    mult -= 1

print(score)
