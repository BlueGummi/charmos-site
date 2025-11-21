+++
title = "kb"
author = "Unknown"
status = "unknown"
+++

# [include/int/kb.h](https://github.com/bluegummi/charmos/blob/main/include/int/kb.h)


+++
title = "idt"
author = "Unknown"
status = "unknown"
+++

# [include/int/idt.h](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h)

### struct [`idt_entry`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L8)

| Member Type | Member Name |
|-------------|-------------|
| `uint16_t` | [`base_low`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L9) |
| `uint16_t` | [`selector`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L10) |
| `uint8_t` | [`ist`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L11) |
| `uint8_t` | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L12) |
| `uint16_t` | [`base_mid`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L13) |
| `uint32_t` | [`base_high`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L14) |
| `uint32_t` | [`reserved`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L15) |


### struct [`idt_table`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L18)

| Member Type | Member Name |
|-------------|-------------|
| [`struct idt_entry`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L8) | [`entries[IDT_ENTRIES]`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L19) |


### struct [`idt_ptr`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L22)

| Member Type | Member Name |
|-------------|-------------|
| `uint16_t` | [`limit`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L23) |
| `uint64_t` | [`base`](https://github.com/bluegummi/charmos/blob/main/include/int/idt.h#L24) |



+++
title = "irq"
author = "Unknown"
status = "unknown"
+++

# [include/int/irq.h](https://github.com/bluegummi/charmos/blob/main/include/int/irq.h)

### struct [`irq_entry`](https://github.com/bluegummi/charmos/blob/main/include/int/irq.h#L7)

| Member Type | Member Name |
|-------------|-------------|
| `irq_handler_t` | [`handler`](https://github.com/bluegummi/charmos/blob/main/include/int/irq.h#L8) |
| `void` | [`*ctx`](https://github.com/bluegummi/charmos/blob/main/include/int/irq.h#L9) |


### struct [`irq_context`](https://github.com/bluegummi/charmos/blob/main/include/int/irq.h#L25)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`rax`](https://github.com/bluegummi/charmos/blob/main/include/int/irq.h#L26) |


### type alias
[`(*irq_handler_t)`](https://github.com/bluegummi/charmos/blob/main/include/int/irq.h#L5) : `void (void *ctx, uint8_t vector, void *rsp)`

