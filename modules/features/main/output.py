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
            datafile.write(f"CoinsFlipped: {str(data['CoinsToFlip'])}\n")
            datafile.write(f"Heads: {str(data['Heads'])}\n")
            datafile.write(f"Tails: {str(data['Tails'])}\n")
            datafile.write(f"Total: {str(data['Total'])}\n")
            datafile.write(f"CoinDataList: {str(data['CoinDataList'])}\n")