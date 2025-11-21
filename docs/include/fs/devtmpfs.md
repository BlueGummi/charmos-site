+++
title = "devtmpfs"
author = "Unknown"
status = "unknown"
+++

# [include/fs/devtmpfs.h](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h)

### struct [`devtmpfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L11)

| Member Type | Member Name |
|-------------|-------------|
| [`enum devtmpfs_node_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L5) | [`type`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L12) |
| [`struct vfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198) | [`*vfs`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L13) |
| [`struct devtmpfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L11) | [`**children`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L15) |
| `char` | [`*data`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L17) |
| `uint64_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L18) |
| [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6) | [`(*read)(struct vfs_node *, void *buf, uint64_t size,
                       uint64_t offset, void *ctx)`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L20) |
| [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6) | [`(*write)(struct vfs_node *, const void *buf, uint64_t size,
                        uint64_t offset, void *ctx)`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L22) |
| `void` | [`*rw_ctx`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L24) |


### enum [`devtmpfs_node_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L5)

| Name | Value |
|------|-------|
| [`DEVTMPFS_DIR`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L6) | `None` |
| [`DEVTMPFS_FILE`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L7) | `None` |
| [`DEVTMPFS_SYMLINK`](https://github.com/bluegummi/charmos/blob/main/include/fs/devtmpfs.h#L8) | `None` |

