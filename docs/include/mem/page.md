# [include/mem/page.h](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h)

<!-- Auto-generated from page.h, do not edit manually -->

### struct [`page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`phys_usable`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L39) |
| `uint8_t` | [`is_free`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L40) |
| `uint8_t` | [`order`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L41) |
| [`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38) | [`*next`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L42) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L43) |


### struct [`page_table`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L47)

| Member Type | Member Name |
|-------------|-------------|
| [`pte_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L16) | [`entries[512]`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L48) |


- [`page_pfn_free()`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L52) — `static inline bool page_pfn_free(uint64_t pfn)`
- [`page_for_pfn()`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L60) — `static inline`[`struct page *`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)`page_for_pfn(uint64_t pfn)`
- [`page_get_pfn()`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L67) — `static inline uint64_t page_get_pfn(`[`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)` *bp)`
- [`page_pfn_phys_usable()`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L71) — `static inline bool page_pfn_phys_usable(uint64_t pfn)`

