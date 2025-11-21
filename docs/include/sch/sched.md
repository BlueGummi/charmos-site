+++
title = "sched"
author = "Unknown"
status = "unknown"
+++

# [include/sch/sched.h](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h)

### struct [`idle_thread_data`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L23)

| Member Type | Member Name |
|-------------|-------------|
| [`enum idle_thread_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L18) | [`state`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L24) |
| `atomic_bool` | [`woken_from_timer`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L26) |
| `atomic_uint_fast64_t` | [`last_entry_ms`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L27) |
| `uint64_t` | [`last_exit_ms`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L28) |


### struct [`scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_bool` | [`tick_enabled`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L33) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`timeslice_duration`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L34) |
| [`struct thread_queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_queue.h#L5) | [`urgent_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L37) |
| [`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26) | [`thread_rbt`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L39) |
| [`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26) | [`completed_rbt`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L40) |
| [`struct thread_queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_queue.h#L5) | [`rt_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L42) |
| [`struct thread_queue`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_queue.h#L5) | [`bg_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L43) |
| `atomic_uint_fast8_t` | [`queue_bitmap`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L45) |
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*current`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L47) |
| `size_t` | [`thread_count[THREAD_PRIO_CLASS_COUNT]`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L50) |
| `size_t` | [`total_thread_count`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L51) |
| `size_t` | [`total_weight`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L52) |
| `bool` | [`period_enabled`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L55) |
| `uint64_t` | [`current_period`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L56) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`period_ms`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L58) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`period_start_ms`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L59) |
| `int64_t` | [`core_id`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L68) |
| `atomic_bool` | [`being_robbed`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L71) |
| `atomic_bool` | [`stealing_work`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L72) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L74) |
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*idle_thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L77) |
| [`struct idle_thread_data`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L23) | [`idle_thread_data`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L78) |


### struct [`scheduler_data`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L120)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`max_concurrent_stealers`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L121) |
| `atomic_uint` | [`active_stealers`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L122) |
| `atomic_uint` | [`total_threads`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L123) |
| `atomic_int_fast64_t` | [`steal_min_diff`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L124) |


### enum [`idle_thread_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L18)

| Name | Value |
|------|-------|
| [`IDLE_THREAD_WORK_STEAL`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L19) | `0` |
| [`IDLE_THREAD_SLEEP`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L20) | `1` |


- [`scheduler_get_current_thread()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L129) — `static inline`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`scheduler_get_current_thread()`
- [`scheduler_pin_current_thread()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L137) — `static inline`[`enum thread_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L68)`scheduler_pin_current_thread()`
- [`scheduler_unpin_current_thread()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L146) — `static inline void scheduler_unpin_current_thread(`[`enum thread_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L68)` flags)`
- [`thread_spawn()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L155) — `static inline`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`thread_spawn(char *name`,`void (*entry)(void))`
- [`thread_spawn_custom_stack()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L166) — `static inline`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`thread_spawn_custom_stack(char *name`,`void (*entry)(void)`,`size_t stack_size)`
- [`thread_spawn_on_core()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L178) — `static inline`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`thread_spawn_on_core(char *name`,`void (*entry)(void)`,`uint64_t core_id)`
- [`scheduler_wake_from_io_block()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L185) — `static inline void scheduler_wake_from_io_block(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`scheduler_self_in_resched()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L189) — `static inline bool scheduler_self_in_resched()`
- [`scheduler_mark_self_in_resched()`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L193) — `static inline bool scheduler_mark_self_in_resched(bool new)`

