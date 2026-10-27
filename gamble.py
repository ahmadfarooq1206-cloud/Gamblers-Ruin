import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Amount of money the Gambler is aiming to win
goal=12

#Amount of money the Gambler starts with
balance=3

#Possible outcomes for each bet (entries must be either 1 or -1)
outcomes=[1,1,1,1,1,-1,-1,-1,-1]
num=(sum(outcomes)+len(outcomes))/2

#Probability of success for each individual bet
p=num/len(outcomes)

#Probability of failure for each individual bet
q=1-p

#Ratio between the probability of failure and probability of success
r=q/p

#Calculation for the overall probability of success
if sum(outcomes)==0:
    P_success=balance/goal
else:
    P_success=(1-r**balance)/(1-r**goal)


#Calculation for the total number of bets before success or ruin
if sum(outcomes)==0:
    E_bets=balance*(goal-balance)
else:
    E_bets=np.abs(1/(q-p)*(goal-balance*((1-r**balance)/(1-r**goal))))
E_bets=round(E_bets)

#Simulation of the Gambler's bets
def Gambler(balance,goal):
    series=[balance]
    while balance<goal and balance>0:
        result=random.choice(outcomes)
        balance+=result
        series.append(balance)
    return series

results=Gambler(balance,goal)
length=len(results)

#Difference between the number of bets expected and actually observed
dev=np.abs(E_bets-length+1)

#X-axis intervals
step=np.ceil(length/30)

#Visual indicator of Gambler's final result
if results[-1]==goal:
    line_colour='g'
else:
    line_colour='r'

print(f'Probability of success: {P_success}')
print(f'Expected number of bets: {E_bets}')
print(f'Actual number of bets: {length-1}')
print(f'Deviation between expected and actual number of bets: {dev}')

plt.figure(figsize=(12,6))
plt.xticks(np.arange(0,step+length,step))
plt.yticks(np.arange(0,1+goal,1))
plt.title("Finite Gambler's Ruin")
plt.xlabel('Number of bets')
plt.ylabel("Gambler's balance")
sns.lineplot(results,color=line_colour)
plt.show()
