# [include/drivers/xhci.h](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h)

<!-- Auto-generated from xhci.h, do not edit manually -->

### struct [`xhci_cap_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L133)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`cap_length`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L134) |
| `uint8_t` | [`reserved`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L135) |
| `uint16_t` | [`hci_version`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L136) |
| `uint32_t` | [`hcs_params1`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L137) |
| `uint32_t` | [`hcs_params2`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L138) |
| `uint32_t` | [`hcs_params3`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L139) |
| `uint32_t` | [`hcc_params1`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L140) |
| `uint32_t` | [`dboff`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L141) |
| `uint32_t` | [`rtsoff`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L142) |
| `uint32_t` | [`hcc_params2`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L143) |


### struct [`xhci_port_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L146)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`portsc`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L147) |
| `uint32_t` | [`portpmsc`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L148) |
| `uint32_t` | [`portli`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L149) |
| `uint32_t` | [`portct`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L150) |


### struct [`xhci_usbcmd`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L153)

| Member Type | Member Name |
|-------------|-------------|
| `union { uint32_t raw; struct { uint32_t run_stop : 1; uint32_t host_controller_reset : 1; uint32_t interrupter_enable : 1; uint32_t host_system_error_en : 1; uint32_t reserved0 : 3; uint32_t light_host_controller_reset : 1; uint32_t controller_save_state : 1; uint32_t controller_restore_state : 1;  uint32_t enable_wrap_event : 1; uint32_t enable_u3_mf_index : 1; uint32_t reserved1 : 1;  uint32_t cem_enable : 1; uint32_t extended_tbc_enable : 1;  uint32_t extended_tbc_trb_status_enable : 1;  uint32_t vtio_enable : 1;  uint32_t reserved2 : 15; }; }` | [`None`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L154) |


### struct [`xhci_slot_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L185)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`route_string`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L186) |
| `uint32_t` | [`speed`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L188) |
| `uint32_t` | [`reserved0`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L190) |
| `uint32_t` | [`mtt`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L192) |
| `uint32_t` | [`hub`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L196) |
| `uint32_t` | [`context_entries`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L200) |
| `uint32_t` | [`max_exit_latency`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L204) |
| `uint32_t` | [`root_hub_port`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L209) |
| `uint32_t` | [`num_ports`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L212) |
| `uint32_t` | [`parent_hub_slot_id`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L217) |
| `uint32_t` | [`parent_port_number`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L220) |
| `uint32_t` | [`parent_think_time`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L223) |
| `uint32_t` | [`reserved1`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L226) |
| `uint32_t` | [`interrupter_target`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L228) |
| `uint32_t` | [`usb_device_address`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L231) |
| `uint32_t` | [`reserved2`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L232) |
| `uint32_t` | [`slot_state`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L233) |
| `uint32_t` | [`reserved3[4]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L235) |


### struct [`xhci_ep_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L239)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`ep_state`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L242) |
| `uint32_t` | [`reserved1`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L251) |
| `uint32_t` | [`mult`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L253) |
| `uint32_t` | [`max_pstreams`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L259) |
| `uint32_t` | [`lsa`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L268) |
| `uint32_t` | [`interval`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L275) |
| `uint32_t` | [`max_esit_payload_hi`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L281) |
| `uint32_t` | [`reserved2`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L289) |
| `uint32_t` | [`error_count`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L291) |
| `uint32_t` | [`ep_type`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L296) |
| `uint32_t` | [`reserved3`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L307) |
| `uint32_t` | [`host_initiate_disable`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L308) |
| `uint32_t` | [`max_burst_size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L316) |
| `uint32_t` | [`max_packet_size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L321) |
| `union { uint64_t dequeue_ptr_raw; struct { uint32_t dcs : 1; /* Dequeue cycle state - value of the xHC CCS * (Consumer Cycle State) flag for the TRB * referenced by the TR Dequeue pointer. * '0' if `max_pstreams` > '0' */  uint32_t reserved4 : 3;  uint64_t dequeue_ptr : 60; /* dequeue pointer * MUST be aligned to 16 BYTE BOUNDARY */ }; }` | [`None`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L327) |
| `uint32_t` | [`average_trb_length`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L345) |
| `uint32_t` | [`max_esit_payload_lo`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L349) |
| `uint32_t` | [`reserved5[3]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L356) |


### struct [`xhci_input_ctrl_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L360)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`drop_flags`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L362) |
| `uint32_t` | [`add_flags`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L370) |
| `uint32_t` | [`reserved[5]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L377) |
| `uint32_t` | [`config`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L379) |
| `uint32_t` | [`interface_num`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L387) |
| `uint32_t` | [`alternate_setting`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L401) |
| `uint32_t` | [`reserved1`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L413) |


### struct [`xhci_input_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L417)

| Member Type | Member Name |
|-------------|-------------|
| [`struct xhci_input_ctrl_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L360) | [`ctrl_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L418) |
| [`struct xhci_slot_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L185) | [`slot_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L419) |
| [`struct xhci_ep_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L239) | [`ep_ctx[31]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L420) |


### struct [`xhci_device_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L424)

| Member Type | Member Name |
|-------------|-------------|
| [`struct xhci_slot_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L185) | [`slot_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L425) |
| [`struct xhci_ep_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L239) | [`ep_ctx[32]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L426) |


### struct [`xhci_op_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L429)

| Member Type | Member Name |
|-------------|-------------|
| [`struct xhci_usbcmd`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L153) | [`usbcmd`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L430) |
| `uint32_t` | [`usbsts`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L431) |
| `uint32_t` | [`pagesize`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L432) |
| `uint32_t` | [`reserved[2]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L433) |
| `uint32_t` | [`dnctrl`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L434) |
| `uint64_t` | [`crcr`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L435) |
| `uint32_t` | [`reserved2[4]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L436) |
| `uint64_t` | [`dcbaap`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L437) |
| `uint32_t` | [`config`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L438) |
| `uint32_t` | [`reserved3[241]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L439) |
| [`struct xhci_port_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L146) | [`regs[]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L440) |


### struct [`xhci_trb`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L443)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`parameter`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L444) |
| `uint32_t` | [`status`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L445) |
| `uint32_t` | [`control`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L446) |


### struct [`xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)

| Member Type | Member Name |
|-------------|-------------|
| [`struct xhci_trb`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L443) | [`*trbs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L452) |
| `uint64_t` | [`phys`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L453) |
| `uint32_t` | [`enqueue_index`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L454) |
| `uint32_t` | [`dequeue_index`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L455) |
| `uint8_t` | [`cycle`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L456) |
| `uint32_t` | [`size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L457) |


### struct [`xhci_erst_entry`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L460)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`ring_segment_base`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L461) |
| `uint32_t` | [`ring_segment_size`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L462) |
| `uint32_t` | [`reserved`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L463) |


### struct [`xhci_erdp`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L466)

| Member Type | Member Name |
|-------------|-------------|
| `union { uint64_t raw; struct { uint64_t desi : 3; /* Dequeue ERST Segment Index */ uint64_t ehb : 1;  /* Event Handler Busy */ uint64_t event_ring_pointer : 60; }; }` | [`None`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L467) |


### struct [`xhci_interrupter_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L482)

| Member Type | Member Name |
|-------------|-------------|
| `uint32_t` | [`iman`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L483) |
| `uint32_t` | [`imod`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L484) |
| `uint32_t` | [`erstsz`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L485) |
| `uint32_t` | [`reserved`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L486) |
| `uint64_t` | [`erstba`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L487) |
| `union { struct xhci_erdp erdp; uint64_t erdp_raw; }` | [`None`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L488) |


### struct [`xhci_port_info`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L495)

| Member Type | Member Name |
|-------------|-------------|
| `bool` | [`device_connected`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L496) |
| `uint8_t` | [`speed`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L497) |
| `uint8_t` | [`slot_id`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L498) |
| `bool` | [`usb3`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L499) |
| [`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451) | [`*ep_rings[32]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L500) |


### struct [`xhci_dcbaa`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L503)

| Member Type | Member Name |
|-------------|-------------|
| `uint64_t` | [`ptrs[256]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L504) |


### struct [`xhci_ext_cap`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L507)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`cap_id`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L508) |
| `uint8_t` | [`next`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L509) |
| `uint16_t` | [`cap_specific`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L510) |


### struct [`xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`irq`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L514) |
| [`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9) | [`*pci`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L515) |
| [`struct xhci_input_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L417) | [`*input_ctx`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L516) |
| [`struct xhci_cap_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L133) | [`*cap_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L517) |
| [`struct xhci_op_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L429) | [`*op_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L518) |
| [`struct xhci_interrupter_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L482) | [`*intr_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L519) |
| [`struct xhci_dcbaa`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L503) | [`*dcbaa`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L521) |
| [`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451) | [`*event_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L523) |
| [`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451) | [`*cmd_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L524) |
| [`struct xhci_erst_entry`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L460) | [`*erst`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L525) |
| [`struct xhci_port_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L146) | [`*port_regs`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L526) |
| `uint64_t` | [`ports`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L527) |
| [`struct xhci_port_info`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L495) | [`port_info[64]`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L528) |
| `uint64_t` | [`num_devices`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L530) |
| [`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352) | [`**devices`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L531) |

