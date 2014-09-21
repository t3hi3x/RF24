import sys
sys.path.append('../RF24/')

from RF24 import *
from bcm2835 import *

from time import *

millis = lambda: int(round(time() * 1000))

radio = RF24(RPI_V2_GPIO_P1_15, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_8MHZ)

pipes = ["2Node","1Node"]

def send_data(msg):
  # swap TX & Rx addr for sending
  print("Sending: %s" % msg)
  radio.openWritingPipe(pipes[1])
  radio.openReadingPipe(0,pipes[0])
  radio.stopListening()
  ok = radio.write(msg,len(msg))

  # restore TX & Rx addr for receiving
  radio.openWritingPipe(pipes[0])
  radio.openReadingPipe(1,pipes[1])
  radio.startListening()

def receive():
  length = 0
  RecvPayload = long()
  if radio.available():
    done = False
    while not done:
      length = radio.getDynamicPayloadSize()
      print("Length: %s" % length)
      RecvPayload = radio.read(RecvPayload, size=length)
      sleep(.005)
      done = True

    print("Recv (%s): %s" % (type(RecvPayload), RecvPayload))
    send_data("Hello world")

def main():
  print("RPi/RF24/py/examples/string_communication.py\n")

  # Let's setup the radio
  print("Setting up radio...")
  radio.begin()

  #radio.setDataRate(RF24_250KBPS)
  radio.setPALevel(RF24_PA_MAX)
  #radio.setChannel(70)

  radio.enableDynamicPayloads()
  radio.setRetries(15,15)
  #radio.setCRCLength(RF24_CRC_16)

  radio.openWritingPipe(pipes[1])
  radio.openReadingPipe(0,pipes[0])

  radio.startListening()
  radio.printDetails()
  print
  while True:
    receive()
    sleep(.005)

if __name__ == "__main__":
  main()
