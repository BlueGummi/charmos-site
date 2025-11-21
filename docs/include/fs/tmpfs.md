# [include/fs/tmpfs.h](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h)

<!-- Auto-generated from tmpfs.h, do not edit manually -->

### struct [`tmpfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L14)

| Member Type | Member Name |
|-------------|-------------|
| [`enum tmpfs_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L7) | [`type`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L15) |
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L16) |
| `void` | [`**pages`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L18) |
| `uint64_t` | [`num_pages`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L19) |
| `uint64_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L20) |
| `char` | [`*symlink_target`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L22) |
| `uint16_t` | [`mode`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L23) |
| `uint32_t` | [`uid`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L24) |
| `uint32_t` | [`gid`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L25) |
| `uint64_t` | [`mtime`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L26) |
| `uint64_t` | [`atime`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L27) |
| [`struct tmpfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L14) | [`*parent`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L29) |
| [`struct tmpfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L14) | [`**children`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L31) |
| `uint64_t` | [`child_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L32) |
| [`struct mutex`](https://github.com/bluegummi/charmos/blob/main/include/sync/mutex.h#L40) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L33) |


### struct [`tmpfs_fs`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L36)

| Member Type | Member Name |
|-------------|-------------|
| [`struct tmpfs_node`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L14) | [`*root`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L37) |


### enum [`tmpfs_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L7)

| Name | Value |
|------|-------|
| [`TMPFS_FILE`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L8) | `None` |
| [`TMPFS_DIR`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L9) | `None` |
| [`TMPFS_SYMLINK`](https://github.com/bluegummi/charmos/blob/main/include/fs/tmpfs.h#L10) | `None` |

