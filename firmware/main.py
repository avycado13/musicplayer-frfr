from machine import Pin
import time

import pins
from dfplayer import DFPlayer

player = DFPlayer(
    0, tx=pins.DFPLAYER_TX, rx=pins.DFPLAYER_RX, busy_pin=pins.DFPLAYER_BUSY
)

play_btn = Pin(pins.PLAY, Pin.IN, Pin.PULL_UP)
next_btn = Pin(pins.NEXT, Pin.IN, Pin.PULL_UP)
back_btn = Pin(pins.BACK, Pin.IN, Pin.PULL_UP)
encoder_switch = Pin(pins.ENCODER_SWITCH, Pin.IN, Pin.PULL_UP)
encoder_a = Pin(pins.ENCODER_A, Pin.IN, Pin.PULL_UP)
encoder_b = Pin(pins.ENCODER_B, Pin.IN, Pin.PULL_UP)

_DEBOUNCE_MS = 200
_volume = 15
_playing = False

_last_press = {}


def _pressed(pin, name):
    if pin.value() != 0:
        return False
    now = time.ticks_ms()
    last = _last_press.get(name, 0)
    if time.ticks_diff(now, last) < _DEBOUNCE_MS:
        return False
    _last_press[name] = now
    return True


def _on_encoder_turn(pin):
    global _volume
    if encoder_a.value() == encoder_b.value():
        _volume = min(30, _volume + 1)
    else:
        _volume = max(0, _volume - 1)
    player.volume(_volume)


def main():
    global _playing

    player.init()
    player.volume(_volume)

    encoder_a.irq(trigger=Pin.IRQ_FALLING, handler=_on_encoder_turn)

    while True:
        if _pressed(play_btn, "play"):
            if _playing:
                player.pause()
            else:
                player.play()
            _playing = not _playing

        if _pressed(next_btn, "next"):
            player.next()
            _playing = True

        if _pressed(back_btn, "back"):
            player.previous()
            _playing = True

        if _pressed(encoder_switch, "encoder_switch"):
            if _volume > 0:
                player.volume(0)
            else:
                player.volume(_volume)

        time.sleep_ms(20)


if __name__ == "__main__":
    main()
