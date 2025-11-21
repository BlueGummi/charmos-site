# [include/mem/movealloc.h](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h)

<!-- Auto-generated from movealloc.h, do not edit manually -->

### struct [`movealloc_callback_node`](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h#L18)

| Member Type | Member Name |
|-------------|-------------|
| `movealloc_callback` | [`callback`](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h#L19) |
| `void` | [`*a`](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h#L20) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h#L21) |


### struct [`movealloc_callback_chain`](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h#L24)

| Member Type | Member Name |
|-------------|-------------|
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h#L25) |


### type alias
[`(*movealloc_callback)`](https://github.com/bluegummi/charmos/blob/main/include/mem/movealloc.h#L16) : `void (void *a, void *b)`