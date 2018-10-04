
# SDS Sensor Reader

This python script can be used to read the data from the SDS011/SDS18/SDS021 and upload it to the aqicn.org server.

The script continuously reads the data from the SDS sensor, and, every minute, uploads the average, median and standard deviation to the server.

# Installation

Make sure to update the `USB port` and `sensor ID` configuration in the script, line 15 and 16:

    SENSORID = "YOUR-SENSOR-ID"
    USBPORT  = "/dev/ttyUSB0"

For the `SENSORID`, use a name like `country.city.organization|name.sensor-name`. For instance `usa.nyc.nuy.outdoor-01` or `uae.dubai.johndoe.outdoor-patio`.

For the USB port, you need to check on which USB port is the serial USB converter mounted. Check https://learn.sparkfun.com/tutorials/terminal-basics/connecting-to-your-device for more information.


# Running the script

Just use: `python sds-reader.py`

Output example:

    Starting reading sensor YOUR-SENSOR-ID on port /dev/ttyUSB0
    [ 0.8] Samples: 1 PM2.5: 335 PM10: 642 StdDev(PM2.5):0.0
    [ 1.8] Samples: 2 PM2.5: 328 PM10: 625 StdDev(PM2.5):3.5
    [ 2.8] Samples: 3 PM2.5: 323 PM10: 613 StdDev(PM2.5):4.9
    [ 3.8] Samples: 4 PM2.5: 318 PM10: 601 StdDev(PM2.5):6.3
    [ 4.8] Samples: 5 PM2.5: 310 PM10: 577 StdDev(PM2.5):8.5
    [ 5.8] Samples: 6 PM2.5: 307 PM10: 569 StdDev(PM2.5):9.8
    ...
    [54.2] Samples:55 PM2.5: 315 PM10: 568 StdDev(PM2.5):7.5
    [55.2] Samples:56 PM2.5: 313 PM10: 569 StdDev(PM2.5):7.6
    [56.2] Samples:57 PM2.5: 312 PM10: 565 StdDev(PM2.5):7.6
    [57.2] Samples:58 PM2.5: 311 PM10: 563 StdDev(PM2.5):7.7
    [58.2] Samples:59 PM2.5: 315 PM10: 570 StdDev(PM2.5):7.7
    [59.2] Samples:60 PM2.5: 316 PM10: 572 StdDev(PM2.5):7.7
    Posting 673 bytes -> 200 OK 
    Data posting ok!
    upload queue(...): all done.
    [ 0.0] Samples: 1 PM2.5: 313 PM10: 567 StdDev(PM2.5):0.0
    [ 1.0] Samples: 2 PM2.5: 312 PM10: 567 StdDev(PM2.5):0.5
