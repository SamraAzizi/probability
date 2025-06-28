import random
import matplotlib.pyplot as plt

def simulate_monty_hall(num_games=1000):
    stick_wins = 0
    switch_wins = 0
    
    for _ in range(num_games):
        doors = ['goat', 'goat', 'car']
        random.shuffle(doors)
        
        first_choice = random.randint(0, 2)