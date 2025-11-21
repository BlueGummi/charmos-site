+++
title = "bitmap"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/bitmap.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/bitmap.c)

- [`bitmap_alloc_page()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/bitmap.c#L14) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`bitmap_alloc_page()`
- [`bitmap_alloc_pages()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/bitmap.c#L18) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`bitmap_alloc_pages(uint64_t count`,[`enum alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)` flags)`
- [`bitmap_free_pages()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/bitmap.c#L73) — `void bitmap_free_pages(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr`,`uint64_t count)`

