# Deferred Receipt

`nc deferred-receipt.wolvctf-2026.kctf.cloud 1337`

## Bug

An amendment stores a pointer into a public receipt slot. Cancelling the receipt frees the slot. A new sealed receipt reuses that slot. Processing the queue writes through the old pointer and sets the approval magic on the new receipt.

## Exploit

Create public receipt 1001 and queue amendment `4c414553`. Cancel 1001. Create sealed receipt 1002 so it reuses slot 0. Process the queue, then export 1002. The stale write approves it and the export prints the flag.

## Flag

`wctf{deferred_receipt_2b6f4058047e5aeb8e1a75aa}`
