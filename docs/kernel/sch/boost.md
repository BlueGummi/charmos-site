# [kernel/sch/boost.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/boost.c)

<!-- Auto-generated from boost.c, do not edit manually -->

- [`scheduler_boost_thread_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/boost.c#L5) — `static bool scheduler_boost_thread_internal(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *boosted`,`size_t new_weight`,[`enum thread_prio_class`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L72)` new_class)`
- [`scheduler_inherit_priority()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/boost.c#L29) — `bool scheduler_inherit_priority(`[`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188)` *boosted`,`size_t new_weight`,[`enum thread_prio_class`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L72)` new_class)`
- [`scheduler_uninherit_priority()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/boost.c#L66) — `void scheduler_uninherit_priority()`

