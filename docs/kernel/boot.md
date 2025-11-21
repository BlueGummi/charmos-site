+++
title = "gdt"
author = "Unknown"
status = "unknown"
+++

# [kernel/boot/gdt.c](https://github.com/bluegummi/charmos/blob/main/kernel/boot/gdt.c)

- [`gdt_set_tss()`](https://github.com/bluegummi/charmos/blob/main/kernel/boot/gdt.c#L10) — `void gdt_set_tss(`[`struct gdt_entry_tss`](https://github.com/bluegummi/charmos/blob/main/include/boot/gdt.h#L18)` *tss_desc`,`uint64_t base`,`uint32_t limit)`
- [`gdt_set_gate()`](https://github.com/bluegummi/charmos/blob/main/kernel/boot/gdt.c#L23) — `void gdt_set_gate(`[`struct gdt_entry`](https://github.com/bluegummi/charmos/blob/main/include/boot/gdt.h#L4)` *gdt`,`int num`,`uint64_t base`,`uint32_t limit`,`uint8_t access`,`uint8_t gran)`
- [`gdt_load()`](https://github.com/bluegummi/charmos/blob/main/kernel/boot/gdt.c#L34) — `void gdt_load(`[`struct gdt_entry`](https://github.com/bluegummi/charmos/blob/main/include/boot/gdt.h#L4)` *gdt`,`uint64_t n_entries)`
- [`reload_segment_registers()`](https://github.com/bluegummi/charmos/blob/main/kernel/boot/gdt.c#L42) — `void reload_segment_registers(uint16_t cs_selector`,`uint16_t ds_selector)`
- [`gdt_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/boot/gdt.c#L61) — `void gdt_init(`[`struct gdt_entry`](https://github.com/bluegummi/charmos/blob/main/include/boot/gdt.h#L4)` *gdt`,`struct tss *tss)`
- [`gdt_install()`](https://github.com/bluegummi/charmos/blob/main/kernel/boot/gdt.c#L90) — `void gdt_install(void)`



