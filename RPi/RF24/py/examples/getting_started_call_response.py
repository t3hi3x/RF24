###
# TMRh20 2014 - Updated to work with optimized RF24 Arduino library
###


###
 # Example for efficient call-response using ack-payloads
 #
 # This example continues to make use of all the normal functionality of the radios including
 # the auto-ack and auto-retry features, but allows ack-payloads to be written optionlly as well.
 # This allows very fast call-response communication, with the responding radio never having to
 # switch out of Primary Receiver mode to send back a payload, but having the option to switch to
 # primary transmitter if wanting to initiate communication instead of respond to a commmunication.
###

import sys
sys.path.append('../RF24')

from RF24 import *
from bcm2835 import *

import time, ctypes

millis = lambda: int(round(time.time() * 1000))

##
## Hardware configuration
##

## CE Pin, CSN Pin, SPI Speed

## Setup for GPIO 22 CE and CE1 CSN with SPI Speed @ 1Mhz
## radio = RF24(RPI_V2_GPIO_P1_22, BCM2835_SPI_CS1, BCM2835_SPI_SPEED_1MHZ);

## Setup for GPIO 15 CE and CE0 CSN with SPI Speed @ 4Mhz
## radio = RF24(RPI_V2_GPIO_P1_15, BCM2835_SPI_CS0, BCM2835_SPI_SPEED_4MHZ);

## Setup for GPIO 15 CE and CE0 CSN with SPI Speed @ 8Mhz
radio = RF24(RPI_V2_GPIO_P1_15, RPI_V2_GPIO_P1_24, BCM2835_SPI_SPEED_8MHZ)


## Radio pipe addresses for the 2 nodes to communicate.
addresses[][6] = {"1Node","2Node"}

role_ping_out = 1
role_pong_back = 0
role = 0

counter = 1                                # A single byte to keep track of the data being sent back and forth


def main():
    print("RPi/RF24/py/examples/gettingstarted_call_response\n")
    radio.begin()
    radio.setAutoAck(1)                    # Ensure autoACK is enabled
    radio.enableAckPayload()               # Allow optional ack payloads
    radio.setRetries(1,15)                 # Smallest time between retries, max no. of retries
    radio.setPayloadSize(1)                # Here we are sending 1-byte payloads to test the call-response speed
    radio.printDetails()                   # Dump the configuration of the rf unit for debugging


#/********* Role chooser ***********/

    print("\n ************ Role Setup ***********\n")
    input = ""
    myChar = {0}
    read_line = input("Choose a role: Enter 0 for pong_back, 1 for ping_out (CTRL+C to exit)\n>")
    
    if read_line.len == 1:
	    myChar = input[0]
    if myChar == '0':
        print("Role: Pong Back, awaiting transmission\n\n")
        role = role_pong_back
    else:
        print("Role: Ping Out, starting transmission\n\n")
        role = role_ping_out

#/***********************************/
    # This opens two pipes for these two nodes to communicate
    # back and forth.
    if role == role_ping_out:
        radio.openWritingPipe(addresses[0])
        radio.openReadingPipe(1,addresses[1])
    else:
        radio.openWritingPipe(addresses[1])
        radio.openReadingPipe(1,addresses[0])
        radio.startListening()

    while True:
        #/****************** Ping Out Role ***************************/
        if role == role_ping_out:                                   # Radio is in ping mode
            gotByte = int()                                         # Initialize a variable for the incoming response

            radio.stopListening();                                  # First, stop listening so we can talk.
            print("Now sending %d as payload. ",counter);           # Use a simple byte counter as payload
            unsigned long time = millis();                          # Record the current microsecond count

            if radio.write(&counter,1):                             # Send the counter variable to the other radio
                if not radio.available():                           # If nothing in the buffer, we got an ack but it is blank
                    print("Got blank response. round-trip delay: %s ms\n" % (millis()-time)
                else:
                    while radio.available():                        # If an ack with payload was received
                        radio.read( &gotByte, 1 )                   # Read it, and display the response time
                        print("Got response %s, round-trip delay: %s ms\n" % (gotByte, (millis()-time))
                        counter++                                   # Increment the counter variable

            else:
                print("Sending failed.\n"); }                       # If no ack response, sending failed

        time.sleep(1)  // Try again later
        #delay(250);

        #/****************** Pong Back Role ***************************/

        if role == role_pong_back:
            pipeNo = int()
            gotByte = int()                                         # Declare variables for the pipe and the byte received
            if radio.available(&pipeNo):                            # Read all available payloads      
                radio.flush_tx()                                    # Clear any unused ACK payloads	  				  
                radio.read( &gotByte, 1 )
                                                                    # Since this is a call-response. Respond directly with an ack payload.
                                                                    # Ack payloads are much more efficient than switching to transmit mode to respond to a call
                radio.writeAckPayload(pipeNo,&gotByte, 1 )          # This can be commented out to send empty payloads.	  
                print("Sent response %d \n\r", gotByte)
                time.sleep(900)                                     # Delay after a response to minimize CPU usage on RPi. Expects a payload every second      

if __name__ == "__main__":
    main()