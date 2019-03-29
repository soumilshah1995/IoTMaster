# IoTMaster

![BeFunky-collage](https://user-images.githubusercontent.com/39345855/55261551-a53b7580-5241-11e9-8190-e811dc25fcdd.jpg)



IoT Master Library Upload Data to any Cloud and get an Email / Text/Phonecall Notification with 4 Line of Python Code

Hello everyone in this Blog I want to tell you about the IoT Master Library. what are benefits of using this library. it was always challenging interfacing sensor and once you get the sensor working we need to process data in order to upload on cloud server. in this process there is lot of encoding while you want to upload the sensor Data and Decoding while you want. to get the data back.

I have Written a simple yet powerful Library which will help you to send SMS, Upload Data on Google Cloud, Upload Data on Thingspeak, Read the data from ThingSpeak and plot the data after receiving the data. get Latitude and long with simple two line of code not only that get email notification when sensor value exceed the amount you have mentioned. Let us see how to use this library.

Motivation to build this Module: - It was back in 2014 when I was not a good programmer I used to always struggle when it came to write code but I was very good at interfacing sensor we realized that in order to upload data on cloud its very tedious you have to write lot of codes and also for different cloud use different API it was time consuming and I was not able to find a single library which has all functionality that was the reason I decided to make one. it is 2019 I am a python developer so decided to contribute to the maker so that they can focus on making project than coding. we do all the hard work for you.

These are the the cloud platform that my library can be used for


=====================================================================
                             IOT MASTER LIBRARY 
======================================================================

1 .  ThingSpeak                        (Read/ Write)
2 .  AdafruitIO                        (Read/Write)
3 .  IFTTT                             (upload get notification etc)
4 .  Get Latitude and Longitude        (get Lat and Long)
5 .  Get Date and Time                 (get Date and Time in Format)
6 .  Get Weather Details               (Supports oopen Weather API )
7 .  Supports Text to Speech           (ONLY for MAC)
8 .  Supports Arduino                  (Read and Write)
9 .  Get Youtube Sub Count             (Get Yout Sub Count)
10.  Suports MQTT                      (Unstable Verison ! )

  ====================================================================

IFTTT
<img width="1313" alt="Screen Shot 2019-03-16 at 5 33 49 PM" src="https://user-images.githubusercontent.com/39345855/54482090-6276a800-4814-11e9-9c89-a53ba0157b87.png">

<img width="1311" alt="Screen Shot 2019-03-16 at 5 41 09 PM" src="https://user-images.githubusercontent.com/39345855/54482093-71f5f100-4814-11e9-9171-a83be3de84ef.png">


whenever sensor value exceeds the limit than what you can do

<img width="1427" alt="Screen Shot 2019-03-16 at 5 42 29 PM" src="https://user-images.githubusercontent.com/39345855/54482098-82a66700-4814-11e9-93a6-2f01a3e09261.png">


This are few examples there are many like this

here is how you would use this Library

temperature=28
humidity=66


# ==============  IFTTT  =============


iftt_k = 'YOUR KEY GOES HERE'
feed = 'MAKER CHANNEL NAME GOES HERE'

ob1 = IfTTT(eventname=feed, key=iftt_k)

ob1.iftt_post(data1=temperature,data2=humidity)

# ======= Latitude and Longitude ========


<img width="1320" alt="Screen Shot 2019-03-16 at 5 45 10 PM" src="https://user-images.githubusercontent.com/39345855/54482114-d749e200-4814-11e9-95ac-719c2b1bfd89.png">


how to use with this 


"""
temperature=28
humidity=66


# ==================== Thingspeak ========
w_key = 'YOUR WRITE  KEY GOES HERE'
r_key = 'YOUR READ  KEY GOES HERE''
channel_id = '12345'

ob = Thingspeak(write_api_key=w_key, read_api_key=r_key,channel_id=channel_id)

ob.post_cloud(value1=temperature,value2=humidity

# ======================================

<img width="697" alt="Screen Shot 2019-03-16 at 5 47 19 PM" src="https://user-images.githubusercontent.com/39345855/54482120-f34d8380-4814-11e9-9d1f-8e55817beed3.png">


how to get location 

# ======================================
ob2 = Location()

lat,long = ob2.get_locations()

print('{} Latitude '.format(lat))

print("{} Longitude ".format(long))

# ======================================

Easy Right ?

How do I get date and time ?

Soumil what about weather ? yes we have that as well

<img width="448" alt="Screen Shot 2019-03-16 at 5 50 10 PM" src="https://user-images.githubusercontent.com/39345855/54482131-111ae880-4815-11e9-95e0-4a6fc57e8ac2.png">


 =============== Weather Details  ==============================================

key ='ce45a4d1079e68c410cd42a3054d00e1'
city = 'Bridgeport'

ob4 = Weather_details(key=key,city=city)
long,lat,humidity,wind_speed = ob4.get_weather_data()


# ================================================================================
















