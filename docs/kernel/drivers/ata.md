+++
title = "rw"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ata/rw.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c)

### type alias
[`(*sync_fn)`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L13) : `bool (struct ata_drive *, uint64_t, uint8_t *, uint8_t)`
- [`translate_status()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L15) — `static`[`enum bio_request_status`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L18)`translate_status(uint8_t status`,`uint8_t error)`
- [`ide_irq_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L34) — `void ide_irq_handler(void *ctx`,`uint8_t irq_num`,`void *rsp)`
- [`ide_on_complete()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L103) — `static void ide_on_complete(`[`struct ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63)` *req)`
- [`ide_wait_ready()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L114) — `static void ide_wait_ready(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *d)`
- [`ide_start_next()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L119) — `static void ide_start_next(`[`struct ide_channel`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L83)` *chan`,`bool locked)`
- [`enqueue_request()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L153) — `static void enqueue_request(`[`struct ide_channel`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L83)` *chan`,[`struct ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63)` *req`,`bool locked)`
- [`submit_async()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L166) — `static void submit_async(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *d`,[`struct ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63)` *req)`
- [`submit_and_wait()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L175) — `static inline void submit_and_wait(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *d`,[`struct ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63)` *req)`
- [`request_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L185) — `static`[`struct ide_request *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63)`request_init(uint64_t lba`,`uint8_t *buffer`,`uint8_t count`,`bool write)`
- [`ide_submit_bio_async()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L203) — `bool ide_submit_bio_async(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *bio)`
- [`rw_sync()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L231) — `static bool rw_sync(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *d`,`uint64_t lba`,`uint8_t *b`,`uint8_t cnt`,`bool write)`
- [`rw_sync_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L244) — `static bool rw_sync_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt`,`sync_fn function)`
- [`ide_read_sector()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L264) — `bool ide_read_sector(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *d`,`uint64_t lba`,`uint8_t *b`,`uint8_t count)`
- [`ide_write_sector()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L269) — `bool ide_write_sector(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *d`,`uint64_t lba`,`uint8_t *b`,`uint8_t count)`
- [`ide_read_sector_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L274) — `bool ide_read_sector_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt)`
- [`ide_write_sector_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/rw.c#L279) — `bool ide_write_sector_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt)`



+++
title = "ide"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ata/ide.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ide.c)

- [`ide_print_info()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ide.c#L15) — `void ide_print_info(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d)`
- [`swap_str()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ide.c#L21) — `static void swap_str(char *dst`,`uint16_t *src`,`uint64_t word_len)`
- [`ide_identify()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ide.c#L36) — `void ide_identify(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *drive)`
- [`ide_create_generic()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ide.c#L135) — [`struct generic_disk *`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)`ide_create_generic(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *ide)`



+++
title = "ata"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ata/ata.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ata.c)

- [`ata_select_drive()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ata.c#L12) — `void ata_select_drive(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *ata_drive)`
- [`ata_soft_reset()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ata.c#L19) — `void ata_soft_reset(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *ata_drive)`
- [`ata_identify()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ata.c#L39) — `bool ata_identify(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *ata_drive)`
- [`ata_setup_drive()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ata.c#L66) — `bool ata_setup_drive(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *ide`,[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *devices`,`uint64_t count`,`int channel`,`bool is_slave)`
- [`ata_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/ata.c#L130) — `void ata_init(`[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *devices`,`uint64_t count)`



+++
title = "atapi"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/ata/atapi.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/atapi.c)

- [`atapi_identify()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/atapi.c#L13) — `bool atapi_identify(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *ide)`
- [`atapi_read_sector()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/atapi.c#L40) — `bool atapi_read_sector(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buffer`,`uint64_t sector_count)`
- [`atapi_write_sector()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/atapi.c#L111) — `bool atapi_write_sector(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buffer`,`uint64_t sector_count)`
- [`atapi_read_sector_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/atapi.c#L121) — `bool atapi_read_sector_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t start_lba`,`uint8_t *buffer`,`uint64_t sector_count)`
- [`atapi_print_info()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/atapi.c#L133) — `void atapi_print_info(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`
- [`atapi_create_generic()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/ata/atapi.c#L138) — [`struct generic_disk *`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)`atapi_create_generic(`[`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)` *d)`



