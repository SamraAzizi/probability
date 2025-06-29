import random
import matplotlib.pyplot as plt
from collections import defaultdict

def simulate_dice_rolls(num_rolls=10000):
    sum_counts = defaultdict(int)
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_val = dice1 + dice2
        sum_counts[sum_val] += 1
