# [kernel/fs/ext2/alloc.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c)

<!-- Auto-generated from alloc.c, do not edit manually -->

- [`find_free_bit()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L7) — `static bool find_free_bit(uint8_t *bitmap`,`uint32_t size`,`uint32_t *byte_pos`,`uint32_t *bit_pos)`
- [`alloc_from_bitmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L21) — `static uint32_t alloc_from_bitmap(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t bitmap_block`,`uint32_t items_per_group`,`uint32_t group`,`void (*update_counts)(struct ext2_fs *`,`
                                                        uint32_t))`
- [`update_block_counts()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L47) — `static void update_block_counts(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t group)`
- [`update_inode_counts()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L58) — `static void update_inode_counts(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t group)`
- [`ext2_alloc_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L65) — `uint32_t ext2_alloc_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_free_block()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L80) — `bool ext2_free_block(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t block_num)`
- [`ext2_alloc_inode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L115) — `uint32_t ext2_alloc_inode(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_free_inode()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/alloc.c#L130) — `bool ext2_free_inode(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs`,`uint32_t inode_num)`

