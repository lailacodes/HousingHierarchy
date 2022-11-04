# Suite Style Building Class

import TraditionalCommunity as TC

class Suite(TC.TraditionalCommunity):
    #common among all suite style residence halls
    campus_location = "on campus"

    #initialize class attribute
    def __init__(self, school = "N/A", school_location = "N/A", num_residents = 0, occupancy_type = "N/A", bathroom_style = "N/A", num_suites = 0):
        super().__init__(school, school_location, num_residents)
        self.occupancy_type = occupancy_type    #private, single, double
        self.bathroom_style = bathroom_style    
        self.num_suites = num_suites
    
    #ACCESSOR METHODS
    # get campus location
    def getCampusLocation(self):
        return self.campus_location

    # set bathroom style
    def setBathroomStyle(self, bathroom_style):
        self.bathroom_style = bathroom_style
    # get bathroom style
    def getBathroomStyle(self):
        return self.bathroom_style

    # set room occupancy type
    def setOccupancyType(self, occupancy_type):
        self.occupancy_type = occupancy_type
    # get room occupancy type
    def getOccupancyType(self):
        return self.occupancy_type

    # set number of suite buildings
    def setNumSuites(self, num_suites):
        self.num_suites = num_suites
    # set number of suite buildings
    def getNumSuites(self):
        return self.num_suites
 
 
    def displayInfo(self):
        print("")
        print("Suite Style Residence Buildings are located", self.campus_location+".")
        print("There are", self.num_suites,"suites", self.campus_location+".")
        print("These halls contain", self.bathroom_style + "-style bathrooms.")
        print("Their dorms have", self.occupancy_type, "occupancy rooms.")
        print("")

    #BEHAVIORS
    def houses(self):
        super().houses()
        return "Suite Style are co-ed residence halls"

# Instantiate object(s)
aggieSuiteHalls = Suite()
aggieSuiteHalls.setOccupancyType("double, single, and private")
aggieSuiteHalls.setNumSuites(9)
aggieSuiteHalls.setBathroomStyle("shared and private")

#aggieSuiteHalls.displayInfo()

