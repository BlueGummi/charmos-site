# [kernel/mem/pmm.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c)

<!-- Auto-generated from pmm.c, do not edit manually -->

### type alias
[`(*alloc_fn)`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L14) : `paddr_t (size_t pages, enum alloc_flags f)`
### type alias
[`(*free_fn)`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L16) : `void (paddr_t addr, size_t pages)`
- [`pmm_early_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L21) — `__no_sanitize_address pmm_early_init(`[`struct limine_memmap_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L485)` m)`
- [`pmm_mid_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L66) — `__no_sanitize_address pmm_mid_init()`
- [`pmm_late_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L72) — `void pmm_late_init(void)`
- [`pmm_alloc_page()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L78) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`pmm_alloc_page(`[`enum alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)` f)`
- [`pmm_free_page()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L82) — `void pmm_free_page(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr)`
- [`pmm_alloc_pages()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L86) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`pmm_alloc_pages(uint64_t count`,[`enum alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)` f)`
- [`pmm_free_pages()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L90) — `void pmm_free_pages(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr`,`uint64_t count)`
- [`pmm_get_usable_ram()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/pmm.c#L94) — `uint64_t pmm_get_usable_ram(void)`

