# [kernel/mem/domain/init.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c)

<!-- Auto-generated from init.c, do not edit manually -->

- [`compare_zonelist_entries()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L14) — `static int compare_zonelist_entries(void *a`,`void *b)`
- [`domain_build_zonelist()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L27) — `static void domain_build_zonelist(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *dom)`
- [`domain_buddy_track_pages()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L44) — `void domain_buddy_track_pages(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *dom)`
- [`remove_block_from_global()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L60) — `static void remove_block_from_global(size_t start_pfn`,`int order)`
- [`buddy_add_block_to_global()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L76) — `static void buddy_add_block_to_global(size_t start_pfn`,`int order)`
- [`domain_buddy_split_for_domain()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L86) — `static void domain_buddy_split_for_domain(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *dom`,`size_t start_pfn`,`int order`,`size_t domain_start`,`size_t domain_end)`
- [`domain_buddy_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L139) — `static void domain_buddy_init(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *dom)`
- [`alloc_up()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L169) — `static void * alloc_up(size_t size)`
- [`domain_structs_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L173) — `static void domain_structs_init(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *dom`,`size_t arena_capacity`,`size_t fq_capacity`,[`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)` *core_domain)`
- [`compute_arena_max()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L224) — `static size_t compute_arena_max(size_t domain_total_pages)`
- [`compute_freequeue_max()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L232) — `static size_t compute_freequeue_max(size_t system_total_pages)`
- [`domain_init_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L240) — `static void domain_init_worker(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain)`
- [`link_domain_cores_to_buddy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L256) — `static void link_domain_cores_to_buddy(`[`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)` *cd`,[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *bd)`
- [`pages_to_bytes()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L263) — `static inline uint64_t pages_to_bytes(size_t pages)`
- [`late_init_from_numa()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L267) — `static void late_init_from_numa(size_t domain_count)`
- [`late_init_non_numa()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L286) — `static void late_init_non_numa(size_t domain_count)`
- [`domain_buddies_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L317) — `void domain_buddies_init(void)`
- [`domain_buddy_dump()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L345) — `void domain_buddy_dump(void)`
- [`move_buddy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L357) — `static void move_buddy(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *buddy)`
- [`domain_buddy_movealloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c#L370) — `static void domain_buddy_movealloc(void *a`,`void *b)`

