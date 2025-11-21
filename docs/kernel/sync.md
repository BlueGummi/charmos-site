+++
title = "mutex"
author = "Unknown"
status = "unknown"
+++

# [kernel/sync/mutex.c](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c)

- [`try_acquire_simple_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L13) — `static bool try_acquire_simple_mutex(`[`struct mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)` *m`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *curr)`
- [`should_spin_on_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L25) — `static bool should_spin_on_mutex(`[`struct mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)` *m)`
- [`spin_wait_simple_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L33) — `static bool spin_wait_simple_mutex(`[`struct mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)` *m`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *curr)`
- [`block_on_simple_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L42) — `static void block_on_simple_mutex(`[`struct mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)` *m)`
- [`mutex_simple_lock()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L49) — `void mutex_simple_lock(`[`struct mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)` *m)`
- [`mutex_simple_unlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L64) — `void mutex_simple_unlock(`[`struct mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)` *m)`
- [`mutex_simple_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L83) — `void mutex_simple_init(`[`struct mutex_simple`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L6)` *m)`
- [`mutex_lock_get_backoff()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L87) — `size_t mutex_lock_get_backoff(size_t current_backoff)`
- [`backoff_jitter()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L100) — `static inline int32_t backoff_jitter(size_t backoff)`
- [`mutex_lock_delay()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L110) — `void mutex_lock_delay(size_t backoff)`
- [`mutex_owner_running()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L124) — `static bool mutex_owner_running(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mutex)`
- [`mutex_sanity_check()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L139) — `static void mutex_sanity_check()`
- [`mutex_lock()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L145) — `void mutex_lock(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mutex)`
- [`mutex_unlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L233) — `void mutex_unlock(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mutex)`
- [`mutex_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex.c#L259) — `void mutex_init(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mtx)`



+++
title = "turnstile"
author = "Unknown"
status = "unknown"
+++

# [kernel/sync/turnstile.c](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c)

- [`turnstiles_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L43) — `void turnstiles_init()`
- [`turnstile_thread_priority()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L59) — `static int32_t turnstile_thread_priority(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`turnstile_pairing_heap_cmp()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L71) — `static int32_t turnstile_pairing_heap_cmp(`[`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)` *l`,[`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)` *r)`
- [`turnstile_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L84) — [`struct turnstile *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)`turnstile_init(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts)`
- [`turnstile_destroy()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L100) — `void turnstile_destroy(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts)`
- [`turnstile_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L104) — [`struct turnstile *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)`turnstile_create(void)`
- [`turnstile_chain_for()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L118) — `static inline`[`struct turnstile_hash_chain *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39)`turnstile_chain_for(void *obj)`
- [`turnstile_insert_to_freelist()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L123) — `static void turnstile_insert_to_freelist(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *parent`,[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *child)`
- [`turnstile_freelist_pop()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L130) — `static`[`struct turnstile *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)`turnstile_freelist_pop(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts)`
- [`turnstile_insert()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L138) — `static void turnstile_insert(`[`struct turnstile_hash_chain`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39)` *chain`,[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts`,`void *lock_obj)`
- [`turnstile_remove()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L146) — `static void turnstile_remove(`[`struct turnstile_hash_chain`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39)` *chain`,[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts)`
- [`turnstile_lookup_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L154) — [`struct turnstile *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)`turnstile_lookup_internal(void *obj)`
- [`turnstile_lookup()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L168) — [`struct turnstile *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)`turnstile_lookup(void *obj`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` *irql_out)`
- [`turnstile_lookup_no_lock_for_hash_chain_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L185) — `static`[`struct turnstile *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)`turnstile_lookup_no_lock_for_hash_chain_internal(`[`struct turnstile_hash_chain`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39)` *except`,`void *obj`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` *irql_out`,[`struct turnstile_hash_chain`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39)` **thc_out)`
- [`turnstile_pi_remove()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L212) — `void turnstile_pi_remove(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts)`
- [`turnstile_dequeue_first()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L219) — [`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`turnstile_dequeue_first(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts`,`size_t queue)`
- [`turnstile_wake()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L249) — `void turnstile_wake(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts`,`size_t queue`,`size_t num_threads`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` lock_irql)`
- [`turnstile_unlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L268) — `void turnstile_unlock(void *obj`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql)`
- [`turnstile_propagate_boost()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L273) — `void turnstile_propagate_boost(`[`struct turnstile_hash_chain`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L39)` *locked_chain`,[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts`,`size_t waiter_weight`,[`enum thread_prio_class`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L72)` waiter_class)`
- [`turnstile_block_on()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L341) — `static void turnstile_block_on(void *lock_obj`,[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts`,`size_t queue_num)`
- [`turnstile_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L352) — [`struct turnstile *`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)`turnstile_block(`[`struct turnstile`](https://github.com/bluegummi/charmos/blob/main/include/sync/turnstile.h#L21)` *ts`,`size_t queue_num`,`void *lock_obj`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` lock_irql)`
- [`turnstile_get_waiter_count()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/turnstile.c#L393) — `size_t turnstile_get_waiter_count(void *lock_obj)`



+++
title = "condvar"
author = "Unknown"
status = "unknown"
+++

# [kernel/sync/condvar.c](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c)

### struct [`condvar_with_cb`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L78)

| Member Type | Member Name |
|-------------|-------------|
| [`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11) | [`*cv`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L79) |
| `condvar_callback` | [`cb`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L80) |
| `void` | [`*cb_arg`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L81) |
| `size_t` | [`cookie`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L82) |


- [`condvar_lock_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L4) — `static`[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)`condvar_lock_internal(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv`,[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock)`
- [`do_block_on_queue()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L12) — `static void do_block_on_queue(`[`struct thread_queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_queue.h#L5)` *q`,[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql)`
- [`condvar_wait()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L19) — [`enum wake_reason`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L117)`condvar_wait(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv`,[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` *out)`
- [`condvar_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L31) — `void condvar_init(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv`,`bool irq_disable)`
- [`set_wake_reason_and_wake()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L36) — `static void set_wake_reason_and_wake(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t`,[`enum wake_reason`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L117)` reason)`
- [`nop_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L49) — `static void nop_callback(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *unused)`
- [`condvar_signal_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L53) — [`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`condvar_signal_callback(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv`,`thread_action_callback tac)`
- [`condvar_signal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L61) — [`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`condvar_signal(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv)`
- [`condvar_broadcast_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L65) — `void condvar_broadcast_callback(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv`,`thread_action_callback tac)`
- [`condvar_broadcast()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L74) — `void condvar_broadcast(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv)`
- [`condvar_timeout_wakeup()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L85) — `static void condvar_timeout_wakeup(void *arg`,`void *arg2)`
- [`condvar_wait_timeout()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/condvar.c#L105) — [`enum wake_reason`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L117)`condvar_wait_timeout(`[`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11)` *cv`,[`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10)` *lock`,[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` timeout_ms`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` *out)`



+++
title = "mutex_internal"
author = "Unknown"
status = "unknown"
+++

# [kernel/sync/mutex_internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h)

- [`mutex_get_owner()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L13) — `static inline`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`mutex_get_owner(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mtx)`
- [`mutex_make_lock_word()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L17) — `static inline uintptr_t mutex_make_lock_word(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *owner)`
- [`mutex_make_unlocked_word()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L21) — `static inline uintptr_t mutex_make_unlocked_word(void)`
- [`mutex_try_lock()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L25) — `static inline bool mutex_try_lock(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mtx`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *self)`
- [`mutex_lock_word_unlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L53) — `static inline void mutex_lock_word_unlock(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mtx)`
- [`mutex_set_waiter_bit()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L58) — `static inline bool mutex_set_waiter_bit(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mtx)`
- [`mutex_unset_waiter_bit()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L64) — `static inline bool mutex_unset_waiter_bit(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mtx)`
- [`mutex_get_waiter_bit()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/mutex_internal.h#L70) — `static inline bool mutex_get_waiter_bit(`[`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40)` *mtx)`



+++
title = "semaphore"
author = "Unknown"
status = "unknown"
+++

# [kernel/sync/semaphore.c](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c)

- [`semaphore_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L11) — `void semaphore_init(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *s`,`int value`,`bool irq_disable)`
- [`semaphore_lock_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L18) — `static`[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)`semaphore_lock_internal(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *sem)`
- [`semaphore_wait()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L25) — `void semaphore_wait(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *s)`
- [`semaphore_timedwait()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L35) — `bool semaphore_timedwait(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *s`,[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` timeout_ms)`
- [`semaphore_post()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L52) — `void semaphore_post(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *s)`
- [`semaphore_postn()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L62) — `void semaphore_postn(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *s`,`int n)`
- [`semaphore_post_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L72) — `void semaphore_post_callback(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *s`,`thread_action_callback cb)`
- [`semaphore_postn_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/sync/semaphore.c#L82) — `void semaphore_postn_callback(`[`struct semaphore`](https://github.com/bluegummi/charmos/blob/main/include/sync/semaphore.h#L9)` *s`,`int n`,`thread_action_callback cb)`



