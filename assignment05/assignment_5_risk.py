# Assignment 05. Risk Battle Simulation
# The aim of this program is to write a programme was to simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender),
# and plots the results.
# Author: Laura Lyons

import numpy as np
import matplotlib.pyplot as plt

# First we need to define a function that simulates rolling a single 6-sided die.
# Initially i tried 'np.random.uniform', however this returned floats.
# With research, I found that np.random.randint would be more suitable for this task.
# Reference: https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html
# Reference: https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html	

def roll_dice():
    return np.random.uniform(1, 7) #(From lecture 5, Random number generation)

# Santiy check, to ensure the code is working as expected.
# result = roll_dice()
# print("You rolled a", result)

attacker_dice = np.random.randint(1, 7, size=3)
defender_dice = np.random.randint(1, 7, size=2)

# Sanity check, to ensure the code is working as expected.
# print(attacker_dice, defender_dice)

# Next we need to sort the dice in descending order, so that we can compare the highest dice rolls.
sorted_attacker_dice = sorted(attacker_dice, reverse=True)
sorted_defender_dice = sorted(defender_dice, reverse=True)

# Sanity check, to ensure the code is working as expected.	
# print("Attacker dice (sorted):", sorted_attacker_dice)
# print("Defender dice (sorted):", sorted_defender_dice)

# Next we need to similate a single battle round, where the attacker rolls 3 dice and the defender rolls 2 dice and compare the outcomes.
# We will use a for loop to compare the dice rolls and determine the outcome of the battle.
# According to the rules of Risk:
# If the attacker's dice roll is higher than the defender's dice roll, the defender loses.
# If the defender's dice roll is higher than the attacker's dice roll, the attacker loses.
# If the dice rolls are equal, the attacker loses a unit.

def battle_round():
    attacker_dice = np.random.randint(1, 7, size=3)
    defender_dice = np.random.randint(1, 7, size=2)  
    attacker_losses = 0
    defender_losses = 0
    
    for i in range(min(len(attacker_dice), len(defender_dice))):
                   # The min function is used, to ensure that the loop stops when the shortest list is complete. 
                   # Reference: https://www.geeksforgeeks.org/python-min-function/
        a = attacker_dice[i]
        d = defender_dice[i]
                    # An if statement is used to compare the dice rolls and determine the outcome of the battle.
                    # we must remember that the attacker will win if the roll great or equal to the defenders roll.
        if a > d:
            defender_losses += 1
        else:
            attacker_losses += 1
        return attacker_losses, defender_losses

# Sanity check, to ensure the code is working as expected.
# result = battle_round()
# print("Attacker losses:", result)

# I was stumped as to how to simulate the result of 1000 battles, so i used Microsoft Co-pilot to assist in how to structure my thoughts.
num_rounds = 1000
attacker_total_losses = 0
defender_total_losses = 0

for _ in range(num_rounds):
    attacker_losses, defender_losses = battle_round()
    attacker_total_losses += attacker_losses
    defender_total_losses += defender_losses

# An if loop is use to determine the winner
if attacker_total_losses > defender_total_losses:
    winner = "Defender"
elif defender_total_losses > attacker_total_losses:
    winner = "Attacker"
else:
    winner = "Draw"

# Print the results, converted from losses to wins.
attacker_wins= (1000 -attacker_total_losses)
defender_wins= (1000-defender_total_losses)

print("Total Attacker Wins:", attacker_wins)
print("Total Defender Wins:", defender_wins)
print("Winner:", winner)

# Plot the results
labels = ['Attacker Wins', 'Defender Wins']
losses = [attacker_wins, defender_wins]

# Add the numbers inside the bars.
# (created with help from: https://stackoverflow.com/questions/28931224/adding-value-labels-on-a-matplotlib-bar-chart)
for i, value in enumerate(losses): 
    plt.text(i, value/2, str(value), ha='center', va='center', color='white', fontweight='bold')

plt.bar(labels, losses, color=['green', 'blue'])
plt.title('Risk Battle Simulation: 1000 rounds', fontweight='bold')
plt.ylabel('Total Battles Won')
plt.xlabel('Teams')
plt.show()

plt.savefig('assignment05/images/Assignment05_Risk Battle Simulation.jpg')