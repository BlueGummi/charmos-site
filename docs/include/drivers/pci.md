# [include/drivers/pci.h](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h)

<!-- Auto-generated from pci.h, do not edit manually -->

### struct [`pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`bus`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L10) |
| `uint8_t` | [`device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L11) |
| `uint8_t` | [`function`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L12) |
| `uint16_t` | [`vendor_id`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L14) |
| `uint16_t` | [`device_id`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L15) |
| `uint8_t` | [`class_code`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L17) |
| `uint8_t` | [`subclass`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L18) |
| `uint8_t` | [`prog_if`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L19) |
| `uint8_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L20) |


### struct [`pci_driver`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L23)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L24) |
| `uint8_t` | [`class_code`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L25) |
| `uint8_t` | [`subclass`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L26) |
| `uint8_t` | [`prog_if`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L27) |
| `uint16_t` | [`vendor_id`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L28) |
| `void` | [`(*initialize)(uint8_t, uint8_t, uint8_t, struct pci_device *)`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L29) |


### struct [`pci_msix_table_entry`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L62)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`msg_addr_low`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L63) |
| `uint32_t` | [`msg_addr_high`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L64) |
| `uint32_t` | [`msg_data`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L65) |
| `uint32_t` | [`vector_ctrl`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L66) |


### struct [`pci_msix_cap`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L69)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`cap_id`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L70) |
| `uint8_t` | [`next_ptr`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L71) |
| `uint16_t` | [`msg_ctl`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L72) |
| `uint32_t` | [`table_offset_bir`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L73) |
| `uint32_t` | [`pba_offset_bir`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L74) |


- [`pci_read_config16()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L91) — `static inline uint16_t pci_read_config16(uint8_t bus`,`uint8_t device`,`uint8_t function`,`uint8_t offset)`
- [`pci_read_config8()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L106) — `static inline uint8_t pci_read_config8(uint8_t bus`,`uint8_t device`,`uint8_t function`,`uint8_t offset)`
- [`pci_write_config16()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L117) — `static inline void pci_write_config16(uint8_t bus`,`uint8_t device`,`uint8_t function`,`uint8_t offset`,`uint16_t value)`
- [`pci_config_address()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L136) — `static inline uint32_t pci_config_address(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t offset)`
- [`pci_read()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L142) — `static inline uint32_t pci_read(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t offset)`
- [`pci_read_word()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L148) — `static inline uint16_t pci_read_word(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t offset)`
- [`pci_read_byte()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L154) — `static inline uint8_t pci_read_byte(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t offset)`
- [`pci_write()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L160) — `static inline void pci_write(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t offset`,`uint32_t value)`
- [`pci_write_word()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L166) — `static inline void pci_write_word(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t offset`,`uint16_t value)`
- [`pci_write_byte()`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L174) — `static inline void pci_write_byte(uint8_t bus`,`uint8_t slot`,`uint8_t func`,`uint8_t offset`,`uint8_t value)`

