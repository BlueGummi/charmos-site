+++
title = "uacpi_interface"
author = "Unknown"
status = "unknown"
+++

# [include/acpi/uacpi_interface.h](https://github.com/bluegummi/charmos/blob/main/include/acpi/uacpi_interface.h)

### type alias
[`uacpi_pci_device`](https://github.com/bluegummi/charmos/blob/main/include/acpi/uacpi_interface.h#L6) : `struct { // typedefing it because of consistency with uacpi naming uint8_t bus, slot, func; bool is_open; }`
### type alias
[`uacpi_io_handle`](https://github.com/bluegummi/charmos/blob/main/include/acpi/uacpi_interface.h#L11) : `struct { uacpi_io_addr base; uacpi_size len; bool valid; }`
### type alias
[`irq_entry_t`](https://github.com/bluegummi/charmos/blob/main/include/acpi/uacpi_interface.h#L17) : `struct { uacpi_interrupt_handler handler; uacpi_handle ctx; bool installed; }`

+++
title = "print"
author = "Unknown"
status = "unknown"
+++

# [include/acpi/print.h](https://github.com/bluegummi/charmos/blob/main/include/acpi/print.h)


+++
title = "acpi"
author = "Unknown"
status = "unknown"
+++

# [include/acpi/acpi.h](https://github.com/bluegummi/charmos/blob/main/include/acpi/acpi.h)


+++
title = "ioapic"
author = "Unknown"
status = "unknown"
+++

# [include/acpi/ioapic.h](https://github.com/bluegummi/charmos/blob/main/include/acpi/ioapic.h)

### struct [`ioapic_info`](https://github.com/bluegummi/charmos/blob/main/include/acpi/ioapic.h#L4)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`id`](https://github.com/bluegummi/charmos/blob/main/include/acpi/ioapic.h#L5) |
| `uint32_t` | [`gsi_base`](https://github.com/bluegummi/charmos/blob/main/include/acpi/ioapic.h#L6) |
| `uint32_t` | [`*mmio_base`](https://github.com/bluegummi/charmos/blob/main/include/acpi/ioapic.h#L7) |



+++
title = "hpet"
author = "Unknown"
status = "unknown"
+++

# [include/acpi/hpet.h](https://github.com/bluegummi/charmos/blob/main/include/acpi/hpet.h)

- [`hpet_write64()`](https://github.com/bluegummi/charmos/blob/main/include/acpi/hpet.h#L67) — `static inline void hpet_write64(uint64_t offset`,`uint64_t value)`
- [`hpet_read64()`](https://github.com/bluegummi/charmos/blob/main/include/acpi/hpet.h#L71) — `static inline uint64_t hpet_read64(uint64_t offset)`



+++
title = "cst"
author = "Unknown"
status = "unknown"
+++

# [include/acpi/cst.h](https://github.com/bluegummi/charmos/blob/main/include/acpi/cst.h)


+++
title = "lapic"
author = "Unknown"
status = "unknown"
+++

# [include/acpi/lapic.h](https://github.com/bluegummi/charmos/blob/main/include/acpi/lapic.h)

- [`lapic_reg_to_x2apic_msr()`](https://github.com/bluegummi/charmos/blob/main/include/acpi/lapic.h#L49) — `static inline uint32_t lapic_reg_to_x2apic_msr(uint32_t reg)`
- [`lapic_write()`](https://github.com/bluegummi/charmos/blob/main/include/acpi/lapic.h#L62) — `static inline void lapic_write(uint32_t reg`,`uint32_t val)`
- [`lapic_read()`](https://github.com/bluegummi/charmos/blob/main/include/acpi/lapic.h#L73) — `static inline uint32_t lapic_read(uint32_t reg)`



