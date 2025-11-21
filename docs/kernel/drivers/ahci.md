+++
title = "rw"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ahci/rw.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c)

### type alias
[`(*async_fn)`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L24) : `bool (struct generic_disk *, uint64_t, uint8_t *, uint16_t, struct ahci_request *)`
### type alias
[`(*sync_fn)`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L27) : `bool (struct generic_disk *, uint64_t, uint8_t *, uint16_t)`
- [`ahci_set_lba_cmd()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L9) — `static void ahci_set_lba_cmd(`[`struct ahci_fis_reg_h2d`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L92)` *fis`,`uint64_t lba`,`uint16_t sector_count)`
- [`rw_async()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L29) — `static bool rw_async(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint16_t count`,[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req`,`bool write)`
- [`rw_sync()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L57) — `static bool rw_sync(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint16_t count`,`async_fn function)`
- [`rw_sync_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L86) — `static bool rw_sync_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt`,`sync_fn function)`
- [`rw_async_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L105) — `static bool rw_async_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt`,[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req`,`async_fn function)`
- [`ahci_read_sector_async()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L124) — `bool ahci_read_sector_async(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint16_t count`,[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req)`
- [`ahci_write_sector_async()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L130) — `bool ahci_write_sector_async(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *in_buf`,`uint16_t count`,[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req)`
- [`ahci_read_sector_blocking()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L136) — `bool ahci_read_sector_blocking(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint16_t count)`
- [`ahci_write_sector_blocking()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L141) — `bool ahci_write_sector_blocking(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint16_t count)`
- [`ahci_read_sector_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L146) — `bool ahci_read_sector_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt)`
- [`ahci_write_sector_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L151) — `bool ahci_write_sector_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt)`
- [`ahci_write_sector_async_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L157) — `bool ahci_write_sector_async_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt`,[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req)`
- [`ahci_read_sector_async_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/rw.c#L164) — `bool ahci_read_sector_async_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt`,[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req)`



+++
title = "ahci"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ahci/ahci.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/ahci.c)

- [`ahci_discover_device()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/ahci.c#L12) — [`struct ahci_disk *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L218)`ahci_discover_device(uint8_t bus`,`uint8_t device`,`uint8_t function`,`uint32_t *out_disk_count)`
- [`ahci_print_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/ahci.c#L54) — `void ahci_print_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d)`
- [`ahci_create_generic()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/ahci.c#L84) — [`struct generic_disk *`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)`ahci_create_generic(`[`struct ahci_disk`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L218)` *disk)`
- [`ahci_pci_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/ahci.c#L109) — `static void ahci_pci_init(uint8_t bus`,`uint8_t slot`,`uint8_t func`,[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *dev)`



+++
title = "init"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ahci/init.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/init.c)

- [`setup_port_slots()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/init.c#L18) — `static void setup_port_slots(`[`struct ahci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L199)` *dev`,`uint32_t port_id)`
- [`allocate_port()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/init.c#L38) — `static void allocate_port(`[`struct ahci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L199)` *dev`,[`struct ahci_port`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L176)` *port`,`uint32_t port_num)`
- [`device_setup()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/init.c#L66) — `static`[`struct ahci_disk *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L218)`device_setup(`[`struct ahci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L199)` *dev`,[`struct ahci_controller`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L224)` *ctrl`,`uint32_t *disk_count)`
- [`ahci_setup_controller()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/init.c#L162) — [`struct ahci_disk *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L218)`ahci_setup_controller(`[`struct ahci_controller`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L224)` *ctrl`,`uint32_t *d_cnt)`



+++
title = "cmd"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ahci/cmd.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c)

- [`ahci_process_completions()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L20) — `void ahci_process_completions(`[`struct ahci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L199)` *dev`,`uint32_t port)`
- [`ahci_isr_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L55) — `void ahci_isr_handler(void *ctx`,`uint8_t vector`,`void *rsp)`
- [`ahci_send_command()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L69) — `void ahci_send_command(`[`struct ahci_disk`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L218)` *disk`,[`struct ahci_full_port`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L166)` *port`,[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req)`
- [`try_find_slot()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L81) — `static uint32_t try_find_slot(`[`struct ahci_full_port`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L166)` *p)`
- [`ahci_find_slot()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L99) — `uint32_t ahci_find_slot(`[`struct ahci_full_port`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L166)` *p)`
- [`ahci_prepare_command()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L111) — `void ahci_prepare_command(`[`struct ahci_full_port`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L166)` *port`,`uint32_t slot`,`bool write`,`uint8_t *buf`,`uint64_t size)`
- [`ahci_setup_fis()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L154) — `void ahci_setup_fis(`[`struct ahci_cmd_table`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L159)` *cmd_tbl`,`uint8_t command`,`bool is_atapi)`
- [`ahci_identify()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L168) — `void ahci_identify(`[`struct ahci_disk`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L218)` *disk)`
- [`ahci_on_bio_complete()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L202) — `static void ahci_on_bio_complete(`[`struct ahci_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ahci.h#L272)` *req)`
- [`ahci_submit_bio_request()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ahci/cmd.c#L214) — `bool ahci_submit_bio_request(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *bio)`



