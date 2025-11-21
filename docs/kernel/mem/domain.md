+++
title = "free_queue"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/domain/free_queue.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free_queue.c)

- [`domain_free_queue_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free_queue.c#L10) — `bool domain_free_queue_enqueue(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr`,`size_t pages)`
- [`domain_free_queue_dequeue()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free_queue.c#L30) — `bool domain_free_queue_dequeue(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` *addr_out`,`size_t *pages_out)`



+++
title = "free"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/domain/free.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c)

- [`try_push_page_onto_arena()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L6) — `static bool try_push_page_onto_arena(`[`struct domain_arena`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)` *arena`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` address)`
- [`try_push_page_onto_domain_arenas()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L12) — `static bool try_push_page_onto_domain_arenas(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` address)`
- [`free_from_local_domain_buddy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L28) — `static void free_from_local_domain_buddy(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *local`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` address`,`size_t page_count)`
- [`free_from_remote_domain_buddy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L55) — `static void free_from_remote_domain_buddy(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *remote`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` address`,`size_t page_count)`
- [`domain_first_arena()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L71) — `static inline`[`struct domain_arena *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)`domain_first_arena(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain)`
- [`get_next_domain_arena()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L76) — `static`[`struct domain_arena *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)`get_next_domain_arena(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain`,`size_t *current_arena_idx)`
- [`find_non_full_arena()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L85) — `static`[`struct domain_arena *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)`find_non_full_arena(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain`,`size_t *current_arena_idx)`
- [`compute_min_elements_to_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L98) — `static size_t compute_min_elements_to_free(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain`,[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *queue)`
- [`flush_free_queue_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L115) — `static void flush_free_queue_internal(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain`,[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *queue`,`size_t minimum_to_free)`
- [`domain_flush_free_queue()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L166) — `void domain_flush_free_queue(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain`,[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *queue)`
- [`domain_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L179) — `void domain_free(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` address`,`size_t page_count)`
- [`domain_flush_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L200) — `void domain_flush_thread()`
- [`domain_enqueue_flush_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free.c#L212) — `void domain_enqueue_flush_worker(`[`struct domain_flush_worker`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L72)` *worker)`



+++
title = "alloc"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/domain/alloc.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c)

- [`domain_free_queue_available()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L8) — `static inline bool domain_free_queue_available(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain)`
- [`domain_freequeue_flush_quota()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L13) — `static inline size_t domain_freequeue_flush_quota(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain)`
- [`flush_freequeue_into_local_arena()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L22) — `static void flush_freequeue_into_local_arena(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *domain`,[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,`size_t quota)`
- [`alloc_from_buddy_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L49) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`alloc_from_buddy_internal(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *this`,`size_t pages)`
- [`try_alloc_from_remote_arenas()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L67) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`try_alloc_from_remote_arenas(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *owner`,`size_t pages`,`bool remote)`
- [`alloc_from_remote_domain()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L85) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`alloc_from_remote_domain(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *remote`,`size_t pages)`
- [`try_alloc_from_free_queue()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L103) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`try_alloc_from_free_queue(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *this`,[`struct domain_arena`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)` *this_arena)`
- [`try_alloc_from_arenas()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L122) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`try_alloc_from_arenas(size_t pages)`
- [`do_alloc_interleaved_local()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L145) — `static inline`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`do_alloc_interleaved_local(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *local`,`size_t pages)`
- [`do_alloc_interleaved()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L154) — `static inline`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`do_alloc_interleaved(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *target`,[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *local`,`size_t pages)`
- [`alloc_interleaved()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L164) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`alloc_interleaved(size_t pages)`
- [`alloc_from_local_buddy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L189) — `static inline`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`alloc_from_local_buddy(size_t pages)`
- [`zonelist_alloc_fallback()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L194) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`zonelist_alloc_fallback(`[`struct domain_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L59)` *zl`,[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *local`,[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *best`,`size_t max_scan`,`size_t pages)`
- [`derive_max_scan_from_zonelist()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L215) — `static size_t derive_max_scan_from_zonelist(`[`struct domain_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L59)` *zl`,`uint16_t locality_degree)`
- [`domain_alloc_pick_best_domain()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L227) — [`struct domain *`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)`domain_alloc_pick_best_domain(`[`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)` *local`,`size_t pages`,`size_t max_scan`,`bool flexible_locality)`
- [`alloc_with_locality()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L259) — `static`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`alloc_with_locality(size_t pages`,`bool flexible_locality`,`uint16_t locality_degree)`
- [`domain_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L306) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`domain_alloc(size_t pages`,[`enum alloc_flags`](https://github.com/bluegummi/charmos/blob/main/include/mem/alloc.h#L56)` flags)`
- [`domain_alloc_from_domain()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L343) — [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)`domain_alloc_from_domain(`[`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)` *cd`,`size_t pages)`
- [`domain_for_addr()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/alloc.c#L351) — [`struct domain *`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9)`domain_for_addr(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr)`



+++
title = "arena"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/domain/arena.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/arena.c)

- [`domain_arena_push()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/arena.c#L10) — `bool domain_arena_push(`[`struct domain_arena`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)` *arena`,[`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)` *page)`
- [`domain_arena_pop()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/arena.c#L28) — [`struct page *`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)`domain_arena_pop(`[`struct domain_arena`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)` *arena)`



+++
title = "init"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/domain/init.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/init.c)

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



+++
title = "internal"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/domain/internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h)

### struct [`domain_arena`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)

| Member Type | Member Name |
|-------------|-------------|
| [`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38) | [`**pages`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L23) |
| `size_t` | [`head`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L24) |
| `size_t` | [`tail`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L25) |
| `size_t` | [`capacity`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L26) |
| `atomic_size_t` | [`num_pages`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L27) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L28) |


### struct [`domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)

| Member Type | Member Name |
|-------------|-------------|
| `struct { paddr_t addr; size_t pages; }` | [`*queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L32) |
| `size_t` | [`head`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L37) |
| `size_t` | [`tail`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L38) |
| `size_t` | [`capacity`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L39) |
| `atomic_size_t` | [`num_elements`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L40) |
| `atomic_bool` | [`free_in_progress`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L41) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L50) |


### struct [`domain_zonelist_entry`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L53)

| Member Type | Member Name |
|-------------|-------------|
| [`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80) | [`*domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L54) |
| `uint8_t` | [`distance`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L55) |
| `size_t` | [`free_pages`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L56) |


### struct [`domain_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L59)

| Member Type | Member Name |
|-------------|-------------|
| [`struct domain_zonelist_entry`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L53) | [`*entries`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L60) |
| `size_t` | [`count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L61) |


### struct [`domain_buddy_stats`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L64)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_size_t` | [`alloc_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L65) |
| `atomic_size_t` | [`free_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L66) |
| `atomic_size_t` | [`remote_alloc_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L67) |
| `atomic_size_t` | [`failed_alloc_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L68) |
| `atomic_size_t` | [`interleaved_alloc_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L69) |


### struct [`domain_flush_worker`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L72)

| Member Type | Member Name |
|-------------|-------------|
| [`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80) | [`*domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L73) |
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*thread`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L74) |
| [`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9) | [`sema`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L75) |
| `atomic_bool` | [`enqueued`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L76) |
| `bool` | [`stop`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L77) |


### struct [`domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)

| Member Type | Member Name |
|-------------|-------------|
| [`struct domain_buddy_stats`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L64) | [`stats`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L81) |
| [`struct domain_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L59) | [`zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L82) |
| [`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38) | [`*buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L84) |
| [`struct free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/buddy/internal.h#L12) | [`*free_area`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L85) |
| [`struct domain_arena`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22) | [`**arenas`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L87) |
| [`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15) | [`**cores`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L88) |
| `size_t` | [`core_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L89) |
| [`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31) | [`*free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L91) |
| [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12) | [`start`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L93) |
| [`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12) | [`end`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L94) |
| `size_t` | [`length`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L95) |
| `atomic_size_t` | [`pages_used`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L97) |
| `atomic_size_t` | [`total_pages`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L98) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L100) |
| [`struct domain_flush_worker`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L72) | [`worker`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L101) |


- [`domain_buddy_for_addr()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L131) — `static inline`[`struct domain_buddy *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)`domain_buddy_for_addr(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr)`
- [`domain_buddy_on_this_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L143) — `static inline`[`struct domain_buddy *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)`domain_buddy_on_this_core(void)`
- [`domain_arena_on_this_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L147) — `static inline`[`struct domain_arena *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L22)`domain_arena_on_this_core(void)`
- [`domain_free_queue_on_this_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L151) — `static inline`[`struct domain_free_queue *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)`domain_free_queue_on_this_core(void)`
- [`domain_rr_on_this_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L155) — `static inline size_t * domain_rr_on_this_core(void)`
- [`domain_stat_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L159) — `static inline void domain_stat_alloc(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *d`,`bool remote`,`bool interleaved)`
- [`domain_stat_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L172) — `static inline void domain_stat_free(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *d)`
- [`domain_stat_mark_interleaved()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L176) — `static inline void domain_stat_mark_interleaved(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *d)`
- [`domain_stat_failed_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L182) — `static inline void domain_stat_failed_alloc(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *d)`
- [`is_free_in_progress()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L188) — `static inline bool is_free_in_progress(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq)`
- [`mark_free_in_progress()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L192) — `static inline void mark_free_in_progress(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,`bool s)`
- [`buddy_page_for_addr()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L196) — `static inline`[`struct page *`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38)`buddy_page_for_addr(`[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` address)`
- [`free_from_buddy_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L200) — `static inline void free_from_buddy_internal(`[`struct domain_buddy`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)` *target`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` address`,`size_t page_count)`



