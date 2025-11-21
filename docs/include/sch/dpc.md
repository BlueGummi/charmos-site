+++
title = "dpc"
author = "Unknown"
status = "unknown"
+++

# [include/sch/dpc.h](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h)

### struct [`dpc`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L9)

| Member Type | Member Name |
|-------------|-------------|
| `dpc_func_t` | [`func`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L10) |
| `void` | [`*ctx`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L11) |
| `(struct dpc *)` | [`next`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L12) |
| `(bool)` | [`enqueued`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L13) |


### struct [`dpc_cpu`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L17)

| Member Type | Member Name |
|-------------|-------------|
| `(struct dpc *)` | [`head`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L18) |
| `(uint8_t)` | [`dpc_queued`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L19) |


### type alias
[`(*dpc_func_t)`](https://github.com/bluegummi/charmos/blob/main/include/sch/dpc.h#L6) : `void (void *ctx)`