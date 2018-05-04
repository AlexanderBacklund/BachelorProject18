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

import subprocess
import time, platform,pymysql.cursors, sys, datetime

def connectToDB(h,u,p,d):
    #return MySQLdb.connect(host="localhost", user="root", passwd="Alabse959393#", db="localisation")
    return pymysql.connect(host=h, user=u, passwd=p, db=d)

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
#creates a object type reference point
class scanAPPoint(object):
    address = ""
    signal = 0
    # The class constructor
    def __init__(self, address, signal):
        self.address = address.upper()
        self.signal = signal

    def __str__(self):
        return "Address: "+self.address+" Signal: "+str(self.signal)

    def __repr__(self):
        return self.__str__()


def checkOperatingSys():
    return platform.system()

def scanNetworks():
    bssidsUnparsed = []
    signalsUnparsed = []
    returnlist = []
    x = 0
    tid = 0
    while(len(returnlist) < 2):
        returnlist = []
        results = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])
        results = results.replace("\r","")
        ls = results.split("\n")
        while x < len(ls):
            if "BSSID" in ls[x]:
                bssidsUnparsed.append(ls[x])
            elif "Signal" in ls[x]:
                signalsUnparsed.append(ls[x])
            x += 1
        i = 0
        while(i < len(bssidsUnparsed)):
            h = bssidsUnparsed[i].split(":")
            bssid = h[1].strip()+":"+h[2]+":"+h[3]+":"+h[4]+":"+h[5]+":"+h[6]
            g = signalsUnparsed[i].split(":")
            signal = g[1].strip()
            s = int(signal.strip('%'))
            dBm = (s / 2) - 100
            obj = scanAPPoint(bssid, dBm)
            returnlist.append(obj)
            i = i+1
        print("Scanning.. - time spent: "+str(tid)+"s")
        tid = tid+2
        time.sleep(2)
    return returnlist

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
                score1 = 4*(10-ap)
            if ref.address2 == myAPs[ap].address:
                score2 = 4*(9-ap)
            if ref.address3 ==  myAPs[ap].address:
                score3 = 4*(8-ap)
        score = score1 + score2 + score3
        if score > highestScore:
            highestScore = score
            listOfEqualscores = []
            listOfEqualscores.append(ref)
        elif score == highestScore:
            listOfEqualscores.append(ref)
    return listOfEqualscores



def sortCandidatesOnMatchingRefs(relRPs, numberOfMatchingRefs):
    listOfCandidatesBig = []
    for ref,n_matches in relRPs:
        if (n_matches == numberOfMatchingRefs):
            listOfCandidatesBig.append(ref)

    return listOfCandidatesBig




def posBasedOnRSSIstrenght(relRPs, myAPs, lengthAP):
    area = "position unknown"
    closestDiff = 300
    for ref in relRPs:
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


def whichPosition(relRPs, myAPs, lengthAP , numberOfMatchingRefs):
    if len(relRPs) == 0:
        return "position unknown, no related reference points"
    position = "position unknown"
    listOfCandidatesBig = sortCandidatesOnMatchingRefs(relRPs, numberOfMatchingRefs)
    listOfCandidatesSmall =  posBasedOnOrder(listOfCandidatesBig, myAPs, lengthAP, numberOfMatchingRefs)
    if len(listOfCandidatesSmall) == 0:
        position = "position unknown"
    elif len(listOfCandidatesSmall) == 1:
        position =  listOfCandidatesSmall[0].position
    elif len(listOfCandidatesSmall) > 1:
        position = posBasedOnRSSIstrenght(listOfCandidatesSmall, myAPs, lengthAP)
    return position


def getRefListFromDB(cur):
    cur.execute("SELECT * FROM show_position_refpoint") # TODO: Change to reftable
    return cur.fetchall()
def createObjectsFromDB(refs):
    refobjlista = []
    for r in refs:
        refobjlista.append(RefPoint(r[1],r[2],r[3],r[4], r[5], r[6], r[7]))
    return refobjlista

def readMySQLCredentials():
    try:
        file  = open("mysql.txt", "r")
        str = file.read()
        s = str.split("\n")
        return s[0],s[1],s[2],s[3]

    except IOError:
        print("create file mysql.txt and for each row put in this order: host, user, pass, db")
        time.sleep(10)
        sys.exit()

def getUsersFromDB(cur):
    userList = []
    cur.execute("SELECT * FROM show_position_users_script")
    users = cur.fetchall()
    for user in users:
        userList.append((user[0],user[1]))
    return userList

def updateUserPosition(cur, username, position, datetime, userId):
    cur.execute ("""
    UPDATE show_position_user_position
    SET u_position=%s, u_datetime=%s
    WHERE u_id_id=%s
    """, (position, datetime, userId))


def checkIfUserInDB(usersFromDB, username):
    temp = False
    for user_id,user in usersFromDB:
        if user == username:
            temp = True
    return temp

def getUserID(usersFromDB, username):
    for user_id,user in usersFromDB:
        if user == username:
            return user_id


def askForUser():
    uName = raw_input('Enter username: ')
    return uName

def main():
    host, usr, passw, db = readMySQLCredentials()
    db = connectToDB(host, usr, passw, db)
    # you must create a Cursor object. It will let
    cur = db.cursor()

    username = askForUser()
    userList = getUsersFromDB(cur)
    userExists = checkIfUserInDB(userList, username)

    #Kill it when given an incorrect Username
    if (not userExists):
        print("user not recognized, terminating")
        time.sleep(10)
        sys.exit()

    #Mainloop that never dies
    while(True):
        rplist = createObjectsFromDB(getRefListFromDB(cur))
        l = scanNetworks()
        numberOfNetworksToScanAroundMe = 10
        myAPs = sortNetworksReturnAmount(numberOfNetworksToScanAroundMe,l)
        relRPs, biggestNumberOfMatches = listOfRelRPs(rplist, myAPs, numberOfNetworksToScanAroundMe)
        myPosition = whichPosition(relRPs, myAPs, numberOfNetworksToScanAroundMe, biggestNumberOfMatches)
        print myPosition

        userList = getUsersFromDB(cur)
        updateUserPosition(cur, username, myPosition ,datetime.datetime.now(), getUserID(userList,username))
        db.commit()
        print("Comitted to db")
        time.sleep(20)

    #Leave me be
    ###############################################
    db.close()

if __name__ == "__main__":
    main()
