from ctypes import c_int

CONFIG      = 0x00
EN_AA       = 0x01
EN_RXADDR   = 0x02
SETUP_AW    = 0x03
SETUP_RETR  = 0x04
RF_CH       = 0x05
RF_SETUP    = 0x06
STATUS      = 0x07
OBSERVE_TX  = 0x08
CD          = 0x09
RX_ADDR_P0  = 0x0A
RX_ADDR_P1  = 0x0B
RX_ADDR_P2  = 0x0C
RX_ADDR_P3  = 0x0D
RX_ADDR_P4  = 0x0E
RX_ADDR_P5  = 0x0F
TX_ADDR     = 0x10
RX_PW_P0    = 0x11
RX_PW_P1    = 0x12
RX_PW_P2    = 0x13
RX_PW_P3    = 0x14
RX_PW_P4    = 0x15
RX_PW_P5    = 0x16
FIFO_STATUS = 0x17
DYNPD	    = 0x1C
FEATURE	    = 0x1D

# Bit Mnemonics
MASK_RX_DR  = c_int(6)
MASK_TX_DS  = c_int(5)
MASK_MAX_RT = c_int(4)
EN_CRC      = c_int(3)
CRCO        = c_int(2)
PWR_UP      = c_int(1)
PRIM_RX     = c_int(0)
ENAA_P5     = c_int(5)
ENAA_P4     = c_int(4)
ENAA_P3     = c_int(3)
ENAA_P2     = c_int(2)
ENAA_P1     = c_int(1)
ENAA_P0     = c_int(0)
ERX_P5      = c_int(5)
ERX_P4      = c_int(4)
ERX_P3      = c_int(3)
ERX_P2      = c_int(2)
ERX_P1      = c_int(1)
ERX_P0      = c_int(0)
AW          = c_int(0)
ARD         = c_int(4)
ARC         = c_int(0)
PLL_LOCK    = c_int(4)
RF_DR       = c_int(3)
RF_PWR      = c_int(6)
RX_DR       = c_int(6)
TX_DS       = c_int(5)
MAX_RT      = c_int(4)
RX_P_NO     = c_int(1)
TX_FULL     = c_int(0)
PLOS_CNT    = c_int(4)
ARC_CNT     = c_int(0)
TX_REUSE    = c_int(6)
FIFO_FULL   = c_int(5)
TX_EMPTY    = c_int(4)
RX_FULL     = c_int(1)
RX_EMPTY    = c_int(0)
DPL_P5	    = c_int(5)
DPL_P4	    = c_int(4)
DPL_P3	    = c_int(3)
DPL_P2	    = c_int(2)
DPL_P1	    = c_int(1)
DPL_P0	    = c_int(0)
EN_DPL	    = c_int(2)
EN_ACK_PAY  = c_int(1)
EN_DYN_ACK  = c_int(0)

# Instruction Mnemonics
R_REGISTER    = 0x00
W_REGISTER    = 0x20
REGISTER_MASK = 0x1F
ACTIVATE      = 0x50
R_RX_PL_WID   = 0x60
R_RX_PAYLOAD  = 0x61
W_TX_PAYLOAD  = 0xA0
W_ACK_PAYLOAD = 0xA8
FLUSH_TX      = 0xE1
FLUSH_RX      = 0xE2
REUSE_TX_PL   = 0xE3
NOP           = 0xFF

# Non-P omissions
LNA_HCURR   c_int(0)

# P model memory Map
RPD         0x09
W_TX_PAYLOAD_NO_ACK  0xB0

# P model bit Mnemonics
RF_DR_LOW   c_int(5)
RF_DR_HIGH  c_int(3)
RF_PWR_LOW  c_int(1)
RF_PWR_HIGH c_int(2)