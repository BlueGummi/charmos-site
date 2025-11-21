# [kernel/fs/ext2/create.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/create.c)

<!-- Auto-generated from create.c, do not edit manually -->

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

