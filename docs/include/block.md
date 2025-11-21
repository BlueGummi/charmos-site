+++
title = "sched"
author = "Unknown"
status = "unknown"
+++

# [include/block/sched.h](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h)

### struct [`bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122)

| Member Type | Member Name |
|-------------|-------------|
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L123) |
| `uint64_t` | [`request_count`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L125) |
| `bool` | [`dirty`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L128) |


### struct [`bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)

| Member Type | Member Name |
|-------------|-------------|
| [`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68) | [`*disk`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L132) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L133) |
| `uint64_t` | [`total_requests`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L134) |
| [`struct bio_rqueue`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L122) | [`queues[BIO_SCHED_LEVELS]`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L135) |
| `bool` | [`defer_pending`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L136) |


### struct [`bio_scheduler_ops`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L139)

| Member Type | Member Name |
|-------------|-------------|
| `bool` | [`(*should_coalesce)(struct generic_disk *dev,
                            const struct bio_request *a,
                            const struct bio_request *b)`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L140) |
| `void` | [`(*do_coalesce)(struct generic_disk *dev, struct bio_request *into,
                        struct bio_request *from)`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L144) |
| `void` | [`(*reorder)(struct generic_disk *dev)`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L147) |
| `uint32_t` | [`max_wait_time[BIO_SCHED_LEVELS]`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L150) |
| `uint32_t` | [`dispatch_threshold`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L154) |
| `uint64_t` | [`boost_occupance_limit[BIO_SCHED_LEVELS]`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L158) |
| `uint64_t` | [`tick_ms`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L162) |
| `uint64_t` | [`min_wait_ms`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L171) |


- [`update_request_timestamp()`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L206) — `static inline void update_request_timestamp(`[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`submit_if_urgent()`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L210) — `static inline bool submit_if_urgent(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`
- [`sched_is_empty()`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L220) — `static inline bool sched_is_empty(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched)`
- [`submit_if_skip_sched()`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L228) — `static inline bool submit_if_skip_sched(`[`struct bio_scheduler`](https://github.com/bluegummi/charmos/blob/main/include/block/sched.h#L131)` *sched`,[`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)` *req)`



+++
title = "bcache"
author = "Unknown"
status = "unknown"
+++

# [include/block/bcache.h](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h)

### struct [`bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`*buffer`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L20) |
| `uint64_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L22) |
| `uint64_t` | [`lba`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L25) |
| `uint64_t` | [`access_time`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L28) |
| [`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L29) |
| `bool` | [`dirty`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L30) |
| `bool` | [`no_evict`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L31) |
| [`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36) | [`*request`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L34) |
| [`refcount_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L11) | [`refcount`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L36) |


### struct [`bcache_wrapper`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L39)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`key`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L40) |
| [`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18) | [`*value`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L41) |
| `bool` | [`occupied`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L42) |
| [`struct bcache_wrapper`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L39) | [`*next`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L43) |


### struct [`bcache`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L47)

| Member Type | Member Name |
|-------------|-------------|
| [`struct bcache_wrapper`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L39) | [`**entries`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L48) |
| `atomic_uint_fast64_t` | [`ticks`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L49) |
| `uint64_t` | [`capacity`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L50) |
| `uint64_t` | [`count`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L51) |
| `uint64_t` | [`spb`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L52) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L53) |


- [`bcache_hash()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L56) — `static inline uint64_t bcache_hash(uint64_t x`,`uint64_t capacity)`
- [`bcache_increment_ticks()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L91) — `static inline void bcache_increment_ticks(`[`struct bcache`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L47)` *cache)`
- [`bcache_get_ticks()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L95) — `static inline uint64_t bcache_get_ticks(`[`struct bcache`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L47)` *cache)`
- [`bcache_ent_lock()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L99) — `static inline void bcache_ent_lock(`[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent)`
- [`bcache_ent_unlock()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L103) — `static inline void bcache_ent_unlock(`[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent)`
- [`bcache_ent_pin()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L107) — `static inline void bcache_ent_pin(`[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent)`
- [`bcache_ent_unpin()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L111) — `static inline void bcache_ent_unpin(`[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent)`
- [`bcache_ent_acquire()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L115) — `static inline void bcache_ent_acquire(`[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent)`
- [`bcache_ent_release()`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L120) — `static inline void bcache_ent_release(`[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent)`



+++
title = "generic"
author = "Unknown"
status = "unknown"
+++

# [include/block/generic.h](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h)

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



+++
title = "bio"
author = "Unknown"
status = "unknown"
+++

# [include/block/bio.h](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h)

### struct [`bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36)

| Member Type | Member Name |
|-------------|-------------|
| [`enum bio_request_priority`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L10) | [`priority`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L40) |
| [`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68) | [`*disk`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L41) |
| `uint64_t` | [`lba`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L44) |
| `void` | [`*buffer`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L46) |
| `uint64_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L49) |
| `uint64_t` | [`sector_count`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L52) |
| `bool` | [`write`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L54) |
| `void` | [`(*on_complete)(struct bio_request *)`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L57) |
| `void` | [`*user_data`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L58) |
| `bool` | [`done`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L61) |
| [`enum bio_request_status`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L18) | [`status`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L62) |
| `void` | [`*driver_private`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L64) |
| `void` | [`*driver_private2`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L65) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L67) |
| `bool` | [`skip`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L72) |
| `bool` | [`is_aggregate`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L73) |
| [`struct bio_request`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L36) | [`*next_coalesced`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L74) |
| `uint64_t` | [`enqueue_time`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L78) |
| `uint8_t` | [`boost_count`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L82) |


### enum [`bio_request_priority`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L10)

| Name | Value |
|------|-------|
| [`BIO_RQ_BACKGROUND`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L11) | `0` |
| [`BIO_RQ_LOW`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L12) | `1` |
| [`BIO_RQ_MEDIUM`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L13) | `2` |
| [`BIO_RQ_HIGH`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L14) | `3` |
| [`BIO_RQ_URGENT`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L15) | `4` |


### enum [`bio_request_status`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L18)

| Name | Value |
|------|-------|
| [`BIO_STATUS_OK`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L19) | `0` |
| [`BIO_STATUS_INFLIGHT`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L20) | `-1` |
| [`BIO_STATUS_INVAL_ARG`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L21) | `-2` |
| [`BIO_STATUS_INVAL_INTERNAL`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L22) | `-3` |
| [`BIO_STATUS_TIMEOUT`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L23) | `-4` |
| [`BIO_STATUS_DEVICE_FAULT`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L24) | `-5` |
| [`BIO_STATUS_UNCORRECTABLE`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L25) | `-6` |
| [`BIO_STATUS_ABRT`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L26) | `-7` |
| [`BIO_STATUS_MEDIA_CHANGE`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L27) | `-8` |
| [`BIO_STATUS_ID_NOT_FOUND`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L28) | `-9` |
| [`BIO_STATUS_BAD_SECTOR`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L29) | `-10` |
| [`BIO_STATUS_WRITE_PROTECT`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L30) | `-11` |
| [`BIO_STATUS_UNKNOWN_ERR`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L31) | `-12` |



