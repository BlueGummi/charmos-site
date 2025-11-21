+++
title = "printf"
author = "Unknown"
status = "unknown"
+++

# [include/console/printf.h](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h)

### enum [`k_log_level`](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h#L25)

| Name | Value |
|------|-------|
| [`K_INFO`](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h#L26) | `None` |
| [`K_WARN`](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h#L27) | `None` |
| [`K_ERROR`](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h#L28) | `None` |
| [`K_TEST`](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h#L29) | `None` |


- [`k_log_level_color()`](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h#L32) — `static inline const char * k_log_level_color(`[`enum k_log_level`](https://github.com/bluegummi/charmos/blob/main/include/console/printf.h#L25)` l)`



+++
title = "panic"
author = "Unknown"
status = "unknown"
+++

# [include/console/panic.h](https://github.com/bluegummi/charmos/blob/main/include/console/panic.h)

### struct [`panic_regs`](https://github.com/bluegummi/charmos/blob/main/include/console/panic.h#L21)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`rsp`](https://github.com/bluegummi/charmos/blob/main/include/console/panic.h#L22) |
| `uint64_t` | [`r15`](https://github.com/bluegummi/charmos/blob/main/include/console/panic.h#L23) |
| `uint64_t` | [`rsi`](https://github.com/bluegummi/charmos/blob/main/include/console/panic.h#L24) |


- [`qemu_exit()`](https://github.com/bluegummi/charmos/blob/main/include/console/panic.h#L17) — `static inline void qemu_exit(int code)`



