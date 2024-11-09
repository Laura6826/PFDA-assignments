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
            defender_losses += 1
        else:
            attacker_losses += 1
    
    return attacker_losses, defender_losses
    # the return function wasmoved outside the loop, to ensure that the function returns the total number of troops,
    # lost by the attacker and defender in each round. Initially the defender wasnt winning any rounds, which is statistically unlikely.
    # The function now returns the number of troops lost by the attacker and defender in each round.

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
    attacker_total_losses = 0
    defender_total_losses = 0
    rounds = 0

    while attacker_size > 0 and defender_size > 0:
        # Apply different loss rules for total dice lost.
        # This was why the defender wasnt winning any rounds, as the attacker
        # was losing 3 dice, and the defender was losing 2 dice.
        attacker_losses, defender_losses = battle_round()
        # Correct the loss application logic
        attacker_size -= attacker_losses
        defender_size -= defender_losses
        attacker_total_losses += attacker_losses * 3
        defender_total_losses += defender_losses * 2
        rounds += 1

    return attacker_total_losses, defender_total_losses, rounds

# Run the simulation
attacker_total_losses, defender_total_losses, rounds = simulate_battle(initial_attacker_size, initial_defender_size)

# Determine the winner
if attacker_total_losses > defender_total_losses:
    winner = "Defender"
elif defender_total_losses > attacker_total_losses:
    winner = "Attacker"
else:
    winner = "Draw"

attacker_wins = max(0, initial_attacker_size - attacker_total_losses)
defender_wins = max(0, initial_defender_size - defender_total_losses)

print(f"Total Attacker Wins: {attacker_wins}")
print(f"Total Defender Wins: {defender_wins}")
print(f"Winner: {winner}")
print(f"Total Rounds: {rounds}")

# Plot the results
labels = ['Attacker Wins', 'Defender Wins']
wins = [attacker_wins, defender_wins]

plt.bar(labels, wins, color=['red', 'blue'])

# Add the numbers on top of the bars
for i, value in enumerate(wins): 
    plt.text(i, value + 5, str(value), ha='center', va='bottom', fontweight='bold')

plt.title('Risk Battle Simulation: 1000 rounds', fontweight='bold')
plt.ylabel('Number of Wins')
plt.xlabel('Teams')
plt.show()


labels = ['Attacker Remaining', 'Defender Remaining']
remaining = [attacker_wins, defender_wins]

plt.bar(labels, remaining, color=['green', 'blue'])

# Add the numbers inside the bars
for i, value in enumerate(remaining): 
    plt.text(i, value/2, str(value), ha='center', va='center', color='white', fontweight='bold')

plt.title('Risk Battle Simulation: Until One Side is Wiped Out', fontweight='bold')
plt.ylabel('Remaining Troops')
plt.xlabel('Teams')
plt.show()
