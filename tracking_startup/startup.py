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





    #Leave me be
    ###############################################
    db.close()

if __name__ == "__main__":
    main()
