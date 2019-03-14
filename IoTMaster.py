""""
Author : Soumil shah
Email : soushah@my.bridgeport.edu
"""


try:                                    # import the important library
    from urllib import request
    from urllib.request import urlopen
    import threading                    # import threadding
    import json                         # import json
    import random                       # import random
    import requests                     # import requests
    import ssl
    import geocoder
    import datetime
    import sqlite3
except:
    print("No Library Found")


class Thingspeak(object):                       # define a class called Thingspeak

    def __init__(self, write_key_api =None, read_api_key=None, channel_id=0):

        """

        :param write_key:  takes a string of write api key
        :param timer: can take integer values
        """

        self.url = 'https://api.thingspeak.com/update?api_key='
        self.write_key = write_key_api

        self.channel_id = channel_id
        self.read_api_key = read_api_key
        self.read_url = 'https://api.thingspeak.com/channels/{}/feeds.json?api_key='.format(channel_id)
        self.feild1 = []
        self.feild2 = []

    def post_cloud(self, value1, value2):
        try:
            """
            :param value1: can be interger or float
            :param value2: can be interger or float
            :return: updated to cloud storage
            """

            URL = self.url
            KEY = self.write_key

            HEADER = '&field1={}&field2={}'.format(str(value1), str(value2))

            NEW_URL = str(URL) + str(KEY) + str(HEADER)
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

            URL_R = self.read_url
            read_key = self.read_api_key
            header_r ='&results={}'.format(result)

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
        self.Url = 'https://maker.ifttt.com/trigger/{}/with/key/'.format(self.eventname)
        self.New_Url =self.Url + self.Key
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


    def get_time_date():
        try:
            """
            :return:  date and time
            """
            my = datetime.datetime.now()
            data_time = '{}:{}:{}'.format(my.hour,my.minute,my.second)
            data_date='{}/{}/{}'.format(my.day,my.month,my.year)
            return data_date,data_time
        except:
            print('could now get date and time ')




