+++
title = "defer"
author = "Unknown"
status = "unknown"
+++

# [include/sch/defer.h](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h)

### struct [`work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)

| Member Type | Member Name |
|-------------|-------------|
| `void` | [`*arg1`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L18) |
| `void` | [`*arg2`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L19) |


### struct [`deferred_event`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L24)

| Member Type | Member Name |
|-------------|-------------|
| `size_t` | [`timer`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L25) |
| `uint64_t` | [`timestamp_ms`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L26) |
| `work_function` | [`callback`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L27) |
| [`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17) | [`args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L28) |
| [`struct deferred_event`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L24) | [`*next`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L29) |


### struct [`work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)

| Member Type | Member Name |
|-------------|-------------|
| `work_function` | [`func`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L33) |
| [`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17) | [`args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L34) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list_node`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L36) |
| `atomic_bool` | [`enqueued`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L38) |
| `atomic_bool` | [`active`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L39) |
| `atomic_uint_fast64_t` | [`seq`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L40) |


### struct [`worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)

| Member Type | Member Name |
|-------------|-------------|
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L49) |
| [`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194) | [`*workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L50) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`last_active`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L52) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`inactivity_check_period`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L55) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`start_idle`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L58) |
| `bool` | [`timeout_ran`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L62) |
| `bool` | [`should_exit`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L63) |
| `bool` | [`is_permanent`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L64) |
| `bool` | [`present`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L65) |
| `bool` | [`idle`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L66) |
| [`enum worker_next_action`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L43) | [`next_action`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L68) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list_node`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L70) |


### struct [`worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)

| Member Type | Member Name |
|-------------|-------------|
| [`enum worklist_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L73) | [`state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L86) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L87) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`creation_time`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L88) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L89) |
| [`enum worklist_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L81) | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L91) |
| [`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11) | [`refcount`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L92) |


### struct [`workqueue_stats`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L99)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`total_tasks_added`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L100) |
| `uint64_t` | [`total_tasks_executed`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L101) |
| `uint64_t` | [`total_workers_spawned`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L102) |
| `uint64_t` | [`total_worker_exits`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L103) |
| `uint64_t` | [`max_queue_length`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L104) |
| `uint64_t` | [`current_queue_length`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L105) |
| `uint64_t` | [`total_spawn_attempts`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L106) |
| `uint64_t` | [`total_spawn_failures`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L107) |
| `uint64_t` | [`num_idle_workers`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L108) |
| `uint64_t` | [`num_active_workers`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L109) |


### struct [`workqueue_attributes`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L174)

| Member Type | Member Name |
|-------------|-------------|
| `size_t` | [`min_workers`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L175) |
| `size_t` | [`max_workers`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L176) |
| `size_t` | [`capacity`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L177) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`spawn_delay`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L178) |
| `struct { uint64_t min; uint64_t max; }` | [`inactive_check_period`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L179) |
| [`enum workqueue_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L113) | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L184) |
| [`struct cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/smp/topology.h#L21) | [`worker_cpu_mask`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L185) |


### struct [`workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L195) |
| `atomic_bool` | [`ignore_timeouts`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L197) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`work_lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L199) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`worker_lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L200) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`worker_array_lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L201) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L202) |
| [`struct condvar`](https://github.com/bluegummi/charmos/blob/main/include/sync/condvar.h#L11) | [`queue_cv`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L204) |
| [`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32) | [`*oneshot_works`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L206) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`workers`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L207) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`works`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L208) |
| [`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48) | [`*worker_array`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L209) |
| `atomic_uint_fast64_t` | [`head`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L211) |
| `atomic_uint_fast64_t` | [`tail`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L212) |
| `atomic_bool` | [`spawn_pending`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L214) |
| `atomic_uint` | [`num_tasks`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L215) |
| `atomic_uint` | [`num_workers`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L217) |
| `atomic_uint` | [`idle_workers`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L218) |
| [`core_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L14) | [`core`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L220) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`last_spawn_attempt`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L221) |
| `atomic_flag` | [`spawner_flag_internal`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L223) |
| [`struct workqueue_attributes`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L174) | [`attrs`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L225) |
| [`enum workqueue_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L165) | [`state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L231) |
| [`struct thread_request`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_request.h#L69) | [`*request`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L234) |
| [`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11) | [`refcount`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L235) |


### enum [`worker_next_action`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L43)

| Name | Value |
|------|-------|
| [`WORKER_NEXT_ACTION_RUN`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L44) | `None` |
| [`WORKER_NEXT_ACTION_EXIT`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L45) | `None` |


### enum [`worklist_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L73)

| Name | Value |
|------|-------|
| [`WORKLIST_STATE_EMPTY`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L74) | `0` |
| [`WORKLIST_STATE_READY`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L75) | `1` |
| [`WORKLIST_STATE_RUNNING`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L76) | `2` |
| [`WORKLIST_STATE_DESTROYING`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L77) | `3` |
| [`WORKLIST_STATE_DEAD`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L78) | `4` |


### enum [`worklist_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L81)

| Name | Value |
|------|-------|
| [`WORKLIST_FLAG_UNBOUND`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L82) | `1` |


### enum [`workqueue_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L113)

| Name | Value |
|------|-------|
| [`WORKQUEUE_FLAG_PERMANENT`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L114) | `1 << 1` |
| [`WORKQUEUE_FLAG_AUTO_SPAWN`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L121) | `1 << 2` |
| [`WORKQUEUE_FLAG_UNMIGRATABLE_WORKERS`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L131) | `1 << 3` |
| [`WORKQUEUE_FLAG_NAMED`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L134) | `1 << 4` |
| [`WORKQUEUE_FLAG_SPAWN_VIA_REQUEST`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L136) | `1 << 5` |
| [`WORKQUEUE_FLAG_STATIC_WORKERS`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L143) | `1 << 6` |
| [`WORKQUEUE_FLAG_NO_AUTO_SPAWN`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L153) | `0` |
| [`WORKQUEUE_FLAG_MIGRATABLE_WORKERS`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L154) | `0` |
| [`WORKQUEUE_FLAG_ON_DEMAND`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L155) | `0` |
| [`WORKQUEUE_FLAG_NAMELESS`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L156) | `0` |
| [`WORKQUEUE_FLAG_SPAWN_NORMALLY`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L157) | `0` |
| [`WORKQUEUE_FLAG_DEFAULTS`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L159) | `WORKQUEUE_FLAG_AUTO_SPAWN` |


### enum [`workqueue_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L165)

| Name | Value |
|------|-------|
| [`WORKQUEUE_STATE_DEAD`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L166) | `None` |
| [`WORKQUEUE_STATE_DESTROYING`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L167) | `None` |
| [`WORKQUEUE_STATE_ACTIVE`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L168) | `None` |


### enum [`workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)

| Name | Value |
|------|-------|
| [`WORKQUEUE_ERROR_NEED_NEW_WORKER`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L243) | `4` |
| [`WORKQUEUE_ERROR_NEED_NEW_WQ`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L244) | `3` |
| [`WORKQUEUE_ERROR_OK`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L245) | `0` |
| [`WORKQUEUE_ERROR_FULL`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L246) | `-1` |
| [`WORKQUEUE_ERROR_WLIST_EXECUTING`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L247) | `-2` |
| [`WORKQUEUE_ERROR_UNUSABLE`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L248) | `-3` |
| [`WORKQUEUE_ERROR_WORK_EXECUTING`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L249) | `-4` |


### type alias
[`(*work_function)`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L15) : `void (void *arg, void *arg2)`
- [`work_active()`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L300) — `static inline bool work_active(`[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work)`

