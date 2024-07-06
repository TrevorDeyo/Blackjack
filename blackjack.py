import random
import time

print("===== Blackjack || Twenty-One =====\n")
time.sleep(1)
print("The standard 52-card pack is used\n")
time.sleep(1)
print("Object of the Game is to beat the dealer by getting a count as close to 21 as possible, without going over 21.\n")
time.sleep(1)
print("Card Values/scoring: Ace is worth 1 or 11. Face cards are 10 and any other card is its number value.\n")
time.sleep(1)
print("*" * 50)

while True:

    deck = ["2 of Clubs", "2 of Diamonds", "2 of Hearts", "2 of Spades",
            "3 of Clubs", "3 of Diamonds", "3 of Hearts", "3 of Spades",
            "4 of Clubs", "4 of Diamonds", "4 of Hearts", "4 of Spades",
            "5 of Clubs", "5 of Diamonds", "5 of Hearts", "5 of Spades",
            "6 of Clubs", "6 of Diamonds", "6 of Hearts", "6 of Spades",
            "7 of Clubs", "7 of Diamonds", "7 of Hearts", "7 of Spades",
            "8 of Clubs", "8 of Diamonds", "8 of Hearts", "8 of Spades",
            "9 of Clubs", "9 of Diamonds", "9 of Hearts", "9 of Spades",
            "10 of Clubs", "10 of Diamonds", "10 of Hearts", "10 of Spades",
            "Jack of Clubs", "Jack of Diamonds", "Jack of Hearts", "Jack of Spades",
            "Queen of Clubs", "Queen of Diamonds", "Queen of Hearts", "Queen of Spades",
            "King of Clubs", "King of Diamonds", "King of Hearts", "King of Spades",
            "Ace of Clubs", "Ace of Diamonds", "Ace of Hearts", "Ace of Spades",]


    # function that calculates the value of the hand
    def hand_value(hand):
        hand_value = 0

        for card in hand:
            if card[0].isdigit() and int(card[0]) > 1:
                hand_value += int(card[0])
            elif card[0] in ("1", "J", "Q", "K"):
                hand_value += 10
            elif card[0] == "A":
                # Handle Ace: choose 1 or 11 based on the total hand value
                hand_value += 11 if hand_value + 11 <= 21 else 1

        return hand_value
            
    # shuffle deck
    random.shuffle(deck)

    # Deal Cards
    players_hand = [deck.pop()]
    players_hand += [deck.pop()]

    dealers_hand = [deck.pop()]
    dealers_hand += [deck.pop()]


    busted = False
    while not busted:

        print(f"Dealers Hand: {dealers_hand[0]} | Hand Value: {hand_value(dealers_hand[0])}")
        print("-" * 50)
        time.sleep(1)
        print(f"Your Hand: {players_hand} | Hand Value: {hand_value(players_hand)}")
        print("=" * 50)
        time.sleep(1)
        print("Would you like to hit or stay?")
        print("1. Hit")
        print("2. Stay")

        user_input = ''

        while user_input not in ("1", "2", "hit", "stay"):
            user_input = input("Your Choice: ")
            user_input = user_input.lower()
            if user_input not in ("1", "2", "hit", "stay"):
                print("INCORRECT CHOICE PICK ONE: ( 1 | 2 | hit | stay )")

        if user_input in ("1", "hit"):
            players_hand += [deck.pop()]

        if hand_value(players_hand) > 21:
            print("\n\n")
            print("YOU BUSTED!\n\n")
            time.sleep(3)
            busted = True



"""
print(players_hand, hand_value(players_hand))

my_hand = ["10C", "JD", "AS"]
print("Hand value:",my_hand ,hand_value(my_hand))  # Should be 21
"""