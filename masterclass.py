""""
Author : Soumil shah
Email : soushah@my.bridgeport.edu
Version 1.0.1

update: Changes made to class added private var and url and read url
cannot be  changed !

"""

try:                                    # import the important library
    from urllib import request
    from urllib.request import urlopen
    import threading                    # import threadding
    import json                         # import json
    import random                       # import random
    import requests                     # import requests for web API
    import ssl
    import geocoder                     # for Locations
    import datetime                     # for date time
    from twilio.rest import Client      # for Sms
    from serial import Serial           # for arduino
    import numpy as np
    from Adafruit_IO import Client      # for Adafruit IO
    import os
    from os import system                # For Text to speech
    import paho.mqtt.publish as publish
    import sqlite3                       # for Database
    import paho.mqtt.publish as publish
    import urllib                        # for web Api

except:
    print("No Library Found")


class Thingspeak(object):                       # define a class called Thingspeak

    def __init__(self, write_api_key = None, read_api_key=None, channel_id=0):

        """

        :param write_key:  takes a string of write api key
        :param timer: can take integer values
        """

        # self.url = 'https://api.thingspeak.com/update?api_key='
        # self.read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)

        self.write_key = write_api_key
        self.channel_id = channel_id
        self.read_api_key = read_api_key

        # Private Var cannot change
        self.__url = 'http://api.thingspeak.com/update?api_key'
        self.__read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)


        self.feild1 = []
        self.feild2 = []

    def post_cloud(self, value1, value2):
        try:
            """
            :param value1: can be interger or float
            :param value2: can be interger or float
            :return: updated to cloud storage
            """

            URL = self.__url

            KEY = self.write_key

            HEADER = '&field1={}&field2={}'.format(str(value1), str(value2))

            NEW_URL = str(URL) + "=" + str(KEY) + str(HEADER)
            print(NEW_URL)

            context = ssl._create_unverified_context()

            data = request.urlopen(NEW_URL,context=context)
            print(data)
        except:
            print('could not post to the cloud server ')

    def read_cloud(self, result=2):
        try:
            """
            :param result: how many data you want to fetch accept interger
            :return: Two List which contains Sensor data
            """

            URL_R = self.__read_url
            read_key = self.read_api_key
            header_r = '&results={}'.format(result)

            new_read_url = URL_R + read_key + header_r

            data = requests.get(new_read_url).json()

            field1 = data['feeds']

            for x in field1:
                self.feild1.append(x['field1'])
                self.feild2.append(x['field2'])

            return self.feild1, self.feild2
        except:
            print('read_cloud failed !!!! ')


class IfTTT(object):

    def __init__(self, eventname='', key=''):

        self.eventname = eventname
        self.Key = key

        self.__Url = 'https://maker.ifttt.com/trigger/{}/with/key/'.format(self.eventname)

        self.New_Url = self.__Url + self.Key

        print(self.New_Url)

    def iftt_post(self, data1=10, data2=11):
        try:
            """
            :param data1:  pass your sensor value only integer
            :param data2: pass your data as interger only
            :return:      True if it was successful
            """

            URl = self.New_Url
            Key = self.Key
            payload = {'value1': data1,
                       'value2': data2}

            requests.post(self.New_Url, data=payload)
            print("Done posted on IFTTT")

            return True
        except:
            print('failed to post to cloud sever ! ')


class Location(object):

    def __init__(self):
        pass

    def get_locations(self):

        """
        :return: Lat and Long
        """
        try:
            g = geocoder.ip('me')
            my_string=g.latlng
            longitude=my_string[0]
            latitude=my_string[1]

            return longitude,latitude
        except:
            print('Error make sure you have Geo-Coder Installed ')


class DateandTime(object):

    def __init__(self):
        pass

    @ staticmethod
    def get_time_date():
        try:
            """
            :return:  date and time
            """
            my = datetime.datetime.now()
            data_time = '{}:{}:{}'.format(my.hour,my.minute,my.second)
            data_date = '{}/{}/{}'.format(my.day,my.month,my.year)
            return data_date,data_time
        except:
            print('could now get date and time ')

    def convert_timestamp(self,timestamp):
        timestamp = 1554506464
        dt_object = datetime.fromtimestamp(timestamp)
        return dt_object


class Weather_details(object):

    def __init__(self,key='', city=''):
        self.city = city
        self.key = key


    def get_weather_data(self):
        try:
            city = self.city
            key = self.key

            URL='http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'.format(key,city)
            print(URL)

            data = requests.get(URL).json()
            long = data['coord']['lon']
            lat = data['coord']['lat']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            wind_degree = data['wind']['deg']
            sunrise = data['sys']['sunrise']
            sunset = data['sys']['sunset']

            m1 = data['weather'][0]['description']
            m2 = data['weather'][0]['main']
            body = '{} {}'.format(m1, m2)

            return long, lat, humidity, wind_speed, wind_degree, sunrise, sunset,body

        except:
            print('Error occured ')


class Arduino(object):

    def __init__(self,comport='/dev/cu.usbmodem14101', baudrate=9600):
        self.comport = comport
        self.baudrate = baudrate

    def read_data(self):
        try:
            """
            :return: data after reading from serial object
            """
            arduino = Serial(self.comport, self.baudrate,timeout=1)
            data =  arduino.readline().decode('ascii')
            return data
        except:
            print("please check your com port and baud rate ")

    def write_data(self,data='1'):
        try:

            """
    
            :param data: pass string 1 or 0 or any character and write if statment in Arduino
            to compare and trigger events
            :return: NONE
            """

            arduinodata = Serial(self.comport, self.baudrate,timeout=1)
            data_send = data.encode('utf-8')
            arduinodata.write(data_send)
        except:
            print("cannot write data please check com port and baud rate ")


class Adafruit_cloud():

    def __init__(self, username='', Aio_key=''):

        self.username = username
        self.Aio_key = Aio_key
        self.aio = Client(self.username,self.Aio_key)
        self.feed_name = []

    def adafruit_send(self,feed_name='',data=''):
        try:
            sensor = self.aio.feeds(feed_name)
            self.aio.send_data(sensor.key,data)
            print('Data was uploaded ')
        except:
            print("cannot send Data !")


    def adafruit_get(self, feedname=''):
        try:
            data = self.aio.receive(feedname)
            return data.value
        except:
            print('cannot get data ! ')

    def adafruit_feed_list(self):
        try:

            feeds = self.aio.feeds()
            for f in feeds:
                print(f)
                self.feed_name.append(f.name)

            return self.feed_name
        except:
            print("cannot get feed list ! ")


class TextSpeech_Mac(object):

    def __init__(self):
        """
        This script works for mac only
        """
        pass

    def speak(self,text):
        try:

            """
            :param text:  Takes String as Input
            :return: Return None
            """
            system("say {}".format(text))
        except:
            print("This works  for mac only ! ")


class Mqtt(object):

    def __init__(self, data):
        self.data= data
        self.hostname="test.mosquitto.org"
        self.topic = ''

    def post(self):
        """
        POst teh 
        :return:
        """
        publish.single(self.topic, "{}".format(self.data), hostname=self.hostname)


class YoutubeSub(object):

    def __init__(self,name ='',google_key=''):
        """

        :param name: Name of Youtube Person , Google Cloud API key
        :param google_key:
        """
        self.name = name
        self.google_key = google_key
        self.context = ssl._create_unverified_context()

    def get_subscriber(self):

        """
        :return: Youtube Sub Count
        """
        self.url = 'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=' \
                   + self.name+'&key='+self.google_key

        data = urllib.request.urlopen(self.url, context=self.context).read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        subs = int(subs)
        return subs


class Text_MP3_converter(object):

    def __init__(self):

        self.__url = 'https://text-to-speech-demo.ng.bluemix.net/api/v1/synthesize?t'
        self.__header ={
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.wikipedia.org/',
    'Connection': 'keep-alive'}

        self.__params = {
            'text': 'hello everyone i am going to teach you python',
            'voice': 'en-US_AllisonV2Voice',
            'download': True,
            'accept': 'audio/mp3'}

    def text_audio(self,name ='test', text='hello world'):

        """

            :param name_file:
            :param text:
            :return:  saves MP3 File on your computer
        """
        try:
            response = requests.get(self.__url, headers=self.__header,params=self.__params)

            with open("{}.mp3".format(name),'wb') as f:
                f.write(response.content)
                print("File has been downloaded on your computer with name {}".format(name))
        except:
            print('Error cannot convert File')


class Spotifypy(object):

    def __init__(self,client_id='', client_secret='',oauth_token=''):
        self.client_id = client_id
        self.client_secret = client_secret
        self.oauth_token = oauth_token

        self.__header = {'Authorization': self.oauth_token,
                  'Accept':'application/json',
                  'Content-Type':'application/json'}


    def play_song(self):

        self.__url_play = 'https://api.spotify.com/v1/me/player/play'
        response = requests.put(self.__url_play, headers=self.__header)
        print(response)

    def pause_song(self):
        self.__url_pause = 'https://api.spotify.com/v1/me/player/pause'
        response = requests.put(self.__url_pause, headers=self.__header)
        print(response)

    def get_recommendation(self):

        self.__url_recommendation = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'
        response = requests.get(self.__url_recommendation, headers=self.__header)
        # print(response.json())
        return response.json()


    def get_device(self):

        self.__url_device = 'https://api.spotify.com/v1/me/player/devices'
        response = requests.get(self.__url_recommendation, headers=self.__header)
        return response.json()




