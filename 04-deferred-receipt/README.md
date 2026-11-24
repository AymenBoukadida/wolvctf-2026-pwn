# Deferred Receipt

`nc deferred-receipt.wolvctf-2026.kctf.cloud 1337`

## Bug

Queuing an amendment stores a pointer to a public receipt's approval-magic field. Cancelling frees the slot; creating a sealed receipt reuses it. Processing the queue then writes through the stale pointer, approving the sealed receipt.

The magic value is `SEAL` = `0x4c414553`.

## Exploit

1. Create public receipt → ID 1001.
2. Queue amendment `4c414553` on 1001.
3. Cancel 1001.
4. Create sealed receipt → ID 1002, reuses slot 0.
5. Process queue.
6. Export 1002.

## Flag

`wctf{deferred_receipt_2b6f4058047e5aeb8e1a75aa}`
