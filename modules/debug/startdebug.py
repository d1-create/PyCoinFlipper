def StartDebug(IsDebug, AskDebug):
    if(AskDebug == True):
        AskDebug = str(input("Do you want to Disable Debug? (Enter-Skip, Disable-D, Skip/Enable-Enter)"))
    elif(AskDebug == False):
        pass
    return IsDebug, AskDebug