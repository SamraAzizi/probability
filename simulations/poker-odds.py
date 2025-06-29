import random
import matplotlib.pyplot as plt
from itertools import combinations

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
    