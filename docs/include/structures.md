+++
title = "hashmap"
author = "Unknown"
status = "unknown"
+++

# [include/structures/hashmap.h](https://github.com/bluegummi/charmos/blob/main/include/structures/hashmap.h)

- [`hash()`](https://github.com/bluegummi/charmos/blob/main/include/structures/hashmap.h#L27) — `static inline uint32_t hash(void *data`,`uint64_t length)`



+++
title = "rbt"
author = "Unknown"
status = "unknown"
+++

# [include/structures/rbt.h](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h)

### struct [`rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`data`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L19) |
| [`enum rbt_node_color`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L16) | [`color`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L20) |
| [`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18) | [`*left`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L21) |
| [`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18) | [`*right`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L22) |
| [`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18) | [`*parent`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L23) |


### struct [`rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)

| Member Type | Member Name |
|-------------|-------------|
| [`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18) | [`*root`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L27) |


### enum [`rbt_node_color`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L16)

| Name | Value |
|------|-------|
| [`TREE_NODE_RED`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L16) | `None` |
| [`TREE_NODE_BLACK`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L16) | `None` |


- [`rb_last()`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L30) — `static inline`[`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rb_last(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *root)`
- [`rbt_prev()`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L39) — `static inline`[`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rbt_prev(`[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *node)`
- [`rbt_init_node()`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L58) — `static inline void rbt_init_node(`[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *n)`
- [`rb_first()`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L63) — `static inline`[`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rb_first(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *root)`



+++
title = "pairing_heap"
author = "Unknown"
status = "unknown"
+++

# [include/structures/pairing_heap.h](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h)

### struct [`pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)

| Member Type | Member Name |
|-------------|-------------|
| [`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6) | [`*parent`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L7) |
| [`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6) | [`*child`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L8) |
| [`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6) | [`*sibling`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L9) |


### struct [`pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)

| Member Type | Member Name |
|-------------|-------------|
| [`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6) | [`*root`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L15) |
| `pairing_cmp_t` | [`cmp`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L16) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L17) |


### type alias
[`(*pairing_cmp_t)`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L12) : `int32_t (struct pairing_node *, struct pairing_node *)`

+++
title = "dll"
author = "Unknown"
status = "unknown"
+++

# [include/structures/dll.h](https://github.com/bluegummi/charmos/blob/main/include/structures/dll.h)


+++
title = "list"
author = "Unknown"
status = "unknown"
+++

# [include/structures/list.h](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h)

### struct [`list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)

| Member Type | Member Name |
|-------------|-------------|
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`*next`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L6) |


- [`INIT_LIST_HEAD()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L13) — `static inline __no_sanitize_address INIT_LIST_HEAD(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *list)`
- [`__list_add()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L19) — `static inline void __list_add(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *new`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *prev`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *next)`
- [`list_add()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L27) — `static inline void list_add(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *new`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *head)`
- [`list_add_tail()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L31) — `static inline void list_add_tail(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *new`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *head)`
- [`__list_del()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L36) — `static inline void __list_del(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *prev`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *next)`
- [`list_del()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L41) — `static inline void list_del(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *entry)`
- [`list_del_init()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L47) — `static inline void list_del_init(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *entry)`
- [`list_empty()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L52) — `static inline int list_empty(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *head)`
- [`list_pop_front()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L56) — `static inline`[`struct list_head *`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)`list_pop_front(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *head)`
- [`list_pop_front_init()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L65) — `static inline`[`struct list_head *`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)`list_pop_front_init(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *head)`
- [`list_splice_init()`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L73) — `static inline void list_splice_init(`[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *src`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *dst)`



+++
title = "locked_list"
author = "Unknown"
status = "unknown"
+++

# [include/structures/locked_list.h](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h)

### struct [`locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)

| Member Type | Member Name |
|-------------|-------------|
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L8) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L9) |
| `atomic_size_t` | [`num_elems`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L10) |


- [`locked_list_empty()`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L23) — `static inline bool locked_list_empty(`[`struct locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)` *ll)`
- [`locked_list_add()`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L28) — `static inline void locked_list_add(`[`struct locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)` *ll`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *lh)`
- [`locked_list_del()`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L34) — `static inline void locked_list_del(`[`struct locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)` *ll`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *lh)`
- [`locked_list_del_locked()`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L40) — `static inline void locked_list_del_locked(`[`struct locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)` *ll`,[`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)` *lh)`
- [`locked_list_pop_front()`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L47) — `static inline`[`struct list_head *`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5)`locked_list_pop_front(`[`struct locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)` *ll)`
- [`locked_list_num_elems()`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L52) — `static inline size_t locked_list_num_elems(`[`struct locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)` *ll)`
- [`locked_list_init()`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L57) — `static inline void locked_list_init(`[`struct locked_list`](https://github.com/bluegummi/charmos/blob/main/include/structures/locked_list.h#L7)` *ll)`



+++
title = "queue"
author = "Unknown"
status = "unknown"
+++

# [include/structures/queue.h](https://github.com/bluegummi/charmos/blob/main/include/structures/queue.h)


+++
title = "sll"
author = "Unknown"
status = "unknown"
+++

# [include/structures/sll.h](https://github.com/bluegummi/charmos/blob/main/include/structures/sll.h)


+++
title = "minheap"
author = "Unknown"
status = "unknown"
+++

# [include/structures/minheap.h](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h)

### struct [`minheap_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L13)

| Member Type | Member Name |
|-------------|-------------|
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L14) |
| `atomic_uint_fast64_t` | [`key`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L15) |
| `atomic_uint_fast32_t` | [`index`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L16) |


### struct [`minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)

| Member Type | Member Name |
|-------------|-------------|
| [`struct minheap_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L13) | [`**nodes`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L21) |
| `atomic_uint_fast32_t` | [`capacity`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L22) |
| `atomic_uint_fast32_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L23) |


- [`minheap_peek()`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L47) — `static inline`[`struct minheap_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L13)`minheap_peek(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap)`
- [`minheap_node_valid()`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L53) — `static inline bool minheap_node_valid(`[`struct minheap_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L13)` *node)`



