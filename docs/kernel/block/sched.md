+++
title = "sched"
author = "Unknown"
status = "unknown"
+++

# [kernel/block/sched/sched.c](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/sched.c)

- [`try_rq_reorder()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/sched.c#L8) — `static void try_rq_reorder(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched)`
- [`bio_sched_tick()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/sched.c#L16) — `static void bio_sched_tick(void *ctx`,`void *unused)`
- [`try_early_submit()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/sched.c#L36) — `static bool try_early_submit(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`bio_sched_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/sched.c#L48) — `void bio_sched_enqueue(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`bio_sched_dequeue()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/sched.c#L77) — `void bio_sched_dequeue(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req`,`bool already_locked)`
- [`bio_sched_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/sched.c#L90) — [`struct bio_scheduler *`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)`bio_sched_create(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_scheduler_ops`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L139)` *ops)`



+++
title = "queue"
author = "Unknown"
status = "unknown"
+++

# [kernel/block/sched/queue.c](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/queue.c)

- [`bio_sched_enqueue_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/queue.c#L13) — `void bio_sched_enqueue_internal(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`bio_sched_dequeue_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/queue.c#L30) — `void bio_sched_dequeue_internal(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`



+++
title = "dispatch"
author = "Unknown"
status = "unknown"
+++

# [kernel/block/sched/dispatch.c](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c)

- [`should_early_dispatch()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c#L12) — `static inline bool should_early_dispatch(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched)`
- [`try_dispatch_queue_head()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c#L16) — `static bool try_dispatch_queue_head(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)` *q)`
- [`dispatch_queue()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c#L32) — `static void dispatch_queue(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)` *q)`
- [`do_early_dispatch()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c#L61) — `static void do_early_dispatch(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched)`
- [`bio_sched_try_early_dispatch()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c#L67) — `void bio_sched_try_early_dispatch(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched)`
- [`bio_sched_dispatch_partial()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c#L73) — `void bio_sched_dispatch_partial(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,[`enum bio_request_priority`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L10)` p)`
- [`bio_sched_dispatch_all()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/dispatch.c#L81) — `void bio_sched_dispatch_all(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d)`



+++
title = "coalesce"
author = "Unknown"
status = "unknown"
+++

# [kernel/block/sched/coalesce.c](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c)

- [`set_coalesced()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c#L10) — `static inline void set_coalesced(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *into`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *from)`
- [`try_do_coalesce()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c#L16) — `static bool try_do_coalesce(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *into`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *from)`
- [`try_merge_candidates()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c#L27) — `static bool try_merge_candidates(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *iter`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *start`,[`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)` *queue)`
- [`check_higher_queue()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c#L55) — `static bool check_higher_queue(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)` *higher`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *candidate)`
- [`coalesce_adjacent_queues()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c#L73) — `static bool coalesce_adjacent_queues(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)` *lower`,[`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)` *higher)`
- [`coalesce_priority_queue()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c#L106) — `static bool coalesce_priority_queue(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)` *queue)`
- [`bio_sched_try_coalesce()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/coalesce.c#L135) — `bool bio_sched_try_coalesce(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched)`



+++
title = "boost"
author = "Unknown"
status = "unknown"
+++

# [kernel/block/sched/boost.c](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/boost.c)

- [`get_boost_depth()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/boost.c#L10) — `static inline uint64_t get_boost_depth(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`get_boosted_prio()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/boost.c#L19) — `static inline uint64_t get_boosted_prio(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`should_boost()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/boost.c#L25) — `static bool should_boost(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`do_boost_prio()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/boost.c#L46) — `static bool do_boost_prio(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`try_boost()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/boost.c#L74) — `static inline bool try_boost(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`bio_sched_boost_starved()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/sched/boost.c#L83) — `bool bio_sched_boost_starved(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched)`



