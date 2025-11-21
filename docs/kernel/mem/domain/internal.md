# [kernel/mem/domain/internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h)

<!-- Auto-generated from internal.h, do not edit manually -->

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

