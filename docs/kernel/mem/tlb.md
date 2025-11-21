+++
title = "tlb"
author = "Unknown"
status = "unknown"
+++

# [kernel/mem/tlb.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/tlb.c)

- [`tlb_shootdown_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/tlb.c#L10) — `static void tlb_shootdown_internal(void)`
- [`tlb_shootdown_isr()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/tlb.c#L44) — `void tlb_shootdown_isr(void *ctx`,`uint8_t irq`,`void *rsp)`
- [`tlb_dpc_func()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/tlb.c#L53) — `void tlb_dpc_func(void *ctx)`
- [`tlb_shootdown()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/tlb.c#L57) — `void tlb_shootdown(uintptr_t addr`,`bool synchronous)`
- [`tlb_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/tlb.c#L110) — `void tlb_init(void)`

