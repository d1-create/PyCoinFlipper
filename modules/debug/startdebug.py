def StartDebug(IsDebug, AskDebug):
    if(AskDebug == True):
        AskDebugOff = str(input("Do you want to Disable Debug? (Enter-Skip, Disable-D)")).upper()
        if(AskDebugOff == "D"):
            AskDebug = False
        elif(AskDebugOff != "D"):
            pass
    elif(AskDebug == False):
        pass
    return IsDebug, AskDebug