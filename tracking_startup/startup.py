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
    adress3 = ""
    rssi1 = 0
    rssi2 = 0
    rssi3 = 0

    # The class constructor
    def __init__(self, name, position, adress1, adress2, adress3, rssi1,rssi2, rssi3):
        self.name = name
        self.position = position
        self.adress1 = adress1
        self.adress2 = adress2
        self.adress3 = adress3
        self.rssi1 = rssi1
        self.rssi2 = rssi2
        self.rssi3 = rssi3

#function to create a reference point
def make_RefPoint(name, position, adress1, adress2,adress3, rssi1,rssi2, rssi3):
    refPoint = RefPoint(name, position, adress1, adress2,adress3, rssi1,rssi2, rssi3)
    return refPoint

#creates a list of dummy reference points
def createTestListOfRPs():
    r1 = make_RefPoint("r1", "Albins dator", "24:01:C7:19:A3:0E", "24:01:C7:19:A3:0F","24:01:C7:19:A3:0D", -48, -48, -48)
    #r2 = make_RefPoint("r2", "Borta vid bordet", "24:01:C7:19:CF:4E", "24:01:C7:19:CF:4F", -49, -46)
    #r3 = make_RefPoint("r3", "Skrubben", "24:01:C7:19:47:10", "24:01:C7:19:47:11", -67, -68)
    rplist = [r1]#, r2, r3]
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
    largestNumberOfMatchingRefs = 0
    for ref in listOfRefPoints:
        numberOfMatches = 0
        for tmp in range(0,lengthAP):
            if ref.adress1 == myPositionInfo[tmp].address or ref.adress2 == myPositionInfo[tmp].address or ref.adress3 ==myPositionInfo[tmp].address:
                numberOfMatches += 1
        if (numberOfMatches > 0):
            RelRPs.append((ref,numberOfMatches))
        if (numberOfMatches > largestNumberOfMatchingRefs):
            largestNumberOfMatchingRefs = numberOfMatches
    toReturn = RelRPs, largestNumberOfMatchingRefs
    return toReturn


#determines which reference point is closest to me
def nearestRP(relRPs, myAPs, lengthAP , numberOfMatchingRefs):
    if len(relRPs) == 0:
        return "position unknown, no related reference points"
    area = "position unknown"
    for ref,n_matches in relRPs:
        if (n_matches == numberOfMatchingRefs):
            closestDiff = 300
            diff = []
            diffsum = 0
            for tmp in range(0,lengthAP):
                if (ref.adress1 == "" + myAPs[tmp].address):
                    temp = ref.rssi1 - myAPs[tmp].signal
                    if temp<0:
                        temp = temp * -1
                    diff.append(temp)
                elif ref.adress2 == "" + myAPs[tmp].address:
                    temp = ref.rssi2 - myAPs[tmp].signal
                    if temp < 0:
                        temp = temp * -1
                    diff.append(temp)
                elif ref.adress3 == "" + myAPs[tmp].address:
                    temp = ref.rssi3 - myAPs[tmp].signal
                    if temp < 0:
                        temp = temp * -1
                    diff.append(temp)
                for diffs in diff:
                    diffsum += diffs
            if diffsum < closestDiff:
                area = ref.position
                closestDiff = diffsum
    return area



def getRefListFromDB(cur):
    cur.execute("SELECT * FROM SEBBE") 
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
    relRPs,biggestNumberOfMatches = listOfRelRPs(rplist, myAPs, numberOfNetworksToScanAroundMe)
    myPosition = nearestRP(relRPs, myAPs, numberOfNetworksToScanAroundMe, biggestNumberOfMatches)
    print myPosition


    #for l2 in l:
    #    print(l2.ssid+" - "+ str(l2.signal) + " - "+str(l2.address))
    #Leave me be
    ###############################################
    #db.close()

if __name__ == "__main__":
    main()
