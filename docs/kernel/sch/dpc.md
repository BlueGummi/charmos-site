+++
title = "dpc"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/dpc.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/dpc.c)

- [`dpc_run_local()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/dpc.c#L9) — `void dpc_run_local(void)`
- [`dpc_enqueue_on_cpu()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/dpc.c#L56) — `bool dpc_enqueue_on_cpu(size_t cpu`,[`struct dpc`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L9)` *d)`
- [`dpc_enqueue_local()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/dpc.c#L92) — `bool dpc_enqueue_local(`[`struct dpc`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L9)` *d)`
- [`dpc_init_percpu()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/dpc.c#L100) — `void dpc_init_percpu(void)`
- [`dpc_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/dpc.c#L111) — [`struct dpc *`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L9)`dpc_create(dpc_func_t fn`,`void *ctx)`

