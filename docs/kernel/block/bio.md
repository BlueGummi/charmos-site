# [kernel/block/bio.c](https://github.com/bluegummi/charmos/blob/main/kernel/block/bio.c)

<!-- Auto-generated from bio.c, do not edit manually -->

- [`create()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/bio.c#L11) — `static`[`struct bio_request *`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)`create(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,`uint64_t lba`,`uint64_t sec`,`uint64_t size`,[`enum bio_request_priority`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L10)` p`,`void (*cb)(struct bio_request *)`,`bool write`,`void *user`,`void *buffer)`
- [`bio_create_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/bio.c#L41) — [`struct bio_request *`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)`bio_create_read(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,`uint64_t lba`,`uint64_t sectors`,`uint64_t size`,`void (*cb)(struct bio_request *)`,`void *user`,`void *buffer)`
- [`bio_create_write()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/bio.c#L49) — [`struct bio_request *`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)`bio_create_write(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,`uint64_t lba`,`uint64_t sectors`,`uint64_t size`,`void (*cb)(struct bio_request *)`,`void *user`,`void *buffer)`
- [`bio_request_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/block/bio.c#L56) — `void bio_request_free(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`

