# [kernel/mem/slab/internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h)

<!-- Auto-generated from internal.h, do not edit manually -->

### struct [`slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140) | [`*self`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L141) |
| `uint8_t` | [`*bitmap`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L150) |
| [`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13) | [`mem`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L151) |
| `size_t` | [`used`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L152) |
| [`struct slab_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L254) | [`*parent_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L153) |
| [`enum slab_type`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L135) | [`type`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L155) |
| [`enum slab_state`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L127) | [`state`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L156) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L157) |
| [`struct page`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L38) | [`*backing_page`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L159) |
| `size_t` | [`pages`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L160) |
| [`struct rbt_node`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L18) | [`rb`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L163) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`list`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L164) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`gc_enqueue_time_ms`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L166) |
| `size_t` | [`recycle_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L168) |


### struct [`slab_magazine`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L182)

| Member Type | Member Name |
|-------------|-------------|
| [`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13) | [`objs[SLAB_MAG_ENTRIES]`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L183) |
| `size_t` | [`count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L184) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L185) |


### struct [`slab_percpu_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L193)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_magazine`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L182) | [`*mag`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L195) |
| [`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423) | [`*domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L196) |


### struct [`slab_free_slot`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L199)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_uint_fast64_t` | [`seq`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L200) |
| [`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13) | [`addr`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L201) |


### struct [`slab_free_queue_list_node`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L224)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_free_queue_list_node`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L224) | [`*next`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L225) |


### struct [`slab_free_queue_list`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L228)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_free_queue_list_node`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L224) | [`*head`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L229) |
| [`struct slab_free_queue_list_node`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L224) | [`*tail`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L230) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L231) |
| `size_t` | [`elements`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L232) |


### struct [`slab_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L236)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_uint_fast64_t` | [`head`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L237) |
| `atomic_uint_fast64_t` | [`tail`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L238) |
| `size_t` | [`capacity`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L239) |
| [`struct slab_free_slot`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L199) | [`*slots`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L240) |
| [`struct slab_free_queue_list`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L228) | [`list`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L242) |
| `atomic_size_t` | [`count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L243) |
| [`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423) | [`*parent`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L245) |


### struct [`slab_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L254)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L279) | [`*parent`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L255) |
| `uint64_t` | [`obj_size`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L256) |
| `uint64_t` | [`objs_per_slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L257) |
| `size_t` | [`pages_per_slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L258) |
| `size_t` | [`order`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L259) |
| [`struct list_head`](https://github.com/bluegummi/charmos/blob/main/include/structures/list.h#L5) | [`slabs[SLAB_STANDARD_STATE_COUNT]`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L261) |
| `atomic_size_t` | [`slabs_count[SLAB_STANDARD_STATE_COUNT]`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L262) |
| [`enum slab_type`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L135) | [`type`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L264) |
| [`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423) | [`*parent_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L266) |
| `size_t` | [`ewma_free_slabs`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L269) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L271) |


### struct [`slab_caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L279)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L254) | [`*caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L280) |
| `atomic_size_t` | [`slabs_count[SLAB_STANDARD_STATE_COUNT]`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L281) |


### struct [`slab_cache_ref`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L284)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423) | [`*domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L285) |
| [`struct slab_caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L279) | [`*caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L286) |
| [`enum slab_type`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L135) | [`type`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L287) |
| `uint8_t` | [`locality`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L288) |


### struct [`slab_cache_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L291)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_cache_ref`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L284) | [`*entries`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L292) |
| `size_t` | [`count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L293) |


### struct [`slab_gc`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L381)

| Member Type | Member Name |
|-------------|-------------|
| [`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423) | [`*parent`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L382) |
| [`struct rbt`](https://github.com/bluegummi/charmos/blob/main/include/structures/rbt.h#L26) | [`rbt`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L383) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L384) |
| `atomic_size_t` | [`num_elements`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L385) |


### struct [`slab_domain_bucket`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L394)

| Member Type | Member Name |
|-------------|-------------|
| `atomic_size_t` | [`alloc_calls`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L396) |
| `atomic_size_t` | [`alloc_magazine_hits`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L397) |
| `atomic_size_t` | [`alloc_page_hits`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L398) |
| `atomic_size_t` | [`alloc_local_hits`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L399) |
| `atomic_size_t` | [`alloc_remote_hits`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L400) |
| `atomic_size_t` | [`alloc_gc_recycle_hits`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L401) |
| `atomic_size_t` | [`alloc_new_slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L402) |
| `atomic_size_t` | [`alloc_new_remote_slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L403) |
| `atomic_size_t` | [`alloc_failures`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L404) |
| `atomic_size_t` | [`free_calls`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L407) |
| `atomic_size_t` | [`free_to_ring`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L408) |
| `atomic_size_t` | [`free_to_freelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L409) |
| `atomic_size_t` | [`free_to_local_slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L410) |
| `atomic_size_t` | [`free_to_remote_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L411) |
| `atomic_size_t` | [`free_to_percpu`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L412) |
| `atomic_size_t` | [`freequeue_enqueues`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L415) |
| `atomic_size_t` | [`freequeue_dequeues`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L416) |
| `atomic_size_t` | [`freelist_enqueues`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L417) |
| `atomic_size_t` | [`freelist_dequeues`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L418) |
| `atomic_size_t` | [`gc_collections`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L419) |
| `atomic_size_t` | [`gc_objects_reclaimed`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L420) |


### struct [`slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423)

| Member Type | Member Name |
|-------------|-------------|
| [`struct domain`](https://github.com/bluegummi/charmos/blob/main/include/smp/domain.h#L9) | [`*domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L425) |
| [`struct slab_caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L279) | [`*local_nonpageable_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L428) |
| [`struct slab_caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L279) | [`*local_pageable_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L429) |
| [`struct slab_cache_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L291) | [`nonpageable_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L432) |
| [`struct slab_cache_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L291) | [`pageable_zonelist`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L433) |
| `size_t` | [`zonelist_entry_count`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L434) |
| [`struct slab_percpu_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L193) | [`**percpu_caches`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L438) |
| [`struct slab_free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L236) | [`free_queue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L441) |
| [`struct slab_gc`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L381) | [`slab_gc`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L445) |
| [`struct daemon`](https://github.com/bluegummi/charmos/blob/main/include/sch/daemon.h#L86) | [`*daemon`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L447) |
| [`struct workqueue`](https://github.com/bluegummi/charmos/blob/main/include/sch/defer.h#L194) | [`*workqueue`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L449) |
| [`struct stat_series`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L26) | [`*stats`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L451) |
| [`struct slab_domain_bucket`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L394) | [`*buckets`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L452) |
| [`struct slab_domain_bucket`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L394) | [`aggregate`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L453) |


### struct [`slab_page_hdr`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L461)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`magic`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L462) |
| `bool` | [`pageable`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L463) |
| `uint32_t` | [`pages`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L464) |
| [`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423) | [`*domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L465) |


### enum [`slab_state`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L127)

| Name | Value |
|------|-------|
| [`SLAB_FREE`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L128) | `0` |
| [`SLAB_PARTIAL`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L129) | `1` |
| [`SLAB_FULL`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L130) | `2` |
| [`SLAB_STANDARD_STATE_COUNT`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L131) | `3` |
| [`SLAB_IN_GC_LIST`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L132) | `4` |


### enum [`slab_type`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L135)

| Name | Value |
|------|-------|
| [`SLAB_TYPE_NONPAGEABLE`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L136) | `None` |
| [`SLAB_TYPE_PAGEABLE`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L137) | `None` |


### enum [`slab_gc_flags`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L353)

| Name | Value |
|------|-------|
| [`SLAB_GC_FLAG_AGG_BG`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L354) | `0` |
| [`SLAB_GC_FLAG_AGG_RECLAIM`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L356) | `1` |
| [`SLAB_GC_FLAG_AGG_STANDARD`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L358) | `2` |
| [`SLAB_GC_FLAG_AGG_LOW_MEM`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L360) | `3` |
| [`SLAB_GC_FLAG_AGG_EMERGENCY`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L362) | `4` |
| [`SLAB_GC_FLAG_AGG_MAX`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L364) | `5` |
| [`SLAB_GC_FLAG_AGG_COUNT`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L369) | `6` |
| [`SLAB_GC_FLAG_FAST`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L371) | `1 << 8` |
| [`SLAB_GC_FLAG_FORCE_DESTROY`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L373) | `1 << 9` |
| [`SLAB_GC_FLAG_SKIP_DESTROY`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L375) | `1 << 10` |


- [`slab_magazine_full()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L189) — `static inline bool slab_magazine_full(`[`struct slab_magazine`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L182)` *mag)`
- [`slab_domain_buddy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L456) — `static inline`[`struct domain_buddy *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/domain/internal.h#L80)`slab_domain_buddy(`[`struct slab_domain`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423)` *domain)`
- [`slab_gc_update_ewma()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L538) — `static inline void slab_gc_update_ewma(`[`struct slab_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L254)` *cache)`
- [`slab_page_hdr_for_addr()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L557) — `static inline`[`struct slab_page_hdr *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L461)`slab_page_hdr_for_addr(void *ptr)`
- [`slab_object_count()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L561) — `static inline size_t slab_object_count(`[`struct slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)` *slab)`
- [`slab_object_size()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L565) — `static inline size_t slab_object_size(`[`struct slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)` *slab)`
- [`slab_for_ptr()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L573) — `static inline`[`struct slab *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)`slab_for_ptr(void *ptr)`
- [`slab_domain_local()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L577) — `static inline`[`struct slab_domain *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L423)`slab_domain_local(void)`
- [`slab_percpu_cache_local()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L581) — `static inline`[`struct slab_percpu_cache *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L193)`slab_percpu_cache_local(void)`
- [`slab_list_del()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L585) — `static inline void slab_list_del(`[`struct slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)` *slab)`
- [`slab_list_add()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L601) — `static inline void slab_list_add(`[`struct slab_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L254)` *cache`,[`struct slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)` *slab)`
- [`slab_move()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L612) — `static inline void slab_move(`[`struct slab_cache`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L254)` *c`,[`struct slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)` *slab`,[`enum slab_state`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L127)` new)`
- [`slab_byte_idx_and_mask_from_idx()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L622) — `static inline void slab_byte_idx_and_mask_from_idx(uint64_t index`,`uint64_t *byte_idx_out`,`uint8_t *bitmask_out)`
- [`slab_index_and_mask_from_ptr()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L629) — `static inline void slab_index_and_mask_from_ptr(`[`struct slab`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L140)` *slab`,`void *obj`,`uint64_t *byte_idx_out`,`uint8_t *bitmask_out)`
- [`slab_caches_alloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L641) — `static inline`[`struct slab_cache *`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/slab/internal.h#L254)`slab_caches_alloc()`

