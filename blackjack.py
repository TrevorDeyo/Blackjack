import random
import time

sleep = 0

print("===== Blackjack || Twenty-One =====\n")
time.sleep(sleep)
print("The standard 52-card pack is used\n")
time.sleep(sleep)
print("Object of the Game is to beat the dealer by getting a count as close to 21 as possible, without going over 21.\n")
time.sleep(sleep)
print("Card Values/scoring: It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its number value.\n")
time.sleep(sleep)


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
        

random.shuffle(deck)

hand = [deck.pop()]

print(hand, hand_value(hand))

my_hand = ["10C", "JD", "AS"]
print("Hand value:",my_hand ,hand_value(my_hand))  # Should be 21