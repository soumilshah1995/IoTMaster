    """
    
        # ============================================================================
                                     IOT MASTER LIBRARY 
        ==============================================================================
        
        1 .  ThingSpeak                              (Read/ Write)
        2 .  AdafruitIO                              (Read/Write)
        3 .  IFTTT                                   (upload get notification etc)
        4 .  Get Latitude and Longitude              (get Lat and Long)
        5 .  Get Date and Time                       (get Date and Time in Format)
        6 .  Get Weather Details                     (Supports oopen Weather API )
        7 .  Supports Text to Speech                 (ONLY for MAC)
        8 .  Supports Arduino                        (Read and Write)
        9 .  Get Youtube Sub Count                   (Get Yout Sub Count)
        10.  Suports MQTT                            (Unstable Verison ! )
    
          ==============================================================================
        
    Soumil Nitin Shah
    
    Bachelor in Electronic Engineering
    Master in Electrical Engineering 
    Master in Computer Engineering 
    
    Graduate Teaching/Research Assistant
    
    Python Developer
    
    soushah@my.bridgeport.edu
    ——————————————————
    Linkedin:	https://www.linkedin.com/in/shah-soumil
    
    Github
    https://github.com/soumilshah1995
    
    Youtube channel
    https://www.youtube.com/channel/UC_eOodxvwS_H7x2uLQa-svw
    
    
"""

from masterclass import *       # Make sure to Import class to avoid Error !

temperature = 22
humidity = 11

# ==================== Thingspeak =========================================

w_key = 'Your Write key goes here '
r_key = 'your read key goes here '
channel_id = 83234                              # replace with channel id

ob = Thingspeak(write_api_key=w_key, read_api_key=r_key, channel_id=channel_id)
ob.post_cloud(value1=temperature,value2=humidity)
print(ob.read_cloud(result=3))                # change result=number of data you want

# ==============================  IFTTT  =====================================

iftt_k = 'Your Webhook Key goes here '
feed = 'Feed name you created using webhook'

ob1 = IfTTT(eventname=feed, key=iftt_k)
ob1.iftt_post(data1=temperature,data2=humidity)

# ================== Latitude and Longitude ===================================

ob2 = Location()
lat,long = ob2.get_locations()
print('{} Latitude '.format(lat))
print("{} Longitude ".format(long))

# ================== Date and Time ==============================================

b3 = DateandTime()
m_date, m_time = ob3.get_time_date()
print('{} Date'.format(m_date))
print("{} Time ".format(m_time))

# =============== Weather Details  ==============================================

key ='open weather API key goes here '
city = 'Bridgeport'

ob4 = Weather_details(key=key,city=city)
long, lat, humidity, wind_speed, wind_degree, sunrise, sunset,body = ob4.get_weather_data()
print(long, lat, humidity, wind_speed, wind_degree, sunrise, sunset,body)

# ========================== ADAFRUIT ===================================

user_name='Adafruit Username Goes here'
Aio_key = 'AIO key goes here '
feed_name='Feed Name you want to upload data to goes here '

ad = Adafruit_cloud(username=user_name, Aio_key=Aio_key)
ad.adafruit_send(feed_name=feed_name, data = 11)
print(ad.adafruit_feed_list)

# ===================  Text to Speech  only Mac ======================================

sp =TextSpeech_Mac()
sp.speak("Hello World ")

# =============================== ARDUINO ==============================================

ComPort = 'COM3'
BaudRate = '9600'
ard = Arduino(comport=ComPort, baudrate=BaudRate)
val = ard.read_data()
print(" arduino got value {}".format(val))
ard.write_data(data='on')


#===============================Youtube sub count ==================================================

YoutubeName = 'Sentdex'
google_apikey = 'Your google api key goes here '
ytd = YoutubeSub(name=YoutubeName, google_key=google_apikey)
sub = ytd.get_subscriber()
print("Youtube Channel {} has {} SUB".format(YoutubeName, sub))

