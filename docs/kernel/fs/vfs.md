+++
title = "vfs"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/vfs.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c)

- [`mount_table_add()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L14) — `static void mount_table_add(`[`struct vfs_mount`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L189)` *mnt)`
- [`mount_table_remove()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L31) — `static void mount_table_remove(`[`struct vfs_mount`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L189)` *mnt)`
- [`vfs_node_print()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L40) — `void vfs_node_print(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *node)`
- [`find_mount_for_node()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L58) — `static`[`struct vfs_mount *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L189)`find_mount_for_node(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *node)`
- [`vfs_finddir()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L66) — [`struct vfs_node *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)`vfs_finddir(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *node`,`char *fname)`
- [`vfs_mount()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L90) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`vfs_mount(`[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *mountpoint`,[`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)` *target`,`char *name)`
- [`vfs_unmount()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L116) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`vfs_unmount(`[`struct vfs_mount`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L189)` *mnt)`
- [`vfs_clear_mounts()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/vfs.c#L128) — `void vfs_clear_mounts(void)`

