# get a number of coins to count and then get the relative frequency of these, returning them to the user

# import all libraries
import random


# function to return a number of coins to flip
def InputCoins():
    numcoins = int(input("How many coins would you like to flip? "))
    return numcoins


# function to return an array of all the coins
def GetCoinData(CoinsToFlip):
    # create a changeable array of coins
    CoinData = []
    # create heads and tails variables
    heads = 0
    tails = 0

    # loop through the stuff and randomly select
    for i in range(CoinsToFlip):
        rand = random.randint(1, 2)
        CoinData.append(rand)

        # get heads and tails
        if (rand == 1):
            heads += 1
        elif (rand == 2):
            tails += 1

    return CoinData, heads, tails


# find the relative frequency
def RelativeFreq(heads, tails):
    # get relative frequency
    total = heads + tails  # get total of heads and tails
    # find heads and tails relative frequency
    headsrelfreq = heads / total
    tailsrelfreq = tails / total
    # round relative frequency values
    headsrelfreq = round(headsrelfreq, 3)
    tailsrelfreq = round(tailsrelfreq, 3)
    return headsrelfreq, tailsrelfreq, total


# print all data if wanted
def PrintAllData(heads, tails, total, headsrelfreq, tailsrelfreq):
    # print out data if user wants to
    userwantsdata = False
    if (str(input("Do you want the data to be printed? ")).lower() == "yes"):
        print(f"Heads: {heads}, Tails: {tails}, Total: {total}")
        # print out the relative frequency
        print(
            f"The relative frequency of heads is {headsrelfreq} and the relative frequency of tails is {tailsrelfreq}")


def Main():
    CoinsToFlip = InputCoins()
    alldata, heads, tails = GetCoinData(CoinsToFlip)
    headsrelfreq, tailsrelfreq, total = RelativeFreq(heads, tails)
    PrintAllData(heads, tails, total, headsrelfreq, tailsrelfreq)


Main()
