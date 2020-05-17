import requests
import random
import time
import math
import json
import sys
from serial import Serial

LOCATION = {'latitude': 28.7501, 'longitude': 77.1177}
TOKEN    = "dummy-token-for-test-purpose-only"
SENSORID = "YOUR-SENSOR-ID"
USBPORT  = "/dev/ttyUSB0"

class SensorDataUploader:

    def __init__(self, station, token):
        self.token = token
        self.station = station


    def send(self,readings):

        params = {'station':self.station,'readings':readings,'token':self.token} 
        print("Uploading: %s"%json.dumps(params, indent=4))

        request = requests.post( url = "https://aqicn.org/sensor/upload/",  json = params)
        data = request.json() 
        if data["status"]!="ok":
            print("Something went wrong: %s" % data)
        else:
            print("Data successfully posted: %s"%data)




class Accumulator:

    def __init__(self, name):
        self.name = name
        self.values = []

    def add(self,val):
        self.values.append(val)

    def count(self):
        return len(self.values)

    def reset(self):
        self.values=[]

    def min(self):
        return self.values[0]

    def max(self):
        return self.values[len(self.values)-1]

    def median(self):
        return self.values[len(self.values)/2]

    def mean(self):
        return float(sum(self.values)) / len(self.values)

    def stddev(self):
        l = len(self.values)
        mean = self.mean()
        return math.sqrt(float(reduce(lambda x, y: x + y, map(lambda x: (x - mean) ** 2, self.values))) / l)


    def summary(self):
        self.values.sort()
        return {"specie":self.name,'value':self.mean(),'min':self.min(),'max':self.max(),'median':self.median(), 'stddev':self.stddev()} 



class DummyReader:

    def read( self ):

        time.sleep(1.1)
        return {"pm2.5":random.random()*10,"pm10":random.random()*10}


class SDS011Reader:

    def __init__(self, inport):
        self.serial = Serial(port=inport,baudrate=9600)
        self.values = []
        self.step = 0

    def read( self ):

        # time.sleep(1)
        # return {"pm2.5":random.random()*100,"pm10":random.random()*100}

        while self.serial.inWaiting()!=0:
            v=ord(self.serial.read())

            if self.step ==0:
                if v==170:
                    self.step=1

            elif self.step==1:
                if v==192:
                    self.values = [0,0,0,0,0,0,0]
                    self.step=2
                else:
                    self.step=0

            elif self.step>8:
                self.step =0
                pm25 = (self.values[0]+self.values[1]*256)/10
                pm10 = (self.values[2]+self.values[3]*256)/10
                return {"pm2.5":pm25,"pm10":pm10}

            elif self.step>=2:
                self.values[self.step-2]=v
                self.step= self.step+1

        return None



def readAndUpload(sensor, uploader):

    try:

        while True:
            accumulators = {}
            startTime = time.time()

            while time.time() < startTime+60:
                values = sensor.read()
                if values==None:
                    continue

                print("Reading [%2d]: %s"%(int(time.time()-startTime),values))
                for specie, value in values.items():
                    if not (specie in accumulators):
                        accumulators[specie]=Accumulator(specie)
                    accumulators[specie].add(value)


            readings = []
            for specie, accumulator in accumulators.items():
                readings.append(accumulator.summary())

            if len(readings)>0:
                uploader.send(readings)
            else:
                print("No value read from the sensor...")


    except KeyboardInterrupt:
        print "Bye"
        sys.exit()



print("Starting reading sensor "+SENSORID+" on port "+USBPORT)

# Station parameter  
station = {'id':SENSORID, 'location':LOCATION}
uploader = SensorDataUploader(station, TOKEN)

sensor = SDS011Reader(USBPORT)
# sensor = DummyReader()
readAndUpload(sensor,uploader)

