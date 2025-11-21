+++
title = "isr_stubs"
author = "Unknown"
status = "unknown"
+++

# [kernel/int/isr_stubs.h](https://github.com/bluegummi/charmos/blob/main/kernel/int/isr_stubs.h)


+++
title = "kb"
author = "Unknown"
status = "unknown"
+++

# [kernel/int/kb.c](https://github.com/bluegummi/charmos/blob/main/kernel/int/kb.c)

- [`keyboard_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/kb.c#L35) — `void keyboard_handler(void *a)`



+++
title = "idt"
author = "Unknown"
status = "unknown"
+++

# [kernel/int/idt.c](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c)

- [`isr_common_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L48) — `void isr_common_entry(uint8_t vector`,`void *rsp)`
- [`isr_timer_routine()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L77) — `void isr_timer_routine(void *ctx`,`uint8_t vector`,`void *rsp)`
- [`nop_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L86) — `static void nop_handler(void *ctx`,`uint8_t vector`,`void *rsp)`
- [`panic_isr()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L90) — `void panic_isr(void *ctx`,`uint8_t vector`,`void *rsp)`
- [`irq_register()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L100) — `void irq_register(uint8_t vector`,`irq_handler_t handler`,`void *ctx)`
- [`idt_set_gate()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L110) — `void idt_set_gate(uint8_t num`,`uint64_t base`,`uint16_t sel`,`uint8_t flags)`
- [`idt_install_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L127) — `int idt_install_handler(uint8_t flags`,`void (*handler)(void))`
- [`idt_load()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L136) — `void idt_load(void)`
- [`irq_alloc_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L142) — `int irq_alloc_entry()`
- [`irq_set_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L152) — `void irq_set_alloc(int entry`,`bool used)`
- [`irq_is_installed()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L156) — `bool irq_is_installed(int entry)`
- [`irq_free_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L160) — `void irq_free_entry(int entry)`
- [`page_fault_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L168) — `static void page_fault_handler(void *context`,`uint8_t vector`,`void *rsp)`
- [`idt_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/idt.c#L210) — `void idt_init()`



+++
title = "isr_vectors_array"
author = "Unknown"
status = "unknown"
+++

# [kernel/int/isr_vectors_array.h](https://github.com/bluegummi/charmos/blob/main/kernel/int/isr_vectors_array.h)


+++
title = "irq"
author = "Unknown"
status = "unknown"
+++

# [kernel/int/irq.c](https://github.com/bluegummi/charmos/blob/main/kernel/int/irq.c)

- [`irq_mark_self_in_interrupt()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/irq.c#L3) — `void irq_mark_self_in_interrupt(bool new)`
- [`irq_in_interrupt()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/irq.c#L7) — `bool irq_in_interrupt(void)`
- [`irq_in_thread_context()`](https://github.com/bluegummi/charmos/blob/main/kernel/int/irq.c#L11) — `bool irq_in_thread_context(void)`



