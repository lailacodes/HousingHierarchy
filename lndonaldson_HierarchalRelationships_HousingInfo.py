# Laila Donaldson
# August 1, 2022
# COMP 163 Summer Session II
# This program creates and displays information regarding student housing options at NCAT

import Util
import CommunityDorm as CD
import SuiteDorm as SD


#Welcome
print("Welcome to the NCAT Housing Portal")

#container for dorms
dormList = list()


def listDorms():
    for dorm in dormList:
        print(dorm)

def createCommunityDorm():
    CD.aggieCommunityDorm.setBuildingName(input("Enter building name: "))
    dormList.append(CD.aggieCommunityDorm.getBuildingName())

def createSuiteDorm():
    SD.aggieSuiteDorm.setBuildingName(input("Enter building name: "),)
    dormList.append(SD.aggieSuiteDorm.getBuildingName())


while True:
    Util.displayMenu()
    menuItem = input("Enter Selection : ").upper()
    if menuItem == "A":
        createCommunityDorm()
    elif menuItem == "B":
        createSuiteDorm()
    elif menuItem == "C":
        listDorms()
    elif menuItem == "D":
        # display general information on the types of housing
        Util.displayInfo()
    elif menuItem == "E":
        # Update general information
        Util.updateRHOptions()
    elif menuItem == "F":
        Util.updateTCOptions()
    elif menuItem == "G":
        pass
    elif menuItem == "H":
        pass
    elif menuItem == "Q":
        # quit menu
        Util.endProgram()
    else:
        # Incorrect Entry, rerun loop
        Util.invalidEntry()      