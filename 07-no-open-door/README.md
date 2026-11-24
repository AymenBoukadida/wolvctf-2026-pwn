# No Open Door

`nc no-open-door.wolvctf-2026.kctf.cloud 1337`

## Bug

`main()` reads `0x200` bytes into a 64-byte stack buffer, so the saved return address can be overwritten. The seccomp filter allows syscall 437. On x86-64 that is `openat2`, not `openat`. This is the missed syscall.

## Exploit

Build a ROP chain that reads `/flag` and an `open_how` structure into bss. Call `openat2(AT_FDCWD, "/flag", &how, 24)`. Move the returned fd into `rdi` with `xchg rdi, rax`, then use `read` and `write` to print the file. Use the clean `syscall; ret` at `0x414b36`. The one at `0x401ee4` issues an extra syscall.

## Flag

`wctf{y0u_f0rg0t_t0_cl0se_0penat2}`
