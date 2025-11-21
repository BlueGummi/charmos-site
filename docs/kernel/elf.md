+++
title = "elf"
author = "Unknown"
status = "unknown"
+++

# [kernel/elf.c](https://github.com/bluegummi/charmos/blob/main/kernel/elf.c)

- [`elf_load()`](https://github.com/bluegummi/charmos/blob/main/kernel/elf.c#L15) — `uint64_t elf_load(void *elf_data)`
- [`elf_map()`](https://github.com/bluegummi/charmos/blob/main/kernel/elf.c#L45) — `void elf_map(uintptr_t user_pml4_phys`,`void *elf_data)`
- [`map_user_stack()`](https://github.com/bluegummi/charmos/blob/main/kernel/elf.c#L102) — `uintptr_t map_user_stack(uintptr_t user_pml4_phys)`
- [`syscall_setup()`](https://github.com/bluegummi/charmos/blob/main/kernel/elf.c#L117) — `void syscall_setup(void *syscall_entry)`
- [`enter_userspace()`](https://github.com/bluegummi/charmos/blob/main/kernel/elf.c#L130) — `void enter_userspace(uintptr_t entry_point`,`uintptr_t user_stack_top`,`uint16_t user_cs`,`uint16_t user_ss`,`uintptr_t user_pml4_phys)`

