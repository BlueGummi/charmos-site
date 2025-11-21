# [kernel/mem/domain/free_queue.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free_queue.c)

<!-- Auto-generated from free_queue.c, do not edit manually -->

- [`domain_free_queue_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free_queue.c#L10) — `bool domain_free_queue_enqueue(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` addr`,`size_t pages)`
- [`domain_free_queue_dequeue()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/free_queue.c#L30) — `bool domain_free_queue_dequeue(`[`struct domain_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L31)` *fq`,[`paddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L12)` *addr_out`,`size_t *pages_out)`

