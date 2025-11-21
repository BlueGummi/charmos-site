+++
title = "defer"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/defer.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c)

### struct [`deferred_event_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L11)

| Member Type | Member Name |
|-------------|-------------|
| [`struct deferred_event`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L24) | [`*head`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L12) |
| `size_t` | [`timer`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L13) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L14) |
| `size_t` | [`next_fire_time`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L15) |
| [`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9) | [`semaphore`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L16) |
| [`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32) | [`work`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L17) |


- [`this_timer()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L23) — `static inline uint64_t this_timer(void)`
- [`this_defer_queue()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L27) — `static inline`[`struct deferred_event_queue *`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L11)`this_defer_queue(void)`
- [`hpet_work()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L31) — `static void hpet_work(void *a`,`void *b)`
- [`hpet_irq_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L64) — `static void hpet_irq_handler(void *ctx`,`uint8_t irq`,`void *rsp)`
- [`defer_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L75) — `bool defer_enqueue(work_function func`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args`,`uint64_t delay_ms)`
- [`defer_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/defer.c#L111) — `void defer_init(void)`

