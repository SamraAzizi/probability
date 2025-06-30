import random
import matplotlib.pyplot as plt
import os
from pathlib import Path

# Get the absolute path to the data folder
current_dir = Path(__file__).parent
data_dir = current_dir.parent / "data"
data_dir.mkdir(exist_ok=True)  # Creates folder if it doesn't exist

def simulate_monty_hall(num_games=1000):
    stick_wins = 0
    switch_wins = 0
    
    for _ in range(num_games):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        
        first_choice = random.randint(0, 2)
        
        host_opens = random.choice([i for i in range(3) 
                                  if i != first_choice and doors[i] == 'goat'])
        
        switch_choice = [i for i in range(3) 
                        if i != first_choice and i != host_opens][0]
        
        if doors[first_choice] == 'car':
            stick_wins += 1
        if doors[switch_choice] == 'car':
            switch_wins += 1
    
    stick_percent = (stick_wins / num_games) * 100
    switch_percent = (switch_wins / num_games) * 100
    
    return stick_percent, switch_percent

def plot_results(stick, switch):
    labels = ['Stick', 'Switch']
    theoretical = [33.3, 66.6]
    simulated = [stick, switch]
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, theoretical, width=0.4, label='Theoretical', color='blue', alpha=0.6)
    plt.bar(labels, simulated, width=0.2, label='Simulated', color='red', alpha=0.8)
    plt.ylabel('Win Percentage (%)')
    plt.title('Monty Hall Problem: Theory vs Simulation')
    plt.legend()
    
    # Save to absolute path
    save_path = data_dir / "monty_hall_results.png"
    plt.savefig(save_path)
    print(f"Graph saved to: {save_path}")
    plt.show()

if __name__ == "__main__":
    stick, switch = simulate_monty_hall(10000)
    print(f"Sticking wins: {stick:.1f}%")
    print(f"Switching wins: {switch:.1f}%")
    plot_results(stick, switch)