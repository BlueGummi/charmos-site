# [kernel/fs/ext2/ext2.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c)

<!-- Auto-generated from ext2.c, do not edit manually -->

- [`ext2_read_superblock()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L11) — `bool ext2_read_superblock(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p`,[`struct ext2_sblock`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L106)` *sblock)`
- [`ext2_write_superblock()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L33) — `bool ext2_write_superblock(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_write_group_desc()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L37) — `bool ext2_write_group_desc(`[`struct ext2_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/ext2.h#L215)` *fs)`
- [`ext2_g_mount()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L41) — [`struct vfs_node *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)`ext2_g_mount(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p)`
- [`ext2_g_print()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/ext2/ext2.c#L63) — `void ext2_g_print(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p)`

