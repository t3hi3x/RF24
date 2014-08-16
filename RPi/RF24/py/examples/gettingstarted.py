import sys
sys.path.append('../RF24')

from RF24 import *
from bcm2835 import *

import time, ctypes

millis = lambda: int(round(time.time() * 1000))

CE_PIN  = RPI_V2_GPIO_P1_15
CSN_PIN = RPI_V2_GPIO_P1_24
CLOCK_S = BCM2835_SPI_SPEED_8MHZ

def main():
    radio = RF24(CE_PIN, CSN_PIN, CLOCK_S)
    pipes[][6] = {"1Node","2Node"};

    role_ping_out = True, role_pong_back = False;
    role = role_pong_back;

    radio.begin();

    # optionally, increase the delay between retries & # of retries
    radio.setRetries(15,15);
    
    #Dump the configuration of the rf unit for debugging
    radio.printDetails();

    # Print preamble:
    print("py/RF24/examples/pingtest/");
    
    print("\n ************ Role Setup ***********");

    read_line = input("Choose a role: Enter 0 for pong_back, 1 for ping_out (CTRL+C to exit)")
    
    if read_line.len() == 1:
        if read_line == "0":
            print("Role: Pong Back, awaiting transmission")
        else:
            print("Role: Ping Out, starting transmission")
            role = role_ping_out
    
    if role == role_ping_out:
        radio.openWritingPipe(pipes[0])
        radio.openReadingPipe(1,pipes[1])
    else:
        radio.openWritingPipe(pipes[1])
        radio.openReadingPipe(1,pipes[0])
        radio.startListening()
    
    while True:
        if role == role_pong_out:
            # First, stop listening so we can talk.
            radio.stopListening()
            
            print("Now sending...")
            time = millis()
            
            ok = radio.write(time, sys.getsizeof(ctypes.c_ulong))
            
            if !ok:
                print("failed")
                
            radio.startListening()
            
            started_waiting_at = millis()
            
            timeout = False
            
            while  not radio.available() and not timeout:
                if millis() - started_waiting_at > 200
                timeout = True;
                
            if timeout:
                print("Failed, response timed out.")
            else:
                got_time = ctypes.c_long()
                
                radio.read(ctypes.byref(got_time), sys.getsizeof(cytpes.c_ulong))
                
                print("Got response %s, round-trip delay: %s" % got_time (millis() - got_time))
                
            time.sleep(0.001)
        elif role == role_ping_out:
            # Pong back role.  Receive each packet, dump it out, and send it back
            
            if radio.available():
                got_time = ctypes.c_long()
                
                radio.read(ctypes.byref(got_time), sys.getsizeof(cytpes.c_ulong))
                
                radio.stopListening()
                
                radio.write(got_time, sys.getsizeof(cytpes.c_ulong))
                
                time.sleep(0.925);

if __name__ == "__main__":
    main()