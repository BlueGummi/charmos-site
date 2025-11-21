# [kernel/fs/ext2/lookup.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/lookup.c)

<!-- Auto-generated from lookup.c, do not edit manually -->

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

