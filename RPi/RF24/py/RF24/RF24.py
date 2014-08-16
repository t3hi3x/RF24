#############################################################################
#
# Python Bindings for RF24.cpp for RPi
#
# License: LGPL (Lesser General Public License) v2.0
# Author:  Alex Breshears (github: @t3hi3x)
# Date:    2014-08-03
#
#############################################################################

from ctypes import cdll, c_int, byref
lib = cdll.LoadLibrary('./librf24-bcm.so.1.0')

RF24_PA_MIN       = c_int(0)
RF24_PA_LOW       = c_int(1)
RF24_PA_HIGH      = c_int(2)
RF24_PA_MAX       = c_int(3)
RF24_PA_ERROR     = c_int(4)

RF24_1MBPS        = c_int(0)
RF24_2MBPS        = c_int(1)
RF24_250KBPS      = c_int(2)

RF24_CRC_DISABLED = c_int(0)
RF24_CRC_8        = c_int(1)
RF24_CRC_16       = c_int(2)

class RF24(object):
    def __init__(self, ce_pin, cs_pin, spi_speed):
        self.obj = lib.RF24_new(ce_pin, cs_pin, spi_speed)
    
    def begin(self):
        lib.RF24_begin(self.obj)
    
    def startListening(self):
        lib.RF24_startListening(self.obj)
    
    def stopListening(self):
        lib.RF24_stopListenting(self.obj)
    
    def write(self, buf, length):
        return lib.RF24_write(self.obj, buf, length)
    
    def available(self):
        return lib.RF24_available(self.obj)
    
    def read(self, buf, length):
        # Python doesn't direclty support referencable parameters, but since it's dynamically typed, we can return an arbitray object
        to_return = buf
        lib.RF24_read(self.obj, byref(to_return), length)
        return to_return
    
    def openWritingPage(self, address):
        lib.RF24_openWritingPage(self.obj, address)
    
    def openReadingPage(self, number, address):
        lib.RF24_openReadingPage(self.obj, number, address)
    
    def flust_tx(self):
        lib.RF24_flush_tx(self.obj)
    
    def setRetries(self, delay, count):
        lib.RF24_setRetries(self.obj, delay, count)
    
    def setChannel(self, channel):
        lib.RF24_setChannel(self.obj, channel)
    
    def setPayloadSize(self, size):
        lib.RF24_setPayloadSize(self.obj, channel)
    
    def getPaylaodSize(self):
        return lib.RF24_getPayloadSize(self.obj)
    
    def getDynamicPayloadSize(self):
        return lib.RF24_getDynamicPayloadSize(self.obj)
    
    def enableAckPayload(self):
        lib.RF24_enableAckPayload(self.obj)
    
    def enableDynamicPayloads(self):
        lib.RF24_enableDynamicPayloads(self.obj)
    
    def enableDynamicAck(self):
        lib.RF24_enableDynamicAck(self.obj)
    
    def isPVarient(self):
        return lib.RF24_isPVariant(self.obj)
    
    def setAutoAck(self, enable):
        lib.RF24_setAutoAck(self.obj, enable)
    
    def setAutoAck(self, pipe, enable):
        lib.RF24_setAutoAck_2(self.obj, pipe, enable)
    
    def setPALevel(self, level):
        lib.RF24_setPALevel(self.obj, level)
    
    def getPALevel(self):
        return lib.RF24_getPALevel(self.obj)
    
    def setDataRate(self, speed):
        return lib.RF24_setDataRate(self.obj, speed)
    
    def getDataRate(self):
        return lib.RF24_getDataRate(self.obj)
    
    def setCRCLength(self, length):
        lib.RF24_setCRCLength(self.obj, length)
    
    def getCRCLength(self):
        return lib.RF24_getCRCLength(self)
    
    # Depreciated Methonds
    def openWritingPipe(self, address):
        lib.RF24_openWritingPipe(self.obj, address)
    
    def openWriingPipe(self, number, address):
        lib.RF24_openWritingPipe(self.obj, number, address)
    
    def printDetails(self):
        lib.RF24_printDetails(self.obj)
    
    def powerDown(self):
        lib.RF24_powerDown(self.obj)
    
    def powerUp(self):
        lib.RF24_PowerUp(self.obj)
    
    def write(self, buf, length, multicast):
        return lib.RF24_write(self.obj, buf, length, multicast)
    
    def writeFast(self, buf, length):
        return lib.RF24_writeFast(self.obj, buf, length)
    
    def writeFast(self, buf, length, multicast):
        return lib.RF24_writeFast(self.obj, buf, length, multicast)
    
    def writeBlocking(self, buf, length, timeout):
        return lib.RF24_writeBlocking(self.obj, buf, length, timeout)
    
    def txStandby(self):
        return lib.RF24_txStandby(self.obj)
    
    def txStandby(self, pipe_num):
        return lib.RF24_txStandby(self.obj, pipe_num)
    
    def available(self, pipe_num):
        return lib.RF24_available(self.obj, pipe_num)
    
    def startFastWrite(self, buf, length, multicast):
        lib.RF24_startFastWrite(self.obj, buf, length, multicast)
    
    def startWrite(self, buf, length, multicast):
        lib.RF24_startWrite(self.obj, buf, length, multicast)
    
    def reUseTX(self):
        lib.RF24_reUseTX(self.obj)
    
    def writeAckPayload(self, pipe, buf, length):
        lib.RF24_writeAckPayload(self.obj, pipe, buf, length)
    
    def whatHappened(self, tx_ok, tx_fail, rx_ready):
        return lib.RF24_whatHappened(self.obj, tx_ok, tx_fail, rx_ready)
    
    def testCarrier(self):
        return lib.RF24_testCarrier(self.obj)
    
    def testRPD(self):
        return lib.RF24_testRPD(self.obj)
    
    def isValid(self):
        return lib.RF24_isValid(self.obj)
    
    def maskIRQ(self, tx_ok, tx_fail, rx_ready):
        lib.RF24_maskIRQ(self.obj, tx_ok, tx_fail, rx_ready)
    
    def setAddressWidth(self, a_width):
        lib.RF24_setAddressWidth(self.obj, a_width)