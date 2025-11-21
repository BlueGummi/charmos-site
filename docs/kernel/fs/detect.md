+++
title = "detect"
author = "Unknown"
status = "unknown"
+++

# [kernel/fs/detect.c](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c)

- [`detect_fstr()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L16) — `const char * detect_fstr(`[`enum fs_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/detect.h#L4)` type)`
- [`dummy_mount()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L33) — [`struct vfs_node *`](https://github.com/bluegummi/charmos/blob/main/include/fs/vfs.h#L198)`dummy_mount(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p)`
- [`dummy_print()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L38) — `void dummy_print(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *p)`
- [`make_partition()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L43) — `static void make_partition(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *part`,[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint64_t start_lba`,`uint64_t sector_count`,`uint8_t idx)`
- [`detect_mbr_partitions()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L57) — `static`[`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`detect_mbr_partitions(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint8_t *sector)`
- [`detect_gpt_partitions()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L91) — `static bool detect_gpt_partitions(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`uint8_t *sector)`
- [`detect_partition_fs()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L141) — `static`[`enum fs_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/detect.h#L4)`detect_partition_fs(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *part`,`uint8_t *sector)`
- [`assign_fs_ops()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L185) — `static void assign_fs_ops(`[`struct generic_partition`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L41)` *part)`
- [`detect_fs()`](https://github.com/bluegummi/charmos/blob/main/kernel/fs/detect.c#L198) — [`enum fs_type`](https://github.com/bluegummi/charmos/blob/main/include/fs/detect.h#L4)`detect_fs(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`

