# Traditional Community Style Building Class

import ResidenceHall as RH

class TraditionalCommunity(RH.ResidenceHall):
    #common among all traditional community style residence halls
    bathroom_style = "community"
    campus_location = "on campus"

    #initialize class attribute
    def __init__(self, school = "N/A", school_location = "N/A", num_residents = 0, occupancy_type = "N/A", num_community_halls = 0):
        super().__init__(school, school_location, num_residents)
        self.occupancy_type = occupancy_type    #private, single, double
        self.num_community_halls = num_community_halls

        
    #ACCESSOR METHODS
    # get campus location
    def getCampusLocation(self):
        return self.campus_location

    # get bathroom style
    def getBathroomStyle(self):
        return self.bathroom_style

    # set number of community buildings
    def setNumCommunityHalls(self, num_community_halls):
        self.num_community_halls = num_community_halls
    # set number of community buildings
    def getNumCommunityHalls(self):
        return self.num_community_halls

    # set room occupancy type
    def setOccupancyType(self, occupancy_type):
        self.occupancy_type = occupancy_type
    # get room occupancy type
    def getOccupancyType(self):
        return self.occupancy_type
 

    def displayInfo(self):
        print("")
        print("Traditional Community Style Residence Buildings are located", self.campus_location+".")
        print("There are", self.num_community_halls,"traditional community halls", self.campus_location+".")
        print("These halls contain", self.bathroom_style + "-style bathrooms.")
        print("Their dorms have", self.occupancy_type, "occupancy rooms.")
        print("")

    #BEHAVIORS
    def houses(self):
        super().houses()
        return "Traditional Community Style are single gendered residence halls"

# Instantiate object(s)
aggieCommunityHalls = TraditionalCommunity()
aggieCommunityHalls.setOccupancyType("double")
aggieCommunityHalls.setNumCommunityHalls(6)

#aggieCommunityHalls.displayInfo()