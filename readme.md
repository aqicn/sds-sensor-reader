
# SDS Sensor Reader

This python script can be used to read the data from the SDS011/SDS18/SDS021 and upload it to the aqicn.org server.

The script continuously reads the data from the SDS sensor, and, every minute, uploads the average, median and standard deviation to the server.

# Installation

Make sure to update the `USB port` and `sensor ID` configuration in the script, lines 9 to 12:

    LOCATION = {'latitude': 28.7501, 'longitude': 77.1177}
    TOKEN    = "dummy-token-for-test-purpose-only"
    SENSORID = "YOUR-SENSOR-ID"
    USBPORT  = "/dev/ttyUSB0"

For the `TOKEN`, you can get one from this page: https://aqicn.org/data-platform/token/

For the `SENSORID`, you can use any name less than 128 characters. This ID is only used for you to help if you have multiple sensors.

For the `USBPORT`, you need to check on which USB port is the serial USB converter mounted. Check https://learn.sparkfun.com/tutorials/terminal-basics/connecting-to-your-device for more information.

# Running the script

Just use: `python sds-reader.py`

Output example:

    Starting reading sensor YOUR-SENSOR-ID on port /dev/ttyUSB0
    Reading [ 1]: {'pm2.5': 6.174900567257725, 'pm10': 3.1934677522143726}
    Reading [ 2]: {'pm2.5': 7.555017736539956, 'pm10': 7.020834793042507}
    Reading [ 3]: {'pm2.5': 0.3844247110354293, 'pm10': 7.771734774405182}
    Reading [ 4]: {'pm2.5': 3.22681824227835, 'pm10': 2.3183160649668055}
    Reading [ 5]: {'pm2.5': 6.571437982807612, 'pm10': 8.10732336965939}
    Reading [ 6]: {'pm2.5': 2.215579055773339, 'pm10': 8.498171362504383}
    Reading [ 7]: {'pm2.5': 8.027524718085807, 'pm10': 5.8429776102899025}
    Reading [ 8]: {'pm2.5': 6.2517504261702515, 'pm10': 2.263619703316302}
    ...
    Reading [60]: {'pm2.5': 5.775826608467894, 'pm10': 2.6825255819326377}
    Uploading: {
        "token": "dummy-token-for-test-purpose-only",
        "station": {
            "id": "YOUR-SENSOR-ID",
            "location": {
                "latitude": 28.7501,
                "longitude": 77.1177
            }
        },
        "readings": [
            {
                "specie": "pm2.5",
                "min": 0.3844247110354293,
                "max": 9.881988173998357,
                "median": 5.775826608467894,
                "value": 5.370915456820213,
                "stddev": 2.6854456309512917
            },
            {
                "specie": "pm10",
                "min": 0.016951997552983045,
                "max": 9.79528005515607,
                "median": 5.114991470114239,
                "value": 4.877448712778561,
                "stddev": 2.8556849925322383
            }
        ]
    }
    Data successfully posted: {u'status': u'ok', u'station': 1000003}    