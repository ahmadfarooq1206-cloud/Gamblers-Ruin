import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Obtains the Gambler's starting balance, end goal and probability of success for each gamble
while True:
    try:
        print('')
        balance=int(input("Enter the Gambler's starting balance: £"))
        goal=int(input("Enter the Gambler's goal: £"))
        p=float(input("Enter the probability of success for each gamble as a decimal: "))
        if goal>balance and 0<p<1:
            break
        else:
            pass
    except ValueError:
        pass
# Probability of failure for each gamble
q=1-p
# Ratio between the probabilities for failure and success
r=q/p

# Formulas for the overall probability of success and expected number of gambles
if p==.5:
    P_success=balance/goal
    E_gambles=balance*(goal-balance)
else:
    P_success=(1-r**balance)/(1-r**goal)
    E_gambles=1/(q-p)*(balance-goal*((1-r**balance)/(1-r**goal)))

E_gambles=round(E_gambles)
P_success=100*P_success

# List of numbers used to determine whether each gamble is succesful
x=np.linspace(0,1,10000001)

# Simulation of the Gambler's actions
def Gambler(balance,goal,p):
    account=[balance]
    while balance<goal and balance>0:
        if p>random.choice(x):
            balance+=1
        else:
            balance-=1
        account.append(balance)
    return account

# Insights from simulation
print(f'\nProbability of success: {P_success} %')
print(f'Expected number of gambles: {E_gambles}\n')

plt.figure(figsize=(13,6))
plt.title("Gambler's Ruin")
plt.xlabel('Number of gambles made')
plt.ylabel("Gambler's balance (£)")

# List of simulation results
pathways=[]
for i in range(50):
    pathways.append(Gambler(balance,goal,p))

# Plot
for i in pathways:
    sns.lineplot(i)

plt.grid()
plt.show()
