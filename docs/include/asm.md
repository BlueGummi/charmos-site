# [include/asm.h](https://github.com/bluegummi/charmos/blob/main/include/asm.h)

<!-- Auto-generated from asm.h, do not edit manually -->

- [`inb()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L17) — `static inline uint8_t inb(uint16_t port)`
- [`inw()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L23) — `static inline uint16_t inw(uint16_t port)`
- [`inl()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L29) — `static inline uint32_t inl(uint16_t port)`
- [`insb()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L35) — `static inline void insb(uint16_t port`,`void *addr`,`uint32_t count)`
- [`insw()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L39) — `static inline void insw(uint16_t port`,`void *addr`,`uint32_t count)`
- [`insl()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L43) — `static inline void insl(uint16_t port`,`void *addr`,`uint32_t count)`
- [`outb()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L59) — `static inline void outb(uint16_t port`,`uint8_t value)`
- [`outw()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L63) — `static inline void outw(uint16_t port`,`uint16_t value)`
- [`outl()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L67) — `static inline void outl(uint16_t port`,`uint32_t value)`
- [`outsw()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L71) — `static inline void outsw(uint16_t port`,`void *addr`,`uint32_t count)`
- [`outsb()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L75) — `static inline void outsb(uint16_t port`,`void *addr`,`uint32_t count)`
- [`outsl()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L79) — `static inline void outsl(uint16_t port`,`void *addr`,`uint32_t count)`
- [`mmio_write_64()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L95) — `static inline void mmio_write_64(void *address`,`uint64_t value)`
- [`mmio_write_32()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L99) — `static inline void mmio_write_32(void *address`,`uint32_t value)`
- [`mmio_write_16()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L103) — `static inline void mmio_write_16(void *address`,`uint16_t value)`
- [`mmio_write_8()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L107) — `static inline void mmio_write_8(void *address`,`uint8_t value)`
- [`mmio_read_64()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L111) — `static inline uint64_t mmio_read_64(void *address)`
- [`mmio_read_32()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L117) — `static inline uint32_t mmio_read_32(void *address)`
- [`mmio_read_16()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L123) — `static inline uint16_t mmio_read_16(void *address)`
- [`mmio_read_8()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L129) — `static inline uint8_t mmio_read_8(void *address)`
- [`write_cr8()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L147) — `static inline void write_cr8(uint64_t cr8)`
- [`rdtsc()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L151) — `static inline uint64_t rdtsc(void)`
- [`cpuid_count()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L157) — `static inline void cpuid_count(uint32_t leaf`,`uint32_t subleaf`,`uint32_t *eax`,`uint32_t *ebx`,`uint32_t *ecx`,`uint32_t *edx)`
- [`cpuid()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L164) — `static inline void cpuid(uint32_t leaf`,`uint32_t subleaf`,`uint32_t *eax`,`uint32_t *ebx`,`uint32_t *ecx`,`uint32_t *edx)`
- [`read_cr4()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L172) — `static inline uint64_t read_cr4()`
- [`write_cr4()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L178) — `static inline void write_cr4(uint64_t cr4)`
- [`get_core_id()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L182) — `static inline uint32_t get_core_id(void)`
- [`are_interrupts_enabled()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L193) — `static inline bool are_interrupts_enabled()`
- [`wrmsr()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L205) — `static inline void wrmsr(uint32_t msr`,`uint64_t value)`
- [`rdmsr()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L211) — `static inline uint64_t rdmsr(uint32_t msr)`
- [`io_wait()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L217) — `static inline void io_wait(void)`
- [`clear_interrupts()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L221) — `static inline void clear_interrupts(void)`
- [`restore_interrupts()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L225) — `static inline void restore_interrupts(void)`
- [`enable_interrupts()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L229) — `static inline void enable_interrupts(void)`
- [`disable_interrupts()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L233) — `static inline void disable_interrupts(void)`
- [`invlpg()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L237) — `static inline void invlpg(uint64_t virt)`
- [`read_cr3()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L242) — `static inline uint64_t read_cr3()`
- [`write_cr3()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L248) — `static inline void write_cr3(uint64_t cr3)`
- [`tlb_flush()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L252) — `static inline void tlb_flush()`
- [`cpu_relax()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L257) — `static inline void cpu_relax(void)`
- [`wait_for_interrupt()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L261) — `static inline void wait_for_interrupt(void)`
- [`clz()`](https://github.com/bluegummi/charmos/blob/main/include/asm.h#L265) — `static inline int clz(uint8_t a)`

