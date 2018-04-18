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
import time, platform#,# MySQLdb

def connectToDB():
    return MySQLdb.connect(host="back.db1.course.it.uu.se", user="fall17_it12", passwd="vXdWAk2K", db="fall17_project_it12")

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
        self.position = position
        self.adress1 = adress1
        self.adress2 = adress2
        self.rssi1 = rssi1
        self.rssi2 = rssi2

#function to create a reference point
def make_RefPoint(name, position, adress1, adress2, rssi1,rssi2):
    refPoint = RefPoint(name, position, adress1, adress2, rssi1,rssi2)
    return refPoint

#creates a list of dummy reference points
def createTestListOfRPs():
    r1 = make_RefPoint("r1", "Albins dator", "24:01:C7:19:A3:00", "24:01:C7:19:A3:01", -52, -52)
    r2 = make_RefPoint("r2", "Borta vid bordet", "24:01:C7:19:CF:4E", "24:01:C7:19:CF:4F", -49, -46)
    r3 = make_RefPoint("r3", "Skrubben", "24:01:C7:19:47:10", "24:01:C7:19:47:11", -67, -68)
    rplist = [r1, r2, r3]
    return rplist

def checkOperatingSys():
    return platform.system()

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
def listOfRelRPs(listOfRefPoints, myPositionInfo, lengthAP):
    RelRPs = []
    for ref in listOfRefPoints:
        numberOfMatches = 0
        for tmp in range(0,lengthAP):
            if ref.adress1 == myPositionInfo[tmp].address or ref.adress2 == myPositionInfo[tmp].address:
                numberOfMatches += 1
        if (numberOfMatches > 0):
            RelRPs.append(ref)
    print("langden 1 " + str(len(RelRPs)))
    return RelRPs

#determines which reference point is closest to me
def nearestRP(relRPs, myAPs, lengthAP):
    for tsk in range(0,10):
        print(myAPs[tsk].address)
    print("langden " + str(len(relRPs)))
    if len(relRPs) == 0:
        return "position unknown"
    area = "position unknown"
    closestDiff = 300
    diff1 = 500
    diff2 = 500
    for rp in relRPs:
        for tmp in range(0,lengthAP):
            if (rp.adress1 == "" + myAPs[tmp].address):
                diff1 = rp.rssi1 - myAPs[tmp].signal
                if diff1<0:
                    diff1 = diff1 * -1
            elif rp.adress2 == "" + myAPs[tmp].address:
                diff2 = rp.rssi2 - myAPs[tmp].signal
                if diff2 < 0:
                    diff2 = diff2 * -1
        diffSum = diff1 + diff2
        if diffSum < closestDiff:
            area = rp.position
            closestDiff = diffSum
    return area



def getRefListFromDB(cur):
    cur.execute("SELECT * FROM SEBBE") # TODO: Change to reftable
    return cur.fetchall()


def main():
    netcard = raw_input("Enter network-card for wifi-scan: ")
    numberOfNetworksToScanAroundMe = 10

    # l = scanNetworks(netcard)
    # l1 = sortNetworksReturnAmount(4,l)
    #db = connectToDB()
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    #cur = db.cursor()

    #getRefListFromDB(cur)

    l = scanNetworks(netcard)
    myAPs = sortNetworksReturnAmount(numberOfNetworksToScanAroundMe,l)
    rplist = createTestListOfRPs()
    relRPs = listOfRelRPs(rplist, myAPs, numberOfNetworksToScanAroundMe)
    myPosition = nearestRP(relRPs, myAPs, numberOfNetworksToScanAroundMe)
    print myPosition


    #for l2 in l:
    #    print(l2.ssid+" - "+ str(l2.signal) + " - "+str(l2.address))
    #Leave me be
    ###############################################
    #db.close()

if __name__ == "__main__":
    main()
