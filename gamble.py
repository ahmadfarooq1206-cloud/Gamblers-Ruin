import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Obtains the Gambler's starting balance, end goal and individual probability of success
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
# Probability of failure for each individual gamble
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
result=Gambler(balance,goal,p)

# Deviation between the expected and observed number of gambles made
gambles=len(result)-1
deviation=np.abs(E_gambles-gambles)

# X-axis scale
x_step=np.ceil(gambles/20)

# Y-axis scale
y_step=np.ceil((max(result)-min(result))/20)

P_success=100*P_success

# Insights from simulation
print(f'\nProbability of success: {P_success} %')
print(f'Expected number of gambles: {E_gambles}')
print(f'Observed number of gambles: {gambles}')
print(f'Deviation between expectation and observation: {deviation}\n')

# Visual indicator of Gamblers final result
if result[-1]==goal:
    line_colour='g'
else:
    line_colour='r'

# Visualisation of the Gambler's actions
plt.figure(figsize=(11,6))
plt.xticks(np.arange(0,x_step+gambles,x_step))
plt.yticks(np.arange(0,y_step+goal,y_step))
plt.title("Gambler's Ruin")
plt.xlabel('Number of gambles made')
plt.ylabel("Gambler's balance (£)")
sns.lineplot(result,color=line_colour)
plt.show()
