+++
title = "vaddr_alloc"
author = "Unknown"
status = "unknown"
+++

# [include/mem/vaddr_alloc.h](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h)

### struct [`vas_range`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L8)

| Member Type | Member Name |
|-------------|-------------|
| [`struct vas_range`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L8) | [`*next_free`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L9) |
| [`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18) | [`node`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L10) |
| [`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13) | [`start`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L11) |
| `size_t` | [`length`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L12) |


### struct [`vas_space`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L15)

| Member Type | Member Name |
|-------------|-------------|
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L16) |
| [`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26) | [`tree`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L17) |
| [`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13) | [`base`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L18) |
| [`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13) | [`limit`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L19) |
| [`struct vas_range`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L8) | [`*freelist`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L20) |
| `struct vas_set` | [`*percpu_sets`](https://github.com/bluegummi/charmos/blob/main/include/mem/vaddr_alloc.h#L21) |

