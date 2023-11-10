import requests
from datetime import datetime

MY_LAT = "51.391810"
MY_LONG = "-0.450201"
my_location = (51.391810,-0.450201)

#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response)
# get response code
# can raise exceptions based on specific status code received back
#response.raise_for_status()
#print(response.json())
#print(response.json()['iss_position']['latitude'])
#print(response.status_code)
#print(type(response))

#data = response.json()['iss_position']['longitude']
#data = response.json()["iss_position"]
#data = response.json()

def is_iss_overhead():
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position = (iss_longitude, iss_latitude)
    #print(iss_pos)

    # your position can be +/- 5 degrees of iss
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
        return True
 
def is_night():
    # lat, long, formatting = Off, gives 24hr clock
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted" : 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T").split(":")[0])
    sunset = int(data["results"]["sunset"].split("T").split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        # its dark
        return True
    
# can use while loop slowed down to run once a minute
#if is_iss_overhead and is_night:
    # send email