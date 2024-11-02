# Assignemtn 05. 
# The aim of this program is to write a programme 
# Author: Laura Lyons


import numpy as np
import matplotlib.pyplot as plt
import random

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
print(attacker_dice, defender_dice)

# Next we need to sort the dice in descending order, so that we can compare the highest dice rolls.
sorted_attacker_dice = sorted(attacker_dice, reverse=True)
sorted_defender_dice = sorted(defender_dice, reverse=True)

# Sanity check, to ensure the code is working as expected.	
print("Attacker dice (sorted):", sorted_attacker_dice)
print("Defender dice (sorted):", sorted_defender_dice)

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
        
        if a > d:
            defender_losses += 1
        else:
            attacker_losses += 1
        return attacker_losses
        if attacker
    


# Sanity check, to ensure the code is working as expected.
result = battle_round()
print("Attacker losses:", result)
'''
#Now we need to simulate the result of 1000 battles.

def simulate_battles(num_rounds):
    attacker_total_losses = 0
    
    for _ in range(num_rounds):
        attacker_losses = battle_round()
        attacker_total_losses += attacker_losses
    
    return attacker

for a,d in battle():
    attacker_losses =0
    defender_losses =0
    if a>d:
        defender_losses = +1   

# Next, we need to define a function that simulates rolling multiple dice.
def roll_dice(num_dice):
    return [roll_dice() for _ in range(num_dice)]

# Sanity check, to ensure the code is working as expected.
results = roll_dice(3)
print("You rolled", results)

def roll_dice(num_dice):
    return sorted(np.random.randint(1, 7, size=num_dice), reverse=True)

def simulate_battle_round():
    attacker_dice = roll_dice(3)
    defender_dice = roll_dice(2)
    
    attacker_losses = 0
    defender_losses = 0
    
    for i in range(len(attacker_dice)):
        a = attacker_dice[i]
        d = defender_dice[i]
        
        if a > d:
            defender_losses += 1
        else:
            attacker_losses += 1

    
    return attacker_losses, defender_losses

def simulate_battles(num_rounds):
    attacker_total_losses = 0
    defender_total_losses = 0
    
    for _ in range(num_rounds):
        attacker_losses, defender_losses = simulate_battle_round()
        attacker_total_losses += attacker_losses
        defender_total_losses += defender_losses
    
    return attacker_total_losses, defender_total_losses

# Simulate 1000 battle rounds
num_rounds = 1000
attacker_losses, defender_losses = simulate_battles(num_rounds)

# Plot the results
labels = ['Attacker Losses', 'Defender Losses']
losses = [attacker_losses, defender_losses]

plt.bar(labels, losses, color=['red', 'blue'])
plt.title('Risk Battle Simulation: 3 Attackers vs 2 Defenders')
plt.ylabel('Total Losses')
plt.show()


import random
import matplotlib.pyplot as plt

# Function to simulate a single battle round
def battle_round():
    attacker_dice = sorted([random.randint(1, 6) for _ in range(3)], reverse=True)
    defender_dice = sorted([random.randint(1, 6) for _ in range(2)], reverse=True)
    
    attacker_losses = 0
    defender_losses = 0
    
    for i in range(min(len(attacker_dice), len(defender_dice))):
        if attacker_dice[i] > defender_dice[i]:
            defender_losses += 1
        else:
            attacker_losses += 1
    
    return attacker_losses, defender_losses

# Simulate 1000 battle rounds
num_rounds = 1000
attacker_total_losses = 0
defender_total_losses = 0

attacker_losses_list = []
defender_losses_list = []

for _ in range(num_rounds):
    attacker_losses, defender_losses = battle_round()
    attacker_total_losses += attacker_losses
    defender_total_losses += defender_losses
    attacker_losses_list.append(attacker_losses)
    defender_losses_list.append(defender_losses)

# Plot the results
plt.hist(attacker_losses_list, bins=range(4), alpha=0.5, label='Attacker Losses')
plt.hist(defender_losses_list, bins=range(3), alpha=0.5, label='Defender Losses')
plt.xlabel('Losses')
plt.ylabel('Frequency')
plt.title('Risk Battle Simulation (1000 Rounds)')
plt.legend(loc='upper right')
plt.show()

# Print the total losses
print("Total Attacker losses:", attacker_total_losses)
print("Total Defender losses:", defender_total_losses)
'''