# [include/sch/irql.h](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h)

<!-- Auto-generated from irql.h, do not edit manually -->

### enum [`irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)

| Name | Value |
|------|-------|
| [`IRQL_PASSIVE_LEVEL`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L3) | `0` |
| [`IRQL_APC_LEVEL`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L4) | `1` |
| [`IRQL_DISPATCH_LEVEL`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L5) | `2` |
| [`IRQL_DEVICE_LEVEL`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L6) | `3` |
| [`IRQL_HIGH_LEVEL`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L7) | `4` |
| [`IRQL_NONE`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L8) | `-1` |


- [`irql_to_str()`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L11) — `static inline const char * irql_to_str(`[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` level)`

