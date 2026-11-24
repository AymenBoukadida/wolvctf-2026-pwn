from pwn import *

context.log_level = 'error'

HOST, PORT = 'deferred-receipt.wolvctf-2026.kctf.cloud', 1337

io = remote(HOST, PORT)

def menu(choice, prompts=()):
    io.recvuntil(b'Choice: ')
    io.sendline(str(choice).encode())
    for prompt, answer in prompts:
        io.recvuntil(prompt)
        io.sendline(answer)

menu(1)
menu(2, [(b'Public receipt ID: ', b'1001'), (b'Amendment (hex): ', b'4c414553')])
menu(3, [(b'Public receipt ID: ', b'1001')])
menu(4)
menu(5)
menu(6, [(b'Sealed receipt ID: ', b'1002')])

print(io.recvall(timeout=5).decode())
