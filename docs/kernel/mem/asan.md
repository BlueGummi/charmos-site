# [kernel/mem/asan.c](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c)

<!-- Auto-generated from asan.c, do not edit manually -->

### struct [`__asan_global`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L234)

| Member Type | Member Name |
|-------------|-------------|
| `void` | [`*addr`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L235) |
| `size_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L236) |
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L237) |


### struct [`stack_record`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L265)

| Member Type | Member Name |
|-------------|-------------|
| `void` | [`*addr`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L266) |
| `size_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L267) |


- [`asan_shadow_for_internal()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L14) — `static inline uint8_t * asan_shadow_for_internal(void *addr)`
- [`asan_poison()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L19) — `void asan_poison(void *addr`,`size_t size)`
- [`asan_unpoison()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L27) — `void asan_unpoison(void *addr`,`size_t size)`
- [`asan_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L35) — `void asan_init(void)`
- [`asan_shadow_for()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L79) — `static inline uint8_t * asan_shadow_for(void *addr)`
- [`__asan_report_and_panic()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L89) — `static void __asan_report_and_panic(char *what`,`void *addr`,`size_t size`,`bool is_write)`
- [`asan_check_access_core()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L100) — `static inline void asan_check_access_core(void *addr`,`size_t size`,`bool is_write)`
- [`__asan_load1()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L139) — `void __asan_load1(void *addr)`
- [`__asan_load2()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L142) — `void __asan_load2(void *addr)`
- [`__asan_load4()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L145) — `void __asan_load4(void *addr)`
- [`__asan_load8()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L148) — `void __asan_load8(void *addr)`
- [`__asan_load16()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L151) — `void __asan_load16(void *addr)`
- [`__asan_store1()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L155) — `void __asan_store1(void *addr)`
- [`__asan_store2()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L158) — `void __asan_store2(void *addr)`
- [`__asan_store4()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L161) — `void __asan_store4(void *addr)`
- [`__asan_store8()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L164) — `void __asan_store8(void *addr)`
- [`__asan_store16()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L167) — `void __asan_store16(void *addr)`
- [`__asan_loadN()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L172) — `void __asan_loadN(void *addr`,`size_t size)`
- [`__asan_storeN()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L175) — `void __asan_storeN(void *addr`,`size_t size)`
- [`__asan_poison_memory_region()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L180) — `void __asan_poison_memory_region(void *addr`,`size_t size)`
- [`__asan_unpoison_memory_region()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L202) — `void __asan_unpoison_memory_region(void *addr`,`size_t size)`
- [`__asan_register_globals()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L241) — `void __asan_register_globals(`[`struct __asan_global`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L234)` *globals`,`size_t n)`
- [`__asan_unregister_globals()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L259) — `void __asan_unregister_globals(void *globals`,`size_t n)`
- [`__asan_stack_malloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L273) — `void __asan_stack_malloc(void *addr`,`size_t size)`
- [`__asan_stack_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L290) — `void __asan_stack_free(void *addr)`
- [`__asan_report_load1()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L309) — `void __asan_report_load1(void *addr)`
- [`__asan_report_load2()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L312) — `void __asan_report_load2(void *addr)`
- [`__asan_report_load4()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L315) — `void __asan_report_load4(void *addr)`
- [`__asan_report_load8()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L318) — `void __asan_report_load8(void *addr)`
- [`__asan_report_load16()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L321) — `void __asan_report_load16(void *addr)`
- [`__asan_report_load32()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L325) — `void __asan_report_load32(void *addr)`
- [`__asan_report_load64()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L329) — `void __asan_report_load64(void *addr)`
- [`__asan_report_load_n()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L333) — `void __asan_report_load_n(void *addr`,`size_t size)`
- [`__asan_report_store1()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L338) — `void __asan_report_store1(void *addr)`
- [`__asan_report_store2()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L341) — `void __asan_report_store2(void *addr)`
- [`__asan_report_store4()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L344) — `void __asan_report_store4(void *addr)`
- [`__asan_report_store8()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L347) — `void __asan_report_store8(void *addr)`
- [`__asan_report_store16()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L350) — `void __asan_report_store16(void *addr)`
- [`__asan_report_store32()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L354) — `void __asan_report_store32(void *addr)`
- [`__asan_report_store64()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L358) — `void __asan_report_store64(void *addr)`
- [`__asan_report_store_n()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L362) — `void __asan_report_store_n(void *addr`,`size_t size)`
- [`__asan_stack_malloc_0()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L376) — `void * __asan_stack_malloc_0(size_t size)`
- [`__asan_stack_malloc_1()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L380) — `void * __asan_stack_malloc_1(size_t size)`
- [`__asan_stack_malloc_2()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L384) — `void * __asan_stack_malloc_2(size_t size)`
- [`__asan_stack_malloc_3()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L388) — `void * __asan_stack_malloc_3(size_t size)`
- [`__asan_stack_malloc_4()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L392) — `void * __asan_stack_malloc_4(size_t size)`
- [`__asan_stack_malloc_5()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L396) — `void * __asan_stack_malloc_5(size_t size)`
- [`__asan_stack_malloc_6()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L400) — `void * __asan_stack_malloc_6(size_t size)`
- [`__asan_stack_malloc_7()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L404) — `void * __asan_stack_malloc_7(size_t size)`
- [`__asan_stack_malloc_8()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L408) — `void * __asan_stack_malloc_8(size_t size)`
- [`__asan_stack_malloc_9()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L412) — `void * __asan_stack_malloc_9(size_t size)`
- [`__asan_stack_free_0()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L417) — `void __asan_stack_free_0(void *p`,`size_t size)`
- [`__asan_stack_free_1()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L421) — `void __asan_stack_free_1(void *p`,`size_t size)`
- [`__asan_stack_free_2()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L425) — `void __asan_stack_free_2(void *p`,`size_t size)`
- [`__asan_stack_free_3()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L429) — `void __asan_stack_free_3(void *p`,`size_t size)`
- [`__asan_stack_free_4()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L433) — `void __asan_stack_free_4(void *p`,`size_t size)`
- [`__asan_stack_free_5()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L437) — `void __asan_stack_free_5(void *p`,`size_t size)`
- [`__asan_stack_free_6()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L441) — `void __asan_stack_free_6(void *p`,`size_t size)`
- [`__asan_stack_free_7()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L445) — `void __asan_stack_free_7(void *p`,`size_t size)`
- [`__asan_stack_free_8()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L449) — `void __asan_stack_free_8(void *p`,`size_t size)`
- [`__asan_stack_free_9()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L453) — `void __asan_stack_free_9(void *p`,`size_t size)`
- [`__asan_malloc()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L458) — `void * __asan_malloc(size_t size)`
- [`__asan_free()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L464) — `void __asan_free(void *p)`
- [`__asan_malloc_hook()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L468) — `void __asan_malloc_hook(void *ptr`,`size_t size)`
- [`__asan_free_hook()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L472) — `void __asan_free_hook(void *ptr)`
- [`__asan_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L478) — `void __asan_init(void)`
- [`__asan_before_dynamic_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L483) — `void __asan_before_dynamic_init(char *module_name)`
- [`__asan_after_dynamic_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L486) — `void __asan_after_dynamic_init(void)`
- [`__asan_memcpy()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L491) — `void * __asan_memcpy(void *dst`,`void *src`,`size_t n)`
- [`__asan_memmove()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L494) — `void * __asan_memmove(void *dst`,`void *src`,`size_t n)`
- [`__asan_memset()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L497) — `void * __asan_memset(void *s`,`int c`,`size_t n)`
- [`__asan_handle_no_return()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L502) — `void __asan_handle_no_return(void)`
- [`__asan_after_load()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L503) — `void __asan_after_load(void)`
- [`__asan_after_store()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L504) — `void __asan_after_store(void)`
- [`__asan_before_memory_access()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L505) — `void __asan_before_memory_access(void)`
- [`__asan_after_memory_access()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L506) — `void __asan_after_memory_access(void)`
- [`__asan_set_shadow_00_to_0x00()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L509) — `void __asan_set_shadow_00_to_0x00(void)`
- [`__asan_set_shadow_f8_to_0x00()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L510) — `void __asan_set_shadow_f8_to_0x00(void)`
- [`__asan_alloca_poison()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L512) — `void __asan_alloca_poison(void *addr`,`size_t size)`
- [`__asan_allocas_unpoison()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L521) — `void __asan_allocas_unpoison(void *addr`,`size_t size)`
- [`__asan_alloca_poison_0()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L530) — `void __asan_alloca_poison_0(void *addr`,`size_t size)`
- [`__asan_allocas_unpoison_0()`](https://github.com/bluegummi/charmos/blob/main/kernel/mem/asan.c#L534) — `void __asan_allocas_unpoison_0(void *addr`,`size_t size)`

