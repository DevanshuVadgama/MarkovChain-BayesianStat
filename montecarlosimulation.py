import random
import matplotlib
import matplotlib.pyplot as plt

# Gambling problem

def rollDice():
    roll=random.randint(1,100)
    
    if roll==100:
        #rint(roll,"roll was 100, you lost")
        return False
    elif roll<=50:
        #rint(roll,'roll was 1-50,you lose')
        return False   
    elif 50<roll<100:
        #rint("You win!!")
        return True
    
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

    print(value)
    plt.plot(wX,vY)

##########################################################################################3

def simple_bettor(funds,initial_wager,wager_count):
    val=funds
    wager=initial_wager

    wX=[]
    vY=[]


    currentWager = 1

    while currentWager<=wager_count:
        if rollDice():
            val +=wager
            wX.append(currentWager)
            vY.append(val)
        else:
            val-=wager
            wX.append(currentWager)
            vY.append(val)


        currentWager +=1

    if val<0:
        val='broke'

    plt.plot(wX,vY)

x=0
broke_count=0

while x<1000:
    doubler_bettor(10000,100,1000)
    x+=1

print("Death rate = ", 100*(broke_count/float(x)))   

plt.axhline(0,color='r') #{if line crossed=> broke}

plt.ylabel('Balance')
plt.xlabel('Wager count') 
plt.show()



