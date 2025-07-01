# Probability in Games: Simulations & Analysis

A Python project demonstrating probability concepts through game simulations

📌 **Table of Contents**

- Project Overview
- Features
- Installation
- Usage
- File Structure
- Results & Interpretation
- Customization
- Troubleshooting

🎯 **Project Overview**

This project simulates three classic probability scenarios:

- **Monty Hall Problem** - Should you switch doors to win?
- **Dice Sum Probabilities** - Why is 7 the most common dice roll?
- **Poker Hand Odds** - What are your chances of getting a flush?

Each simulation:
- ✅ Runs thousands of trials
- ✅ Compares results with theoretical probabilities
- ✅ Generates visualizations
## ✨ Features

### 1. Monty Hall Problem Simulation
- **Concept**: Tests the counterintuitive probability behind door-switching
- **Key Insight**: Switching doors wins ~66% of the time vs 33% when sticking
- **Code File**: `simulations/monty_hall.py`
- **Output Example**:
  ```text
  Sticking wins: 33.2%
  Switching wins: 66.8%
  ```
https://data/monty_hall_results.png

  ### 2. Dice SUm Probability Analyzer
  - **Concept**: Calculates likehood of sums when rolling two 6 sided dice
  - **Key Insight**: 7 is the most probable sum(16.67%)
  - **Code File**: `simulations/dice_probability.py`
  - **Output Example**:
    ```text
    Sum 2: 2.81%
    Sum 7: 16.64%
    Sum 12: 2.77% 
    ```
    https://data/dice_probabilities.png

### 3. Poker Hand Odds Calculator
- **Concept**: Simulates probability of poker hands in a 5-card draw
- **Key Insight**:
    - Pair: ~42% chance
    - Flush: ~0.2% chance

- **Code File**: `simulations/poker_odds.py`
- **Output Example:**
    ```text
    High Card: 50.14%
    Pair: 42.38%
    Flush: 0.21%
    ```

    https://data/poker_odds.png



### Installation
Clone the repository:

```bash
https://github.com/SamraAzizi/probability.git
cd probability
```

Install dependencies:

```bash
pip install matplotlib
```

### Usage
Run any simulation:

```bash
# Monty Hall Problem
python simulations/monty_hall.py

# Dice Probabilities
python simulations/dice_probabilities.py

# Poker Hand Odds
python simulations/poker_odds.py
```

### Outputs:
- Results printed in terminal
- Graphs saved to `/data/` folder

### File Structure
```bash
probability-in-games/
├── data/                  # Generated graphs
├── simulations/
│   ├── monty_hall.py      # Door-switching simulation
│   ├── dice_probabilities.py  # Dice sum analysis
│   └── poker_odds.py      # Poker hand probabilities
└── README.md

```