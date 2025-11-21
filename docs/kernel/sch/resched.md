+++
title = "resched"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/resched.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c)

- [`scheduler_mark_core_needs_resched()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c#L5) — `bool scheduler_mark_core_needs_resched(`[`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)` *c`,`bool new)`
- [`scheduler_mark_self_needs_resched()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c#L9) — `bool scheduler_mark_self_needs_resched(bool new)`
- [`scheduler_self_needs_resched()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c#L13) — `bool scheduler_self_needs_resched(void)`
- [`scheduler_resched_if_needed()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c#L17) — `void scheduler_resched_if_needed(void)`
- [`scheduler_mark_self_idle()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c#L27) — `void scheduler_mark_self_idle(bool new)`
- [`scheduler_core_idle()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c#L32) — `bool scheduler_core_idle(`[`struct core`](https://github.com/bluegummi/charmos/blob/main/include/smp/core.h#L15)` *c)`
- [`scheduler_force_resched()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/resched.c#L37) — `void scheduler_force_resched(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched)`

