+++
title = "gpt"
author = "Unknown"
status = "unknown"
+++

# [include/fs/gpt.h](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h)

### struct [`gpt_header`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L4)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`signature`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L5) |
| `uint32_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L6) |
| `uint32_t` | [`header_size`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L7) |
| `uint32_t` | [`header_crc32`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L8) |
| `uint32_t` | [`reserved`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L9) |
| `uint64_t` | [`current_lba`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L10) |
| `uint64_t` | [`backup_lba`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L11) |
| `uint64_t` | [`first_usable_lba`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L12) |
| `uint64_t` | [`last_usable_lba`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L13) |
| `uint8_t` | [`disk_guid[16]`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L14) |
| `uint64_t` | [`partition_entry_lba`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L15) |
| `uint32_t` | [`num_partition_entries`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L16) |
| `uint32_t` | [`size_of_partition_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L17) |
| `uint32_t` | [`partition_crc32`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L18) |
| `uint8_t` | [`reserved2[420]`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L19) |


### struct [`gpt_partition_entry`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L22)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`type_guid[16]`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L23) |
| `uint8_t` | [`unique_guid[16]`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L24) |
| `uint64_t` | [`first_lba`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L25) |
| `uint64_t` | [`last_lba`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L26) |
| `uint64_t` | [`attributes`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L27) |
| `uint16_t` | [`name[36]`](https://github.com/bluegummi/charmos/blob/main/include/fs/gpt.h#L28) |

