# Linker Lite

`nc linker-lite.wolvctf-2026.kctf.cloud 1337`

## Bug

`load_plugin()` reads `0x100` bytes into a 64-byte stack buffer, so the saved return address can be overwritten. The binary has no win function and no address leak. Partial RELRO leaves the linker tables writable, so `ret2dlresolve` still works.

## Exploit

First overflow into a ROP chain that calls `read(0, 0x404500, 0x100)`. Use it to write a fake symbol, fake relocation, and the string `cat /flag` into bss. Then jump to PLT0 with a forged relocation index. The dynamic linker resolves the fake entry and calls `system("cat /flag")`. One extra `ret` is needed before `read@plt`.

## Flag

`wctf{n0_le4k_n0_pr0blem_ret2dlresolve}`
