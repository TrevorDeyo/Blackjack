import random
import time

# Function so I dont have to type so much
def sleep_print(text):
    print(text)
    time.sleep(.5)

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

sleep_print("===== Blackjack || Twenty-One =====\n")

sleep_print("The standard 52-card pack is used\n")

sleep_print("Object of the Game is to beat the dealer by getting a count as close to 21 as possible, without going over 21.\n")

sleep_print("Card Values/scoring: Ace is worth 1 or 11. Face cards are 10 and any other card is its number value.\n")

while True:
    sleep_print("===== GAME STARTING =====\n")
    # Game Setup Begins

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


    # shuffle deck
    random.shuffle(deck)

    # Deal Cards
    players_hand = [deck.pop()]
    players_hand += [deck.pop()]

    dealers_hand = [deck.pop()]
    dealers_hand += [deck.pop()]

    players_hand_value = hand_value(players_hand)
    dealers_hand_value = hand_value(dealers_hand)

    # Game Setup Ends

    # Game Starts / Game Loop
    game_running = True
    while game_running:

        sleep_print(f"Dealers Hand: {dealers_hand[0]} and a turned over card |?|, Hand Value: {hand_value(dealers_hand[0])} + |?|")
        sleep_print("-" * 100)
        sleep_print(f"Your Hand: {players_hand}, Hand Value: {players_hand_value}")
        sleep_print("=" * 100 + "\n")
        sleep_print("Would you like to hit or stay?")
        sleep_print("1. Hit")
        sleep_print("2. Stay\n")

        user_input = ''

        while user_input not in ("1", "2", "hit", "stay"):
            user_input = input("Your Choice: ")
            print()
            user_input = user_input.lower()
            if user_input not in ("1", "2", "hit", "stay"):
                sleep_print("INCORRECT CHOICE PICK ONE: ( 1 | 2 | hit | stay )")

        if user_input in ("1", "hit"):
            sleep_print(f"PLAYER HITS\n")

            players_hand += [deck.pop()]
            players_hand_value = hand_value(players_hand)
            
            sleep_print(f"You draw a {players_hand[-1]}, Card Value: {hand_value(players_hand[-1])} \n")

            if players_hand_value > 21:
                sleep_print(f"Making your hand over 21, {players_hand}, Hand Value: {players_hand_value}")
                sleep_print("YOU BUSTED :(\n\n")
                game_running = False

        if user_input in ("2", "stay"):
            sleep_print("PLAYER STAYS\n")
            sleep_print("Revealing Dealers hand")    
            sleep_print(f"Dealers Hand: {dealers_hand} , Hand Value: {dealers_hand_value}\n")
            
            while dealers_hand_value < 17:
                dealers_hand += [deck.pop()]
                dealers_hand_value = hand_value(dealers_hand)
                sleep_print("DEALER HITS\n")    
                sleep_print(f"Dealer draws a {dealers_hand[-1]}, Card Value: {hand_value(dealers_hand[-1])}\n")
                sleep_print(f"Dealers hand is {dealers_hand}, Hand Value: {dealers_hand_value}")
                if dealers_hand_value > 21:
                    sleep_print("DEALER BUSTED")
                    game_running = False

            sleep_print("DEALER STAYS")
            if dealers_hand_value >= players_hand_value:
                sleep_print(f"Dealer's hand {dealers_hand}, Value: {dealers_hand_value} is >= players hand {players_hand}, Value: {players_hand_value}\n")
                sleep_print("----- DEALER WINS -----\n")
            else:
                sleep_print(f"Player's Hand {players_hand}, Value: {players_hand_value} is greater than the Dealers Hand: {dealers_hand}, Value: {dealers_hand_value} and therefor wins")
                sleep_print("***** YOU WIN!!! *****\n")