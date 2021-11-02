class Location:

    def __init__(self,name,country):
        self.name = name
        self.country = country 

    def MyLocation(self):
        print("Hi, my name is " + self.name + " and I live in " + self.country + ".")


#Primera instancia de la ubicación de la clase
loc1 = Location("Tomas", "Protugal")

#Llamar a un método de la clase instanciada
loc1.MyLocation()

loc2 = Location("Ying","CHina")
loc3 = Location("Amare", "Kenya")
loc2.MyLocation()
loc3.MyLocation()

your_loc = Location("Your_Name",  "Your_Country")
your_loc.MyLocation()