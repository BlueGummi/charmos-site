+++
title = "uacpi_interface"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/uacpi_interface.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c)

- [`uacpi_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L33) — `void uacpi_init(uint64_t rsdp)`
- [`uacpi_print_devs()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L43) — `void uacpi_print_devs()`
- [`uacpi_kernel_get_rsdp()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L49) — `uacpi_status uacpi_kernel_get_rsdp(uacpi_phys_addr *out_rsdp_address)`
- [`uacpi_kernel_map()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L61) — `void * uacpi_kernel_map(uacpi_phys_addr addr`,`uacpi_size len)`
- [`uacpi_kernel_unmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L66) — `void uacpi_kernel_unmap(void *addr`,`uacpi_size len)`
- [`uacpi_kernel_log()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L70) — `void uacpi_kernel_log(uacpi_log_level level`,`uacpi_char *data)`
- [`uacpi_kernel_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L80) — `void * uacpi_kernel_alloc(uacpi_size size)`
- [`uacpi_kernel_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L85) — `void uacpi_kernel_free(void *mem)`
- [`uacpi_kernel_io_map()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L89) — `uacpi_status uacpi_kernel_io_map(uacpi_io_addr base`,`uacpi_size len`,`uacpi_handle *out_handle)`
- [`uacpi_kernel_io_unmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L109) — `void uacpi_kernel_io_unmap(uacpi_handle h)`
- [`uacpi_kernel_get_nanoseconds_since_boot()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L118) — `uacpi_u64 uacpi_kernel_get_nanoseconds_since_boot(void)`
- [`uacpi_kernel_stall()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L123) — `void uacpi_kernel_stall(uacpi_u8 usec)`
- [`uacpi_kernel_sleep()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L132) — `void uacpi_kernel_sleep(uacpi_u64 msec)`
- [`uacpi_kernel_install_interrupt_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L138) — `uacpi_status uacpi_kernel_install_interrupt_handler(uacpi_u32 irq`,`uacpi_interrupt_handler handler`,`uacpi_handle ctx`,`uacpi_handle *out_irq_handle)`
- [`uacpi_kernel_uninstall_interrupt_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L154) — `uacpi_status uacpi_kernel_uninstall_interrupt_handler(uacpi_interrupt_handler handler`,`uacpi_handle irq_handle)`
- [`uacpi_kernel_create_spinlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L172) — `uacpi_handle uacpi_kernel_create_spinlock(void)`
- [`uacpi_kernel_free_spinlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L177) — `void uacpi_kernel_free_spinlock(uacpi_handle a)`
- [`uacpi_kernel_create_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L181) — `uacpi_handle uacpi_kernel_create_mutex(void)`
- [`uacpi_kernel_free_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L187) — `void uacpi_kernel_free_mutex(uacpi_handle a)`
- [`uacpi_kernel_acquire_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L191) — `uacpi_status uacpi_kernel_acquire_mutex(uacpi_handle m`,`uacpi_u16 b)`
- [`uacpi_kernel_release_mutex()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L197) — `void uacpi_kernel_release_mutex(uacpi_handle m)`
- [`uacpi_kernel_lock_spinlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L201) — `uacpi_cpu_flags uacpi_kernel_lock_spinlock(uacpi_handle a)`
- [`uacpi_kernel_unlock_spinlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L205) — `void uacpi_kernel_unlock_spinlock(uacpi_handle a`,`uacpi_cpu_flags b)`
- [`uacpi_kernel_get_thread_id()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L209) — `uacpi_thread_id uacpi_kernel_get_thread_id(void)`
- [`uacpi_kernel_schedule_work()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L224) — `uacpi_status uacpi_kernel_schedule_work(uacpi_work_type`,`uacpi_work_handler`,`uacpi_handle)`
- [`uacpi_kernel_wait_for_work_completion()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L229) — `uacpi_status uacpi_kernel_wait_for_work_completion(void)`
- [`uacpi_kernel_create_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L234) — `uacpi_handle uacpi_kernel_create_event(void)`
- [`uacpi_kernel_free_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L238) — `void uacpi_kernel_free_event(uacpi_handle a)`
- [`uacpi_kernel_wait_for_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L243) — `uacpi_bool uacpi_kernel_wait_for_event(uacpi_handle`,`uacpi_u16)`
- [`uacpi_kernel_signal_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L246) — `void uacpi_kernel_signal_event(uacpi_handle)`
- [`uacpi_kernel_reset_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L248) — `void uacpi_kernel_reset_event(uacpi_handle)`
- [`uacpi_kernel_handle_firmware_request()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_interface.c#L250) — `uacpi_status uacpi_kernel_handle_firmware_request(uacpi_firmware_request *)`



+++
title = "srat"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/srat.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/srat.c)

- [`srat_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/srat.c#L12) — `void srat_init(void)`
- [`numa_dump()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/srat.c#L126) — `void numa_dump(void)`
- [`slit_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/srat.c#L151) — `void slit_init(void)`



+++
title = "uacpi_rw"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/uacpi_rw.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c)

- [`uacpi_kernel_pci_device_open()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L13) — `uacpi_status uacpi_kernel_pci_device_open(uacpi_pci_address address`,`uacpi_handle *out_handle)`
- [`uacpi_kernel_pci_device_close()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L44) — `void uacpi_kernel_pci_device_close(uacpi_handle handle)`
- [`uacpi_kernel_pci_read8()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L53) — `uacpi_status uacpi_kernel_pci_read8(uacpi_handle device`,`uacpi_size offset`,`uacpi_u8 *value)`
- [`uacpi_kernel_pci_read16()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L64) — `uacpi_status uacpi_kernel_pci_read16(uacpi_handle device`,`uacpi_size offset`,`uacpi_u16 *value)`
- [`uacpi_kernel_pci_read32()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L76) — `uacpi_status uacpi_kernel_pci_read32(uacpi_handle device`,`uacpi_size offset`,`uacpi_u32 *value)`
- [`uacpi_kernel_pci_write8()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L88) — `uacpi_status uacpi_kernel_pci_write8(uacpi_handle device`,`uacpi_size offset`,`uacpi_u8 value)`
- [`uacpi_kernel_pci_write16()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L100) — `uacpi_status uacpi_kernel_pci_write16(uacpi_handle device`,`uacpi_size offset`,`uacpi_u16 value)`
- [`uacpi_kernel_pci_write32()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L112) — `uacpi_status uacpi_kernel_pci_write32(uacpi_handle device`,`uacpi_size offset`,`uacpi_u32 value)`
- [`uacpi_kernel_io_read8()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L130) — `uacpi_status uacpi_kernel_io_read8(uacpi_handle h`,`uacpi_size offset`,`uacpi_u8 *out)`
- [`uacpi_kernel_io_read16()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L138) — `uacpi_status uacpi_kernel_io_read16(uacpi_handle h`,`uacpi_size offset`,`uacpi_u16 *out)`
- [`uacpi_kernel_io_read32()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L146) — `uacpi_status uacpi_kernel_io_read32(uacpi_handle h`,`uacpi_size offset`,`uacpi_u32 *out)`
- [`uacpi_kernel_io_write8()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L154) — `uacpi_status uacpi_kernel_io_write8(uacpi_handle h`,`uacpi_size offset`,`uacpi_u8 val)`
- [`uacpi_kernel_io_write16()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L162) — `uacpi_status uacpi_kernel_io_write16(uacpi_handle h`,`uacpi_size offset`,`uacpi_u16 val)`
- [`uacpi_kernel_io_write32()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/uacpi_rw.c#L170) — `uacpi_status uacpi_kernel_io_write32(uacpi_handle h`,`uacpi_size offset`,`uacpi_u32 val)`



+++
title = "ioapic"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/ioapic.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c)

- [`ioapic_write()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L13) — `void ioapic_write(uint8_t reg`,`uint32_t val)`
- [`ioapic_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L18) — `uint32_t ioapic_read(uint8_t reg)`
- [`make_redirection_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L23) — `static uint64_t make_redirection_entry(uint8_t vector`,`uint8_t dest_apic_id`,`bool masked)`
- [`ioapic_set_redirection_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L36) — `void ioapic_set_redirection_entry(int irq`,`uint64_t entry)`
- [`ioapic_route_irq()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L41) — `void ioapic_route_irq(uint8_t irq`,`uint8_t vector`,`uint8_t dest_apic_id`,`bool masked)`
- [`ioapic_mask_irq()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L47) — `void ioapic_mask_irq(uint8_t irq)`
- [`ioapic_unmask_irq()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L53) — `void ioapic_unmask_irq(uint8_t irq)`
- [`ioapic_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/ioapic.c#L59) — `void ioapic_init(void)`



+++
title = "hpet"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/hpet.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c)

- [`hpet_enable()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L15) — `void hpet_enable(void)`
- [`hpet_disable()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L21) — `void hpet_disable(void)`
- [`hpet_clear_interrupt_status()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L27) — `void hpet_clear_interrupt_status(void)`
- [`hpet_us_to_ticks()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L31) — `static inline uint64_t hpet_us_to_ticks(uint64_t us)`
- [`hpet_setup_periodic_interrupt_us()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L35) — `void hpet_setup_periodic_interrupt_us(uint64_t microseconds_period)`
- [`hpet_program_oneshot()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L52) — `void hpet_program_oneshot(uint64_t future_ms)`
- [`pit_disable()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L72) — `static inline void pit_disable(void)`
- [`hpet_setup_timer()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L78) — `void hpet_setup_timer(uint8_t timer_index`,`uint8_t irq_line`,`bool periodic`,`bool edge_triggered)`
- [`hpet_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L122) — `void hpet_init(void)`
- [`hpet_timestamp_us()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L151) — `uint64_t hpet_timestamp_us(void)`
- [`hpet_timestamp_ms()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/hpet.c#L158) — `uint64_t hpet_timestamp_ms(void)`



+++
title = "shutdown"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/shutdown.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/shutdown.c)

- [`system_shutdown()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/shutdown.c#L10) — `int system_shutdown(void)`
- [`handle_power_button()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/shutdown.c#L29) — `static uacpi_interrupt_ret handle_power_button(uacpi_handle ctx)`
- [`power_button_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/shutdown.c#L34) — `int power_button_init(void)`



+++
title = "cst"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/cst.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/cst.c)

- [`walk_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/cst.c#L11) — `static uacpi_iteration_decision walk_callback(void *`,`uacpi_namespace_node *node`,`uacpi_u32)`
- [`acpi_find_cst()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/cst.c#L26) — `void acpi_find_cst(void)`



+++
title = "lapic"
author = "Unknown"
status = "unknown"
+++

# [kernel/acpi/lapic.c](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c)

- [`lapic_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L12) — `void lapic_init(void)`
- [`lapic_timer_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L17) — `void lapic_timer_init(uint64_t core_id)`
- [`lapic_timer_set_ms()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L41) — `void lapic_timer_set_ms(uint32_t ms)`
- [`lapic_timer_disable()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L47) — `void lapic_timer_disable()`
- [`lapic_timer_enable()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L53) — `void lapic_timer_enable()`
- [`lapic_timer_is_enabled()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L59) — `bool lapic_timer_is_enabled()`
- [`lapic_send_ipi()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L64) — `static void lapic_send_ipi(uint8_t apic_id`,`uint8_t vector)`
- [`x2apic_send_ipi()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L70) — `void x2apic_send_ipi(uint32_t apic_id`,`uint8_t vector)`
- [`broadcast_nmi_except()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L81) — `void broadcast_nmi_except(uint64_t exclude_core)`
- [`cpu_has_x2apic()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L90) — `static int cpu_has_x2apic(void)`
- [`x2apic_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L101) — `void x2apic_init(void)`
- [`x2apic_get_id()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L113) — `uint32_t x2apic_get_id(void)`
- [`lapic_get_id()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L117) — `uint64_t lapic_get_id(void)`
- [`cpu_get_this_id()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L123) — `uint32_t cpu_get_this_id(void)`
- [`ipi_send()`](https://github.com/bluegummi/charmos/blob/main/kernel/acpi/lapic.c#L127) — `void ipi_send(uint32_t apic_id`,`uint8_t vector)`



