# [include/drivers/ata.h](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h)

<!-- Auto-generated from ata.h, do not edit manually -->

### struct [`ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`lba`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L64) |
| `void` | [`*buffer`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L65) |
| `uint64_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L66) |
| `uint64_t` | [`sector_count`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L67) |
| `uint16_t` | [`current_sector`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L68) |
| `bool` | [`write`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L70) |
| `bool` | [`done`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L71) |
| `int` | [`status`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L72) |
| `void` | [`(*on_complete)(struct ide_request *)`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L74) |
| `void` | [`*user_data`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L75) |
| `bool` | [`trigger_completion`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L77) |
| [`struct thread`](https://github.com/bluegummi/charmos/blob/main/include/sch/thread.h#L188) | [`*waiter`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L78) |
| [`struct ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63) | [`*next`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L79) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L80) |


### struct [`ide_channel`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L83)

| Member Type | Member Name |
|-------------|-------------|
| [`struct ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63) | [`*head`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L84) |
| [`struct ide_request`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L63) | [`*tail`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L85) |
| `bool` | [`busy`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L87) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L88) |
| [`struct ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92) | [`*current_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L89) |


### struct [`ata_drive`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L92)

| Member Type | Member Name |
|-------------|-------------|
| `bool` | [`actually_exists`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L93) |
| `uint32_t` | [`sector_size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L94) |
| `uint16_t` | [`io_base`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L95) |
| `uint16_t` | [`ctrl_base`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L96) |
| `uint16_t` | [`slave`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L97) |
| [`enum ide_type`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L58) | [`type`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L98) |
| `void` | [`*identify_data`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L99) |
| `char` | [`model[41]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L101) |
| `char` | [`serial[21]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L102) |
| `char` | [`firmware[9]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L103) |
| `uint64_t` | [`total_sectors`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L104) |
| `uint8_t` | [`supports_lba48`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L105) |
| `uint8_t` | [`supports_dma`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L106) |
| `uint8_t` | [`udma_mode`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L107) |
| `uint8_t` | [`pio_mode`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L108) |
| `uint8_t` | [`irq`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L109) |
| [`struct ide_channel`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L83) | [`channel`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L110) |


### struct [`ata_identify`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L131)

| Member Type | Member Name |
|-------------|-------------|
| `uint16_t` | [`config`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L132) |
| `uint16_t` | [`cylinders`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L133) |
| `uint16_t` | [`reserved1`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L134) |
| `uint16_t` | [`heads`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L135) |
| `uint16_t` | [`vendor1[2]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L136) |
| `uint16_t` | [`sectors_per_track`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L137) |
| `uint16_t` | [`vendor2[3]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L138) |
| `uint16_t` | [`serial_number[10]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L139) |
| `uint16_t` | [`vendor3[2]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L140) |
| `uint16_t` | [`obsolete1`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L141) |
| `uint16_t` | [`firmware_revision[4]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L142) |
| `uint16_t` | [`model_number[20]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L143) |
| `uint16_t` | [`max_rw_multiple`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L144) |
| `uint16_t` | [`reserved2`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L145) |
| `uint16_t` | [`capabilities[2]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L146) |
| `uint16_t` | [`obsolete2[2]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L147) |
| `uint16_t` | [`field_validity`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L148) |
| `uint16_t` | [`current_cylinders`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L149) |
| `uint16_t` | [`current_heads`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L150) |
| `uint16_t` | [`current_sectors`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L151) |
| `uint16_t` | [`current_capacity_lo`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L152) |
| `uint16_t` | [`current_capacity_hi`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L153) |
| `uint16_t` | [`rw_multiple`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L154) |
| `uint32_t` | [`lba28_capacity`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L155) |
| `uint16_t` | [`dma_supported`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L156) |
| `uint16_t` | [`advanced_pio_modes`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L157) |
| `uint16_t` | [`min_dma_cycle_time`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L158) |
| `uint16_t` | [`recommended_dma_cycle_time`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L159) |
| `uint16_t` | [`min_pio_cycle_time`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L160) |
| `uint16_t` | [`min_pio_cycle_time_iordy`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L161) |
| `uint16_t` | [`additional_supported`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L162) |
| `uint16_t` | [`reserved3[5]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L163) |
| `uint16_t` | [`queue_depth`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L164) |
| `uint16_t` | [`sata_capabilities`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L165) |
| `uint16_t` | [`sata_additional`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L166) |
| `uint16_t` | [`sata_features_supported`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L167) |
| `uint16_t` | [`sata_features_enabled`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L168) |
| `uint16_t` | [`major_version`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L169) |
| `uint16_t` | [`minor_version`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L170) |
| `uint16_t` | [`command_set_supported[3]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L171) |
| `uint16_t` | [`command_set_enabled[3]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L172) |
| `uint16_t` | [`features_supported_extension`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L173) |
| `uint16_t` | [`security_erase_time`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L174) |
| `uint16_t` | [`enhanced_security_erase_time`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L175) |
| `uint16_t` | [`current_advanced_power_mgmt`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L176) |
| `uint16_t` | [`master_password_revision`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L177) |
| `uint16_t` | [`hardware_reset_result`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L178) |
| `uint16_t` | [`acoustic_management`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L179) |
| `uint16_t` | [`stream_min_req_size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L180) |
| `uint16_t` | [`stream_transfer_time_dma`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L181) |
| `uint16_t` | [`stream_access_latency`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L182) |
| `uint32_t` | [`streaming_performance_gran`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L183) |
| `uint64_t` | [`lba48_sector_count`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L184) |
| `uint16_t` | [`streaming_transfer_time`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L185) |
| `uint16_t` | [`dsm_cap`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L186) |
| `uint16_t` | [`phys_log_sector_size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L187) |
| `uint16_t` | [`inter_seek_delay`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L188) |
| `uint16_t` | [`world_wide_name[4]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L189) |
| `uint16_t` | [`reserved4[144]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L190) |


### enum [`ide_type`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L58)

| Name | Value |
|------|-------|
| [`IDE_TYPE_ATA`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L59) | `None` |
| [`IDE_TYPE_ATAPI`](https://github.com/bluegummi/charmos/blob/main/include/drivers/ata.h#L60) | `None` |

