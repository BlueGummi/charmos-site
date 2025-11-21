# [kernel/fs/ext2/io.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c)

<!-- Auto-generated from io.c, do not edit manually -->

- [`ext2_block_to_lba()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L7) — `uint32_t ext2_block_to_lba(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num)`
- [`ext2_block_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L18) — `uint8_t * ext2_block_read(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num`,[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` **out)`
- [`ext2_block_write()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L36) — `bool ext2_block_write(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` *ent`,[`enum bio_request_priority`](https://github.com/bluegummi/charmos/blob/main/include/block/bio.h#L10)` prio)`
- [`ext2_inode_read()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L48) — [`struct ext2_inode *`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)`ext2_inode_read(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t inode_idx`,[`struct bcache_entry`](https://github.com/bluegummi/charmos/blob/main/include/block/bcache.h#L18)` **out_ent)`
- [`ext2_inode_write()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/io.c#L82) — `bool ext2_inode_write(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t inode_num`,[`struct ext2_inode`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L178)` *inode)`

