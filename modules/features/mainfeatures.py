import time, random, os

#get the input from the user and return the coin value
def GetInput():
    coins = int(input("how many coins do you want to flip "))
    return coins 

#create all the raw data
def CreateData(CoinsToFlip, IsDebug):
    start = time.process_time()
    CoinData = []
    heads = 0
    tails = 0

    #do the loop that creates all the data and the list
    for i in range(CoinsToFlip):
        randomnumber = random.randint(1,2)
        CoinData.append(randomnumber)
        if(randomnumber == 1):
            tails +=1
        if(randomnumber == 2):
            heads +=1

    #if debug mode is on show the time taken for the process to start
    if(IsDebug):
        print(f"Time Taken : {(time.process_time() - start)}")

    total = heads+tails
    return CoinData, heads, tails, total

def Output(data):
    #does the user want output to happen
    DoesWantOutput = str(input("Do you want to print out the input of this data? ")).upper()
    #if yes then ask for more info
    if(DoesWantOutput == "YES" or DoesWantOutput == "OK"):
        #ask for type of input
        TypeOfOutput = str(input("Text file(put TEXT) or printed to the console without the list(put PRINT) ")).upper()
        #if they want to print it to the console the do that
        if(TypeOfOutput == "PRINT"):
            print(f"Coins Flipped: {data['CoinsToFlip']}, Heads: {data['Heads']}, Tails: {data['Tails']}, Total: {data['Total']}")
        #else print to a text file
        if(TypeOfOutput == "TEXT"):
            datafile = open("CoinDataFile.txt", "wt")
            #open it for writing and write all the data
            for name,value in data.items():
                datafile.write(f"{name}: {str(value)}\n")
