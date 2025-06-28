import random
import matplotlib.pyplot as plt

def simulate_monty_hall(num_games=1000):
    stick_wins = 0
    switch_wins = 0
    
    for _ in range(num_games):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        
        first_choice = random.randint(0, 2)
        
        # Host opens a remaining goat door
        host_opens = random.choice([i for i in range(3) if i != first_choice and doors[i] == 'goat'])
        
        # Switching strategy
        switch_choice = [i for i in range(3) if i != first_choice and i != host_opens][0]
        
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
    plt.savefig('../data/monty_hall_results.png')
    plt.show()

if __name__ == "__main__":
    stick, switch = simulate_monty_hall(10000)
    print(f"Sticking wins: {stick:.1f}%")
    print(f"Switching wins: {switch:.1f}%")
    plot_results(stick, switch)