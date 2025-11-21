+++
title = "queue"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/queue.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/queue.c)

- [`scheduler_add_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/queue.c#L13) — `void scheduler_add_thread(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *task`,`bool lock_held)`
- [`scheduler_remove_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/queue.c#L51) — `void scheduler_remove_thread(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t`,`bool lock_held)`
- [`scheduler_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/queue.c#L78) — `void scheduler_enqueue(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t)`
- [`scheduler_enqueue_on_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/queue.c#L107) — `void scheduler_enqueue_on_core(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t`,`uint64_t core_id)`
- [`scheduler_wake()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/queue.c#L112) — `void scheduler_wake(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *t`,[`enum thread_wake_reason`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L84)` reason`,[`enum thread_prio_class`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L72)` prio)`

