#libraries
import random
import os
import time
import configparser

#modules to import
import modules.debug.startdebug as DebugFile
import settings.settings as settings
import modules.features.mainfeatures as mainfeatures
import modules.features.relativefreq as relativefrequency
#import extra features
#set important variables
IsDebug = settings.IsDebug
AskDebug = settings.AskDebug
#ask to disable debug if settings turned on
DebugFile.StartDebug(IsDebug,AskDebug)
os.system("clear")

def Main():
    #data stored in a dictionary
    data = {"CoinsToFlip":None,"Heads":None, "HeadsRel":None, "TailsRel":None,"Tails":None,"Total":None,"CoinDataList":None}
    #enter coins to flip data
    data["CoinsToFlip"] = mainfeatures.GetInput()
    print(data["CoinsToFlip"])
    #input the rest of the RAW data, not processed using equations or complex calculations
    data["CoinDataList"], data["Heads"], data["Tails"], data["Total"] = mainfeatures.CreateData(data["CoinsToFlip"], IsDebug)
    data["HeadsRel"],data["TailsRel"] = relativefrequency.FindRelativeFreq(data["Heads"],data["Tails"],data["Total"])
    #choose to output the data in a text file, command line (console) or to not output anything
    mainfeatures.Output(data)

    #thank the user and clear everything
    print("Thanks for using this software!" )
Main() 