+++
title = "rw"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/nvme/rw.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c)

### type alias
[`(*sync_fn)`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L15) : `bool (struct generic_disk *, uint64_t, uint8_t *, uint16_t)`
### type alias
[`(*async_fn)`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L16) : `bool (struct generic_disk *, struct nvme_request *)`
- [`enqueue_request()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L18) — `static void enqueue_request(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *dev`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req)`
- [`nvme_bio_fill_prps()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L28) — `static bool nvme_bio_fill_prps(`[`struct nvme_bio_data`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L73)` *data`,`void *buffer`,`uint64_t size)`
- [`nvme_setup_prps()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L49) — `static void nvme_setup_prps(`[`struct nvme_command`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L10)` *cmd`,[`struct nvme_bio_data`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L73)` *data)`
- [`rw_send_command()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L74) — `static bool rw_send_command(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req`,`uint8_t opc)`
- [`rw_sync()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L122) — `static bool rw_sync(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buffer`,`uint16_t count`,`async_fn function)`
- [`rw_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L145) — `static bool rw_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt`,`sync_fn function)`
- [`rw_async_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L164) — `static bool rw_async_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req`,`async_fn function)`
- [`nvme_read_sector()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L193) — `bool nvme_read_sector(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buffer`,`uint16_t count)`
- [`nvme_write_sector()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L198) — `bool nvme_write_sector(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buffer`,`uint16_t count)`
- [`nvme_read_sector_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L203) — `bool nvme_read_sector_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt)`
- [`nvme_write_sector_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L208) — `bool nvme_write_sector_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t lba`,`uint8_t *buf`,`uint64_t cnt)`
- [`nvme_read_sector_async()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L213) — `bool nvme_read_sector_async(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req)`
- [`nvme_write_sector_async()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L218) — `bool nvme_write_sector_async(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req)`
- [`nvme_write_sector_async_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L223) — `bool nvme_write_sector_async_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req)`
- [`nvme_read_sector_async_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L228) — `bool nvme_read_sector_async_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req)`
- [`nvme_send_nvme_req()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/rw.c#L233) — `bool nvme_send_nvme_req(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *r)`



+++
title = "init"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/nvme/init.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/init.c)

- [`nvme_enable_controller()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/init.c#L17) — `void nvme_enable_controller(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme)`
- [`nvme_setup_admin_queues()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/init.c#L50) — `void nvme_setup_admin_queues(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme)`
- [`nvme_alloc_admin_queues()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/init.c#L67) — `void nvme_alloc_admin_queues(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme)`
- [`nvme_alloc_io_queues()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/init.c#L94) — `void nvme_alloc_io_queues(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme`,`uint32_t qid)`



+++
title = "cmd"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/nvme/cmd.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c)

- [`nvme_to_bio_status()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L21) — `static`[`enum bio_request_status`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L18)`nvme_to_bio_status(uint16_t status)`
- [`nvme_send_waiters()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L31) — `static void nvme_send_waiters(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *dev)`
- [`nvme_process_one()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L50) — `static void nvme_process_one(`[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req)`
- [`nvme_finished_pop_front()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L66) — `static`[`struct nvme_request *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)`nvme_finished_pop_front(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *dev)`
- [`nvme_work()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L80) — `void nvme_work(void *dvoid`,`void *nothing)`
- [`nvme_process_completions()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L96) — `void nvme_process_completions(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *dev`,`uint32_t qid)`
- [`nvme_isr_handler()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L138) — `void nvme_isr_handler(void *ctx`,`uint8_t vector`,`void *rsp)`
- [`nvme_submit_io_cmd()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L145) — `void nvme_submit_io_cmd(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme`,[`struct nvme_command`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L10)` *cmd`,`uint32_t qid`,[`struct nvme_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L78)` *req)`
- [`nvme_submit_admin_cmd()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L172) — `uint16_t nvme_submit_admin_cmd(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme`,[`struct nvme_command`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L10)` *cmd`,`uint32_t *dw0_out)`
- [`nvme_identify_controller()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L211) — `uint8_t * nvme_identify_controller(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme)`
- [`nvme_set_num_queues()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L236) — `uint32_t nvme_set_num_queues(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme`,`uint16_t desired_sq`,`uint16_t desired_cq)`
- [`nvme_identify_namespace()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/cmd.c#L260) — `uint8_t * nvme_identify_namespace(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme`,`uint32_t nsid)`



+++
title = "nvme"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/nvme/nvme.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/nvme.c)

- [`nvme_discover_device()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/nvme.c#L19) — [`struct nvme_device *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)`nvme_discover_device(uint8_t bus`,`uint8_t slot`,`uint8_t func)`
- [`nvme_print_wrapper()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/nvme.c#L151) — `void nvme_print_wrapper(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *d)`
- [`nvme_create_generic()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/nvme.c#L184) — [`struct generic_disk *`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)`nvme_create_generic(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *nvme)`
- [`nvme_pci_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/nvme.c#L209) — `static void nvme_pci_init(uint8_t bus`,`uint8_t device`,`uint8_t function`,[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *dev)`



+++
title = "internal"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/nvme/internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/internal.h)

- [`nvme_work_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/nvme/internal.h#L46) — `static inline`[`enum workqueue_error`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L242)`nvme_work_enqueue(`[`struct nvme_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/nvme.h#L124)` *dev`,[`struct work`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L32)` *work)`



