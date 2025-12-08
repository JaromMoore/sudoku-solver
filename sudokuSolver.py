from tkinter import *
from tkinter import ttk

'''

'''







SNumberList = [9, 0, 0, 3, 2, 6, 0, 0, 4, 0, 7, 0, 0, 8, 9, 1, 3, 6, 0, 3, 1, 0, 0, 0, 5, 4, 0, 3, 0, 0, 8, 0, 4, 7, 0, 0, 0, 8, 0, 3, 0, 1, 6, 0, 0, 0, 4, 2, 0, 0, 5, 0, 0, 8, 7, 1, 9, 0, 6, 0, 4, 5, 3, 0, 0, 0, 5, 0, 0, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 1]
solvedSNumberList = [0] * 81
possibleList = []

def createWindow():
    window = Tk()
    window.title("sukoku solver")

    frame = ttk.Frame(window)
    frame.grid(column=0, row=0, sticky=(N, W, E, S))

    SFrame = ttk.Frame(frame, padding=(10, 10, 10, 10))
    SFrame.grid(column=(0), row=(0), sticky=(W))

    SEntryContainer = []
    for i in range(0,80):
        SNumberList.append(StringVar())
        SEntryContainer.append(ttk.Entry(SFrame, textvariable=SNumberList[i]))

    counter = 0
    for i in range(0,8):
        for j in range (0,8):
            SEntryContainer[counter].grid(column=(i), row=(j))
            SEntryContainer[counter]['width'] = 1
            counter += 1

    solveButton = ttk.Button(frame, text="solve")
    solveButton.grid(column=(1), row=(0))

    solvedSFrame = ttk.Frame(frame, padding=(10, 10, 10, 10))
    solvedSFrame.grid(column=(2), row=(0), sticky=(E))

    solvedSLabelContainer = []
    for i in range(0, 80):
        solvedSLabelContainer.append(ttk.Label(solvedSFrame, text=solvedSNumberList[i]))

    counter = 0
    for i in range(0,8):
        for j in range (0,8):
            solvedSLabelContainer[counter].grid(column=(i), row=(j))
            solvedSLabelContainer[counter]['width'] = 1
            counter += 1
    
    frame.focus()
    window.mainloop()

def getIndexRow(num):
    if num <= 8:
        return 0
    elif num <= 17:
        return 1
    elif num <= 26:
        return 2
    elif num <= 35:
        return 3
    elif num <= 44:
        return 4
    elif num <= 53:
        return 5
    elif num <= 62:
        return 6
    elif num <= 71:
        return 7
    elif num <= 80:
        return 8
    else:
        return None

def getIndexCol(num):
    if num in (0, 9, 18, 27, 36, 45, 54, 63, 72):
        return 0
    elif num in (1, 10, 19, 28, 37, 46, 55, 64, 73):
        return 1
    elif num in (2, 11, 20, 29, 38, 47, 56, 65, 74):
        return 2
    elif num in (3, 12, 21, 30, 39, 48, 57, 66, 75):
        return 3
    elif num in (4, 13, 22, 31, 40, 49, 58, 67, 76):
        return 4
    elif num in (5, 14, 23, 32, 41, 50, 59, 68, 77):
        return 5
    elif num in (6, 15, 24, 33, 42, 51, 60, 69, 78):
        return 6
    elif num in (7, 16, 25, 34, 43, 52, 61, 70, 79):
        return 7
    elif num in (8, 17, 26, 35, 44, 53, 62, 71, 80):
        return 8
    else:
        return None

def getIndexBlock(num):
    if num in (0, 1, 2, 9, 10, 11, 18, 19, 20):
        return 0
    elif num in (3, 4, 6, 12, 13, 14, 21, 22, 23):
        return 1
    elif num in (6, 7, 8, 15, 16, 17, 24, 25, 26):
        return 2
    elif num in (27, 28, 29, 36, 37, 38, 45, 46, 47):
        return 3
    elif num in (30, 31, 32, 39, 40, 41, 48, 49, 50):
        return 4
    elif num in (33, 34, 35, 42, 43, 44, 51, 52, 53):
        return 5
    elif num in (54, 55, 56, 63, 64, 65, 72, 73, 74):
        return 6
    elif num in (57, 58, 59, 66, 67, 68, 75, 76, 77):
        return 7
    elif num in (60, 61, 62, 69, 70, 71, 78, 79, 80):
        return 8
    else:
        return None
    
def fillPossibleNums():
    for i in range(0,80):
        temp = []
        if SNumberList[i] == 0:
            for j in range(1,9):
                if j not in getRow(getIndexRow(i)) and j not in getColumn(getIndexCol(i)) and j not in getBlock(getIndexBlock(i)):
                    temp.append(j)
        possibleList.append(temp)   

def parsePossibleNums():
    for i in range(0,80):
        if len(possibleList[i]) == 1:
            SNumberList[i] = possibleList[i][1]

    for i in range(0,8):
        counter = 0
        for j in range(0,8):
            for k in range(1,9):
                if  getPossibleBlock(i)[j].count(k) == 1:
                    return
 ########   



def solve():
    
    return

def getRow(rowNum):
    return SNumberList[rowNum*9:(rowNum+1)*9-1]

def getColumn(colNum):
    temp = []
    for i in range(0,8):
        temp.append(SNumberList[colNum + i*9])
    return temp

def getBlock(blockNum):
    temp = []
    match blockNum:
        case 0:
            temp.append(SNumberList[0])
            temp.append(SNumberList[1])
            temp.append(SNumberList[2])
            temp.append(SNumberList[9])
            temp.append(SNumberList[10])
            temp.append(SNumberList[11])
            temp.append(SNumberList[18])
            temp.append(SNumberList[19])
            temp.append(SNumberList[20])
        case 1:
            temp.append(SNumberList[3])
            temp.append(SNumberList[4])
            temp.append(SNumberList[5])
            temp.append(SNumberList[12])
            temp.append(SNumberList[13])
            temp.append(SNumberList[14])
            temp.append(SNumberList[21])
            temp.append(SNumberList[22])
            temp.append(SNumberList[23])
        case 2:
            temp.append(SNumberList[6])
            temp.append(SNumberList[7])
            temp.append(SNumberList[8])
            temp.append(SNumberList[15])
            temp.append(SNumberList[16])
            temp.append(SNumberList[17])
            temp.append(SNumberList[24])
            temp.append(SNumberList[25])
            temp.append(SNumberList[26])
        case 3:
            temp.append(SNumberList[27])
            temp.append(SNumberList[28])
            temp.append(SNumberList[29])
            temp.append(SNumberList[36])
            temp.append(SNumberList[37])
            temp.append(SNumberList[38])
            temp.append(SNumberList[45])
            temp.append(SNumberList[46])
            temp.append(SNumberList[47])
        case 4:
            temp.append(SNumberList[30])
            temp.append(SNumberList[31])
            temp.append(SNumberList[32])
            temp.append(SNumberList[39])
            temp.append(SNumberList[40])
            temp.append(SNumberList[41])
            temp.append(SNumberList[48])
            temp.append(SNumberList[49])
            temp.append(SNumberList[50])
        case 5:
            temp.append(SNumberList[33])
            temp.append(SNumberList[34])
            temp.append(SNumberList[35])
            temp.append(SNumberList[42])
            temp.append(SNumberList[43])
            temp.append(SNumberList[44])
            temp.append(SNumberList[51])
            temp.append(SNumberList[52])
            temp.append(SNumberList[53])
        case 6:
            temp.append(SNumberList[54])
            temp.append(SNumberList[55])
            temp.append(SNumberList[56])
            temp.append(SNumberList[63])
            temp.append(SNumberList[64])
            temp.append(SNumberList[65])
            temp.append(SNumberList[72])
            temp.append(SNumberList[73])
            temp.append(SNumberList[74])
        case 7:
            temp.append(SNumberList[57])
            temp.append(SNumberList[58])
            temp.append(SNumberList[59])
            temp.append(SNumberList[66])
            temp.append(SNumberList[67])
            temp.append(SNumberList[68])
            temp.append(SNumberList[75])
            temp.append(SNumberList[76])
            temp.append(SNumberList[77])
        case 8:
            temp.append(SNumberList[60])
            temp.append(SNumberList[61])
            temp.append(SNumberList[62])
            temp.append(SNumberList[69])
            temp.append(SNumberList[70])
            temp.append(SNumberList[71])
            temp.append(SNumberList[78])
            temp.append(SNumberList[79])
            temp.append(SNumberList[80])
    return temp
        
def getPossibleBlock(blockNum):
    temp = []
    match blockNum:
        case 0:
            temp.append(possibleList[0])
            temp.append(possibleList[1])
            temp.append(possibleList[2])
            temp.append(possibleList[9])
            temp.append(possibleList[10])
            temp.append(possibleList[11])
            temp.append(possibleList[18])
            temp.append(possibleList[19])
            temp.append(possibleList[20])
        case 1:
            temp.append(possibleList[3])
            temp.append(possibleList[4])
            temp.append(possibleList[5])
            temp.append(possibleList[12])
            temp.append(possibleList[13])
            temp.append(possibleList[14])
            temp.append(possibleList[21])
            temp.append(possibleList[22])
            temp.append(possibleList[23])
        case 2:
            temp.append(possibleList[6])
            temp.append(possibleList[7])
            temp.append(possibleList[8])
            temp.append(possibleList[15])
            temp.append(possibleList[16])
            temp.append(possibleList[17])
            temp.append(possibleList[24])
            temp.append(possibleList[25])
            temp.append(possibleList[26])
        case 3:
            temp.append(possibleList[27])
            temp.append(possibleList[28])
            temp.append(possibleList[29])
            temp.append(possibleList[36])
            temp.append(possibleList[37])
            temp.append(possibleList[38])
            temp.append(possibleList[45])
            temp.append(possibleList[46])
            temp.append(possibleList[47])
        case 4:
            temp.append(possibleList[30])
            temp.append(possibleList[31])
            temp.append(possibleList[32])
            temp.append(possibleList[39])
            temp.append(possibleList[40])
            temp.append(possibleList[41])
            temp.append(possibleList[48])
            temp.append(possibleList[49])
            temp.append(possibleList[50])
        case 5:
            temp.append(possibleList[33])
            temp.append(possibleList[34])
            temp.append(possibleList[35])
            temp.append(possibleList[42])
            temp.append(possibleList[43])
            temp.append(possibleList[44])
            temp.append(possibleList[51])
            temp.append(possibleList[52])
            temp.append(possibleList[53])
        case 6:
            temp.append(possibleList[54])
            temp.append(possibleList[55])
            temp.append(possibleList[56])
            temp.append(possibleList[63])
            temp.append(possibleList[64])
            temp.append(possibleList[65])
            temp.append(possibleList[72])
            temp.append(possibleList[73])
            temp.append(possibleList[74])
        case 7:
            temp.append(possibleList[57])
            temp.append(possibleList[58])
            temp.append(possibleList[59])
            temp.append(possibleList[66])
            temp.append(possibleList[67])
            temp.append(possibleList[68])
            temp.append(possibleList[75])
            temp.append(possibleList[76])
            temp.append(possibleList[77])
        case 8:
            temp.append(possibleList[60])
            temp.append(possibleList[61])
            temp.append(possibleList[62])
            temp.append(possibleList[69])
            temp.append(possibleList[70])
            temp.append(possibleList[71])
            temp.append(possibleList[78])
            temp.append(possibleList[79])
            temp.append(possibleList[80])
    return temp
        
def getPossibleRow(rowNum):
    return possibleList[rowNum*9:(rowNum+1)*9-1]


def getPossibleColumn(colNum):
    temp = []
    for i in range(0,8):
        temp.append(possibleList[colNum + i*9])
    return temp

def main():
    #createWindow()
    fillPossibleNums()
    print(getPossibleBlock(0))


if __name__ == "__main__":
    main()
