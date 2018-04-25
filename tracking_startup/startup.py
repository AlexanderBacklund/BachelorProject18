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
import time, platform,MySQLdb

def connectToDB():
    #return MySQLdb.connect(host="localhost", user="root", passwd="Alabse959393#", db="localisation")
    return MySQLdb.connect(host="back.db1.course.it.uu.se", user="fall17_it12", passwd="vXdWAk2K", db="fall17_project_it12")

#creates a object type reference point
class RefPoint(object):
    #name = ""
    position = ""
    address1 = ""
    address2 = ""
    address3 = ""
    rssi1 = 0
    rssi2 = 0
    rssi3 = 0

    # The class constructor
    def __init__(self, position, address1, address2, address3, rssi1,rssi2, rssi3):
        self.position = position
        self.address1 = address1.upper()
        self.address2 = address2.upper()
        self.address3 = address3.upper()
        self.rssi1 = int(rssi1)
        self.rssi2 = int(rssi2)
        self.rssi3 = int(rssi3)

    def __str__(self):
        return "Position: "+self.position+" mac1: "+self.address1+" mac2: "+self.address2+" mac3: "+self.address3+" rssi1: "+str(self.rssi1)+" rssi2: "+str(self.rssi2)+" rssi3: "+str(self.rssi3)

    def __repr__(self):
        return self.__str__()


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
            if ref.address1 == myPositionInfo[tmp].address or ref.address2 == myPositionInfo[tmp].address or ref.address3 ==myPositionInfo[tmp].address:
                numberOfMatches += 1
        if (numberOfMatches > 0):
            RelRPs.append((ref,numberOfMatches))
        if (numberOfMatches > largestNumberOfMatchingRefs):
            largestNumberOfMatchingRefs = numberOfMatches
    toReturn = RelRPs, largestNumberOfMatchingRefs
    return toReturn

def posBasedOnOrder(relAps, myAPs, lengthAP, numberOfMatchingRefs):
    highestScore = 0
    myposition = "position unknown"
    listOfEqualscores = []
    for ref in relAps:
        score1 = 0
        score2 = 0
        score3 = 0
        for ap in range(0,lengthAP):
            if ref.address1 == myAPs[ap].address:
                score1 = 2*(10-ap)
            if ref.address2 == myAPs[ap].address:
                score2 = 2*(9-ap)
            if ref.address3 ==  myAPs[ap].address:
                score3 = 2*(8-ap)
        score = score1 + score2 + score3
        if score > highestScore:
            highestScore = score
            del listOfEqualscores[:]
            listOfEqualscores.append(ref)
        if score == highestScore:
            listOfEqualscores.append(ref)

    return listOfEqualscores

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
                if (ref.address1 == "" + myAPs[tmp].address):
                    temp = ref.rssi1 - myAPs[tmp].signal
                    if temp<0:
                        temp = temp * -1
                    diff.append(temp)
                elif ref.address2 == "" + myAPs[tmp].address:
                    temp = ref.rssi2 - myAPs[tmp].signal
                    if temp < 0:
                        temp = temp * -1
                    diff.append(temp)
                elif ref.address3 == "" + myAPs[tmp].address:
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
    cur.execute("SELECT * FROM test") # TODO: Change to reftable
    return cur.fetchall()
def createObjectsFromDB(refs):
    refobjlista = []
    for r in refs:
        refobjlista.append(RefPoint(r[1],r[2],r[3],r[4], r[5], r[6], r[7]))
    return refobjlista

def main():
    netcard = raw_input("Enter network-card for wifi-scan: ")
    numberOfNetworksToScanAroundMe = 10
    db = connectToDB()

    # you must create a Cursor object. It will let
    cur = db.cursor()

    print(createObjectsFromDB(getRefListFromDB(cur)))
    rplist = createObjectsFromDB(getRefListFromDB(cur))


    l = scanNetworks(netcard)
    myAPs = sortNetworksReturnAmount(numberOfNetworksToScanAroundMe,l)
    for a in myAPs:
        print(a.address, a.signal)
    relRPs, biggestNumberOfMatches = listOfRelRPs(rplist, myAPs, numberOfNetworksToScanAroundMe)
    myPosition = nearestRP(relRPs, myAPs, numberOfNetworksToScanAroundMe, biggestNumberOfMatches)
    print myPosition


    #for l2 in l:
    #    print(l2.ssid+" - "+ str(l2.signal) + " - "+str(l2.address))
    #Leave me be
    ###############################################
    db.close()

if __name__ == "__main__":
    main()
