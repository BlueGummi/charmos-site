+++
title = "xhci"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/xhci/xhci.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c)

- [`xhci_address_device()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L18) — `bool xhci_address_device(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *ctrl`,`uint8_t slot_id`,`uint8_t speed`,`uint8_t port)`
- [`xhci_send_control_transfer()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L84) — `bool xhci_send_control_transfer(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,`uint8_t slot_id`,[`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)` *ep0_ring`,[`struct usb_setup_packet`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L170)` *setup`,`void *buffer)`
- [`allocate_endpoint_ring()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L134) — `static`[`struct xhci_ring *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)`allocate_endpoint_ring(void)`
- [`xhci_configure_device_endpoints()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L160) — `bool xhci_configure_device_endpoints(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *xhci`,[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *usb)`
- [`xhci_control_transfer()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L214) — `static bool xhci_control_transfer(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,[`struct usb_packet`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L292)` *packet)`
- [`xhci_isr()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L233) — `static void xhci_isr(void *ctx`,`uint8_t vector`,`void *rsp)`
- [`xhci_device_start_interrupts()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L241) — `static void xhci_device_start_interrupts(uint8_t bus`,`uint8_t slot`,`uint8_t func`,[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L249) — `void xhci_init(uint8_t bus`,`uint8_t slot`,`uint8_t func`,[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *pci)`
- [`xhci_pci_init()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/xhci.c#L342) — `static void xhci_pci_init(uint8_t bus`,`uint8_t slot`,`uint8_t func`,[`struct pci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/pci.h#L9)` *dev)`



+++
title = "init"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/xhci/init.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c)

- [`xhci_setup_event_ring()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c#L14) — `void xhci_setup_event_ring(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_setup_command_ring()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c#L49) — `void xhci_setup_command_ring(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_enable_slot()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c#L83) — `uint8_t xhci_enable_slot(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_consume_port_status_change()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c#L91) — `bool xhci_consume_port_status_change(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_reset_port()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c#L139) — `bool xhci_reset_port(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,`uint32_t portnum)`
- [`xhci_parse_ext_caps()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c#L274) — `void xhci_parse_ext_caps(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_detect_usb3_ports()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/init.c#L311) — `void xhci_detect_usb3_ports(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`



+++
title = "cmd"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/xhci/cmd.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c)

### type alias
[`(*xhci_wait_cb)`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L36) : `uint64_t (struct xhci_device *, struct xhci_trb *evt, uint8_t slot_id, uint32_t *dq_idx, struct xhci_ring *evt_ring, uint8_t expected_cycle, bool *success_out)`
- [`xhci_advance_enqueue()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L14) — `void xhci_advance_enqueue(`[`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)` *cmd_ring)`
- [`xhci_send_command()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L22) — `void xhci_send_command(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,`uint64_t parameter`,`uint32_t control)`
- [`xhci_generic_wait()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L41) — `static uint64_t xhci_generic_wait(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,`uint8_t slot_id`,`xhci_wait_cb callback)`
- [`wait_for_response()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L64) — `static uint64_t wait_for_response(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,[`struct xhci_trb`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L443)` *evt`,`uint8_t slot_id`,`uint32_t *dq_idx`,[`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)` *event_ring`,`uint8_t expected_cycle`,`bool *success_out)`
- [`wait_for_transfer_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L86) — `static uint64_t wait_for_transfer_event(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,[`struct xhci_trb`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L443)` *evt`,`uint8_t slot_id`,`uint32_t *dq_idx`,[`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)` *event_ring`,`uint8_t expected_cycle`,`bool *success_out)`
- [`wait_for_interrupt_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L121) — `static uint64_t wait_for_interrupt_event(`[`struct xhci_trb`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L443)` *evt`,`uint8_t slot_id`,`uint32_t *dq_idx`,[`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)` *event_ring`,`uint8_t expected_cycle`,`bool *success_out`,`uint8_t ep_id)`
- [`xhci_wait_for_interrupt()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L152) — `static bool xhci_wait_for_interrupt(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *xhci`,`uint8_t slot_id`,`uint8_t ep_id)`
- [`xhci_wait_for_response()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L175) — `uint64_t xhci_wait_for_response(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_wait_for_transfer_event()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L179) — `bool xhci_wait_for_transfer_event(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,`uint8_t slot_id)`
- [`xhci_submit_interrupt_transfer()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/cmd.c#L184) — `bool xhci_submit_interrupt_transfer(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,[`struct usb_packet`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L292)` *packet)`



+++
title = "internal"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/xhci/internal.h](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/internal.h)

- [`xhci_clear_interrupt_pending()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/internal.h#L6) — `static inline void xhci_clear_interrupt_pending(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_interrupt_enable_ints()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/internal.h#L12) — `static inline void xhci_interrupt_enable_ints(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`usb_to_xhci_ep_type()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/internal.h#L17) — `static inline uint8_t usb_to_xhci_ep_type(bool in`,`uint8_t type)`
- [`xhci_ring_doorbell()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/internal.h#L51) — `static inline void xhci_ring_doorbell(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev`,`uint32_t slot_id`,`uint32_t ep_id)`
- [`xhci_advance_dequeue()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/internal.h#L57) — `static inline void xhci_advance_dequeue(`[`struct xhci_ring`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L451)` *event_ring`,`uint32_t *dq_idx`,`uint8_t *expected_cycle)`
- [`xhci_controller_restart()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/internal.h#L70) — `static inline void xhci_controller_restart(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`



+++
title = "util"
author = "Unknown"
status = "unknown"
+++

# [kernel/drivers/xhci/util.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/util.c)

- [`xhci_map_mmio()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/util.c#L13) — `void * xhci_map_mmio(uint8_t bus`,`uint8_t slot`,`uint8_t func)`
- [`xhci_device_create()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/util.c#L26) — [`struct xhci_device *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)`xhci_device_create(void *mmio)`
- [`xhci_controller_stop()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/util.c#L46) — `bool xhci_controller_stop(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_controller_reset()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/util.c#L61) — `bool xhci_controller_reset(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_controller_start()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/util.c#L77) — `bool xhci_controller_start(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`
- [`xhci_controller_enable_ints()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/xhci/util.c#L93) — `void xhci_controller_enable_ints(`[`struct xhci_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/xhci.h#L513)` *dev)`



