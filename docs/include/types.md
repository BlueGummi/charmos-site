+++
title = "rcu"
author = "Unknown"
status = "unknown"
+++

# [include/types/rcu.h](https://github.com/bluegummi/charmos/blob/main/include/types/rcu.h)

### struct [`rcu_defer_op`](https://github.com/bluegummi/charmos/blob/main/include/types/rcu.h#L9)

| Member Type | Member Name |
|-------------|-------------|
| `void` | [`(*func)(void *)`](https://github.com/bluegummi/charmos/blob/main/include/types/rcu.h#L10) |
| `void` | [`*arg`](https://github.com/bluegummi/charmos/blob/main/include/types/rcu.h#L11) |



+++
title = "refcount"
author = "Unknown"
status = "unknown"
+++

# [include/types/refcount.h](https://github.com/bluegummi/charmos/blob/main/include/types/refcount.h)

- [`refcount_init()`](https://github.com/bluegummi/charmos/blob/main/include/types/refcount.h#L9) — `static inline void refcount_init(`[`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11)` *rc`,`unsigned int val)`
- [`refcount_inc()`](https://github.com/bluegummi/charmos/blob/main/include/types/refcount.h#L13) — `static inline bool refcount_inc(`[`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11)` *rc)`
- [`refcount_inc_not_zero()`](https://github.com/bluegummi/charmos/blob/main/include/types/refcount.h#L25) — `static inline bool refcount_inc_not_zero(`[`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11)` *rc)`
- [`refcount_dec_and_test()`](https://github.com/bluegummi/charmos/blob/main/include/types/refcount.h#L39) — `static inline bool refcount_dec_and_test(`[`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11)` *rc)`



+++
title = "types"
author = "Unknown"
status = "unknown"
+++

# [include/types/types.h](https://github.com/bluegummi/charmos/blob/main/include/types/types.h)

### type alias
[`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) : `uint64_t`
### type alias
[`inode_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L7) : `uint32_t`
### type alias
[`mode_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L8) : `uint16_t`
### type alias
[`gid_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L9) : `uint32_t`
### type alias
[`uid_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L10) : `uint32_t`
### type alias
[`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11) : `atomic_uint`
### type alias
[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12) : `uintptr_t`
### type alias
[`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13) : `uintptr_t`
### type alias
[`core_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L14) : `uint64_t`
### type alias
[`cpumask_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L15) : `uint64_t`
### type alias
[`pte_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L16) : `uint64_t`
### type alias
[`page_flags_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L17) : `uint64_t`
### type alias
[`thread_prio_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L18) : `uint32_t`

