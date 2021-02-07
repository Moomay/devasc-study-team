class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    def myLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")

loc = Location("Your_Name", "Your_Country")
loc1 = Location("Tomas", "Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
your_loc = Location("Jame", "Thailand")


loc1.myLocation()
loc2.myLocation()
loc3.myLocation()
your_loc.myLocation()
#print(loc.name)
#print(loc.country)
#print(type(loc))