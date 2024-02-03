import random

cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def sum_cards(cards):
    sum = 0
    for card in cards:
        sum += card
    return sum


play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play_game == "y":
    player_cards = []
    computer_cards = []

    # Generate starting cards
    player_cards.append(cards_deck[random.randint(0, len(cards_deck) - 1)])
    player_cards.append(cards_deck[random.randint(0, len(cards_deck) - 1)])
    print(f"Your cards: {player_cards}")

    # Generate computer starting cards
    computer_cards.append(cards_deck[random.randint(0, len(cards_deck) - 1)])
    print(f"Computer card: {computer_cards}")

    draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
    sum = 0
    while draw_card == 'y' and sum < 21:
        new_card = cards_deck[random.randint(0, len(cards_deck) - 1)]
        player_cards.append(new_card)
        print(f"Dealer draws: {new_card}")
        sum = sum_cards(player_cards)

    if draw_card == 'n':
        player_sum = sum_cards(player_cards)
        computer_sum = sum_cards(computer_cards)
        if player_sum > computer_sum:
            print("You Win")
        else:
            print("You Lose")
    else:
        print("You Lose")

