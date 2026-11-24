# Linker Lite

`nc linker-lite.wolvctf-2026.kctf.cloud 1337`

## Protections

Partial RELRO, no canary, NX, no PIE. No win function and no address leak.

## Bug

`load_plugin()` reads `0x100` bytes into a 64-byte stack buffer. Offset to RIP: `0x48`.

Because RELRO is partial, `ret2dlresolve` works: forge `Elf64_Sym` / `Elf64_Rela` and a command string in bss, then jump to PLT0 with a forged relocation index so the linker resolves and calls `system`.

The `g` function at `0x401223` provides `pop rdi; pop rsi; pop rdx; ret`, used to `read()` the fake structures into `0x404500`.

## Exploit

1. Overflow with a ROP chain: `read(0, 0x404500, 0x100)`, then ret2dlresolve for `system`.
2. Send the forged linker payload as the second stage.

An extra `ret` is needed before `read@plt`, but not before PLT0.

## Flag

`wctf{n0_le4k_n0_pr0blem_ret2dlresolve}`
