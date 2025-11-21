+++
title = "noop_bio"
author = "Unknown"
status = "unknown"
+++

# [kernel/block/noop_bio.c](https://github.com/bluegummi/charmos/blob/main/kernel/block/noop_bio.c)

- [`noop_should_coalesce()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/noop_bio.c#L3) — `bool noop_should_coalesce(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *a`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *b)`
- [`noop_do_coalesce()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/noop_bio.c#L10) — `void noop_do_coalesce(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *into`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *from)`
- [`noop_reorder()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/noop_bio.c#L15) — `void noop_reorder(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`

