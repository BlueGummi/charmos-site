+++
title = "spawn"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/workqueue/spawn.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c)

- [`get_inactivity_timeout()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L7) — `static`[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)`get_inactivity_timeout(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_link_thread_and_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L24) — `void workqueue_link_thread_and_worker(`[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *worker`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *thread)`
- [`claim_spawner()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L33) — `static bool claim_spawner(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *p)`
- [`release_spawner()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L38) — `static void release_spawner(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *p)`
- [`worker_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L42) — `static void worker_init(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *w`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`workqueue_worker_thread_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L56) — `static`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`workqueue_worker_thread_create(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_enqueue_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L63) — `static void workqueue_enqueue_thread(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`workqueue_worker_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L71) — [`struct worker *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)`workqueue_worker_create(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_init_new_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L90) — `static void workqueue_init_new_worker(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *w`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`workqueue_request_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L99) — [`enum thread_request_decision`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread_request.h#L44)`workqueue_request_callback(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t`,`void *data)`
- [`workqueue_spawn_via_request()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L115) — `void workqueue_spawn_via_request(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_spawn_worker_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L132) — `bool workqueue_spawn_worker_internal(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_should_spawn_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L158) — `bool workqueue_should_spawn_worker(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_try_spawn_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L176) — `bool workqueue_try_spawn_worker(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`worker_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L188) — [`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`worker_create(void)`
- [`worker_create_unmigratable()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/spawn.c#L194) — [`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`worker_create_unmigratable()`



+++
title = "main"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/workqueue/main.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/main.c)

- [`worker_wait()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/main.c#L4) — `static`[`enum wake_reason`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L117)`worker_wait(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *w`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` *out)`
- [`worker_should_exit()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/main.c#L31) — `static inline bool worker_should_exit(`[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *worker`,[`enum wake_reason`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L117)` signal)`
- [`worker_reset()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/main.c#L46) — `static void worker_reset(`[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *worker)`
- [`worker_destroy()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/main.c#L50) — `static void worker_destroy(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *worker)`
- [`worker_exit()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/main.c#L75) — `static void worker_exit(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *worker`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql)`
- [`worker_main()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/main.c#L95) — `void worker_main(void)`



+++
title = "list"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/workqueue/list.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c)

- [`worklist_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L3) — [`struct worklist *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)`worklist_create(`[`enum worklist_flags`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L81)` flags)`
- [`worklist_destroy()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L14) — `void worklist_destroy(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *list)`
- [`worklist_change_state()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L18) — `static`[`enum worklist_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L73)`worklist_change_state(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *wlist`,[`enum worklist_state`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L73)` new)`
- [`worklist_add_work()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L27) — `void worklist_add_work(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *list`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *task)`
- [`worklist_remove_work()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L34) — `void worklist_remove_work(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *list`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *task)`
- [`worklist_pop_front()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L44) — [`struct work *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)`worklist_pop_front(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *list)`
- [`worklist_empty()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L55) — `bool worklist_empty(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *list)`
- [`worklist_execute_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L62) — `static void worklist_execute_internal(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *list)`
- [`worklist_cancel_work()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L77) — `void worklist_cancel_work(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *wl`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *wlw)`
- [`worklist_execute()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/list.c#L81) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`worklist_execute(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *w)`



+++
title = "workqueue"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/workqueue/workqueue.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c)

- [`workqueue_add_oneshot()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L14) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add_oneshot(work_function func`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args)`
- [`workqueue_add_remote_oneshot()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L20) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add_remote_oneshot(work_function func`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args)`
- [`workqueue_add_local_oneshot()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L26) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add_local_oneshot(work_function func`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args)`
- [`find_optimal_domain_wq()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L32) — `static`[`struct workqueue *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)`find_optimal_domain_wq(void)`
- [`(pos)()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L42) — `domain_for_each_local (pos)()`
- [`workqueue_add_fast_oneshot()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L55) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add_fast_oneshot(work_function func`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args)`
- [`workqueue_add_fast()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L61) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add_fast(`[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work)`
- [`workqueue_add()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L66) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add(`[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work)`
- [`workqueue_add_local()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L71) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add_local(`[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work)`
- [`workqueue_add_remote()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L76) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_add_remote(`[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work)`
- [`work_execute()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L81) — `void work_execute(`[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *task)`
- [`workqueue_create_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L87) — [`struct workqueue *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)`workqueue_create_internal(`[`struct workqueue_attributes`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L174)` *attrs`,`char *fmt`,`va_list args)`
- [`workqueue_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L172) — [`struct workqueue *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)`workqueue_create(`[`struct workqueue_attributes`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L174)` *attrs`,`char *fmt)`
- [`mark_worker_exit()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L189) — `static void mark_worker_exit(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`workqueue_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L196) — `void workqueue_free(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *wq)`
- [`workqueue_destroy()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L205) — `void workqueue_destroy(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_kick()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L238) — `void workqueue_kick(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_spawn_permanent_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L242) — [`struct worker *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)`workqueue_spawn_permanent_worker(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,`int64_t core)`
- [`workqueues_permanent_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L279) — `void workqueues_permanent_init(void)`
- [`work_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L314) — [`struct work *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)`work_init(`[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work`,`work_function fn`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args)`
- [`work_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/workqueue.c#L325) — [`struct work *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)`work_create(work_function fn`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args)`



+++
title = "queue"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/workqueue/queue.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/queue.c)

- [`signal_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/queue.c#L3) — `static void signal_callback(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`signal_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/queue.c#L9) — `static`[`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`signal_worker(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`dequeue_oneshot_task()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/queue.c#L31) — `static bool dequeue_oneshot_task(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *out)`
- [`workqueue_enqueue_oneshot()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/queue.c#L62) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_enqueue_oneshot(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,`work_function func`,[`struct work_args`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L17)` args)`
- [`workqueue_dequeue_task()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/queue.c#L97) — `int32_t workqueue_dequeue_task(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` **out`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *oneshot_task)`
- [`workqueue_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/queue.c#L117) — [`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`workqueue_enqueue(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work)`



+++
title = "internal"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/workqueue/internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h)

- [`workqueue_current_worker_count()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L23) — `static inline uint64_t workqueue_current_worker_count(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *q)`
- [`workqueue_works_empty()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L27) — `static inline bool workqueue_works_empty(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_empty()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L34) — `static inline bool workqueue_empty(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_set_needs_spawn()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L38) — `static inline void workqueue_set_needs_spawn(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue`,`bool needs)`
- [`workqueue_needs_spawn()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L43) — `static inline bool workqueue_needs_spawn(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_get()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L47) — `static inline bool workqueue_get(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`workqueue_put()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L51) — `static inline void workqueue_put(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *queue)`
- [`worklist_get()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L56) — `static inline bool worklist_get(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *wlist)`
- [`worklist_put()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L60) — `static inline void worklist_put(`[`struct worklist`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L85)` *wlist)`
- [`workqueue_add_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L67) — `static inline void workqueue_add_worker(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *wq`,[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *wker)`
- [`workqueue_remove_worker()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L74) — `static inline void workqueue_remove_worker(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *wq`,[`struct worker`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L48)` *worker)`
- [`ignore_timeouts()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L81) — `static inline bool ignore_timeouts(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *q)`
- [`workqueue_usable()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L85) — `static inline bool workqueue_usable(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *q)`
- [`workqueue_workers()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L89) — `static inline size_t workqueue_workers(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *wq)`
- [`workqueue_idlers()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/internal.h#L93) — `static inline size_t workqueue_idlers(`[`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)` *wq)`



+++
title = "misc"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/workqueue/misc.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/misc.c)

- [`workqueue_least_loaded_queue_except()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/misc.c#L3) — [`struct workqueue *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)`workqueue_least_loaded_queue_except(int64_t except_core_num)`
- [`workqueue_get_least_loaded()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/misc.c#L23) — [`struct workqueue *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)`workqueue_get_least_loaded(void)`
- [`workqueue_get_least_loaded_remote()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/workqueue/misc.c#L27) — [`struct workqueue *`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194)`workqueue_get_least_loaded_remote(void)`



