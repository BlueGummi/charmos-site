+++
title = "init"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/buddy/init.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c)

- [`pfn_usable_from_memmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L13) — `static bool pfn_usable_from_memmap(uint64_t pfn)`
- [`is_block_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L31) — `static bool is_block_free(uint64_t pfn`,`uint64_t order)`
- [`order_base_2()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L48) — `static inline int order_base_2(uint64_t x)`
- [`buddy_add_to_free_area()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L52) — `void buddy_add_to_free_area(`[`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)` *page`,[`struct free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L12)` *area)`
- [`buddy_remove_from_free_area()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L59) — [`struct page *`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)`buddy_remove_from_free_area(`[`struct free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L12)` *area)`
- [`buddy_add_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L70) — `void buddy_add_entry(`[`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)` *page_array`,[`struct limine_memmap_entry`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L473)` *entry`,[`struct free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L12)` *farea)`
- [`fast_memset()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L111) — `static inline void * fast_memset(void *dst`,`int c`,`size_t n)`
- [`mid_init_buddy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L137) — `static void mid_init_buddy(size_t pages_needed)`
- [`buddy_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/init.c#L168) — `void buddy_init(void)`



+++
title = "internal"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/buddy/internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h)

### struct [`free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L12)

| Member Type | Member Name |
|-------------|-------------|
| [`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38) | [`*next`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L13) |
| `uint64_t` | [`nr_free`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L14) |


- [`page_pfn_allocated_in_boot_bitmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L19) — `static inline bool page_pfn_allocated_in_boot_bitmap(uint64_t pfn)`
- [`page_pfn_available()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L23) — `static inline bool page_pfn_available(uint64_t pfn)`



+++
title = "core"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/buddy/core.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/core.c)

- [`buddy_alloc_pages()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/core.c#L17) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`buddy_alloc_pages(`[`struct free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L12)` *free_area`,`size_t count)`
- [`buddy_free_pages()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/core.c#L70) — `void buddy_free_pages(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr`,`size_t count`,[`struct free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L12)` *free_area`,`size_t total_pages)`
- [`buddy_free_pages_global()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/core.c#L118) — `void buddy_free_pages_global(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr`,`uint64_t count)`
- [`buddy_alloc_pages_global()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/core.c#L124) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`buddy_alloc_pages_global(size_t count`,[`enum alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)` f)`



