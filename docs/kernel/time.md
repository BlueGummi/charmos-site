# [kernel/time.c](https://github.com/bluegummi/charmos/blob/main/kernel/time.c)

<!-- Auto-generated from time.c, do not edit manually -->

- [`time_print_unix()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L13) — `void time_print_unix(uint32_t timestamp)`
- [`time_print_current()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L53) — `void time_print_current()`
- [`is_leap()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L57) — `static uint32_t is_leap(int year)`
- [`days_in_month()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L61) — `static uint32_t days_in_month(int year`,`int month)`
- [`datetime_to_unix()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L68) — `static uint32_t datetime_to_unix(int year`,`int month`,`int day`,`int hour`,`int minute`,`int second)`
- [`cmos_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L89) — `static inline uint8_t cmos_read(uint8_t reg)`
- [`is_updating()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L94) — `static bool is_updating()`
- [`bcd_to_bin()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L99) — `static uint8_t bcd_to_bin(uint8_t bcd)`
- [`time_get_unix()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L125) — `uint32_t time_get_unix()`
- [`time_get_ms()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L131) — `uint64_t time_get_ms(void)`
- [`time_get_us()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L135) — `uint64_t time_get_us(void)`
- [`tsc_calibrate()`](https://github.com/bluegummi/charmos/blob/main/kernel/time.c#L158) — `uint64_t tsc_calibrate(void)`

