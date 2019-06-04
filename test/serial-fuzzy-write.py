#!/usr/bin/env python

import serial
import random
import time

#random.randint(0, 255)

# Testing with `socat`
s = serial.Serial('/dev/pts/8', 31250, timeout=0.1)

# noteon = b'\x80\x18\x00'
# noteoff = b'\x90\x18\x64'
# polyphonickeypressure = None
# controlchange = None
# programchange = None

noteon = bytes([
    int('10000000', 2),
    int('00000001', 2),
    int('00000001', 2)
])

noteoff = bytes([
    int('10010000', 2),
    int('00000001', 2),
    int('00000001', 2)
])

poly = bytes([
    int('10100000', 2),
    int('00000001', 2),
    int('00000001', 2)
])

controlchange = bytes([
    int('10110000', 2),
    int('00000001', 2),
    int('00000001', 2)
])

programchange = bytes([
    int('11000000', 2),
    int('00000001', 2)
])

channelpressure = bytes([
    int('11010000', 2),
    int('00000001', 2)
])

pitchbend = bytes([
    int('11100000', 2),
    int('00000001', 2),
    int('00000001', 2)
])

# same as control change? Yes, special controller numbers.
channelmodemessage = bytes([
    int('10110000', 2),
    120,
    0
])

sysex_begin = bytes([
    int('11110000', 2),
    int('01111111', 2),
    int('01111111', 2)
])
sysex_end = bytes([
    int('11110111', 2)
])

timecode_quarter_frame = bytes([
    int('11110001', 2),
    int('01110001', 2)
])

song_position_pointer = bytes([
    int('11110010', 2),
    int('01110010', 2),
    int('01110010', 2)
])

song_select = bytes([
    int('11110011', 2),
    int('01110010', 2)
])

time_clock = bytes([
    int('11111000', 2)
])

time_start = bytes([
    int('11111010', 2)
])

time_continue = bytes([
    int('11111011', 2)
])

time_stop = bytes([
    int('11111100', 2)
])

active_sensing = bytes([
    int('11111110', 2)
])

reset = bytes([
    int('11111111', 2)
])

# s.write(noteon)
# s.write(noteoff)
# s.write(poly)
# s.write(controlchange)

# s.write(programchange)
# s.write(channelpressure)
# s.write(pitchbend)
# s.write(channelmodemessage)

# s.write(timecode_quarter_frame)
# s.write(song_position_pointer)
# s.write(song_select)
# s.write(time_clock)

# s.write(time_start)
# s.write(time_continue)
# s.write(time_stop)
# s.write(active_sensing)

# s.write(reset)

# s.write(sysex_begin)
# s.write(sysex_end)

bootmsg = [ 0xf0, 0x7f, 0x7f, 0x4, 0x1, 0x7f, 0x7f, 0xf7, 0xb0, 0x0,
            0x0, 0xb0, 0x20, 0x0, 0xc0, 0x00, 0x0b0, 0x4d, 0x40,
            0xb0, 0x4c, 0x40, 0xb0, 0x46 , 0x40, 0xb0, 0xa, 0x40,
            0xb0, 0x49, 0x40, 0xb0, 0x4b, 0x40, 0xb0, 0x48 , 0x40,
            0xb0, 0x5b, 0xd, 0xb0, 0x5e, 0x0, 0xb0, 0x4a, 0x40, 0xb0,
            0xa , 0x40, 0xb0, 0x65, 0x0, 0xb0, 0x64, 0x1, 0xb0, 0x6,
            0x40, 0xb0, 0x26 , 0x0, 0xb0, 0x65, 0x7f, 0xb0, 0x64,
            0x7f, 0xb0, 0x7, 0x7f, 0xb0, 0x65 , 0x0, 0xb0, 0x64, 0x0,
            0xb0, 0x6, 0x2, 0xb0, 0x65, 0x7f, 0xb0, 0x64 , 0x7f, 0xb0,
            0x5c, 0x0, 0xb0, 0x7, 0x7f, 0xb0, 0x1, 0x19, 0xb0, 0xb ,
            0x7f, 0x90, 0x47, 0x6a, 0x90, 0x48, 0x5a, 0x90, 0x47, 0x0,
            0x90, 0x46 , 0x66, 0x90, 0x48, 0x0, 0x90, 0x44, 0x62,
            0x90, 0x46, 0x0, 0x90, 0x46 , 0x52, 0x90, 0x44, 0x0, 0x90,
            0x48, 0x44, 0x90, 0x44, 0x66, 0x90, 0x48 , 0x0, 0x90,
            0x46, 0x0, 0x90, 0x41, 0x6a, 0x90, 0x44, 0x0, 0x90, 0x41 ,
            0x0, 0x90, 0x40, 0x6b, 0x90, 0x41, 0x44, 0x90, 0x40, 0x0,
            0x90, 0x3f , 0x64, 0x90, 0x41, 0x0, 0x90, 0x3c, 0x59,
            0x90, 0x3f, 0x0, 0x90, 0x3c , 0x0, 0x90, 0x3f, 0x61, 0x90,
            0x3c, 0x63, 0x90, 0x3f, 0x0, 0x90, 0x3c , 0x0, 0x90, 0x3a,
            0x66, 0x90, 0x38, 0x62, 0x90, 0x3a, 0x0, 0x90, 0x35 ,
            0x60, 0x90, 0x38, 0x0, 0x90, 0x33, 0x69, 0x90, 0x35, 0x0,
            0x90, 0x33 , 0x0, 0x90, 0x30, 0x57, 0x90, 0x33, 0x4c,
            0x90, 0x30, 0x0, 0x90, 0x33 , 0x0, 0x90, 0x34, 0x61, 0x90,
            0x35, 0x43, 0x90, 0x34, 0x0, 0x90, 0x35 , 0x0, 0x90, 0x39,
            0x31, 0x90, 0x39, 0x0, 0x90, 0x3c, 0x5f, 0x90, 0x3f ,
            0x60, 0x90, 0x3c, 0x0, 0x90, 0x3f, 0x0, 0x90, 0x41, 0x46,
            0x90, 0x40 , 0x3a, 0x90, 0x40, 0x0, 0x90, 0x41, 0x0, 0x90,
            0x44, 0x69, 0x90, 0x44, 0x0, 0x90, 0x41, 0x55, 0x90, 0x44,
            0x6d, 0x90, 0x41, 0x0, 0x90, 0x46 , 0x52, 0x90, 0x44, 0x0,
            0x90, 0x46, 0x0, 0x90, 0x48, 0x46, 0x90, 0x48 , 0x0, 0x90,
            0x4b, 0x64, 0x90, 0x4b, 0x0, 0x90, 0x4c, 0x57, 0x90, 0x4d
            , 0x55, 0x90, 0x4c, 0x0, 0x90, 0x4b, 0x6c, 0x90, 0x4d,
            0x0, 0x90, 0x4b , 0x0, 0x90, 0x48, 0x54, 0x90, 0x48, 0x0,
            0x90, 0x4b, 0x67, 0x90, 0x4b , 0x0, 0x90, 0x48, 0x5e,
            0x90, 0x48, 0x0, 0x90, 0x46, 0x5d, 0x90, 0x44 , 0x60,
            0x90, 0x46, 0x0, 0x90, 0x44, 0x0, 0x90, 0x46, 0x46, 0x90,
            0x44 , 0x5a, 0x90, 0x46, 0x0, 0x90, 0x41, 0x5d, 0x90,
            0x44, 0x0, 0x90, 0x41 , 0x0 ]

events = [
    int('11110111', 2),
    int('11110110', 2),
    int('11110000', 2)
]

print("Bootmsg len {0}".format(len(bootmsg)))
s.write(bytes(bootmsg))

# sleeptime = 32/48000
# for k in range(1, 100000000):
#     values = random.sample(list(range(0, 256)), 1)
    
#     time.sleep(sleeptime)
#     print("{0}, {1}".format(bytes(values), sleeptime))
#     s.write(bytes(values))
#     if sleeptime > 2/48000:
#         sleeptime /= 2
