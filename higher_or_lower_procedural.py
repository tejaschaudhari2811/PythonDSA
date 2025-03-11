import random

suit_tuple = ("Spades", "Hearts", "clubs", "Diamonds")
rank_tuple = ("1","2","3","4","5","6","7","8","9","10","Jack","Queen","King")

N_CARDS = 8

def get_card(deck_list):
    this_card = deck_list.pop()
    return this_card

def shuffle(deck_list):
    deck_list_out = deck_list.copy()
    random.shuffle(deck_list_out)
    return deck_list_out

# Main code
print("Welcome to Higher or Lower")
print("You have to choose whether the next card to be shown will be higher\
      or lower than the current card.")
print("Getting it right adds 20 points; get it wrong and you lose 15 points")
print("You have 50 points to start.")
print()

starting_deck_list = []

for suit in suit_tuple:
    for this_value, rank in enumerate(rank_tuple):
        card_dict = {'rank':rank, 'suit':suit, 'value':this_value}
        starting_deck_list.append(card_dict)

score = 50

while True:
    print()
    game_deck_list = shuffle(starting_deck_list)
    current_card_dict = get_card(game_deck_list)
    current_card_rank = current_card_dict['rank']
    current_card_suit = current_card_dict['suit']
    current_card_value = current_card_dict['value']
    print("Starting card is:", current_card_rank + "of " + current_card_suit)
    print()

    for card_number in range(0, N_CARDS):
        answer = input("Will the next card be higher or lower than the current card")
        answer = answer.casefold()

        next_card_dict = get_card(game_deck_list)
        next_card_rank = next_card_dict["rank"]
        next_card_value = next_card_dict["value"]
        next_card_suit = next_card_dict["suit"]

        if answer == "h":
            if next_card_value > current_card_value:
                print("You are right! it was higher")
                score +=20
            else:
                print("Sorry it was not higher")
                score -= 15

        elif answer == "l":
            if next_card_value < current_card_value:
                score +=20
                print("You are right! it was lower")
            else:
                score -=15
                print("Sorry, it was not lower.")

        print("Your score is: ", score)
        print()
        current_card_rank = next_card_rank
        current_card_value = next_card_value

    play_again = input("To play again, press Enter or q to quit")
    if play_again == "q":
        break

print("OK, Bye")