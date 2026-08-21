from machine import UART, Pin
import time

_START = 0x7E
_VERSION = 0xFF
_LEN = 0x06
_END = 0xEF
_FEEDBACK_NONE = 0x00

_CMD_NEXT = 0x01
_CMD_PREV = 0x02
_CMD_PLAY_TRACK = 0x03
_CMD_VOLUME_UP = 0x04
_CMD_VOLUME_DOWN = 0x05
_CMD_VOLUME = 0x06
_CMD_PLAYBACK_SOURCE = 0x09
_CMD_PAUSE = 0x0E
_CMD_PLAY = 0x0D
_CMD_RESET = 0x0C

_SOURCE_SD = 0x02


class DFPlayer:
    def __init__(self, uart_id, tx, rx, busy_pin=None):
        self.uart = UART(uart_id, baudrate=9600, tx=Pin(tx), rx=Pin(rx))
        self.busy = Pin(busy_pin, Pin.IN, Pin.PULL_UP) if busy_pin is not None else None

    def _send(self, cmd, param1=0, param2=0):
        checksum = -(_VERSION + _LEN + cmd + _FEEDBACK_NONE + param1 + param2) & 0xFFFF
        frame = bytes([
            _START, _VERSION, _LEN, cmd, _FEEDBACK_NONE,
            param1, param2,
            (checksum >> 8) & 0xFF, checksum & 0xFF,
            _END,
        ])
        self.uart.write(frame)

    def init(self):
        self._send(_CMD_PLAYBACK_SOURCE, 0, _SOURCE_SD)
        time.sleep_ms(200)

    def play_track(self, track_num):
        self._send(_CMD_PLAY_TRACK, 0, track_num)

    def play(self):
        self._send(_CMD_PLAY)

    def pause(self):
        self._send(_CMD_PAUSE)

    def next(self):
        self._send(_CMD_NEXT)

    def previous(self):
        self._send(_CMD_PREV)

    def volume(self, level):
        self._send(_CMD_VOLUME, 0, max(0, min(30, level)))

    def volume_up(self):
        self._send(_CMD_VOLUME_UP)

    def volume_down(self):
        self._send(_CMD_VOLUME_DOWN)

    def reset(self):
        self._send(_CMD_RESET)

    def is_playing(self):
        # DFPlayer BUSY line is active-low: low while a track is playing.
        if self.busy is None:
            return None
        return self.busy.value() == 0
