# Apartment Style Building Class

import ResidenceHall as RH

class Apartment(RH.ResidenceHall):
    #common among all apartment style residence halls
    bathroom_style = "2 Bath"
    campus_location = "off campus"

    #initialize class attribute
    def __init__(self, school = "N/A", school_location = "N/A", num_residents = 0):
        super().__init__(school, school_location, num_residents)
        
    #ACCESSOR METHODS
    # get campus location
    def getCampusLocation(self):
        return self.campus_location

    # get bathroom style
    def getBathroomStyle(self):
        return self.bathroom_style
 

    def displayInfo(self):
        print("")
        print("Apartments Style Residence Buildings are located", self.campus_location+".")
        print("These halls contain", self.bathroom_style, "bathrooms.")
        print("")

    #BEHAVIORS
    def houses(self):
        super().houses()
        return

# Instantiate object(s)
aggieApartmentHalls = Apartment()

#aggieApartmentHalls.displayInfo()