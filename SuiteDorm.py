# Suite Dorm Class

import TraditionalCommunity as TH

class SuiteDorm(TH.TraditionalCommunity):
    #common among all suite style residence buildings
    campus_location = "on campus"

    #initialize class attribute
    def __init__(self, school="N/A", school_location="N/A", num_residents=0, occupancy_type="N/A", bathroom_style = "N/A", num_community_halls=0, building_name = "N/A", date_built = 0, building_capacity = 0, num_floors = 0, num_staff = 0):
        super().__init__(school, school_location, num_residents, occupancy_type, num_community_halls)
        self.building_name = building_name
        self.date_built = date_built
        self.building_capacity = building_capacity
        self.num_floors = num_floors
        self.num_staff = num_staff
        self.bathroom_style = bathroom_style
        
    #ACCESSOR METHODS
    #set building name
    def setBuildingName(self, building_name):
        self.building_name = building_name
    #get building name
    def getBuildingName(self):
        return self.building_name

    # get campus location
    def getCampusLocation(self):
        return self.campus_location

    # get bathroom style
    def getBathroomStyle(self):
        return self.bathroom_style

    # set room occupancy type
    def setOccupancyType(self, occupancy_type):
        self.occupancy_type = occupancy_type
    # get room occupancy type
    def getOccupancyType(self):
        return self.occupancy_type
 
    # set bathroom style 
    def setBathroomStyle(self, bathroom_style):
        self.bathroom_style = bathroom_style
    # get bathroom
    def getBathroomStyle(self):
        return self.bathroom_style

    def displayInfo(self):
        print("")
        print(self.building_name, "is a Suite Dorms located", self.campus_location+".")
        print(aggieSuiteDorm.houses())
        print("This dorm was built on", str(self.date_built)+".")
        print("This dorm has", self.num_floors, "floors.")
        print("These dorms contains", self.bathroom_style + "-style bathrooms.")
        print("The dorms have", self.occupancy_type, "occupancy rooms.")
        print("")

    #BEHAVIORS
    def houses(self):
        super().houses()
        return "This Suite Style dorm holds " + str(self.building_capacity) + " students and is houses males and females."

# Instantiate object(s)
aggieSuiteDorm = SuiteDorm()

#aggieSuiteDorm.displayInfo()