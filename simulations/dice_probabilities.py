import random
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path
import os

# Set up paths - this will work on Windows, Mac, and Linux
current_dir = Path(__file__).parent
data_dir = current_dir.parent / "data"
data_dir.mkdir(exist_ok=True)  # Creates folder if it doesn't exist

def simulate_dice_rolls(num_rolls=10000):
    sum_counts = defaultdict(int)
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_val = dice1 + dice2
        sum_counts[sum_val] += 1
    
    sums = sorted(sum_counts.keys())
    probabilities = [(sum_counts[s] / num_rolls) * 100 for s in sums]
    
    return sums, probabilities

def plot_dice_probabilities(sums, probabilities):
    theoretical = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 
                  13.89, 11.11, 8.33, 5.56, 2.78]  # Exact % for sums 2-12
    
    plt.figure(figsize=(12, 6))
    plt.bar(sums, probabilities, width=0.6, label='Simulated', color='green', alpha=0.7)
    plt.plot(sums, theoretical, 'r-', marker='o', label='Theoretical')
    plt.xlabel('Dice Sum')
    plt.ylabel('Probability (%)')
    plt.title('Probability Distribution of Two Dice Sums')
    plt.legend()
    plt.grid(True)
    
    # Save to absolute path
    save_path = data_dir / "dice_probabilities.png"
    plt.savefig(save_path)
    print(f"Graph saved to: {save_path}")
    plt.show()

if __name__ == "__main__":
    sums, probs = simulate_dice_rolls()
    print("Dice Sum Probabilities:")
    for s, p in zip(sums, probs):
        print(f"Sum {s}: {p:.2f}%")
    plot_dice_probabilities(sums, probs)