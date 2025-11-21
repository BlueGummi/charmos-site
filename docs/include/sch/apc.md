# [include/sch/apc.h](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h)

<!-- Auto-generated from apc.h, do not edit manually -->

### struct [`apc`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L35)

| Member Type | Member Name |
|-------------|-------------|
| `apc_func_t` | [`func`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L36) |
| `void` | [`*arg1`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L37) |
| `void` | [`*arg2`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L38) |
| `bool` | [`enqueued`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L39) |
| `atomic_bool` | [`cancelled`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L40) |
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*owner`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L41) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L42) |


### enum [`apc_type`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L14)

| Name | Value |
|------|-------|
| [`APC_TYPE_SPECIAL_KERNEL`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L14) | `None` |
| [`APC_TYPE_KERNEL`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L14) | `None` |
| [`APC_TYPE_COUNT`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L14) | `None` |


### enum [`apc_event`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L16)

| Name | Value |
|------|-------|
| [`APC_EVENT_THREAD_MIGRATE`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L17) | `None` |
| [`APC_EVENT_THREAD_EXIT`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L18) | `None` |
| [`APC_EVENT_COUNT`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L19) | `None` |
| [`APC_EVENT_NONE`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L20) | `None` |


### type alias
[`(*apc_func_t)`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L33) : `void (struct apc *apc, void *arg1, void *arg2)`
- [`apc_event_str()`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L23) — `static inline const char * apc_event_str(`[`enum apc_event`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L16)` evt)`
- [`safe_to_exec_apcs()`](https://github.com/bluegummi/charmos/blob/main/include/sch/apc.h#L65) — `static inline bool safe_to_exec_apcs(void)`

