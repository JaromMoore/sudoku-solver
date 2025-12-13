possibleList= []
SNumberList = []
def wentWrong():
    global SNumberList
    for i in range(0,81):
        if len(possibleList[i]) == 0:
            if SNumberList[i] == 0:
                SNumberList = copy.deepcopy(listBackups[-1])