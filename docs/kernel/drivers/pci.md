# [kernel/drivers/pci.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c)

<!-- Auto-generated from pci.c, do not edit manually -->

- [`pci_class_name()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L13) — `const char * pci_class_name(uint8_t class_code`,`uint8_t subclass)`
- [`init_device()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L39) — `static void init_device(`[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *dev)`
- [`pci_init_devices()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L57) — `void pci_init_devices(`[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *devices`,`uint64_t count)`
- [`pci_scan_devices()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L69) — `void pci_scan_devices(`[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` **devices_out`,`uint64_t *count_out)`
- [`pci_find_capability()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L149) — `uint8_t pci_find_capability(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t cap_id)`
- [`pci_read_bar()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L164) — `uint32_t pci_read_bar(uint8_t bus`,`uint8_t device`,`uint8_t function`,`uint8_t bar_index)`
- [`pci_read_bar64()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L170) — `static uint64_t pci_read_bar64(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t bar_index)`
- [`pci_program_msix_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L182) — `void pci_program_msix_entry(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint32_t table_index`,`uint8_t vector`,`uint8_t apic_id)`
- [`pci_enable_msix_on_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L234) — `void pci_enable_msix_on_core(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t vector_index`,`uint8_t apic_id)`
- [`pci_enable_msix()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/pci.c#L280) — `void pci_enable_msix(uint8_t bus`,`uint8_t slot`,`uint8_t func)`

