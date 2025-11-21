+++
title = "spinlock"
author = "Unknown"
status = "unknown"
+++

# [include/sync/spinlock.h](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h)

### struct [`spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_bool` | [`state`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L11) |


- [`spinlock_init()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L16) — `static inline __no_sanitize_address spinlock_init(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`
- [`spin_lock_raw()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L20) — `static inline __no_sanitize_address spin_lock_raw(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`
- [`spin_unlock_raw()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L35) — `static inline __no_sanitize_address spin_unlock_raw(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`
- [`spin_unlock()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L40) — `static inline __no_sanitize_address spin_unlock(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` old)`
- [`spin_lock()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L46) — `irql spin_lock(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`
- [`spin_lock_irq_disable()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L55) — `irql spin_lock_irq_disable(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`
- [`spin_trylock_raw()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L62) — `static inline __no_sanitize_address spin_trylock_raw(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`
- [`spin_trylock()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L69) — `static inline __no_sanitize_address spin_trylock(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` *out)`
- [`spin_trylock_irq_disable()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L83) — `static inline __no_sanitize_address spin_trylock_irq_disable(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` *out)`
- [`spinlock_held()`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L97) — `static inline __no_sanitize_address spinlock_held(`[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`



+++
title = "mutex"
author = "Unknown"
status = "unknown"
+++

# [include/sync/mutex.h](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h)

### struct [`mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)

| Member Type | Member Name |
|-------------|-------------|
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*owner`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L7) |
| [`struct thread_queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_queue.h#L5) | [`waiters`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L8) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L9) |


### struct [`mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)

| Member Type | Member Name |
|-------------|-------------|
| `union { _Atomic(void *) lock_word_ptr; _Atomic(uintptr_t) lock_word; }` | [`None`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L41) |


### enum [`mutex_bits`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L33)

| Name | Value |
|------|-------|
| [`MUTEX_HELD_BIT`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L34) | `1` |
| [`MUTEX_WAITER_BIT`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L35) | `1 << 1` |



+++
title = "turnstile"
author = "Unknown"
status = "unknown"
+++

# [include/sync/turnstile.h](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h)

### struct [`turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)

| Member Type | Member Name |
|-------------|-------------|
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*inheritor`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L22) |
| `bool` | [`applied_pi_boost`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L23) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`hash_list`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L24) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`freelist`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L25) |
| `size_t` | [`waiters`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L26) |
| [`thread_prio_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L18) | [`waiter_max_prio`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L27) |
| `void` | [`*lock_obj`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L28) |
| [`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14) | [`queues[TURNSTILE_NUM_QUEUES]`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L29) |
| [`enum turnstile_state`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L9) | [`state`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L30) |


### struct [`turnstile_hash_chain`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39)

| Member Type | Member Name |
|-------------|-------------|
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L40) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L41) |


### struct [`turnstile_hash_table`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L53)

| Member Type | Member Name |
|-------------|-------------|
| [`struct turnstile_hash_chain`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39) | [`heads[TURNSTILE_HASH_SIZE]`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L54) |


### enum [`turnstile_state`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L9)

| Name | Value |
|------|-------|
| [`TURNSTILE_STATE_UNUSED`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L10) | `None` |
| [`TURNSTILE_STATE_IN_HASH_TABLE`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L12) | `None` |
| [`TURNSTILE_STATE_IN_FREE_LIST`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L16) | `None` |



+++
title = "condvar"
author = "Unknown"
status = "unknown"
+++

# [include/sync/condvar.h](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h)

### struct [`condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)

| Member Type | Member Name |
|-------------|-------------|
| [`struct thread_queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_queue.h#L5) | [`waiters`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L12) |
| `bool` | [`irq_disable`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L13) |


### type alias
[`(*condvar_callback)`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L8) : `void (void *)`
### type alias
[`(*thread_action_callback)`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L9) : `void (struct thread *woke)`

+++
title = "semaphore"
author = "Unknown"
status = "unknown"
+++

# [include/sync/semaphore.h](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h)

### struct [`semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_int` | [`count`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L10) |
| `bool` | [`irq_disable`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L11) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L13) |
| [`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11) | [`cv`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L14) |



