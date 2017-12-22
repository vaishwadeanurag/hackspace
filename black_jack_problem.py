from random import shuffle

ranks = [i for i in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']


def get_deck():
    "Prepare a deck of cards and return"
    deck = [[rank, suit] for rank in ranks for suit in suits]
    shuffle(deck)
    return deck


def card_value(card):
    "gets the value of the card"
    rank = card[0]
    if isinstance(rank, int):
        return int(rank)
    elif rank is 'Ace':
        return 11
    else:
        return 10


def hand_value(hand):
    """Returns the integer value of a set of cards."""

    hand_value = sum(card_value(_) for _ in hand)
    # Count the number of Aces in the hand.
    num_aces = len([_ for _ in hand if _[0] is 'Ace'])
    while num_aces > 0:
        if hand_value > 21 and 'Ace' in ranks:
            hand_value -= 10
            num_aces -= 1
        else:
            break
    return hand_value


def generate_score(player_dict):
    for player, player_properties in player_dict.items():
        player_properties['score'] = hand_value(player_properties['deck_in_hand'])


def check_status_of_player(player_dict):
    has_winner = False
    for player, player_properties in player_dict.items():
        if player_properties['score'] == 21 and player != 'Dealer' and player_dict['Dealer']['score'] != 21:
            has_winner = True
            player_properties['player_status'] = "Winner"
        elif player_properties['score'] > 21:
            if player == 'Dealer':
                has_winner = True
            player_properties['player_status'] = "Busted"
        elif player_properties['score'] > 17:
            player_properties['player_status'] = "Hold"
    return has_winner


def print_winners_in_specific_format(player_dict):
    if player_dict['Dealer']['player_status'] == 'busted':
        for player, player_properties in player_dict.items():
            print(player, ["%s(%s)" % (i[0], i[1]) for i in player_properties['deck_in_hand']],
                  '- %s -' % player_properties['score'],
                  'Winner' if player_properties['player_status'] != 'Busted' else 'Busted')
    else:
        for player, player_properties in player_dict.items():
            print(player, ["%s(%s)" % (i[0], i[1]) for i in player_properties['deck_in_hand']],
                  '- %s -' % player_properties['score'],
                  player_properties['player_status'])


def check_player_with_max_score(player_dict):
    max_score = 0
    winner_players = []
    for player, player_properties in player_dict.items():
        if player_properties['score'] >= 17 and player_properties['score'] <= 21:
            if player_properties['score'] > max_score:
                winner_players = [player]
                max_score = player_properties['score']
            elif player_properties['score'] == max_score:
                winner_players.append(player)
    for player in winner_players:
        player_dict[player]['player_status'] = "Winner"


def main():
    no_of_players = int(input("Please enter no of players:"))
    if no_of_players > 26 or no_of_players == 0:
        print("Game requires players between 1 to 26")
        return
    player_dict = {}
    deck = get_deck()
    for i in range(1, no_of_players):
        player_dict['Player %s' % i] = {"deck_in_hand": [deck.pop(), deck.pop()], "score": 0, "player_status": "Looser"}
    player_dict['Dealer'] = {"deck_in_hand": [deck.pop(), deck.pop()], "score": 0, "player_status": "Looser"}
    has_winner = False
    while not has_winner:
        card_drawed_in_hand = False
        generate_score(player_dict)
        has_winner = check_status_of_player(player_dict)
        if has_winner:
            if player_dict['Dealer']['player_status'] == 'Busted':
                check_player_with_max_score(player_dict)
            print_winners_in_specific_format(player_dict)
            break
        else:
            try:
                for player, player_properties in player_dict.items():
                    if player_properties['player_status'] == 'Looser':
                        card_drawed_in_hand = True
                        player_properties['deck_in_hand'].append(deck.pop())
            except IndexError:
                print("Not sufficent cards for all players game drawn")
            if not card_drawed_in_hand:
                # nobody drawed any card player with max score wins here
                check_player_with_max_score(player_dict)
                print_winners_in_specific_format(player_dict)
                break


if __name__ == '__main__':
    main()
