# [kernel/fs/ext2/util.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c)

<!-- Auto-generated from util.c, do not edit manually -->

- [`ext2_get_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L6) — `static uint32_t ext2_get_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num`,`uint32_t depth`,`uint32_t block_index`,`uint32_t new_block_num`,`bool allocate`,`bool *was_allocated)`
- [`ext2_get_or_set_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L71) — `uint32_t ext2_get_or_set_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`uint32_t block_index`,`uint32_t new_block_num`,`bool allocate`,`bool *was_allocated)`
- [`ext2_init_inode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L123) — `void ext2_init_inode(`[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *new_inode`,`uint16_t mode)`
- [`ext2_init_dirent()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L135) — `void ext2_init_dirent(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_dir_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L207)` *new_entry`,`uint32_t inode_num`,`char *name`,`uint8_t type)`
- [`ext2_extract_ftype()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/util.c#L144) — `uint8_t ext2_extract_ftype(uint16_t mode)`

