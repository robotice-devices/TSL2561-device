#!/usr/bin/env python

from TSL2561 import *

def get_data(sensor):
    """
    Get the luminosity readings.
    """

    name = sensor.get('name')
    bus = 1
    
    tsl = TSL2561() 
     
    if tsl.foundSensor(): 
        print("Found sensor...")
        
        tsl.setGain(tsl.GAIN_16X);  
        tsl.setTiming(tsl.INTEGRATIONTIME_13MS)

        x = tsl.getFullLuminosity()     
        print("Full luminosity value: %d" % x)
        print("Full luminosity value: %#08x" % x)

        full = tsl.getLuminosity(tsl.FULLSPECTRUM)
        visible = tsl.getLuminosity(tsl.VISIBLE)
        infrared = tsl.getLuminosity(tsl.INFRARED)

        print("IR: %x" % infrared)
        print("Full: %x" % full )
        print("Visible: %#x" % visible )
        print("Visible, calculated: %#x" % (full - infrared) )
        print("Lux: %d" % tsl.calculateLux(full, infrared) )
    else:
        print("No sensor?")


    luminosity = 0
 
    values = [
        ('%s.luminosity' % name, luminosity, ),
    ]
    return values
