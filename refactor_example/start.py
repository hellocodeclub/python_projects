import pickle
print('pickle imported.')
print()

newGame = True

try:
    masterList = pickle.load(open('everythingSimulatorLoadData','rb'))

    if newGame == False:
        EverythingSimulatorFirstTime = False
    else:
        EverythingSimulatorFirstTime = True

except NameError:
    EverythingSimulatorFirstTime = True

except FileNotFoundError:
    EverythingSimulatorFirstTime = True

if EverythingSimulatorFirstTime == True:
    print('Program started for the first time.')
    print()

    masterDictionary = {}
    print('masterDictionary = ',masterDictionary)

    masterList = []
    print('masterList = ',masterList)

    content = '0'
    eName = 'eventCount'
    one = 'masterDictionary[' + "'" + eName + "'" + '] = ' + content
    two = eName + ' = ' + content

    print()
    print(one)
    print(two)
    print()

    exec(one)
    exec(two)

    print()
    print('masterDictionary = ', masterDictionary)
    print(eName + ' = ',eventCount)
    print()

    content = '0'
    eName = 'selected'
    one = 'masterDictionary[' + "'" + eName + "'" + '] = ' + content
    two = eName + ' = ' + content

    print()
    print(one)
    print(two)
    print()

    exec(one)
    exec(two)

    print()
    print('masterDictionary = ', masterDictionary)
    print(eName + ' = ',eventCount)
    print()

    createEvent = False
    simulate = False
    print('While loop determining variables created and set.')

    EverythingSimulatorFirstTime = False

from tkinter import *
import Pmw
import os.path
import random
import copy
from math import *
from decimal import *
print('Libraries imported.')

print('No functions created.')

master = Tk()

eventViewer = Frame(master)
eventViewer.grid(row = 0,column = 0)

events1 = Frame(eventViewer)
events1.grid(row = 1,column = 0)

createEvent = True
simulate = True

nameList = ['generalFor','multiplierFor','generalAgainst','multiplierAgainst','amount','name','contained']
contentList = ['[30]','[1.5,4]','[30]','[0.5,1]','1000',"'Event'",'[]']

nameList = ['generalFor','multiplierFor','generalAgainst','multiplierAgainst','amount','name','contained','eventCount','selected']

saveSlot = '1'

saveGame = True
loadGame = True
if saveGame == True:
    i = 0
    while i <= len(nameList) - 1:
        try:
            variable = eval(nameList[i])
            parent = os.path.dirname(__file__)
            backslash = '\\'
            directory = parent + backslash + 'saves' + backslash + 'save' + saveSlot
            directory2 = directory + backslash + nameList[i]
            print('directory = ',directory)
            print('directory2 = ',directory2)

            if not os.path.exists(directory):
                os.makedirs(directory)

            outFile = open(directory2,'wb')
            pickle.dump(variable,outFile)
            outFile.close()
            print(nameList[i] + ' was saved.')
        except NameError:
            print(nameList[i] + ' is not defined. I can' + "'" + 't save it because it doesn' + "'" + 't exist. Sorry.')
        print()
        i += 1

if loadGame == True:
    i = 0
    while i <= len(nameList) - 1:
        try:
            parent = os.path.dirname(__file__)
            backslash = '\\'
            directory = parent + backslash + 'saves' + backslash + 'save' + saveSlot
            directory2 = directory + backslash + nameList[i]
            print('directory = ',directory)
            print('directory2 = ',directory2)

            if not os.path.exists(directory):
                os.makedirs(directory)

            inFile = open(directory2,'rb')
            pickle.load(inFile)
            inFile.close()
            print(nameList[i] + ' was loaded.')
        except FileNotFoundError:
            print('The ' + nameList[i] + ' file was not found. I can' + "'" + 't load it. Sorry.')
        print()
        i += 1

nameList = ['generalFor','multiplierFor','generalAgainst','multiplierAgainst','amount','name','contained']

try:
    toViewer = round(amountTrue[selected],)
    print('Viewer would see: ',toViewer)

    percentage = (100 / amount[selected]) * amountTrue
    print('(100 / ',amount[selected],') * ',amountTrue,'.')
    viewerPercentage = round(percentage)
    print('percentage = ',percentage,'.')
    print('Viewer would see: ',viewerPercentage,'%.')
except NameError:
    print('No event selected.')

#This code prints information about the selected event.
try:
    print()
    print('Events:')
    print(name)

    if amountTrue[selected] > 1000000:
        viewedAmountTrue = '> 1000000'
    else:
        viewedAmountTrue = str(amountTrue[selected])

    if amount[selected] > 1000000:
        viewedAmount = '> 1000000'
    else:
        viewedAmount = str(amount[selected])

    print('amount: ' + viewedAmountTrue + ' / ' + viewedAmount + ', <decimal or integer between 1 and 100>%')
    print('Contained events:')

    i = 0
    while i <= len(contained[selected]) - 1:
        container = contained[selected]
        used = container[i]
        key = dict.get(used,default = None)
        print(name[key])
        i += 1


    print('User selects everything.')
except NameError:
    print('No event selected.')

#This code creates a set of variables known as an event, which, after being created, share an associated event number, known as a key.
i = 0
while createEvent == True:
    created = 0
    while created <= len(nameList) - 1:
        eName = nameList[i]
        content = contentList[i]

        one = eName + ' = {}'
        two = eName + '[eventCount] = ' + content
        three = 'print(' + "'" + eName + "'" + ',[eventCount],' + "'" + ' was created, containing ' + "'" + ',' + eName + '[eventCount],' + "'" + '.' + "'" + ')'
        four = 'masterDictionary[' + "'" + eName + "'" + '] = ' + content
        five = eName + ' = ' + content
        six = 'print (' + "'" + eName + "'" + ',[eventCount],' + "'" + ' was saved in RAM.' + "'" + ')'

        print()

        print(one)
        print(two)
        print(three)
        print()
        print(four)
        print(five)
        print()
        print(six)

        print()

        exec(one)
        exec(two)
        exec(three)
        exec(four)
        exec(five)
        exec(six)

        print()
        print('masterDictionary = ', masterDictionary)
        print(eName + ' = ',eventCount)
        print()

        i += 1
        created += 1
    print()
    eventCount += 1

    print(one)

    exec(one)

    print('eventCount was saved.')
    print()
    createEvent = False

while simulate == True:
    print('Simulating ',selected,'.')

    try:
        multiplierForLength = len(multiplierFor[selected])
    except TypeError:
        multiplierForLength = 1
    print('multiplierForLength = ',multiplierForLength)
    print('multiplierFor[',selected,'] = ',multiplierFor[selected])
    print()

    try:
        multiplierAgainstLength = len(multiplierAgainst[selected])
    except:
        multiplierAgainstLength = 1

    if multiplierForLength >= multiplierAgainstLength:
        try:
            largest = fsum(multiplierFor[selected])
        except TypeError:
            largest = multiplierFor[selected]
        try:
            smallest = fsum(multiplierAgainst[selected])
        except TypeError:
            smallest = multiplierAgainst[selected]

        print('largest = ',largest,'.')
        print('largest = multiplierFor[selected]')
        print('smallest = ',smallest,'.')
        print('smallest = multiplierAgainst[selected]')
    else:
        largest = fsum(multiplierAgainst[selected])
        smallest = fsum(multiplierFor[selected])
        print('largest = ',largest,'.')
        print('largest = multiplierAgainst[selected]')
        print('smallest = ',smallest,'.')
        print('smallest = multiplierFor[selected]')

    timesDone = 0
    while timesDone < 4:
        if timesDone == 0:
            subject = copy.deepcopy(generalFor[selected])
            print('generalFor ',selected,' copied.')
        elif timesDone == 1:
            subject = copy.deepcopy(multiplierFor[selected])
            print('multiplierFor ',selected,' copied.')
        elif timesDone == 2:
            subject = copy.deepcopy(generalAgainst[selected])
            print('generalAgainst copied.')
        else:
            subject = copy.deepcopy(multiplierAgainst[selected])
            print('multiplierAgainst copied.')

        try:
            subjectAverage = fsum(subject) / len(subject)
            print(fsum(subject),' / ',len(subject),'.')
        except TypeError:
            subjectAverage = subject
            print('I cannot average a single object because attempting to do so returns a TypeError, so I' + "'" + 'm going to make subjectAverage equal to subject because that is the average.')
        print('subjectAverage = ',subjectAverage,'.')

        try:
            subjectLength = len(subject)
        except TypeError:
            subjectLength = 1

        subjectCalculated = subjectAverage ** subjectLength
        print(subjectAverage,' ** ',subjectLength,'.')
        print('subjectCalculated = ',subjectAverage,'.')
        half = subjectCalculated / largest
        print(subjectCalculated,' / ',largest,'.')
        print('half = ',half,'.')

        if timesDone == 0:
            half1 = half
            print('half1 = ',half1,'.')
        elif timesDone == 1:
            half2 = half
            print('half2 = ',half2,'.')
        elif timesDone == 2:
            half3 = half
            print('half3 = ',half3,'.')
        else:
            half4 = half
            print('half4 = ',half4,'.')
        timesDone += 1

    supportFor = 1 - (half1 ** half2)
    print('1 - (',half1,' ** ',half2,').')
    print('supportFor = ',supportFor,'.')
    supportAgainst = 1 - (half3 ** half4)
    print('1 - ',half3,' ** ',half4,').')
    print('supportAgainst = ',supportAgainst,'.')

    #This part of the code calculates the support for and against the event.

    probability = supportFor / (supportFor + supportAgainst)
    print(supportFor,' / ','(',supportFor,' + ',supportAgainst,')','.')
    print('probability = ',probability,'.')

    estimate = amount[selected] * float(probability)
    print(amount[selected],' * ',probability,'.')
    print('estimate = ',estimate,'.')

    go = True
    while go == True:
        randomNumber = random.uniform(0,1.00000000000000001)
        print('randomNumber = ',randomNumber,'.')
        if randomNumber <= 0.5:
            print('estimate to be changed.')
            randomNumber = random.uniform(0,1.00000000000000001)
            print('randomNumber = ',randomNumber,'.')
            if randomNumber <= probability:
                estimate = estimate + 1
                print(estimate,' + 1.')
                if estimate > amount[selected]:
                    estimate = amount[selected]
                print('estimate = ',estimate,'.')
            else:
                estimate = estimate - 1
                print(estimate,' - 1.')
                if estimate < 0:
                    estimate = 0
                print('estimate = ',estimate,'.')
        else:
            print('estimate not to be changed.')
            go = False

    amountTrue = {}
    amountTrue[selected] = estimate
    print ('amountTrue', [selected], ' was created, containing ',amountTrue[selected],'.')
    eName = 'amountTrue'
    one = 'pickle.dump(' + eName + '[selected],open(' + "'" + eName + "'" + ',' + "'" + 'wb' + "'" + '))'

    print(one)

    exec(one)

    print(eName + ' was saved.')

    simulate = False

    master.mainloop()