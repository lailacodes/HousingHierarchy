# Residence Hall Base Class

class ResidenceHall():
    #common among all residence halls
    internet_and_cable_access = True
    air_conditioning_access = True 
    laundry_access = True

    #initialize class attributes
    def __init__(self, school = "N/A", school_location = "N/A", num_residents = 0):
        self.school = school
        self.school_location = school_location
        self.num_residents = num_residents

    #ACCESOR METHODS
    #set school name
    def setSchool(self, school):
        self.school = school
    #get name of school
    def getSchool(self):
        return self.school

    #set school location
    def setSchoolLocation(self, school_location):
        self.school_location = school_location
    #get school location
    def getSchoolLocation(self):
        return self.school_location   

    #set number of residents living at the school
    def setNumResidents(self, num_residents):
        self.num_residents = num_residents
    #get number of residents living at the school
    def getNumResidents(self):
        return self.num_residents   


    def displayInfo(self):
        print("")
        print(self.school + ", located in", self.school_location + ", is home to", str(self.num_residents), "students.")
        print(ResidenceHall.houses(self))
        print(ResidenceHall.hasLaundryRooms(self))
        print(ResidenceHall.hasAC(self))
        print(ResidenceHall.hasInternetCableAccess(self))
        print("")


    #BEHAVIORS
    def houses(self):   # who resides in these halls
        return "Residence Halls house all current students at " + self.school + "."

    # accomodations of residence halls
    def hasInternetCableAccess(self):
        if self.internet_and_cable_access is True:
            return "All residence halls have access to wireless internet and cable."
        else:
            return "Not all halls have access to wireless internet and cable"

    def hasAC(self):
        if self.air_conditioning_access is True:
            return "All residence halls have air conditioning."
        else:
            return "Not all halls have air conditioning"

    def hasLaundryRooms(self):
        if self.laundry_access is True:
            return "All residence halls have laundry rooms."
        else:
            return "Not all halls have laundry rooms"

# Instantiate object(s)
aggieHalls = ResidenceHall()

aggieHalls.setSchool("North Carolina A&T")
aggieHalls.setSchoolLocation("Greensboro, NC")
aggieHalls.setNumResidents(13300)

#aggieHalls.displayInfo()