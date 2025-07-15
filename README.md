# 🃏 Blackjack (Twenty-One) - Python Terminal Game

This is a simple terminal-based Blackjack game implemented in Python. The goal is to get as close to 21 as possible without going over. Play against a computer dealer using a standard 52-card deck.

## 🎮 How to Play

- You are dealt two cards.
- The dealer is also dealt two cards, one face up and one hidden.
- You choose to **Hit** (draw a card) or **Stay** (end your turn).
- If your total exceeds 21, you bust and lose the round.
- Once you stay, the dealer plays by fixed rules (draws until reaching at least 17).
- The closest to 21 without busting wins!

## 🧠 Rules

- Number cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are worth 10.
- Aces can be worth **1 or 11**, whichever is more favorable without busting.
- Dealer must hit until reaching at least 17.

## ▶️ Running the Game

Make sure you have Python 3 installed.

```bash
python blackjack.py
```

## ⌨️ Input Options
When prompted:
- To hit: 1 or hit
- To stay: 2 or stay
- To play again: yes, y, 1
- To exit: no, n, 2

## 💡 Features
- Full game loop with replay option
- Realistic card drawing and hand value calculation
- Dealer behavior mimics real Blackjack rules
- Handles aces dynamically as 1 or 11
- Uses clear printed messages with delays for pacing
