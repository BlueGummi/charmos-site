+++
title = "del_mv"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/del_mv.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/del_mv.c)

- [`fat_delete()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/del_mv.c#L9) — `bool fat_delete(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t dir_cluster`,`char *filename)`
- [`fat_rename()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/del_mv.c#L29) — `bool fat_rename(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t dir_cluster`,`char *filename`,`char *new_filename)`



+++
title = "file"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/file.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/file.c)

- [`fat_read_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/file.c#L7) — `bool fat_read_file(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *ent`,`uint32_t offset`,`uint32_t size`,`uint8_t *out_buf)`
- [`fat_write_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/file.c#L60) — `bool fat_write_file(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *ent`,`uint32_t offset`,`uint8_t *data`,`uint32_t size)`



+++
title = "walk"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/walk.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/walk.c)

- [`fat32_walk_cluster()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/walk.c#L9) — `static bool fat32_walk_cluster(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`fat_walk_callback callback`,`void *ctx)`
- [`fat12_16_walk_cluster()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/walk.c#L33) — `static bool fat12_16_walk_cluster(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`fat_walk_callback callback`,`void *ctx)`
- [`fat_walk_cluster()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/walk.c#L91) — `bool fat_walk_cluster(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`fat_walk_callback cb`,`void *ctx)`



+++
title = "fat"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/fat.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/fat.c)

- [`fat_write_fsinfo()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/fat.c#L10) — `void fat_write_fsinfo(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs)`
- [`fat_first_data_sector()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/fat.c#L28) — `uint32_t fat_first_data_sector(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs)`
- [`fat_cluster_to_lba()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/fat.c#L40) — `uint32_t fat_cluster_to_lba(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster)`
- [`fat_read_bpb()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/fat.c#L53) — [`struct fat_bpb *`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L77)`fat_read_bpb(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *drive`,[`enum fat_fstype`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L20)` *out_type`,`uint32_t *out_lba`,`uint32_t base_lba)`
- [`fat_g_mount()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/fat.c#L130) — [`struct vfs_node *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)`fat_g_mount(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p)`
- [`fat_g_print()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/fat.c#L215) — `void fat_g_print(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *d)`



+++
title = "alloc"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/alloc.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/alloc.c)

- [`fat_alloc_cluster()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/alloc.c#L4) — `uint32_t fat_alloc_cluster(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs)`
- [`fat_free_chain()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/alloc.c#L22) — `void fat_free_chain(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t start_cluster)`



+++
title = "create"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/create.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c)

- [`fat12_16_root_dir_lba()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c#L9) — `static inline uint32_t fat12_16_root_dir_lba(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs)`
- [`fat12_16_root_dir_sectors()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c#L14) — `static inline uint32_t fat12_16_root_dir_sectors(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs)`
- [`fat_find_free_dirent_slot()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c#L19) — `static bool fat_find_free_dirent_slot(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t dir_cluster`,`uint8_t *dir_buf`,`uint32_t *out_cluster`,`uint32_t *out_offset`,`uint32_t *out_prev_cluster)`
- [`fat_extend_directory()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c#L70) — `static bool fat_extend_directory(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t prev_cluster`,`uint32_t *new_cluster_out`,`uint8_t *dir_buf)`
- [`fat_initialize_dirent()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c#L99) — `static void fat_initialize_dirent(`[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *ent`,`char *filename`,`uint32_t cluster`,[`enum fat_fileattr`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L26)` attr)`
- [`fat_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c#L128) — `bool fat_create(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t dir_cluster`,`char *filename`,[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *out_dirent`,[`enum fat_fileattr`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L26)` attr`,`uint32_t *out_cluster)`
- [`fat_mkdir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/create.c#L191) — `bool fat_mkdir(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t parent_cluster`,`char *name`,[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *out_dirent)`



+++
title = "util"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/util.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/util.c)

- [`fat_eoc()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/util.c#L7) — `uint32_t fat_eoc(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs)`
- [`fat_is_eoc()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/util.c#L16) — `bool fat_is_eoc(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster)`
- [`fat_format_filename_83()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/util.c#L25) — `void fat_format_filename_83(char *name`,`char out[11])`
- [`fat_get_dir_cluster()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/util.c#L47) — `uint32_t fat_get_dir_cluster(`[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *d)`
- [`fat_get_current_time()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/util.c#L51) — [`struct fat_time`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L105)`fat_get_current_time()`
- [`fat_get_current_date()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/util.c#L58) — [`struct fat_date`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L99)`fat_get_current_date()`



+++
title = "lookup"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/lookup.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c)

### struct [`fat_lookup_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c#L7)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*fname`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c#L8) |
| [`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111) | [`*found_dir`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c#L9) |
| `uint32_t` | [`index`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c#L11) |


- [`fat_lookup_cb()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c#L14) — `static bool fat_lookup_cb(`[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *d`,`uint32_t indx`,`void *c)`
- [`fat_lookup()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c#L24) — [`struct fat_dirent *`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)`fat_lookup(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`char *f`,`uint32_t *out_index)`
- [`fat_contains()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/lookup.c#L38) — `bool fat_contains(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`char *f)`



+++
title = "io"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/fat/io.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c)

- [`fat_write_cluster()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L17) — `bool fat_write_cluster(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`uint8_t *buffer)`
- [`fat_write_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L31) — `bool fat_write_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`uint32_t value)`
- [`fat12_write_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L40) — `static bool fat12_write_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`uint32_t value)`
- [`fat16_write_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L108) — `static bool fat16_write_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`uint32_t value)`
- [`fat32_write_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L143) — `static bool fat32_write_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`uint32_t value)`
- [`fat_read_cluster()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L187) — `bool fat_read_cluster(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster`,`uint8_t *buffer)`
- [`fat_read_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L199) — `uint32_t fat_read_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster)`
- [`fat12_read_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L208) — `static uint32_t fat12_read_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster)`
- [`fat16_read_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L250) — `static uint32_t fat16_read_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster)`
- [`fat32_read_fat_entry()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L271) — `static uint32_t fat32_read_fat_entry(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t cluster)`
- [`fat_write_dirent()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/fat/io.c#L292) — `bool fat_write_dirent(`[`struct fat_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L127)` *fs`,`uint32_t dir_cluster`,[`struct fat_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/fat.h#L111)` *dirent_to_write`,`uint32_t entry_index)`



