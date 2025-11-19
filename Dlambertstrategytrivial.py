import random
import matplotlib.pyplot as plt

def Roulette():
    roll = random.randint(1, 100)
    return 50 < roll < 100

busts = 0
profits = 0

def DLambStrat(funds, initial_wager, wager_count):
    global busts
    global profits

    value = funds
    wager = initial_wager
    currentwager = 1
    previouswager = 'win'  
    previouswageramount = initial_wager
    vY = []
    wX = []

    while currentwager <= wager_count:
        if previouswager == 'win':
            if wager != initial_wager:
                wager -= initial_wager

            if Roulette():
                value += wager
                previouswageramount = wager
            else:
                value -= wager
                previouswager = 'loss'
                previouswageramount = wager
                if value <= 0:
                    busts += 1
                    break

        elif previouswager == 'loss':
            wager = previouswageramount + initial_wager
            if value - wager <= 0:
                wager = value

            if Roulette():
                value += wager
                previouswageramount = wager
                previouswager = 'win'
            else:
                value -= wager
                previouswageramount = wager
                previouswager = 'loss'
                if value <= 0:
                    busts += 1
                    break

        vY.append(wager)
        wX.append(currentwager)
        currentwager += 1

    profits += value - funds
    return value, wX, vY

# Run simulation
final_value, wX, vY = DLambStrat(10000, 1000, 10000)

# Plot
plt.plot(wX, vY, marker='o')
plt.xlabel("Wager Number")
plt.ylabel("Wager Amount")
plt.title("d'Alembert Betting Progress")
plt.show()
