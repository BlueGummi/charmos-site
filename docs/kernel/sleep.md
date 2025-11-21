+++
title = "sleep"
author = "Unknown"
status = "unknown"
+++

# [kernel/sleep.c](https://github.com/bluegummi/charmos/blob/main/kernel/sleep.c)

- [`sleep_hpet_fs()`](https://github.com/bluegummi/charmos/blob/main/kernel/sleep.c#L9) — `static void sleep_hpet_fs(uint64_t femtoseconds)`
- [`sleep_ms()`](https://github.com/bluegummi/charmos/blob/main/kernel/sleep.c#L19) — `void sleep_ms(uint64_t ms)`
- [`sleep_us()`](https://github.com/bluegummi/charmos/blob/main/kernel/sleep.c#L23) — `void sleep_us(uint64_t us)`
- [`sleep()`](https://github.com/bluegummi/charmos/blob/main/kernel/sleep.c#L27) — `void sleep(uint64_t seconds)`
- [`mmio_wait()`](https://github.com/bluegummi/charmos/blob/main/kernel/sleep.c#L31) — `bool mmio_wait(uint32_t *reg`,`uint32_t mask`,`uint64_t timeout)`

