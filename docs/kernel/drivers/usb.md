# [kernel/drivers/usb.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c)

<!-- Auto-generated from usb.c, do not edit manually -->

- [`usb_construct_rq_bitmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L7) — `uint8_t usb_construct_rq_bitmap(uint8_t transfer`,`uint8_t type`,`uint8_t recip)`
- [`get_desc_bitmap()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L15) — `static uint8_t get_desc_bitmap(void)`
- [`usb_get_string_descriptor()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L21) — `bool usb_get_string_descriptor(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,`uint8_t string_idx`,`char *out`,`size_t max_len)`
- [`usb_get_device_descriptor()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L59) — `void usb_get_device_descriptor(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev)`
- [`match_interfaces()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L103) — `static void match_interfaces(`[`struct usb_driver`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L330)` *driver`,[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev)`
- [`usb_try_bind_driver()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L122) — `void usb_try_bind_driver(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev)`
- [`usb_register_dev_interface()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L130) — `static void usb_register_dev_interface(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,[`struct usb_interface_descriptor`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L208)` *interface)`
- [`usb_register_dev_ep()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L143) — `static void usb_register_dev_ep(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,[`struct usb_endpoint_descriptor`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L244)` *endpoint)`
- [`setup_config_descriptor()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L164) — `static void setup_config_descriptor(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,`uint8_t *ptr`,`uint8_t *end)`
- [`usb_parse_config_descriptor()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L182) — `bool usb_parse_config_descriptor(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev)`
- [`usb_set_configuration()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb.c#L229) — `bool usb_set_configuration(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev)`

