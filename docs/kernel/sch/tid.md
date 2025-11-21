# [kernel/sch/tid.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/tid.c)

<!-- Auto-generated from tid.c, do not edit manually -->

- [`tid_space_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/tid.c#L6) — [`struct tid_space *`](https://github.com/bluegummi/charmos/blob/main/include/sch/tid.h#L14)`tid_space_init(uint64_t max_id)`
- [`tid_range_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/tid.c#L39) — `static`[`struct tid_range *`](https://github.com/bluegummi/charmos/blob/main/include/sch/tid.h#L7)`tid_range_alloc(`[`struct tid_space`](https://github.com/bluegummi/charmos/blob/main/include/sch/tid.h#L14)` *ts)`
- [`tid_range_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/tid.c#L55) — `static void tid_range_free(`[`struct tid_space`](https://github.com/bluegummi/charmos/blob/main/include/sch/tid.h#L14)` *ts`,[`struct tid_range`](https://github.com/bluegummi/charmos/blob/main/include/sch/tid.h#L7)` *r)`
- [`tid_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/tid.c#L67) — `uint64_t tid_alloc(`[`struct tid_space`](https://github.com/bluegummi/charmos/blob/main/include/sch/tid.h#L14)` *ts)`
- [`tid_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/tid.c#L92) — `void tid_free(`[`struct tid_space`](https://github.com/bluegummi/charmos/blob/main/include/sch/tid.h#L14)` *ts`,`uint64_t id)`

