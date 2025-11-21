# Big Idea: Turnstiles

**Author:** Unknown | **Status:** unknown


# Alerts
This is still EXPERIMENTAL. Be wary of bugs that may be from this component.
# Audience
Synchronization subsystem authors and others interested. not necessary to read.
# Overview
Turnstiles give us pointer sized adaptive mutexes (see "Locking Philosophy" [^1])...
# Background
Turnstiles were invented by Solaris, and are used in FreeBSD and XNU...
# Summary
Turnstiles give us a unified structure with functionalities... this functionality is provided by turnstile_block()...
# API
Turnstiles expose these functions, use them like such...
# Interactions
Turnstiles are used in our mutex implementation and are not to be used on their own outside of tests...
# Constraints
Turnstiles must be efficient and avoid taking the slow blocking path too frequently...
# Errors
Turnstiles don't "fail", but these things can...
# Rationale
Turnstiles spin when the owner is running because it avoids a slowpath...
# Diagrams
-- note: diagrams should have the 3 grave stones preceding and following them. this is omitted
```
here because this document is also in markdown and that would interfere with this.
                 Diagram A: Turnstile Donation
             turnstile       ┌────────────┐      no existing
             ┌─exists────────│   Block    │───────turnstile┐
             │               └────────────┘                │
             │                                             │
             │                                             │
             │                                             │
             ▼                                             ▼
 ┌─────────────────────────┐                      ┌──────────────────┐
 │Add Turnstile to freelist│                      │ Donate Turnstile │
 └─────────────────────────┘                      └──────────────────┘
```
# Bugs
  [#44](https://github.com/bluegummi/charmos/issues/44) "missed wakeup"
# Tests
  [`./kernel/tests/turnstile.c`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/turnstile.c) - general turnstile tests
  [`./kernel/tests/mutex.c`](https://github.com/bluegummi/charmos/blob/main/kernel/tests/mutex.c) - general mutex tests that use turnstiles
# References
[^1] "Locking Philosophy" [`./docs/locking_idea.md`](https://github.com/bluegummi/charmos/blob/main/docs/locking_idea.md)
# Changelog
  09/02/2005 - Eleanor Semaphore: Added second queue for rwlocks (commit 0b4e)
  09/01/2005 - Eleanor Semaphore: Created Idea (commit 62ef)
# Notes
  Here is some stuff you might be interested in reading regarding the history of turnstiles

---

# [kernel/sch/sched.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c)

<!-- Auto-generated from sched.c, do not edit manually -->

- [`tick_disable()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L93) — `static inline void tick_disable()`
- [`tick_enable()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L101) — `static inline void tick_enable()`
- [`change_timeslice_duration()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L109) — `static inline void change_timeslice_duration(uint64_t new_duration)`
- [`scheduler_change_timeslice_duration()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L122) — `void scheduler_change_timeslice_duration(uint64_t new_duration)`
- [`update_core_current_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L126) — `static inline void update_core_current_thread(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *next)`
- [`update_thread_before_save()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L130) — `static inline void update_thread_before_save(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *thread`,[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` time)`
- [`thread_done_for_period()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L139) — `static inline bool thread_done_for_period(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *thread)`
- [`re_enqueue_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L144) — `static inline void re_enqueue_thread(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *thread)`
- [`update_idle_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L164) — `static inline void update_idle_thread(`[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` time)`
- [`update_min_steal_diff()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L169) — `static inline void update_min_steal_diff(void)`
- [`save_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L174) — `static inline void save_thread(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *curr`,[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` time)`
- [`available_prio_level_from_bitmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L188) — `static inline`[`enum thread_prio_class`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L72)`available_prio_level_from_bitmap(uint8_t bitmap)`
- [`pick_from_special_queues()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L193) — `static`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`pick_from_special_queues(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`enum thread_prio_class`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L72)` prio)`
- [`pick_from_regular_queues()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L209) — `static`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`pick_from_regular_queues(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` now_ms`,[`enum thread_prio_class`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L72)` prio)`
- [`pick_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L225) — `static`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`pick_thread(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` now_ms)`
- [`load_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L246) — `static void load_thread(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *next`,[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6)` time)`
- [`load_idle_thread()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L269) — `static inline`[`struct thread *`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)`load_idle_thread(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched)`
- [`change_timeslice()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L289) — `static void change_timeslice(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *next)`
- [`context_switch()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L306) — `static inline void context_switch(`[`struct scheduler`](https://github.com/bluegummi/charmos/blob/main/include/sch/sched.h#L31)` *sched`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *curr`,[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *next`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql)`
- [`schedule()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L326) — `void schedule(void)`
- [`scheduler_yield()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/sched.c#L359) — `void scheduler_yield()`

