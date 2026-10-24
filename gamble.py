import random
import matplotlib.pyplot as plt

#Possible outcomes for the simple symmetric gamblers ruin problem
outcomes=[1,-1]

#Amount of money the Gambler is aiming to win
goal=9 #change at will

#Amount of money the Gambler starts with
balance=5 #change at will

series=[balance]

#Simulation of the Gamblers bets
def Gambler(balance,goal):
    while balance<goal and balance>0:
        result=random.choice(outcomes)
        balance+=result
        series.append(balance)
    return series

Gambler(balance,goal)

#Number of bets made by the Gambler
bets=[]
for i in range(0,len(series)):
    bets.append(i)

#Colour indicating whether the Gambler reached his goal or not
if series[-1]==goal:
    line_colour='g'
else:
    line_colour='r'

#Probability of the Gambler reaching his goal 
p_success=round(balance/goal,2)
print('Probability of success: ',p_success)

#Graph of how the Gambler fared on his bets
plt.title("Gambler's ruin")
plt.xlabel('Number of bets made by Gambler')
plt.ylabel('Money held by Gambler (£)')
plt.plot(bets,series,color=line_colour)
plt.grid(True)
plt.show()
