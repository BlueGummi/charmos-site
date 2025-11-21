# [kernel/fs/ext2/truncate.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c)

<!-- Auto-generated from truncate.c, do not edit manually -->

- [`blocks_per_indirection()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c#L13) — `static uint32_t blocks_per_indirection(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`clear_block_pointer()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c#L17) — `static void clear_block_pointer(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode`,`uint32_t block_index)`
- [`ext2_truncate_file()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/truncate.c#L102) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`ext2_truncate_file(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct ext2_full_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L201)` *inode`,`uint32_t new_size)`

