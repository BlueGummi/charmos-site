# [kernel/drivers/usb_kb.c](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c)

<!-- Auto-generated from usb_kb.c, do not edit manually -->

### struct [`usb_kbd_report`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L11)

| Member Type | Member Name |
|-------------|-------------|
| `uint8_t` | [`modifiers`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L12) |
| `uint8_t` | [`reserved`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L13) |
| `uint8_t` | [`keys[6]`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L14) |


- [`parse_keyboard_report()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L44) — `void parse_keyboard_report(`[`struct usb_kbd_report`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L11)` *report)`
- [`usb_find_interface()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L66) — [`struct usb_interface_descriptor *`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L208)`usb_find_interface(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,`uint8_t class`,`uint8_t subclass`,`uint8_t protocol)`
- [`usb_keyboard_get_descriptor()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L79) — `bool usb_keyboard_get_descriptor(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev`,`uint8_t interface_number`,`uint16_t len`,`void *buf)`
- [`usb_keyboard_poll()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L102) — `void usb_keyboard_poll(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev)`
- [`usb_keyboard_probe()`](https://github.com/bluegummi/charmos/blob/main/kernel/drivers/usb_kb.c#L144) — `bool usb_keyboard_probe(`[`struct usb_device`](https://github.com/bluegummi/charmos/blob/main/include/drivers/usb.h#L352)` *dev)`

