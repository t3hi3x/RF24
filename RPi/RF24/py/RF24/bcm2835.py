from ctypes import c_int

## BCM2835 CONSTANTS ##

HIGH = 0x1
LOW  = 0x0

BCM2835_CORE_CLK_HZ = c_int(250000000)

BCM2835_PERI_BASE   = 0x20000000
BCM2835_ST_BASE     = (BCM2835_PERI_BASE + 0x3000)
BCM2835_GPIO_PADS   = (BCM2835_PERI_BASE + 0x100000)
BCM2835_CLOCK_BASE  = (BCM2835_PERI_BASE + 0x101000)
BCM2835_GPIO_BASE   = (BCM2835_PERI_BASE + 0x200000)
BCM2835_SPI0_BASE   = (BCM2835_PERI_BASE + 0x204000)
BCM2835_BSC0_BASE   = (BCM2835_PERI_BASE + 0x205000)
BCM2835_GPIO_PWM    = (BCM2835_PERI_BASE + 0x20C000)
BCM2835_BSC1_BASE   = (BCM2835_PERI_BASE + 0x804000)

BCM2835_PAGE_SIZE  = c_int(4*1024)
BCM2835_BLOCK_SIZE = c_int(4*1024)

BCM2835_GPFSEL0   = 0x0000 # GPIO Function Select 0
BCM2835_GPFSEL1   = 0x0004 # GPIO Function Select 1
BCM2835_GPFSEL2   = 0x0008 # GPIO Function Select 2
BCM2835_GPFSEL3   = 0x000c # GPIO Function Select 3
BCM2835_GPFSEL4   = 0x0010 # GPIO Function Select 4
BCM2835_GPFSEL5   = 0x0014 # GPIO Function Select 5
BCM2835_GPSET0    = 0x001c # GPIO Pin Output Set 0
BCM2835_GPSET1    = 0x0020 # GPIO Pin Output Set 1
BCM2835_GPCLR0    = 0x0028 # GPIO Pin Output Clear 0
BCM2835_GPCLR1    = 0x002c # GPIO Pin Output Clear 1
BCM2835_GPLEV0    = 0x0034 # GPIO Pin Level 0
BCM2835_GPLEV1    = 0x0038 # GPIO Pin Level 1
BCM2835_GPEDS0    = 0x0040 # GPIO Pin Event Detect Status 0
BCM2835_GPEDS1    = 0x0044 # GPIO Pin Event Detect Status 1
BCM2835_GPREN0    = 0x004c # GPIO Pin Rising Edge Detect Enable 0
BCM2835_GPREN     = 0x0050 # GPIO Pin Rising Edge Detect Enable 1
BCM2835_GPFEN0    = 0x0058 # GPIO Pin Falling Edge Detect Enable 0
BCM2835_GPFEN1    = 0x005c # GPIO Pin Falling Edge Detect Enable 1
BCM2835_GPHEN0    = 0x0064 # GPIO Pin High Detect Enable 0
BCM2835_GPHEN1    = 0x0068 # GPIO Pin High Detect Enable 1
BCM2835_GPLEN0    = 0x0070 # GPIO Pin Low Detect Enable 0
BCM2835_GPLEN1    = 0x0074 # GPIO Pin Low Detect Enable 1
BCM2835_GPAREN0   = 0x007c # GPIO Pin Async. Rising Edge Detect 0
BCM2835_GPAREN1   = 0x0080 # GPIO Pin Async. Rising Edge Detect 1
BCM2835_GPAFEN0   = 0x0088 # GPIO Pin Async. Falling Edge Detect 0
BCM2835_GPAFEN1   = 0x008c # GPIO Pin Async. Falling Edge Detect 1
BCM2835_GPPUD     = 0x0094 # GPIO Pin Pull-up/down Enable
BCM2835_GPPUDCLK0 = 0x0098 # GPIO Pin Pull-up/down Enable Clock 0
BCM2835_GPPUDCLK1 = 0x009c # GPIO Pin Pull-up/down Enable Clock 1

BCM2835_GPIO_FSEL_INPT  = 0b000   # Input
BCM2835_GPIO_FSEL_OUTP  = 0b001   # Output
BCM2835_GPIO_FSEL_ALT0  = 0b100   # Alternate function 0
BCM2835_GPIO_FSEL_ALT1  = 0b101   # Alternate function 1
BCM2835_GPIO_FSEL_ALT2  = 0b110   # Alternate function 2
BCM2835_GPIO_FSEL_ALT3  = 0b111   # Alternate function 3
BCM2835_GPIO_FSEL_ALT4  = 0b011   # Alternate function 4
BCM2835_GPIO_FSEL_ALT5  = 0b010   # Alternate function 5
BCM2835_GPIO_FSEL_MASK  = 0b111   # Function select bits mask
 
BCM2835_GPIO_PUD_OFF  = 0b00   # Off ? disable pull-up/down
BCM2835_GPIO_PUD_DOWN = 0b01   # Enable Pull Down control
BCM2835_GPIO_PUD_UP   = 0b10   # Enable Pull Up control

BCM2835_PADS_GPIO_0_27  = 0x002c # Pad control register for pads 0 to 27
BCM2835_PADS_GPIO_28_45 = 0x0030 # Pad control register for pads 28 to 45
BCM2835_PADS_GPIO_46_53 = 0x0034 # Pad control register for pads 46 to 53

BCM2835_PAD_PASSWRD             = (0x5A << 24)  # Password to enable setting pad mask
BCM2835_PAD_SLEW_RATE_UNLIMITED = 0x10 # Slew rate unlimited
BCM2835_PAD_HYSTERESIS_ENABLED  = 0x08 # Hysteresis enabled
BCM2835_PAD_DRIVE_2mA           = 0x00 # 2mA drive current
BCM2835_PAD_DRIVE_4mA           = 0x01 # 4mA drive current
BCM2835_PAD_DRIVE_6mA           = 0x02 # 6mA drive current
BCM2835_PAD_DRIVE_8mA           = 0x03 # 8mA drive current
BCM2835_PAD_DRIVE_10mA          = 0x04 # 10mA drive current
BCM2835_PAD_DRIVE_12mA          = 0x05 # 12mA drive current
BCM2835_PAD_DRIVE_14mA          = 0x06 # 14mA drive current
BCM2835_PAD_DRIVE_16mA          = 0x07 # 16mA drive current

BCM2835_PAD_GROUP_GPIO_0_27  = c_int(0) # Pad group for GPIO pads 0 to 27
BCM2835_PAD_GROUP_GPIO_28_45 = c_int(1) # Pad group for GPIO pads 28 to 45
BCM2835_PAD_GROUP_GPIO_46_53 = c_int(2)  # Pad group for GPIO pads 46 to 53

RPI_GPIO_P1_03 = c_int(0)# Version 1 Pin P1-03
RPI_GPIO_P1_05 = c_int(1)# Version 1 Pin P1-05
RPI_GPIO_P1_07 = c_int(4)# Version 1 Pin P1-07
RPI_GPIO_P1_08 = c_int(14)   # Version 1 Pin P1-08 defaults to alt function 0 UART0_TXD
RPI_GPIO_P1_10 = c_int(15)   # Version 1 Pin P1-10 defaults to alt function 0 UART0_RXD
RPI_GPIO_P1_11 = c_int(17)   # Version 1 Pin P1-11
RPI_GPIO_P1_12 = c_int(18)   # Version 1 Pin P1-12 can be PWM channel 0 in ALT FUN 5
RPI_GPIO_P1_13 = c_int(21)   # Version 1 Pin P1-13
RPI_GPIO_P1_15 = c_int(22)   # Version 1 Pin P1-15
RPI_GPIO_P1_16 = c_int(23)   # Version 1 Pin P1-16
RPI_GPIO_P1_18 = c_int(24)   # Version 1 Pin P1-18
RPI_GPIO_P1_19 = c_int(10)   # Version 1 Pin P1-19 MOSI when SPI0 in use
RPI_GPIO_P1_21 = c_int(9)# Version 1 Pin P1-21 MISO when SPI0 in use
RPI_GPIO_P1_22 = c_int(25)   # Version 1 Pin P1-22
RPI_GPIO_P1_23 = c_int(11)   # Version 1 Pin P1-23 CLK when SPI0 in use
RPI_GPIO_P1_24 = c_int(8)# Version 1 Pin P1-24 CE0 when SPI0 in use
RPI_GPIO_P1_26 = c_int(7)# Version 1 Pin P1-26 CE1 when SPI0 in use

# RPi Version 2
RPI_V2_GPIO_P1_03 = c_int(2)# Version 2 Pin P1-03
RPI_V2_GPIO_P1_05 = c_int(3)# Version 2 Pin P1-05
RPI_V2_GPIO_P1_07 = c_int(4)# Version 2 Pin P1-07
RPI_V2_GPIO_P1_08 = c_int(14)   # Version 2 Pin P1-08 defaults to alt function 0 UART0_TXD
RPI_V2_GPIO_P1_10 = c_int(15)   # Version 2 Pin P1-10 defaults to alt function 0 UART0_RXD
RPI_V2_GPIO_P1_11 = c_int(17)   # Version 2 Pin P1-11
RPI_V2_GPIO_P1_12 = c_int(18)   # Version 2 Pin P1-12 can be PWM channel 0 in ALT FUN 5
RPI_V2_GPIO_P1_13 = c_int(27)   # Version 2 Pin P1-13
RPI_V2_GPIO_P1_15 = c_int(22)   # Version 2 Pin P1-15
RPI_V2_GPIO_P1_16 = c_int(23)   # Version 2 Pin P1-16
RPI_V2_GPIO_P1_18 = c_int(24)   # Version 2 Pin P1-18
RPI_V2_GPIO_P1_19 = c_int(10)   # Version 2 Pin P1-19 MOSI when SPI0 in use
RPI_V2_GPIO_P1_21 = c_int(9)# Version 2 Pin P1-21 MISO when SPI0 in use
RPI_V2_GPIO_P1_22 = c_int(25)   # Version 2 Pin P1-22
RPI_V2_GPIO_P1_23 = c_int(11)   # Version 2 Pin P1-23 CLK when SPI0 in use
RPI_V2_GPIO_P1_24 = c_int(8)# Version 2 Pin P1-24 CE0 when SPI0 in use
RPI_V2_GPIO_P1_26 = c_int(7)# Version 2 Pin P1-26 CE1 when SPI0 in use

# RPi Version 2 new plug P5
RPI_V2_GPIO_P5_03 = c_int(28)   # Version 2 Pin P5-03
RPI_V2_GPIO_P5_04 = c_int(29)   # Version 2 Pin P5-04
RPI_V2_GPIO_P5_05 = c_int(30)   # Version 2 Pin P5-05
RPI_V2_GPIO_P5_06 = c_int(31)   # Version 2 Pin P5-06

BCM2835_SPI0_CS   = 0x0000 # SPI Master Control and Status
BCM2835_SPI0_FIFO = 0x0004 # SPI Master TX and RX FIFOs
BCM2835_SPI0_CLK  = 0x0008 # SPI Master Clock Divider
BCM2835_SPI0_DLEN = 0x000c # SPI Master Data Length
BCM2835_SPI0_LTOH = 0x0010 # SPI LOSSI mode TOH
BCM2835_SPI0_DC   = 0x0014 # SPI DMA DREQ Controls

# Register masks for SPI0_CS
BCM2835_SPI0_CS_LEN_LONG    = 0x02000000 # Enable Long data word in Lossi mode if DMA_LEN is set
BCM2835_SPI0_CS_DMA_LEN     = 0x01000000 # Enable DMA mode in Lossi mode
BCM2835_SPI0_CS_CSPOL2      = 0x00800000 # Chip Select 2 Polarity
BCM2835_SPI0_CS_CSPOL1      = 0x00400000 # Chip Select 1 Polarity
BCM2835_SPI0_CS_CSPOL0      = 0x00200000 # Chip Select 0 Polarity
BCM2835_SPI0_CS_RXF         = 0x00100000 # RXF - RX FIFO Full
BCM2835_SPI0_CS_RXR         = 0x00080000 # RXR RX FIFO needs Reading ( full)
BCM2835_SPI0_CS_TXD         = 0x00040000 # TXD TX FIFO can accept Data
BCM2835_SPI0_CS_RXD         = 0x00020000 # RXD RX FIFO contains Data
BCM2835_SPI0_CS_DONE        = 0x00010000 # Done transfer Done
BCM2835_SPI0_CS_TE_EN       = 0x00008000 # Unused
BCM2835_SPI0_CS_LMONO       = 0x00004000 # Unused
BCM2835_SPI0_CS_LEN         = 0x00002000 # LEN LoSSI enable
BCM2835_SPI0_CS_REN         = 0x00001000 # REN Read Enable
BCM2835_SPI0_CS_ADCS        = 0x00000800 # ADCS Automatically Deassert Chip Select
BCM2835_SPI0_CS_INTR        = 0x00000400 # INTR Interrupt on RXR
BCM2835_SPI0_CS_INTD        = 0x00000200 # INTD Interrupt on Done
BCM2835_SPI0_CS_DMAEN       = 0x00000100 # DMAEN DMA Enable
BCM2835_SPI0_CS_TA          = 0x00000080 # Transfer Active
BCM2835_SPI0_CS_CSPOL       = 0x00000040 # Chip Select Polarity
BCM2835_SPI0_CS_CLEAR       = 0x00000030 # Clear FIFO Clear RX and TX
BCM2835_SPI0_CS_CLEAR_RX    = 0x00000020 # Clear FIFO Clear RX
BCM2835_SPI0_CS_CLEAR_TX    = 0x00000010 # Clear FIFO Clear TX
BCM2835_SPI0_CS_CPOL        = 0x00000008 # Clock Polarity
BCM2835_SPI0_CS_CPHA        = 0x00000004 # Clock Phase
BCM2835_SPI0_CS_CS          = 0x00000003 # Chip Select

BCM2835_SPI_BIT_ORDER_LSBFIRST = c_int(0)  # LSB First
BCM2835_SPI_BIT_ORDER_MSBFIRST = c_int(1)   # MSB First

BCM2835_SPI_MODE0 = c_int(0)  # CPOL = 0, CPHA = 0
BCM2835_SPI_MODE1 = c_int(1)  # CPOL = 0, CPHA = 1
BCM2835_SPI_MODE2 = c_int(2)  # CPOL = 1, CPHA = 0
BCM2835_SPI_MODE3 = c_int(3)  # CPOL = 1, CPHA = 1

BCM2835_SPI_CS0 = c_int(0) # Chip Select 0
BCM2835_SPI_CS1 = c_int(1) # Select 1
BCM2835_SPI_CS2 = c_int(2) # Chip Select 2 (ie pins CS1 and CS2 are asserted)
BCM2835_SPI_CS_NONE = c_int(3) # No CS, control it yourself

# Only GPIO > 3 can be used (to not interfere with the previous value just above )
# Lucky we have plenty of theese pins
BCM2835_SPI_CS_GPIO4  = RPI_V2_GPIO_P1_07 # BCM GPIO 4
BCM2835_SPI_CS_GPIO17 = RPI_V2_GPIO_P1_11 # BCM GPIO 17
BCM2835_SPI_CS_GPIO18 = RPI_V2_GPIO_P1_12 # BCM GPIO 18
BCM2835_SPI_CS_GPIO22 = RPI_V2_GPIO_P1_15 # BCM GPIO 22
BCM2835_SPI_CS_GPIO23 = RPI_V2_GPIO_P1_16 # BCM GPIO 23
BCM2835_SPI_CS_GPIO24 = RPI_V2_GPIO_P1_18 # BCM GPIO 24
BCM2835_SPI_CS_GPIO25 = RPI_V2_GPIO_P1_22 # BCM GPIO 25
BCM2835_SPI_CS_GPIO28 = RPI_V2_GPIO_P5_03 # BCM GPIO 28
BCM2835_SPI_CS_GPIO29 = RPI_V2_GPIO_P5_04 # BCM GPIO 29
BCM2835_SPI_CS_GPIO30 = RPI_V2_GPIO_P5_05 # BCM GPIO 30
BCM2835_SPI_CS_GPIO31 = RPI_V2_GPIO_P5_06 # BCM GPIO 31

BCM2835_SPI_CLOCK_DIVIDER_65536 = c_int(0)   # 65536 = 262.144us = 3.814697260kHz
BCM2835_SPI_CLOCK_DIVIDER_32768 = c_int(32768)   # 32768 = 131.072us = 7.629394531kHz
BCM2835_SPI_CLOCK_DIVIDER_16384 = c_int(16384)   # 16384 = 65.536us = 15.25878906kHz
BCM2835_SPI_CLOCK_DIVIDER_8192  = c_int(8192)# 8192 = 32.768us = 30/51757813kHz
BCM2835_SPI_CLOCK_DIVIDER_4096  = c_int(4096)# 4096 = 16.384us = 61.03515625kHz
BCM2835_SPI_CLOCK_DIVIDER_2048  = c_int(2048)# 2048 = 8.192us = 122.0703125kHz
BCM2835_SPI_CLOCK_DIVIDER_1024  = c_int(1024)# 1024 = 4.096us = 244.140625kHz
BCM2835_SPI_CLOCK_DIVIDER_512   = c_int(512) # 512 = 2.048us = 488.28125kHz
BCM2835_SPI_CLOCK_DIVIDER_256   = c_int(256) # 256 = 1.024us = 976.5625MHz
BCM2835_SPI_CLOCK_DIVIDER_128   = c_int(128) # 128 = 512ns = = 1.953125MHz
BCM2835_SPI_CLOCK_DIVIDER_64    = c_int(64)  # 64 = 256ns = 3.90625MHz
BCM2835_SPI_CLOCK_DIVIDER_32    = c_int(32)  # 32 = 128ns = 7.8125MHz
BCM2835_SPI_CLOCK_DIVIDER_16    = c_int(16)  # 16 = 64ns = 15.625MHz
BCM2835_SPI_CLOCK_DIVIDER_8     = c_int(8)   # 8 = 32ns = 31.25MHz
BCM2835_SPI_CLOCK_DIVIDER_4     = c_int(4)   # 4 = 16ns = 62.5MHz
BCM2835_SPI_CLOCK_DIVIDER_2     = c_int(2)   # 2 = 8ns = 125MHz fastest you can get
BCM2835_SPI_CLOCK_DIVIDER_1     = c_int(1)   # 1 = 262.144us = 3.814697260kHz same as 0/65536

BCM2835_SPI_SPEED_64MHZ  = BCM2835_SPI_CLOCK_DIVIDER_4
BCM2835_SPI_SPEED_32MHZ  = BCM2835_SPI_CLOCK_DIVIDER_8
BCM2835_SPI_SPEED_16MHZ  = BCM2835_SPI_CLOCK_DIVIDER_16
BCM2835_SPI_SPEED_8MHZ   = BCM2835_SPI_CLOCK_DIVIDER_32
BCM2835_SPI_SPEED_4MHZ   = BCM2835_SPI_CLOCK_DIVIDER_64
BCM2835_SPI_SPEED_2MHZ   = BCM2835_SPI_CLOCK_DIVIDER_128
BCM2835_SPI_SPEED_1MHZ   = BCM2835_SPI_CLOCK_DIVIDER_256
BCM2835_SPI_SPEED_512KHZ = BCM2835_SPI_CLOCK_DIVIDER_512
BCM2835_SPI_SPEED_256KHZ = BCM2835_SPI_CLOCK_DIVIDER_1024
BCM2835_SPI_SPEED_128KHZ = BCM2835_SPI_CLOCK_DIVIDER_2048
BCM2835_SPI_SPEED_64KHZ  = BCM2835_SPI_CLOCK_DIVIDER_4096
BCM2835_SPI_SPEED_32KHZ  = BCM2835_SPI_CLOCK_DIVIDER_8192
BCM2835_SPI_SPEED_16KHZ  = BCM2835_SPI_CLOCK_DIVIDER_16384
BCM2835_SPI_SPEED_8KHZ   = BCM2835_SPI_CLOCK_DIVIDER_32768

BCM2835_BSC_C     = 0x0000 # BSC Master Control
BCM2835_BSC_S     = 0x0004 # BSC Master Status
BCM2835_BSC_DLEN  = 0x0008 # BSC Master Data Length
BCM2835_BSC_A     = 0x000c # BSC Master Slave Address
BCM2835_BSC_FIFO  = 0x0010 # BSC Master Data FIFO
BCM2835_BSC_DIV   = 0x0014 # BSC Master Clock Divider
BCM2835_BSC_DEL   = 0x0018 # BSC Master Data Delay
BCM2835_BSC_CLKT  = 0x001c # BSC Master Clock Stretch Timeout

BCM2835_BSC_C_I2CEN   = 0x00008000 # I2C Enable, 0 = disabled, 1 = enabled
BCM2835_BSC_C_INTR    = 0x00000400 # Interrupt on RX
BCM2835_BSC_C_INTT    = 0x00000200 # Interrupt on TX
BCM2835_BSC_C_INTD    = 0x00000100 # Interrupt on DONE
BCM2835_BSC_C_ST      = 0x00000080 # Start transfer, 1 = Start a new transfer
BCM2835_BSC_C_CLEAR_1 = 0x00000020 # Clear FIFO Clear
BCM2835_BSC_C_CLEAR_2 = 0x00000010 # Clear FIFO Clear
BCM2835_BSC_C_READ    = 0x00000001 # Read transfer

BCM2835_BSC_S_CLKT = 0x00000200 # Clock stretch timeout
BCM2835_BSC_S_ERR  = 0x00000100 # ACK error
BCM2835_BSC_S_RXF  = 0x00000080 # RXF FIFO full, 0 = FIFO is not full, 1 = FIFO is full
BCM2835_BSC_S_TXE  = 0x00000040 # TXE FIFO full, 0 = FIFO is not full, 1 = FIFO is full
BCM2835_BSC_S_RXD  = 0x00000020 # RXD FIFO contains data
BCM2835_BSC_S_TXD  = 0x00000010 # TXD FIFO can accept data
BCM2835_BSC_S_RXR  = 0x00000008 # RXR FIFO needs reading (full)
BCM2835_BSC_S_TXW  = 0x00000004 # TXW FIFO needs writing (full)
BCM2835_BSC_S_DONE = 0x00000002 # Transfer DONE
BCM2835_BSC_S_TA   = 0x00000001 # Transfer Active

BCM2835_BSC_FIFO_SIZE  = c_int(16) # BSC FIFO size

BCM2835_I2C_CLOCK_DIVIDER_2500 = c_int(2500)  # 2500 = 10us = 100 kHz
BCM2835_I2C_CLOCK_DIVIDER_626  = c_int(626)   # 622 = 2.504us = 399.3610 kHz
BCM2835_I2C_CLOCK_DIVIDER_150  = c_int(150)   # 150 = 60ns = 1.666 MHz (default at reset)
BCM2835_I2C_CLOCK_DIVIDER_148  = c_int(148)   # 148 = 59ns = 1.689 MHz

BCM2835_I2C_REASON_OK   	  = 0x00  # Success
BCM2835_I2C_REASON_ERROR_NACK = 0x01  # Received a NACK
BCM2835_I2C_REASON_ERROR_CLKT = 0x02  # Received Clock Stretch Timeout
BCM2835_I2C_REASON_ERROR_DATA = 0x04  # Not all data is sent / received

BCM2835_ST_CS  = 0x0000 # System Timer Control/Status
BCM2835_ST_CLO = 0x0004 # System Timer Counter Lower 32 bits
BCM2835_ST_CHI = 0x0008 # System Timer Counter Upper 32 bits

BCM2835_PWM_CONTROL = c_int(0)
BCM2835_PWM_STATUS  = c_int(1)
BCM2835_PWM_DMAC    = c_int(2)
BCM2835_PWM0_RANGE  = c_int(4)
BCM2835_PWM0_DATA   = c_int(5)
BCM2835_PWM_FIF1    = c_int(6)
BCM2835_PWM1_RANGE  = c_int(8)
BCM2835_PWM1_DATA   = c_int(9)

BCM2835_PWMCLK_CNTL = c_int(40)
BCM2835_PWMCLK_DIV  = c_int(41)
BCM2835_PWM_PASSWRD = (0x5A << 24)  # Password to enable setting PWM clock

BCM2835_PWM1_MS_MODE   = 0x8000  # Run in Mark/Space mode
BCM2835_PWM1_USEFIFO   = 0x2000  # Data from FIFO
BCM2835_PWM1_REVPOLAR  = 0x1000  # Reverse polarity
BCM2835_PWM1_OFFSTATE  = 0x0800  # Ouput Off state
BCM2835_PWM1_REPEATFF  = 0x0400  # Repeat last value if FIFO empty
BCM2835_PWM1_SERIAL    = 0x0200  # Run in serial mode
BCM2835_PWM1_ENABLE    = 0x0100  # Channel Enable

BCM2835_PWM0_MS_MODE   = 0x0080  # Run in Mark/Space mode
BCM2835_PWM_CLEAR_FIFO = 0x0040  # Clear FIFO
BCM2835_PWM0_USEFIFO   = 0x0020  # Data from FIFO
BCM2835_PWM0_REVPOLAR  = 0x0010  # Reverse polarity
BCM2835_PWM0_OFFSTATE  = 0x0008  # Ouput Off state
BCM2835_PWM0_REPEATFF  = 0x0004  # Repeat last value if FIFO empty
BCM2835_PWM0_SERIAL    = 0x0002  # Run in serial mode
BCM2835_PWM0_ENABLE    = 0x0001  # Channel Enable

BCM2835_PWM_CLOCK_DIVIDER_32768 = c_int(32768)  # 32768 = 585Hz
BCM2835_PWM_CLOCK_DIVIDER_16384 = c_int(16384)  # 16384 = 1171.8Hz
BCM2835_PWM_CLOCK_DIVIDER_8192  = c_int(8192)   # 8192 = 2.34375kHz
BCM2835_PWM_CLOCK_DIVIDER_4096  = c_int(4096)   # 4096 = 4.6875kHz
BCM2835_PWM_CLOCK_DIVIDER_2048  = c_int(2048)   # 2048 = 9.375kHz
BCM2835_PWM_CLOCK_DIVIDER_1024  = c_int(1024)   # 1024 = 18.75kHz
BCM2835_PWM_CLOCK_DIVIDER_512   = c_int(512)    # 512 = 37.5kHz
BCM2835_PWM_CLOCK_DIVIDER_256   = c_int(256)    # 256 = 75kHz
BCM2835_PWM_CLOCK_DIVIDER_128   = c_int(128)    # 128 = 150kHz
BCM2835_PWM_CLOCK_DIVIDER_64    = c_int(64)     # 64 = 300kHz
BCM2835_PWM_CLOCK_DIVIDER_32    = c_int(32)     # 32 = 600.0kHz
BCM2835_PWM_CLOCK_DIVIDER_16    = c_int(16)     # 16 = 1.2MHz
BCM2835_PWM_CLOCK_DIVIDER_8     = c_int(8)      # 8 = 2.4MHz
BCM2835_PWM_CLOCK_DIVIDER_4     = c_int(4)      # 4 = 4.8MHz
BCM2835_PWM_CLOCK_DIVIDER_2     = c_int(2)      # 2 = 9.6MHz, fastest you can get
BCM2835_PWM_CLOCK_DIVIDER_1     = c_int(1)      # 1 = 4.6875kHz, same as divider 4096