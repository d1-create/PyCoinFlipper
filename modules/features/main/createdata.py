import time, random
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
