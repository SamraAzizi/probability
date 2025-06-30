import random
import matplotlib.pyplot as plt
from itertools import combinations
import os
from pathlib import Path

# ===== NEW CODE =====
current_dir = Path(__file__).parent
data_dir = current_dir.parent / "data"
data_dir.mkdir(exist_ok=True)
# ====================

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [f"{rank} of {suit}" for suit in suits for rank in ranks]

def simulate_poker_hands(num_simulations=10000):
    hand_types = {
        'High Card': 0,
        'Pair': 0,
        'Two Pair': 0,
        'Three of a Kind': 0,
        'Straight': 0,
        'Flush': 0,
        'Full House': 0,
        'Four of a Kind': 0,
        'Straight Flush': 0,
        'Royal Flush': 0
    }
    
    deck = create_deck()
    
    for _ in range(num_simulations):
        random.shuffle(deck)
        hand = deck[:5]
        
        ranks = [card.split()[0] for card in hand]
        suits = [card.split()[2] for card in hand]
        
        if len(set(suits)) == 1:
            if set(ranks) == {'10', 'J', 'Q', 'K', 'A'}:
                hand_types['Royal Flush'] += 1
            else:
                hand_types['Flush'] += 1
        elif len(set(ranks)) == 2:
            if any(ranks.count(r) == 4 for r in set(ranks)):
                hand_types['Four of a Kind'] += 1
            else:
                hand_types['Full House'] += 1
        elif len(set(ranks)) == 3:
            if any(ranks.count(r) == 3 for r in set(ranks)):
                hand_types['Three of a Kind'] += 1
            else:
                hand_types['Two Pair'] += 1
        elif len(set(ranks)) == 4:
            hand_types['Pair'] += 1
        else:
            hand_types['High Card'] += 1
    
    probabilities = {hand: (count / num_simulations) * 100 for hand, count in hand_types.items()}
    return probabilities

def plot_poker_odds(probabilities):
    hands = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.figure(figsize=(12, 6))
    plt.barh(hands, probs, color='purple', alpha=0.7)
    plt.xlabel('Probability (%)')
    plt.title('Poker Hand Probabilities (Simulated)')
    plt.grid(True)
    plt.savefig(data_dir / "poker_odds.png")  # CHANGED THIS LINE
    plt.show()

if __name__ == "__main__":
    probs = simulate_poker_hands()
    print("Poker Hand Probabilities:")
    for hand, p in probs.items():
        print(f"{hand}: {p:.2f}%")
    plot_poker_odds(probs)