# [include/block/generic.h](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h)

<!-- Auto-generated from generic.h, do not edit manually -->

### struct [`generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)

| Member Type | Member Name |
|-------------|-------------|
| [`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68) | [`*disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L42) |
| `uint64_t` | [`start_lba`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L43) |
| `uint64_t` | [`sector_count`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L44) |
| [`enum fs_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/detect.h#L4) | [`fs_type`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L45) |
| `void` | [`*fs_data`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L46) |
| `char` | [`name[16]`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L47) |
| `bool` | [`mounted`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L48) |
| [`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198) | [`*(*mount)(struct generic_partition *)`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L50) |


### struct [`generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)

| Member Type | Member Name |
|-------------|-------------|
| [`enum disk_flags`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L53) | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L69) |
| [`enum generic_disk_type`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L14) | [`type`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L70) |
| [`enum fs_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/detect.h#L4) | [`fs_type`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L71) |
| `void` | [`*fs_data`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L72) |
| `char` | [`name[16]`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L73) |
| `uint64_t` | [`total_sectors`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L74) |
| `bool` | [`is_removable`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L75) |
| `void` | [`*driver_data`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L76) |
| `uint32_t` | [`sector_size`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L77) |
| `bool` | [`(*read_sector)(struct generic_disk *disk, uint64_t lba,
                        uint8_t *buffer, uint64_t sector_count)`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L86) |
| `bool` | [`(*write_sector)(struct generic_disk *disk, uint64_t lba,
                         const uint8_t *buffer, uint64_t sector_count)`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L89) |
| `bool` | [`(*submit_bio_async)(struct generic_disk *disk,
                             struct bio_request *bio)`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L93) |
| [`struct bio_scheduler_ops`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L139) | [`*ops`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L96) |
| [`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131) | [`*scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L97) |
| [`struct bcache`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L47) | [`*cache`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L98) |
| `uint64_t` | [`partition_count`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L99) |
| [`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41) | [`*partitions`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L100) |


### enum [`generic_disk_type`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L14)

| Name | Value |
|------|-------|
| [`G_IDE_DRIVE`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L15) | `None` |
| [`G_NVME_DRIVE`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L16) | `None` |
| [`G_AHCI_DRIVE`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L17) | `None` |
| [`G_ATAPI_DRIVE`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L18) | `None` |


### enum [`disk_flags`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L53)

| Name | Value |
|------|-------|
| [`DISK_FLAG_NO_REORDER`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L55) | `1` |
| [`DISK_FLAG_NO_COALESCE`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L58) | `1 << 1` |
| [`DISK_FLAG_NO_SCHED`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L65) | `1 << 2` |


- [`get_generic_disk_str()`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L21) — `static inline const char * get_generic_disk_str(`[`enum generic_disk_type`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L14)` type)`
- [`get_generic_disk_dev_str()`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L31) — `static inline const char * get_generic_disk_dev_str(`[`enum generic_disk_type`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L14)` t)`
- [`disk_skip_coalesce()`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L103) — `static inline bool disk_skip_coalesce(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`
- [`disk_skip_sched()`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L107) — `static inline bool disk_skip_sched(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`
- [`disk_skip_reorder()`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L111) — `static inline bool disk_skip_reorder(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`

