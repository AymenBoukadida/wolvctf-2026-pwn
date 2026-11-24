# No Open Door

`nc no-open-door.wolvctf-2026.kctf.cloud 1337`

## Protections

Static binary, NX, no PIE. Canary present but not used in the vulnerable function.

## Bug

`main()` reads `0x200` bytes into a 64-byte buffer. Offset to RIP: `0x48`.

`install_filter()` installs a seccomp BPF whitelist: `read`, `write`, `mmap`, `exit_group`, `brk`, `rt_sigreturn`, `close`, `lseek`, and syscall **437**. The author meant `openat` but 437 is `openat2` — that is the missed syscall.

`g10` provides `pop r10; ret`, needed for `openat2`'s fourth argument (`sizeof(struct open_how)`).

## Exploit

ROP chain: `read(0, bss, ...)` for the path and `open_how`, then `openat2(AT_FDCWD, "/flag", &how, 24)`, `xchg rdi,rax` to move the fd, then `read` and `write`.

Use the clean `syscall; ret` at `0x414b36`; the one at `0x401ee4` jumps back and issues an extra syscall.

## Flag

`wctf{y0u_f0rg0t_t0_cl0se_0penat2}`
