import random
import matplotlib
import matplotlib.pyplot as plt
import time

sampleSize=100
startingFunds=10000
wagerSize=100
wagerCount=1000


def rollDice():
    roll=random.randint(1,100)
    return 50<roll<100

def simple_bettor(funds,intial_wager,wager_count):
    global broke_count
    val=funds
    wager=intial_wager

    wX=[]
    vY=[]

    currentwager=1

    while currentwager<=wager_count:
        if rollDice():
            val+=wager
            wX.append(currentwager)
            vY.append(val)

        else:
            val-=wager   
            wX.append(currentwager)
            vY.append(val)

        if val<=0:
            broke_count+=1
            break
            
        currentwager+=1

    plt.plot(wX,vY,'k')

def doubler_bettor(funds,initial_wager,wager_count):
    value=funds
    wager=initial_wager
    global broke_count

    wX=[]
    vY=[]

    currentWager=1
    previousWager= 'Win'
    previousWagerAmount=initial_wager

    while currentWager<= wager_count:
        if previousWager=='Win':
            if rollDice():
                value+=wager
               
                wX.append(currentWager)
                vY.append(value)
            else:
                value-=wager
                previousWager='loss'
                
                previousWagerAmount=wager
                wX.append(currentWager)
                vY.append(value)
                if value<0:
                    
                    broke_count +=1
                    break

        elif previousWager=='loss':
           
            wager=previousWagerAmount*2
            if rollDice():
               
                value+=wager
                
                wager = initial_wager
                previousWager='Win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager=previousWagerAmount*2
                value -= wager 
                if value<0:
                    broke_count +=1
                    break

                previousWager='loss'

                previousWagerAmount=wager
                wX.append(currentWager)
                vY.append(value)

        currentWager+=1

    plt.plot(wX,vY,'c')    


x=0
broke_count=0

while x<sampleSize:
    simple_bettor(startingFunds,wagerSize,wagerCount)
    doubler_bettor(startingFunds,wagerSize,wagerCount)
    x+=1


plt.ylabel('balance')
plt.xlabel('wager count')
plt.show()

