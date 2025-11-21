+++
title = "limine"
author = "Unknown"
status = "unknown"
+++

# [include/limine.h](https://github.com/bluegummi/charmos/blob/main/include/limine.h)

### struct [`limine_uuid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L73)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`a`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L74) |
| `uint16_t` | [`b`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L75) |
| `uint16_t` | [`c`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L76) |
| `uint8_t` | [`d[8]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L77) |


### struct [`limine_file`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L84)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L85) |
| `LIMINE_PTR(void *)` | [`address`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L86) |
| `uint64_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L87) |
| `LIMINE_PTR(char *)` | [`path`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L88) |
| `uint32_t` | [`media_type`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L94) |
| `uint32_t` | [`unused`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L95) |
| `uint32_t` | [`tftp_ip`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L96) |
| `uint32_t` | [`tftp_port`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L97) |
| `uint32_t` | [`partition_index`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L98) |
| `uint32_t` | [`mbr_disk_id`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L99) |
| [`struct limine_uuid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L73) | [`gpt_disk_uuid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L100) |
| [`struct limine_uuid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L73) | [`gpt_part_uuid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L101) |
| [`struct limine_uuid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L73) | [`part_uuid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L102) |


### struct [`limine_bootloader_info_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L109)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L110) |
| `LIMINE_PTR(char *)` | [`name`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L111) |
| `LIMINE_PTR(char *)` | [`version`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L112) |


### struct [`limine_bootloader_info_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L115)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L116) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L117) |
| `LIMINE_PTR(struct limine_bootloader_info_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L118) |


### struct [`limine_executable_cmdline_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L125)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L126) |
| `LIMINE_PTR(char *)` | [`cmdline`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L127) |


### struct [`limine_executable_cmdline_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L130)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L131) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L132) |
| `LIMINE_PTR(struct limine_executable_cmdline_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L133) |


### struct [`limine_firmware_type_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L145)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L146) |
| `uint64_t` | [`firmware_type`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L147) |


### struct [`limine_firmware_type_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L150)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L151) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L152) |
| `LIMINE_PTR(struct limine_firmware_type_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L153) |


### struct [`limine_stack_size_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L160)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L161) |


### struct [`limine_stack_size_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L164)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L165) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L166) |
| `LIMINE_PTR(struct limine_stack_size_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L167) |
| `uint64_t` | [`stack_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L168) |


### struct [`limine_hhdm_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L175)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L176) |
| `uint64_t` | [`offset`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L177) |


### struct [`limine_hhdm_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L180)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L181) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L182) |
| `LIMINE_PTR(struct limine_hhdm_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L183) |


### struct [`limine_video_mode`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L192)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`pitch`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L193) |
| `uint64_t` | [`width`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L194) |
| `uint64_t` | [`height`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L195) |
| `uint16_t` | [`bpp`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L196) |
| `uint8_t` | [`memory_model`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L197) |
| `uint8_t` | [`red_mask_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L198) |
| `uint8_t` | [`red_mask_shift`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L199) |
| `uint8_t` | [`green_mask_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L200) |
| `uint8_t` | [`green_mask_shift`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L201) |
| `uint8_t` | [`blue_mask_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L202) |
| `uint8_t` | [`blue_mask_shift`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L203) |


### struct [`limine_framebuffer`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L206)

| Member Type | Member Name |
|-------------|-------------|
| `LIMINE_PTR(void *)` | [`address`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L207) |
| `uint64_t` | [`width`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L208) |
| `uint64_t` | [`height`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L209) |
| `uint64_t` | [`pitch`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L210) |
| `uint16_t` | [`bpp`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L211) |
| `uint8_t` | [`memory_model`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L212) |
| `uint8_t` | [`red_mask_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L213) |
| `uint8_t` | [`red_mask_shift`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L214) |
| `uint8_t` | [`green_mask_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L215) |
| `uint8_t` | [`green_mask_shift`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L216) |
| `uint8_t` | [`blue_mask_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L217) |
| `uint8_t` | [`blue_mask_shift`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L218) |
| `uint8_t` | [`unused[7]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L219) |
| `uint64_t` | [`edid_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L220) |
| `LIMINE_PTR(void *)` | [`edid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L221) |
| `uint64_t` | [`mode_count`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L223) |
| `LIMINE_PTR(struct limine_video_mode **)` | [`modes`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L224) |


### struct [`limine_framebuffer_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L227)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L228) |
| `uint64_t` | [`framebuffer_count`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L229) |
| `LIMINE_PTR(struct limine_framebuffer **)` | [`framebuffers`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L230) |


### struct [`limine_framebuffer_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L233)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L234) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L235) |
| `LIMINE_PTR(struct limine_framebuffer_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L236) |


### struct [`limine_paging_mode_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L327)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L328) |
| `uint64_t` | [`mode`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L329) |


### struct [`limine_paging_mode_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L332)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L333) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L334) |
| `LIMINE_PTR(struct limine_paging_mode_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L335) |
| `uint64_t` | [`mode`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L336) |
| `uint64_t` | [`max_mode`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L337) |
| `uint64_t` | [`min_mode`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L338) |


### struct [`limine_memmap_entry`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L473)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`base`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L474) |
| `uint64_t` | [`length`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L475) |
| `uint64_t` | [`type`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L476) |


### struct [`limine_memmap_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L479)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L480) |
| `uint64_t` | [`entry_count`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L481) |
| `LIMINE_PTR(struct limine_memmap_entry **)` | [`entries`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L482) |


### struct [`limine_memmap_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L485)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L486) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L487) |
| `LIMINE_PTR(struct limine_memmap_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L488) |


### struct [`limine_entry_point_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L497)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L498) |


### struct [`limine_entry_point_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L501)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L502) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L503) |
| `LIMINE_PTR(struct limine_entry_point_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L504) |
| `LIMINE_PTR(limine_entry_point)` | [`entry`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L505) |


### struct [`limine_kernel_file_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L519)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L521) |


### struct [`limine_kernel_file_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L532)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L534) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L535) |


### struct [`limine_internal_module`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L550)

| Member Type | Member Name |
|-------------|-------------|
| `LIMINE_PTR(const char *)` | [`path`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L551) |
| `uint64_t` | [`flags`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L557) |


### struct [`limine_module_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L560)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L561) |
| `uint64_t` | [`module_count`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L562) |
| `LIMINE_PTR(struct limine_file **)` | [`modules`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L563) |


### struct [`limine_module_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L566)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L567) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L568) |
| `LIMINE_PTR(struct limine_module_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L569) |
| `uint64_t` | [`internal_module_count`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L572) |
| `LIMINE_PTR(struct limine_internal_module **)` | [`internal_modules`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L573) |


### struct [`limine_rsdp_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L580)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L581) |


### struct [`limine_rsdp_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L589)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L590) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L591) |
| `LIMINE_PTR(struct limine_rsdp_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L592) |


### struct [`limine_smbios_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L599)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L600) |


### struct [`limine_smbios_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L610)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L611) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L612) |
| `LIMINE_PTR(struct limine_smbios_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L613) |


### struct [`limine_efi_system_table_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L620)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L621) |


### struct [`limine_efi_system_table_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L629)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L630) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L631) |
| `LIMINE_PTR(struct limine_efi_system_table_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L632) |


### struct [`limine_efi_memmap_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L639)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L640) |
| `LIMINE_PTR(void *)` | [`memmap`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L641) |
| `uint64_t` | [`memmap_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L642) |
| `uint64_t` | [`desc_size`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L643) |
| `uint64_t` | [`desc_version`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L644) |


### struct [`limine_efi_memmap_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L647)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L648) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L649) |
| `LIMINE_PTR(struct limine_efi_memmap_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L650) |


### struct [`limine_boot_time_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L664)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L666) |


### struct [`limine_boot_time_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L677)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L679) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L680) |


### struct [`limine_kernel_address_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L699)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L701) |
| `uint64_t` | [`physical_base`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L702) |
| `uint64_t` | [`virtual_base`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L703) |


### struct [`limine_kernel_address_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L709)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L711) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L712) |


### struct [`limine_dtb_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L724)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L725) |
| `LIMINE_PTR(void *)` | [`dtb_ptr`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L726) |


### struct [`limine_dtb_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L729)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L730) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L731) |
| `LIMINE_PTR(struct limine_dtb_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L732) |


### struct [`limine_riscv_bsp_hartid_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L739)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L740) |
| `uint64_t` | [`bsp_hartid`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L741) |


### struct [`limine_riscv_bsp_hartid_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L744)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L745) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L746) |
| `LIMINE_PTR(struct limine_riscv_bsp_hartid_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L747) |


### struct [`limine_bootloader_performance_response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L754)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L755) |
| `uint64_t` | [`reset_usec`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L756) |
| `uint64_t` | [`init_usec`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L757) |
| `uint64_t` | [`exec_usec`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L758) |


### struct [`limine_bootloader_performance_request`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L761)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`id[4]`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L762) |
| `uint64_t` | [`revision`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L763) |
| `LIMINE_PTR(struct limine_bootloader_performance_response *)` | [`response`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L764) |


### type alias
[`(*limine_terminal_write)`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L274) : `void (struct limine_terminal *, char *, uint64_t)`
### type alias
[`(*limine_terminal_callback)`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L275) : `void (struct limine_terminal *, uint64_t, uint64_t, uint64_t, uint64_t)`
### type alias
[`(*limine_goto_address)`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L371) : `void (struct LIMINE_MP (info))`
### type alias
[`(*limine_entry_point)`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L495) : `void (void)`
- [`limine_terminal()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L277) — `struct LIMINE_DEPRECATED limine_terminal()`
- [`limine_terminal_response()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L283) — `struct LIMINE_DEPRECATED limine_terminal_response()`
- [`limine_terminal_request()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L290) — `struct LIMINE_DEPRECATED limine_terminal_request()`
- [`limine_5_level_paging_response()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L347) — `LIMINE_DEPRECATED limine_5_level_paging_response()`
- [`limine_5_level_paging_request()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L351) — `struct LIMINE_DEPRECATED limine_5_level_paging_request()`
- [`(info)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L381) — `struct LIMINE_MP (info)()`
- [`(response)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L389) — `struct LIMINE_MP (response)()`
- [`(info)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L399) — `struct LIMINE_MP (info)()`
- [`(response)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L408) — `struct LIMINE_MP (response)()`
- [`(info)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L418) — `struct LIMINE_MP (info)()`
- [`(response)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L426) — `struct LIMINE_MP (response)()`
- [`(info)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L436) — `struct LIMINE_MP (info)()`
- [`(response)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L440) — `struct LIMINE_MP (response)()`
- [`(request)()`](https://github.com/bluegummi/charmos/blob/main/include/limine.h#L449) — `struct LIMINE_MP (request)()`

