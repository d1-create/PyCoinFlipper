#libraries
import os

#modules to import
import settings.settings as settingsfile #settings
import modules.features.mainfeatures as mainfeatures #main feature
import modules.features.relativefreq as relativefrequency #relative frequency

def Main():
    #data stored locally in a dictionary
    data = {"CoinsToFlip":int,"Heads":int, "HeadsRel":float, "TailsRel":float,"Tails":int,"Total":int,"CoinDataList":list}
    #enter coins to flip data
    data["CoinsToFlip"] = mainfeatures.GetInput()
    print(data["CoinsToFlip"])
    #input the rest of the RAW data, not processed using equations or complex calculations
    data["CoinDataList"], data["Heads"], data["Tails"], data["Total"] = mainfeatures.CreateData(data["CoinsToFlip"], settingsfile.IsDebug)
    data["HeadsRel"],data["TailsRel"] = relativefrequency.FindRelativeFreq(data["Heads"],data["Tails"],data["Total"])
    #choose to output the data in a text file, command line (console) or to not output anything
    mainfeatures.Output(data)

    #thank the user and clear everything
    print("Thanks for using this software!" )

Main() 