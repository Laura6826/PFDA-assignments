# Assignment 05. Risk Battle Simulation
# The aim of this program is to write a programme was to simulates a full series of rounds for armies of arbitrary sizes, 
# until one side is wiped out, and plots the results.
# Author: Laura Lyons

import numpy as np
import matplotlib.pyplot as plt

# The base code was taken from the first part of the assignment, and modified to simulate a full series of rounds for armies of arbitrary sizes.
# The code was also modified to plot the results.
# the originial over writing describing the code was removed, and addtional comments were added to explain the new code.
# On this occassion we need to take into account the size of the armies, so we need to modify the function to accept these parameters.
# The function 'battle_round' was modified to accept the size of the armies as parameters.

def roll_dice(num_dice):
    return np.random.randint(1, 7, size=num_dice)

def battle_round():
    # Orignially i had 'attacker_size and defender_size into the battle_round brackets, 
    # however this may have been biasing the battle towards the attacker, so i removed them.
    attacker_dice = sorted(roll_dice(3), reverse=True)
    defender_dice = sorted(roll_dice(2), reverse=True)
    
    attacker_losses = 0
    defender_losses = 0
    
    for a, d in zip(attacker_dice, defender_dice):
        if a >= d:
            defender_losses = 2  # Defender loses 2 units
            break  # Only one side can lose dice in each round
        else:
            attacker_losses = 3  # Attacker loses 3 units
            break  # Only one side can lose dice in each round
    return attacker_losses, defender_losses

# Ensure that the input is a positive integer for attacker size
initial_attacker_size = int(input('Please enter the size of the attacking army: '))
while initial_attacker_size <= 0:
    initial_attacker_size = int(input('That is not a positive integer. Please enter a positive integer: '))

# Ensure that the input is a positive integer for defender size
initial_defender_size = int(input('Please enter the size of the defending army: '))
while initial_defender_size <= 0:
    initial_defender_size = int(input('That is not a positive integer. Please enter a positive integer: '))

# Simulate a full series of rounds until one side is wiped out
def simulate_battle(attacker_size, defender_size):
    rounds = 0
    attacker_rounds_won = 0
    defender_rounds_won = 0

    while attacker_size > 0 and defender_size > 0:
        # Apply different loss rules for total dice lost.
        # This was why the defender wasnt winning any rounds, as the attacker
        # was losing 3 dice, and the defender was losing 2 dice.
        attacker_losses, defender_losses = battle_round()
        # Correct the loss application logic
        attacker_size -= attacker_losses
        defender_size -= defender_losses
        rounds += 1

        # Ensure the size does not go below zero
        attacker_size = max(0, attacker_size)
        defender_size = max(0, defender_size)

        if attacker_losses > 0:
            defender_rounds_won += 1
        else:
            attacker_rounds_won += 1

        print(f"Round: {rounds}, Attacker Losses: {attacker_losses}, Defender Losses: {defender_losses}, Attacker Size: {attacker_size}, Defender Size: {defender_size}")

    return attacker_size, defender_size, rounds, attacker_rounds_won, defender_rounds_won

# Run the simulation
attacker_size, defender_size, rounds, attacker_rounds_won, defender_rounds_won = simulate_battle(initial_attacker_size, initial_defender_size)

# Determine the winner
if attacker_size > 0:
    winner = "Attacker"
else:
    winner = "Defender"

print(f"Winner: {winner}")
print(f"Total Rounds: {rounds}")
print(f"Attacker Rounds Won: {attacker_rounds_won}")
print(f"Defender Rounds Won: {defender_rounds_won}")

# Plot the results
labels = ['Attacker Rounds Won', 'Defender Rounds Won']
rounds_won = [attacker_rounds_won, defender_rounds_won]

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, rounds_won, color=['red', 'blue'])

# Add the numbers inside the bars (generated from CoPilot)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval - 5, int(yval), ha='center', va='top', fontweight='bold', color='white', fontsize=14)

# Add the word "Winner" over the winning team's bar (generated from CoPilot)
if attacker_rounds_won > defender_rounds_won:
    plt.text(bars[0].get_x() + bars[0].get_width()/2, bars[0].get_height() + 5, 'Winner', ha='center', va='top', fontweight='bold', color='green', fontsize=16)
else:
    plt.text(bars[1].get_x() + bars[1].get_width()/2, bars[1].get_height() + 5, 'Winner', ha='center', va='top', fontweight='bold', color='green', fontsize=16)

plt.title('Risk Battle Simulation: Rounds Won by Each Side', fontsize=16, fontweight='bold')
plt.ylabel('Number of Rounds Won', fontsize= 12)
plt.xlabel('Teams')
plt.show()

plt.savefig('images/Assignment05_EXTRA_Risk Battle Simulation.jpg')