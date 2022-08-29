# 🛰ISS Location Notifier using Requests API of Python

🌟An interesting program which makes use of Requests & SMTP modules to GET the location of the ISS and verify if its within your Latitude and Longitude range and also if 
its night time rigth now and then, sends you a mail notifying to spot it in the night sky.

👉In the main.py file first the location of the ISS i.e. its latitude and longitude data is fetched from the API request made to the url 
'http://api.open-notify.org/iss-now.json' in the 'check_iss_location' function. After that the location data is compared with users location and if ISS is within range,
the function returns true value.

👉From the 'check_dark()' function, the sunrise and sunset timings are obtained from the API request made to the url 'https://api.sunrise-sunset.org/json' with latitude 
and longitude of user passed as parameters. This data is compared with the present time data obtained from datetime module and if its evening time then the function
returns true.

👉Inside an infinite while loop with the time module used to make it sleep for certain amount of time, the both conditions are checked and if both conditions are
satisfied then a mail is sent to the user via the SMTP modules methods and the user can spot the ISS in the night sky.

🌟In this way, using the API requests module, datetime module and the SMTP module the program is implemented.  
