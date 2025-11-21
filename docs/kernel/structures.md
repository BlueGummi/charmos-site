+++
title = "rbt"
author = "Unknown"
status = "unknown"
+++

# [kernel/structures/rbt.c](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c)

- [`rbt_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L8) — [`struct rbt *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)`rbt_create(void)`
- [`rbt_find_min()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L14) — [`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rbt_find_min(`[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *node)`
- [`rbt_find_max()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L21) — [`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rbt_find_max(`[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *node)`
- [`rbt_max()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L28) — [`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rbt_max(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree)`
- [`rbt_min()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L32) — [`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rbt_min(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree)`
- [`rbt_next()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L36) — [`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rbt_next(`[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *node)`
- [`rb_transplant()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L48) — `static void rb_transplant(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *u`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *v)`
- [`left_rotate()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L61) — `static void left_rotate(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *x)`
- [`right_rotate()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L80) — `static void right_rotate(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *y)`
- [`fix_deletion()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L98) — `static void fix_deletion(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *x)`
- [`validate_rbtree()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L187) — `static int validate_rbtree(`[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *node`,`int *black_height)`
- [`rb_delete()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L221) — `void rb_delete(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *z)`
- [`rbt_search()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L260) — [`struct rbt_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)`rbt_search(`[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *root`,`uint64_t data)`
- [`rbt_remove()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L270) — `void rbt_remove(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,`uint64_t data)`
- [`fix_insertion()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L276) — `static void fix_insertion(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *node)`
- [`rbt_insert()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/rbt.c#L320) — `void rbt_insert(`[`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26)` *tree`,[`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18)` *new_node)`



+++
title = "pairing_heap"
author = "Unknown"
status = "unknown"
+++

# [kernel/structures/pairing_heap.c](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c)

- [`pairing_heap_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c#L4) — `void pairing_heap_init(`[`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)` *h`,`pairing_cmp_t cmp)`
- [`pairing_merge()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c#L10) — `static`[`struct pairing_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)`pairing_merge(`[`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)` *h`,[`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)` *a`,[`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)` *b)`
- [`pairing_heap_insert()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c#L36) — `void pairing_heap_insert(`[`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)` *h`,[`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)` *node)`
- [`pairing_heap_peek()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c#L46) — [`struct pairing_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)`pairing_heap_peek(`[`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)` *h)`
- [`pairing_two_pass()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c#L53) — `static`[`struct pairing_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)`pairing_two_pass(`[`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)` *h`,[`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)` *first)`
- [`pairing_heap_pop()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c#L70) — [`struct pairing_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)`pairing_heap_pop(`[`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)` *h)`
- [`pairing_heap_decrease()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/pairing_heap.c#L91) — `void pairing_heap_decrease(`[`struct pairing_heap`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L14)` *h`,[`struct pairing_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/pairing_heap.h#L6)` *node)`



+++
title = "minheap"
author = "Unknown"
status = "unknown"
+++

# [kernel/structures/minheap.c](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c)

- [`minheap_swap()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L7) — `static void minheap_swap(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap`,`uint32_t a`,`uint32_t b)`
- [`minheap_sift_up()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L16) — `static void minheap_sift_up(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap`,`uint32_t idx)`
- [`minheap_sift_down()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L27) — `static void minheap_sift_down(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap`,`uint32_t idx)`
- [`minheap_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L51) — [`struct minheap *`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)`minheap_create(void)`
- [`minheap_expand()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L59) — `void minheap_expand(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap`,`uint32_t new_size)`
- [`minheap_insert()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L77) — `void minheap_insert(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap`,[`struct minheap_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L13)` *node`,`uint64_t key)`
- [`minheap_remove()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L104) — `void minheap_remove(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap`,[`struct minheap_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L13)` *node)`
- [`minheap_pop()`](https://github.com/bluegummi/charmos/blob/main/kernel/structures/minheap.c#L125) — [`struct minheap_node *`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L13)`minheap_pop(`[`struct minheap`](https://github.com/bluegummi/charmos/blob/main/include/structures/minheap.h#L20)` *heap)`



