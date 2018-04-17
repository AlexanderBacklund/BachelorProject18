#################################################################
# Python Script for sending connection information from client to SQL-database
# Authors: Albin Hjelm, Alexander Backlund & Sebastian Gustafsson
#
# Script Idea:
# 1. Check wether it's run on an Windows or Linux machine
# 2. Prompt for user input, UserID or such
# 3. Scan with wifi-card for available AccessPoints Limit to 5 results
# 4. Connect to SQL-database and insert data to table
# 5. Open website. (Which also might be inserted through userinput)
#
#################################################################
#Todos:
# TODO: prompting user for  checking which networkcard they want to use
# TODO: (maybe) prompt user for which system they're on
# TODO: prompt user for username
#################################################################

from wifi import Cell, Scheme
import time, platform

#creates a object type reference point
class RefPoint(object):
    name = ""
    position = ""
    adress1 = ""
    adress2 = ""
    rssi1 = 0
    rssi2 = 0

    # The class constructor
    def __init__(self, name, position, adress1, adress2, rssi1,rssi2):
        self.name = name
        self.age = age
        self.major = major
#function to create a reference point
def make_RefPoint(name, position, adress1, adress2, rssi1,rssi2):
    refPoint = RefPoint(name, position, adress1, adress2, rssi1,rssi2)
    return refPoint

#creates a list of dummy reference points
def createTestListOfRPs():
    r1 = make_RefPoint(r1, A1, AAA, BBB, -34, -55)
    r2 = make_RefPoint(r2, A2, CCC, DDD, -14, -18)
    r3 = make_RefPoint(r3, A3, EEE, FFF, -25, -33)
    rplist = [r1, r2, r3]
    return rplist

def checkOperatingSys():
    return platform.system()

#def checkWifiCard():

def scanNetworks(netwrkCard):
    cells = Cell.all(netwrkCard)
    while(len(cells) < 2):
        cells = Cell.all(netwrkCard)
        time.sleep(2)
        print('Scanning...')
    return cells

def sortNetworksReturnAmount(amountReturned, netwrkList):
    nList = sorted(netwrkList, key=lambda x: x.signal, reverse=True)[:amountReturned]
    return nList

#creates a list of relevant Reference points to check based on my position
def listOfRelRPs(listOfRefPoints, myPositionInfo):
    mac1 = myPositionInfo[0].address
    mac2 = myPositionInfo[1].address
    RelRPs = []
    for ref in listOfRefPoints:
        if ref.adress1 = mac1 and ref.adress2 = mac2:
        RelRPs.append(refs)
        elif ref.adress1 = mac1 and ref.adress2 = mac2:
        RelRPs.append(refs)
    return RelRPs

#determines which reference point is closest to me
def nearestRP(relRPs, myAPs):
    area = "position unknown"
    closestDiff = 100
    for rp in relRPs:
        if rp.adress1 = myAPs[0].adress1:
            diff1 = rp.rssi1 - myAPs[0].signal
            if diff1<0:
                diff1 = diff1 * -1
            diff2 = rp.rssi2 - myAPs[1].signal
            if diff2 < 0:
                diff2 = diff2 * -1
            diffSum = diff1 + diff2
        else
            diff1 = rp.rssi1 - myAPs[1].signal
            if diff1<0:
                diff1 = diff1 * -1
            diff2 = rp.rssi2 - myAPs[0].signal
            if diff2 < 0:
                diff2 = diff2 * -1
            diffSum = diff1 + diff2
        if diffSum < closestDiff:
            area = rp.position
            closestDiff = diffSum
    return area



def main():
    netcard = raw_input("Enter network-card for wifi-scan: ")

    l = scanNetworks(netcard)
    myAPs = sortNetworksReturnAmount(2,l)
    rplist = createTestListOfRPs()
    relRPs = listOfRelRPs(rplist, myAPs)
    myPosition = nearestRP(relRPs, myAPs)
    print myPosition


    #for l2 in myAPs:
    #    print(l2.ssid+" - "+str(l2.signal)+" - "+str(l2.address))

if __name__ == "__main__":
    main()
