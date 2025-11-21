+++
title = "mbr"
author = "Unknown"
status = "unknown"
+++

# [include/fs/mbr.h](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h)

### struct [`mbr_partition_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L4)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`status`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L5) |
| `uint8_t` | [`chs_first[3]`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L6) |
| `uint8_t` | [`type`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L7) |
| `uint8_t` | [`chs_last[3]`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L8) |
| `uint32_t` | [`lba_start`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L9) |
| `uint32_t` | [`sector_count`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L10) |


### struct [`mbr`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L13)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`bootstrap[446]`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L14) |
| [`struct mbr_partition_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L4) | [`partitions[4]`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L15) |
| `uint16_t` | [`signature`](https://github.com/bluegummi/charmos/blob/main/include/fs/mbr.h#L16) |

