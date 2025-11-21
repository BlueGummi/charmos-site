+++
title = "printf"
author = "Unknown"
status = "unknown"
+++

# [kernel/console/printf.c](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c)

### struct [`printf_cursor`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L18)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*buffer`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L19) |
| `int` | [`buffer_len`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L20) |
| `int` | [`cursor`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L21) |


- [`serial_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L24) — `void serial_init()`
- [`serial_is_transmit_empty()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L40) — `static int serial_is_transmit_empty()`
- [`serial_putc()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L44) — `static void serial_putc(char c)`
- [`serial_puts()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L51) — `void serial_puts(`[`struct printf_cursor`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L18)` *csr`,`char *str`,`int len)`
- [`double_print()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L65) — `void double_print(struct flanterm_context *f`,[`struct printf_cursor`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L18)` *csr`,`char *str`,`int len)`
- [`k_printf_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L72) — `void k_printf_init(`[`struct limine_framebuffer`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L206)` *fb)`
- [`print_signed()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L84) — `static int print_signed(char *buffer`,`int64_t num)`
- [`print_unsigned()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L113) — `static int print_unsigned(char *buffer`,`uint64_t num)`
- [`print_hex()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L130) — `static int print_hex(char *buffer`,`uint64_t num)`
- [`print_hex_upper()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L148) — `static int print_hex_upper(char *buffer`,`uint64_t num)`
- [`print_binary()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L165) — `static int print_binary(char *buffer`,`uint64_t num)`
- [`print_octal()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L186) — `static int print_octal(char *buffer`,`uint64_t num)`
- [`apply_padding()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L209) — `static void apply_padding(char *str`,`int len`,`int width`,`bool left_align`,`bool zero_pad`,[`struct printf_cursor`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L18)` *csr)`
- [`handle_format_specifier()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L237) — `static void handle_format_specifier(`[`struct printf_cursor`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L18)` *csr`,`char **format_ptr`,`va_list args)`
- [`v_k_printf()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L402) — `void v_k_printf(`[`struct printf_cursor`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L18)` *csr`,`char *format`,`va_list args)`
- [`k_printf()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L419) — `void k_printf(char *format)`
- [`snprintf()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L434) — `int snprintf(char *buffer`,`int buffer_len`,`char *format)`
- [`panic()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/printf.c#L456) — `void panic(char *format)`



+++
title = "panic"
author = "Unknown"
status = "unknown"
+++

# [kernel/console/panic.c](https://github.com/bluegummi/charmos/blob/main/kernel/console/panic.c)

- [`panic_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/console/panic.c#L7) — `void panic_handler(`[`struct panic_regs`](https://github.com/bluegummi/charmos/blob/main/include/console/panic.h#L21)` *regs)`



