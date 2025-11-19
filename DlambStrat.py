import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    roll=random.randint(1,100)
    return 50<roll<100

def Dlambstrat(funds,initial_wager,wager_count):
    global busts
    global profits
    global ROI

    value=funds
    wager=initial_wager
    currentwager=1
    previouswager='win'
    previouswageramount=initial_wager

    while currentwager<=wager_count:
        if previouswager=='win':
            if wager==initial_wager:
                pass
            else:
                wager-=initial_wager

            if rollDice():
                value+=wager
                previouswageramount=wager
            else:
                value-=wager
                previouswager='loss'
                previouswageramount=wager

                if value<=0:
                    busts+=1
                    break

        elif previouswager=='loss':
            wager=previouswageramount+initial_wager
            if (value-wager)<=0:
                wager=value

            if rollDice():
                value+=wager
                previouswager='win'
                previouswageramount=wager
            else:
                value-=wager
                previouswageramount=wager

                if value <=0:
                    busts+=1
                    break

        currentwager+=1

    if value>funds:
        profits+=1
    
    ROI=value
    return ROI

sampleSize=1000
startingFunds=100000
wagerSize=1000
wagerCount=10000
busts=0
profits=0

x=0

count=0
death=0
ret=0
while x<sampleSize:
    r=Dlambstrat(startingFunds,wagerSize,wagerCount)
    ret=r+ret
    if r>startingFunds:
        count+=1
    if r<startingFunds:
        death+=1
    x+=1

    
print("Bust Rate-> ",death/x,"Profit Rtae -> ",count/x, "ROI=",ret)


