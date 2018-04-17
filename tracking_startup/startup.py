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
import time, platform, MySQLdb

def connectToDB():
    return MySQLdb.connect(host="back.db1.course.it.uu.se", user="fall17_it12", passwd="vXdWAk2K", db="fall17_project_it12")

class RefPoint(object):
    name = ""
    position = ""
    adress1 = ""
    adress2 = ""
    rssi1 = 0
    rssi2 = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, position, adress1, adress2, rssi1,rssi2):
        self.name = name
        self.age = age
        self.major = major

def make_RefPoint(name, position, adress1, adress2, rssi1,rssi2):
    refPoint = RefPoint(name, position, adress1, adress2, rssi1,rssi2)
    return refPoint

def createTestListOfRPs():
    r1 = make_RefPoint(r1, A1, AAA, BBB, -34, -55)
    r2 = make_RefPoint(r2, A2, CCC, DDD, -14, -18)
    r3 = make_RefPoint(r3, A3, EEE, FFF, -25, -33)
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

def listOfRelRPs(listOfRefPoints, myPositionInfo):
    mac1 = myPositionInfo[0].address
    mac2 = myPositionInfo[1].address
    RelRPs = []
    for ref in listOfRefPoints:
        if (ref.adress1 == mac1 and ref.adress2 == mac2mac2):
            RelRPs.append(refs)
        elif (ref.adress1 == mac1 and ref.adress2 == mac2):
            RelRPs.append(refs)
    return RelRPs

def nearestRP(relRPs, myAPs):
    for rp in relRPs:
        rp.

def getRefListFromDB(cur):
    cur.execute("SELECT * FROM SEBBE") # TODO: Change to reftable
    return cur.fetchall()


def main():
    #netcard = raw_input("Enter network-card for wifi-scan: ")

    # l = scanNetworks(netcard)
    # l1 = sortNetworksReturnAmount(4,l)
    db = connectToDB()
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    getRefListFromDB(cur)

    l = scanNetworks(netcard)
    myAPs = sortNetworksReturnAmount(2,l)
    rplist = createTestListOfRPs()
    relRPs = listOfRelRPs(rplist, myAPs)
    myPosition = nearestRP(relRPs, myAPs)


    for l2 in myAPs:
        print(l2.ssid+" - "+str(l2.signal)+" - "+str(l2.address))
    #Leave me be
    ###############################################
    db.close()


if __name__ == "__main__":
    main()
