+++
title = "profiling"
author = "Unknown"
status = "unknown"
+++

# [include/profiling.h](https://github.com/bluegummi/charmos/blob/main/include/profiling.h)

### struct [`profiling_entry`](https://github.com/bluegummi/charmos/blob/main/include/profiling.h#L9)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/include/profiling.h#L10) |
| `void` | [`*data`](https://github.com/bluegummi/charmos/blob/main/include/profiling.h#L11) |
| `char` | [`*(*to_str)(void *data)`](https://github.com/bluegummi/charmos/blob/main/include/profiling.h#L12) |
| `void` | [`(*log)(void *data)`](https://github.com/bluegummi/charmos/blob/main/include/profiling.h#L13) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list_node`](https://github.com/bluegummi/charmos/blob/main/include/profiling.h#L14) |

