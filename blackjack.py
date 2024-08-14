import random
import time
from typing import List, Tuple

# Constants
BLACKJACK = 21
DEALER_STAND = 17

# Card values
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '1': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def sleep_print(text: str) -> None:
    print(text)
    time.sleep(0.5)

def hand_value(hand: List[str]) -> int:
    total = sum(VALUES[card[0]] for card in hand)
    aces = sum(card.startswith('A') for card in hand)
    while total > BLACKJACK and aces:
        total -= 10
        aces -= 1
    return total

def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_choices:
            return user_input
        sleep_print(f"Invalid choice. Please choose from: {', '.join(valid_choices)}")

def player_turn(deck: List[str], player_hand: List[str]) -> Tuple[List[str], bool]:
    while True:
        sleep_print(f"Your Hand: {player_hand}, Hand Value: {hand_value(player_hand)}")
        sleep_print("Would you like to hit or stay?")
        sleep_print("1. Hit")
        sleep_print("2. Stay")

        choice = get_user_choice("Your Choice: ", ["1", "2", "hit", "stay"])

        if choice in ("1", "hit"):
            player_hand.append(deck.pop())
            sleep_print(f"You draw a {player_hand[-1]}")
            if hand_value(player_hand) > BLACKJACK:
                sleep_print(f"Your hand: {player_hand}, Hand Value: {hand_value(player_hand)}")
                sleep_print("YOU BUSTED :(")
                return player_hand, True
        else:
            return player_hand, False

def dealer_turn(deck: List[str], dealer_hand: List[str]) -> Tuple[List[str], bool]:
    while hand_value(dealer_hand) < DEALER_STAND:
        dealer_hand.append(deck.pop())
        sleep_print(f"Dealer draws a {dealer_hand[-1]}")
        sleep_print(f"Dealer's hand: {dealer_hand}, Hand Value: {hand_value(dealer_hand)}\n")

        if hand_value(dealer_hand) > BLACKJACK:
            sleep_print("DEALER BUSTED")
            return dealer_hand, True
    return dealer_hand, False

def determine_winner(player_hand: List[str], dealer_hand: List[str]) -> None:
    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)

    sleep_print(f"\nYour hand: {player_hand}, Value: {player_value}")
    sleep_print(f"Dealer's hand: {dealer_hand}, Value: {dealer_value}")

    if dealer_value >= player_value:
        sleep_print("\n----- DEALER WINS -----")
    else:
        sleep_print("\n***** YOU WIN!!! *****")

def play_blackjack() -> None:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    sleep_print(f"Dealer's Hand: {dealer_hand[0]} and a hidden card")

    player_hand, player_busted = player_turn(deck, player_hand)

    if not player_busted:
        sleep_print("Revealing Dealer's hand")
        sleep_print(f"Dealer's Hand: {dealer_hand}, Value: {hand_value(dealer_hand)}")
        dealer_hand, dealer_busted = dealer_turn(deck, dealer_hand)

        if not dealer_busted:
            determine_winner(player_hand, dealer_hand)

def main() -> None:
    sleep_print("===== Blackjack || Twenty-One =====")
    sleep_print("The standard 52-card pack is used")
    sleep_print("Object of the Game: Get as close to 21 as possible without going over")
    sleep_print("Card Values: Ace is 1 or 11. Face cards are 10. Other cards are their pip value.")

    while True:
        play_blackjack()
        play_again = get_user_choice("Do you want to play again? ( yes or no | y or n | 1 or 2 ): ", ["yes", "no", "y", "n", "1", "2"])
        if play_again in ("no", "n", "2"):
            break
        sleep_print("Starting a new game...\n")

    sleep_print("Thanks for playing!")

if __name__ == "__main__":
    main()
