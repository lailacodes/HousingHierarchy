# Util for Housing Info

import ResidenceHall as RH
import TraditionalCommunity as TC
import Suite as S
import Apartment as A

#MENUS
def displayMenu():
    print("")
    print("A) Create a New Community Dorm")
    print("B) Create a New Suite Dorm")
    print("C) View Dorm Options")
    print("D) View General Housing Information")
    print("E) Update Residence Hall Information")
    print("F) Update Traditional Community Hall Information")
    print("G) Update Suite Hall Information")
    print("Q)uit")
    print("")

def displayInfo():
    return RH.aggieHalls.displayInfo(), TC.aggieCommunityHalls.displayInfo(), S.aggieSuiteHalls.displayInfo(), A.aggieApartmentHalls.displayInfo()


#SET NEW INFORMATION
# for residence halls
def updateRHOptions():
    return RH.aggieHalls.setSchool(input("Update school name: ")), RH.aggieHalls.setSchoolLocation(input("Update school location: ")), RH.aggieHalls.setNumResidents(int(input("Update number of residents: ")))
# for traditional community
def updateTCOptions():
    return TC.aggieCommunityHalls.setNumCommunityHalls(int(input("Update number of community halls: "))), TC.aggieCommunityHalls.setOccupancyType(input("Update room occupancy type for community halls: "))
# for suite
def updateSOptions():
    return S.aggieSuiteHalls.setBathroomStyle(input("Update bathroom style: ")), S.aggieSuiteHalls.setNumSuites(int(input("Update number of suite halls: "))), S.aggieSuiteHalls.setOccupancyType(input("Update room occupancy type for suite halls: "))


#VALIDATION
def invalidEntry():
    print("")
    print("Invalid Entry. Please choose a selection.")
    print("")


#END
def endProgram():
    print("Thank you for using the NCAT Housing Portal.")
    quit()