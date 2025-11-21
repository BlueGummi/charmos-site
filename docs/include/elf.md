# [include/elf.h](https://github.com/bluegummi/charmos/blob/main/include/elf.h)

<!-- Auto-generated from elf.h, do not edit manually -->

### struct [`elf64_ident`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L4)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`magic`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L5) |
| `uint8_t` | [`class`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L6) |
| `uint8_t` | [`data`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L7) |
| `uint8_t` | [`version`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L8) |
| `uint8_t` | [`os_abi`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L9) |
| `uint8_t` | [`abi_version`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L10) |
| `uint8_t` | [`pad[7]`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L11) |


### struct [`elf64_ehdr`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L14)

| Member Type | Member Name |
|-------------|-------------|
| [`struct elf64_ident`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L4) | [`ident`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L15) |
| `uint16_t` | [`type`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L16) |
| `uint16_t` | [`machine`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L17) |
| `uint32_t` | [`version`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L18) |
| `uint64_t` | [`entry`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L19) |
| `uint64_t` | [`phoff`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L20) |
| `uint64_t` | [`shoff`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L21) |
| `uint32_t` | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L22) |
| `uint16_t` | [`ehsize`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L23) |
| `uint16_t` | [`phentsize`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L24) |
| `uint16_t` | [`phnum`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L25) |
| `uint16_t` | [`shentsize`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L26) |
| `uint16_t` | [`shnum`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L27) |
| `uint16_t` | [`shstrndx`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L28) |


### struct [`elf64_phdr`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L31)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`type`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L32) |
| `uint32_t` | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L33) |
| `uint64_t` | [`offset`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L34) |
| `uint64_t` | [`vaddr`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L35) |
| `uint64_t` | [`paddr`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L36) |
| `uint64_t` | [`filesz`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L37) |
| `uint64_t` | [`memsz`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L38) |
| `uint64_t` | [`align`](https://github.com/bluegummi/charmos/blob/main/include/elf.h#L39) |

