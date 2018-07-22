#hashSet = range(-100000,10001)
hashSet = [0]*20001


def readFile(srcFile):    
    fl = open(srcFile)
    dataSet = []    
    for line in fl:
        dataSet.append(int(line))

def find_target_values(dataSet,minTarget=-10000,maxTarget=10000):   
    dataSet.sort() 
    setCounter = [0]*(maxTarget-minTarget + 1)
    for x in range (0,len(dataSet)):
        y_min = minTarget-x
        y_max = maxTarget-x
        while True:
            y = x+1
            if dataSet[y] < y_min:
                y+=1
            elif dataSet[y] > y_max:
                break
            else:
                setCounter[dataSet[x] + dataSet[y]+minTarget]=1
    tCount = 0
    for i in range(0,len(setCounter)):
        tCount+=setCounter[i]
    return tCount
    