+++
title = "ext2"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/ext2.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c)

- [`ext2_read_superblock()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L11) — `bool ext2_read_superblock(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p`,[`struct ext2_sblock`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L106)` *sblock)`
- [`ext2_write_superblock()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L33) — `bool ext2_write_superblock(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_write_group_desc()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L37) — `bool ext2_write_group_desc(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_g_mount()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L41) — [`struct vfs_node *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)`ext2_g_mount(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p)`
- [`ext2_g_print()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L63) — `void ext2_g_print(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p)`



+++
title = "file"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/file.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c)

### struct [`file_read_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L67)

| Member Type | Member Name |
|-------------|-------------|
| [`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215) | [`*fs`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L68) |
| [`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178) | [`*inode`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L69) |
| `uint32_t` | [`offset`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L70) |
| `uint32_t` | [`length`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L71) |
| `uint8_t` | [`*buffer`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L72) |
| `uint32_t` | [`bytes_read`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L73) |


- [`ext2_write_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L7) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_write_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *inode`,`uint32_t offset`,`uint8_t *src`,`uint32_t size)`
- [`file_read_visitor()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L76) — `static void file_read_visitor(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`uint32_t depth`,`uint32_t *block_ptr`,`void *user_data)`
- [`ext2_read_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L113) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_read_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *inode`,`uint32_t offset`,`uint8_t *buffer`,`uint64_t length)`
- [`ext2_chmod()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L137) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_chmod(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *node`,`uint16_t new_mode)`
- [`ext2_chown()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/file.c#L151) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_chown(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *node`,`uint32_t new_uid`,`uint32_t new_gid)`



+++
title = "walk"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/walk.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c)

- [`walk_dir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L5) — `static bool walk_dir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num`,`dir_entry_callback callback`,`void *ctx)`
- [`walk_direct_blocks()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L38) — `static bool walk_direct_blocks(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *inode`,`dir_entry_callback cb`,`void *ctx`,`bool ff_avail)`
- [`walk_indirect()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L57) — `static bool walk_indirect(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num`,`int level`,`dir_entry_callback cb`,`void *ctx`,`bool ff_avail`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *inode)`
- [`do_walk_dir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L103) — `static bool do_walk_dir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir_inode`,`dir_entry_callback cb`,`void *ctx`,`bool ff_avail)`
- [`readahead_blocks()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L126) — `static void readahead_blocks(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t *entries`,`uint32_t count`,`uint32_t start_index)`
- [`traverse_indirect()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L135) — `static void traverse_indirect(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`uint32_t block_num`,`int depth`,`ext2_block_visitor visitor`,`void *user_data`,`bool readahead)`
- [`ext2_traverse_inode_blocks()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L167) — `void ext2_traverse_inode_blocks(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`ext2_block_visitor visitor`,`void *user_data`,`bool readahead)`
- [`ext2_walk_dir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L190) — `bool ext2_walk_dir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir`,`dir_entry_callback cb`,`void *ctx)`
- [`ext2_find_first_available()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/walk.c#L197) — `bool ext2_find_first_available(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir`,`uint32_t *new_block)`



+++
title = "alloc"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/alloc.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c)

- [`find_free_bit()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L7) — `static bool find_free_bit(uint8_t *bitmap`,`uint32_t size`,`uint32_t *byte_pos`,`uint32_t *bit_pos)`
- [`alloc_from_bitmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L21) — `static uint32_t alloc_from_bitmap(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t bitmap_block`,`uint32_t items_per_group`,`uint32_t group`,`void (*update_counts)(struct ext2_fs *`,`
                                                        uint32_t))`
- [`update_block_counts()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L47) — `static void update_block_counts(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t group)`
- [`update_inode_counts()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L58) — `static void update_inode_counts(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t group)`
- [`ext2_alloc_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L65) — `uint32_t ext2_alloc_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_free_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L80) — `bool ext2_free_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num)`
- [`ext2_alloc_inode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L115) — `uint32_t ext2_alloc_inode(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_free_inode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L130) — `bool ext2_free_inode(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t inode_num)`



+++
title = "vfs_impl"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/vfs_impl.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c)

### struct [`rename_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L286)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*old_name`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L287) |
| `char` | [`*new_name`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L288) |
| `bool` | [`success`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L289) |


- [`vfs_dummy_open()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L52) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`vfs_dummy_open(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *a`,`uint32_t b)`
- [`vfs_dummy_close()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L57) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`vfs_dummy_close(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *a)`
- [`ext2_to_vfs_flags()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L92) — `static uint32_t ext2_to_vfs_flags(uint32_t ext2_flags)`
- [`vfs_to_ext2_flags()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L113) — `static uint32_t vfs_to_ext2_flags(uint32_t vfs_flags)`
- [`ext2_to_vfs_mode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L134) — `static uint16_t ext2_to_vfs_mode(uint16_t ext2_mode)`
- [`vfs_to_ext2_mode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L182) — `static uint16_t vfs_to_ext2_mode(uint16_t vfs_mode)`
- [`ext2_to_vfs_stat()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L230) — `static`[`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_to_vfs_stat(`[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *node`,[`struct vfs_stat`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L78)` *out)`
- [`make_vfs_node()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L249) — `static`[`struct vfs_node *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)`make_vfs_node(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *node`,`char *fname)`
- [`ext2_to_vfs_dirent()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L275) — `static`[`struct vfs_dirent *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L98)`ext2_to_vfs_dirent(`[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *ext2)`
- [`dir_entry_rename_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L292) — `static bool dir_entry_rename_callback(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *entry`,`void *ctx_ptr`,`uint32_t b`,`uint32_t e_num`,`uint32_t c)`
- [`dir_entry_rename()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L315) — `static`[`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`dir_entry_rename(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *node`,`char *old`,`char *new)`
- [`ext2_mount()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L339) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_mount(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p`,[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_sblock`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L106)` *sblock`,[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *out_node)`
- [`ext2_vfs_finddir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L408) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_finddir(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *node`,`char *fname`,[`struct vfs_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L98)` *out)`
- [`ext2_vfs_readdir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L436) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_readdir(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *node`,[`struct vfs_dirent`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L98)` *out`,`uint64_t index)`
- [`ext2_vfs_rename()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L461) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_rename(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *old_parent`,`char *old_name`,[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *new_parent`,`char *new_name)`
- [`ext2_vfs_stat()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L487) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_stat(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *v`,[`struct vfs_stat`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L78)` *out)`
- [`ext2_vfs_link()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L492) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_link(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *parent`,[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *target`,`char *name)`
- [`ext2_vfs_symlink()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L509) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_symlink(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *parent`,`char *target`,`char *link_name)`
- [`ext2_vfs_readlink()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L520) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_readlink(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`char *out_buf`,`uint64_t size)`
- [`ext2_vfs_chmod()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L530) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_chmod(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`uint16_t mode)`
- [`ext2_vfs_chown()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L545) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_chown(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`uint32_t uid`,`uint32_t gid)`
- [`ext2_vfs_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L560) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_read(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`void *buf`,`uint64_t size`,`uint64_t offset)`
- [`ext2_vfs_write()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L570) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_write(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`void *buf`,`uint64_t size`,`uint64_t offset)`
- [`ext2_vfs_utime()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L586) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_utime(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`uint64_t atime`,`uint64_t mtime)`
- [`ext2_vfs_truncate()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L603) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_truncate(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`uint64_t length)`
- [`ext2_vfs_unlink()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L612) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_unlink(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`char *name)`
- [`ext2_vfs_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L621) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_create(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`char *name`,`uint16_t mode)`
- [`ext2_vfs_mkdir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L632) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_mkdir(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`char *name`,`uint16_t mode)`
- [`ext2_vfs_rmdir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/vfs_impl.c#L642) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_vfs_rmdir(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *n`,`char *name)`



+++
title = "dir"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/dir.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/dir.c)

- [`ext2_dirent_valid()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/dir.c#L7) — `bool ext2_dirent_valid(`[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *entry)`
- [`init_dir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/dir.c#L14) — `static void init_dir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir`,`uint32_t new_block)`
- [`init_dot_ents()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/dir.c#L22) — `static void init_dot_ents(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint8_t *block`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *parent_dir`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir)`
- [`ext2_mkdir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/dir.c#L40) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_mkdir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *parent_dir`,`char *name`,`uint16_t mode)`
- [`ext2_rmdir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/dir.c#L84) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_rmdir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *parent_dir`,`char *name)`



+++
title = "symlink"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/symlink.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/symlink.c)

- [`ext2_symlink_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/symlink.c#L8) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_symlink_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir_inode`,`char *name`,`char *target)`
- [`ext2_readlink()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/symlink.c#L60) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_readlink(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *node`,`char *buf`,`uint64_t size)`



+++
title = "create"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/create.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c)

### struct [`link_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L8)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L9) |
| `uint32_t` | [`inode`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L10) |
| `uint32_t` | [`dir_inode`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L11) |
| `uint8_t` | [`type`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L12) |
| `bool` | [`success`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L13) |


- [`link_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L16) — `static bool link_callback(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *entry`,`void *ctx_ptr`,`uint32_t block_num`,`uint32_t e`,`uint32_t o)`
- [`ext2_link_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L52) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_link_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *inode`,`char *name`,`uint8_t type`,`bool increment_links)`
- [`ext2_create_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c#L100) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_create_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *parent_dir`,`char *name`,`uint16_t mode`,`bool increment)`



+++
title = "delete"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/delete.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c)

### struct [`unlink_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L9)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L10) |
| `bool` | [`found`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L11) |
| `uint32_t` | [`inode_num`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L12) |
| `uint32_t` | [`block_num`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L13) |
| `uint32_t` | [`entry_offset`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L14) |
| `uint32_t` | [`prev_offset`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L15) |


- [`free_block_visitor()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L18) — `void free_block_visitor(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`uint32_t depth`,`uint32_t *block_ptr`,`void *user_data)`
- [`unlink_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L27) — `bool unlink_callback(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *entry`,`void *arg`,`uint32_t block_num`,`uint32_t e`,`uint32_t entry_offset)`
- [`unlink_adjust_neighbors()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L53) — `static void unlink_adjust_neighbors(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint8_t *block`,`uint32_t offset`,`uint32_t prev_offset)`
- [`unlink_target_update()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L70) — `static inline void unlink_target_update(`[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *target_inode)`
- [`unlink_free_blocks()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L75) — `static inline void unlink_free_blocks(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *target_inode`,`uint32_t inode_num)`
- [`ext2_unlink_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c#L83) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_unlink_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir_inode`,`char *name`,`bool free_blocks`,`bool decrement_links)`



+++
title = "truncate"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/truncate.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c)

- [`blocks_per_indirection()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c#L13) — `static uint32_t blocks_per_indirection(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`clear_block_pointer()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c#L17) — `static void clear_block_pointer(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`uint32_t block_index)`
- [`ext2_truncate_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c#L102) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_truncate_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *inode`,`uint32_t new_size)`



+++
title = "util"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/util.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c)

- [`ext2_get_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L6) — `static uint32_t ext2_get_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num`,`uint32_t depth`,`uint32_t block_index`,`uint32_t new_block_num`,`bool allocate`,`bool *was_allocated)`
- [`ext2_get_or_set_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L71) — `uint32_t ext2_get_or_set_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`uint32_t block_index`,`uint32_t new_block_num`,`bool allocate`,`bool *was_allocated)`
- [`ext2_init_inode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L123) — `void ext2_init_inode(`[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *new_inode`,`uint16_t mode)`
- [`ext2_init_dirent()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L135) — `void ext2_init_dirent(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *new_entry`,`uint32_t inode_num`,`char *name`,`uint8_t type)`
- [`ext2_extract_ftype()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L144) — `uint8_t ext2_extract_ftype(uint16_t mode)`



+++
title = "lookup"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/lookup.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c)

### struct [`search_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L9)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*target`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L10) |
| [`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201) | [`*result`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L11) |
| `uint8_t` | [`type`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L12) |
| `bool` | [`found`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L13) |


### struct [`contains_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L16)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*target`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L17) |
| `bool` | [`found`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L18) |


### struct [`readdir_ctx`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L21)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`entry_offset`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L22) |
| [`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207) | [`*out`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L23) |
| `bool` | [`found`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L24) |
| `uint32_t` | [`count`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L25) |


- [`search_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L29) — `static bool search_callback(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *entry`,`void *ctx_ptr`,`uint32_t b`,`uint32_t e_num`,`uint32_t offset)`
- [`contains_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L63) — `static bool contains_callback(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *entry`,`void *ctx_ptr`,`uint32_t b`,`uint32_t e`,`uint32_t offset)`
- [`readdir_callback()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L86) — `static bool readdir_callback(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *entry`,`void *ctx_ptr`,`uint32_t block`,`uint32_t entry_num`,`uint32_t entry_offset)`
- [`ext2_find_file_in_dir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L106) — [`struct ext2_full_inode *`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)`ext2_find_file_in_dir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir_inode`,`char *fname`,`uint8_t *type_out)`
- [`ext2_dir_contains_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L127) — `bool ext2_dir_contains_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir_inode`,`char *fname)`
- [`ext2_readdir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c#L137) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_readdir(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *dir_inode`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *out`,`uint32_t entry_offset)`



+++
title = "io"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/ext2/io.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c)

- [`ext2_block_to_lba()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L7) — `uint32_t ext2_block_to_lba(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num)`
- [`ext2_block_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L18) — `uint8_t * ext2_block_read(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num`,[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` **out)`
- [`ext2_block_write()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L36) — `bool ext2_block_write(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent`,[`enum bio_request_priority`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L10)` prio)`
- [`ext2_inode_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L48) — [`struct ext2_inode *`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)`ext2_inode_read(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t inode_idx`,[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` **out_ent)`
- [`ext2_inode_write()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L82) — `bool ext2_inode_write(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t inode_num`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode)`



