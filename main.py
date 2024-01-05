#libraries
import random
import os
import time
import configparser

#important variables for runtime 
IsDebug = True
AskDebug = True
#modules to import
import modules.startdebug as DebugFile
import settings.settings as settings
from modules.functions import *
#set important variables
IsDebug = settings.IsDebug
AskDebug = settings.AskDebug
#ask to disable debug if settings turned on
DebugFile.StartDebug(IsDebug,AskDebug)
os.system("clear")

def Main():
    #data stored in a dictionary
    data = {"CoinsToFlip":None,"CoinDataList":None,"Heads":None,"Tails":None,"Total":None}
    #enter coins to flip data
    data["CoinsToFlip"] = GetInput()
    print(data["CoinsToFlip"])
    #input the rest of the RAW data, not processed using equations or complex calculations
    data["CoinDataList"], data["Heads"], data["Tails"], data["Total"] = CreateData(data["CoinsToFlip"], IsDebug)
    #choose to output the data in a text file, command line (console) or to not output anything
    Output(data)

    #thank the user and clear everything
    print("Thanks for using this software!" )
Main() 