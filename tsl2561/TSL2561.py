#!/usr/bin/python


from Adafruit_I2C import Adafruit_I2C
from time import sleep

# ===========================================================================
# TSL2561 Class
# ===========================================================================

TSL2561_COMMAND_BIT               = (0x80)    # Must be 1
TSL2561_CLEAR_BIT                 = (0x40)    # Clears any pending interrupt (write 1 to clear)
TSL2561_WORD_BIT                  = (0x20)    # 1 = read/write word (rather than byte)
TSL2561_BLOCK_BIT                 = (0x10)    # 1 = using block read/write

TSL2561_CONTROL_POWERON           = 0x03
TSL2561_CONTROL_POWEROFF          = 0x00

TSL2561_REGISTER_CHAN0_LOW        = 0x0C
TSL2561_REGISTER_CHAN0_HIGH       = 0x0D
TSL2561_REGISTER_CHAN1_LOW        = 0x0E
TSL2561_REGISTER_CHAN1_HIGH       = 0x0F

TSL2561_REGISTER_CONTROL          = 0x00

class TSL2561 :
  i2c = None
  
  def __init__(self, address=0x39, debug=False):
    self.i2c = Adafruit_I2C(address)
    self.address = address
    self.debug = debug
    self._visible = 0
    self._ir = 0
    
  def enable(self) :
    self.i2c.write8(TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL, TSL2561_CONTROL_POWERON)
    
  def disable(self) :
    self.i2c.write8(TSL2561_COMMAND_BIT | TSL2561_REGISTER_CONTROL, TSL2561_CONTROL_POWEROFF)
    
  def readData(self) :
    self.enable()
    
    # Wait ADC
    sleep(0.403)      # Default value.
    
    
    # Reads a two byte value from channel 0 (visible + infrared)
    self._visible = self.i2c.readU16(TSL2561_COMMAND_BIT | TSL2561_WORD_BIT | TSL2561_REGISTER_CHAN0_LOW);

    # Reads a two byte value from channel 1 (infrared)
    self._ir = self.i2c.readU16(TSL2561_COMMAND_BIT | TSL2561_WORD_BIT | TSL2561_REGISTER_CHAN1_LOW);
    #self._visible = self._visible - self._ir
    
    self.disable();
    
  def getVisible(self):
        return self._visible
        
  def getInfrared(self):
        return self._ir

