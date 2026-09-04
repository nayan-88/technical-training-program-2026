def cityName(city='Nashik'):#default argument
    print("City Name=",city)

cityName("mumbai")
cityName("pune")
cityName()

def stateName(*cityNames):
    print("City Names=",cityNames)

stateName("mumbai","nashik","pune")