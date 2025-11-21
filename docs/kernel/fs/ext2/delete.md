# [kernel/fs/ext2/delete.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/delete.c)

<!-- Auto-generated from delete.c, do not edit manually -->

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

