from datetime import datetime
import requests
import smtplib
import time

MY_EMAIL = "xyz123@gmail.com"
PASSWORD = "PASSWORD"

MY_LAT = 18.520430
MY_LNG = 73.856743
FORMAT = 0

time_now = datetime.now()
hour_utc = time_now.hour - 5


def check_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5 <= iss_lat <= MY_LAT + 5) and (MY_LNG - 5 <= iss_lng <= MY_LNG + 5):
        return True
    else:
        return False


def check_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": FORMAT
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    global hour_utc
    if 0 < hour_utc <= sunrise or sunset <= hour_utc < 24:
        return True
    else:
        return False


while True:
    time.sleep(120)
    if check_dark() and check_iss_location():
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg="Subject:Look UP!!👆👆\n\nThe ISS is above you in the sky.")

