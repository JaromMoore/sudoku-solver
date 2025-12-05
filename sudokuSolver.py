from tkinter import *
from tkinter import ttk

SNumberList = []
solvedSNumberList = [0] * 81

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

def solve():
    
    return

def getRow(rowNum):
    return SNumberList[rowNum*9:(rowNum+1)*9-1]

def getColumn(colNum):
    temp = []
    for i in range(0,8):
        temp.append(SNumberList[colNum + i*9])
    return SNumberList[colNum]

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
        




def main():
    createWindow()

if __name__ == "__main__":
    main()
