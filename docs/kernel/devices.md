+++
title = "registry"
author = "Unknown"
status = "unknown"
+++

# [kernel/devices/registry.c](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c)

### struct [`disk_node`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L17)

| Member Type | Member Name |
|-------------|-------------|
| [`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68) | [`*disk`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L18) |
| [`struct disk_node`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L17) | [`*next`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L19) |


- [`registry_register()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L25) — `void registry_register(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`
- [`registry_unregister()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L36) — `void registry_unregister(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk)`
- [`registry_get_by_name()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L51) — [`struct generic_disk *`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)`registry_get_by_name(char *name)`
- [`registry_get_by_index()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L59) — [`struct generic_disk *`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)`registry_get_by_index(uint64_t index)`
- [`registry_get_disk_cnt()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L66) — `uint64_t registry_get_disk_cnt(void)`
- [`mkname()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L70) — `static char * mkname(char *prefix`,`uint64_t counter)`
- [`device_mkname()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L81) — `static void device_mkname(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`char *prefix`,`uint64_t counter)`
- [`registry_mkname()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L91) — `void registry_mkname(`[`struct generic_disk`](https://github.com/bluegummi/charmos/blob/main/include/block/generic.h#L68)` *disk`,`char *prefix`,`uint64_t counter)`
- [`registry_setup()`](https://github.com/bluegummi/charmos/blob/main/kernel/devices/registry.c#L96) — `void registry_setup()`



