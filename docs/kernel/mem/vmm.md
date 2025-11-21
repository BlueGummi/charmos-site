# [kernel/mem/vmm.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c)

<!-- Auto-generated from vmm.c, do not edit manually -->

- [`vmm_tlb_shootdown()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L25) — `static void vmm_tlb_shootdown(`[`vaddr_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L13)` addr)`
- [`sub_offset()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L30) — `uint64_t sub_offset(uint64_t a)`
- [`alloc_pt()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L34) — `static inline`[`struct page_table *`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L47)`alloc_pt(void)`
- [`vmm_make_user_pml4()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L44) — `uintptr_t vmm_make_user_pml4(void)`
- [`vmm_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L58) — `void vmm_init(`[`struct limine_memmap_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L479)` *memmap`,`struct limine_executable_address_response *xa)`
- [`vmm_is_table_empty()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L132) — `static inline bool vmm_is_table_empty(`[`struct page_table`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L47)` *table)`
- [`pte_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L140) — `static`[`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`pte_init(`[`pte_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L16)` *entry`,`uint64_t flags)`
- [`page_table_lock()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L151) — [`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)`page_table_lock(`[`struct page_table`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L47)` *pt)`
- [`page_table_unlock()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L157) — `void page_table_unlock(`[`struct page_table`](https://github.com/bluegummi/charmos/blob/main/include/mem/page.h#L47)` *pt`,[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` irql)`
- [`vmm_map_2mb_page()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L163) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`vmm_map_2mb_page(uintptr_t virt`,`uintptr_t phys`,`uint64_t flags)`
- [`vmm_unmap_2mb_page()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L220) — `void vmm_unmap_2mb_page(uintptr_t virt)`
- [`vmm_map_page()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L278) — [`enum errno`](https://github.com/bluegummi/charmos/blob/main/include/errno.h#L6)`vmm_map_page(uintptr_t virt`,`uintptr_t phys`,`uint64_t flags)`
- [`vmm_map_page_user()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L327) — `void vmm_map_page_user(uintptr_t pml4_phys`,`uintptr_t virt`,`uintptr_t phys`,`uint64_t flags)`
- [`vmm_unmap_page()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L351) — `void vmm_unmap_page(uintptr_t virt)`
- [`vmm_get_phys()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L407) — `uintptr_t vmm_get_phys(uintptr_t virt)`
- [`vmm_get_phys_unsafe()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L466) — `uintptr_t vmm_get_phys_unsafe(uintptr_t virt)`
- [`vmm_map_phys()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L506) — `void * vmm_map_phys(uint64_t addr`,`uint64_t len`,`uint64_t flags)`
- [`vmm_unmap_virt()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/vmm.c#L529) — `void vmm_unmap_virt(void *addr`,`uint64_t len)`

