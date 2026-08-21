# GPIO assignments for the XIAO RP2350, derived from the schematic net labels
# in pcb/musicplayer-frfr.kicad_sch and the XIAO RP2350 pin multiplexing table:
# https://wiki.seeedstudio.com/XIAO_RP2350_Pin_Multiplexing/
#
# D0-D10 use the same GPIO mapping as XIAO RP2040. D11-D14 are the extra
# castellated pads on the back of the SMD module (verify against your build
# before trusting these if anything doesn't respond).

PLAY = 26             # D0  - PLAY button
NEXT = 27             # D1  - NEXT button
BACK = 28             # D2  - BACK button

SDA = 6               # D4  - unused for now, broken out for future I2C
SCL = 7               # D5  - unused for now, broken out for future I2C

DFPLAYER_RX = 0       # D6  - XIAO RX  <- DFPlayer TX
DFPLAYER_TX = 1       # D7  - XIAO TX  -> DFPlayer RX

ENCODER_SWITCH = 21   # D11 - rotary encoder push button
DFPLAYER_BUSY = 20    # D12 - DFPlayer BUSY line (low while playing)
ENCODER_A = 17        # D13 - rotary encoder A
ENCODER_B = 16        # D14 - rotary encoder B
