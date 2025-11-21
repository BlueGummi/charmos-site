+++
title = "irql"
author = "Unknown"
status = "unknown"
+++

# [kernel/sch/irql.c](https://github.com/bluegummi/charmos/blob/main/kernel/sch/irql.c)

- [`irql_get()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/irql.c#L5) — [`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)`irql_get(void)`
- [`irql_raise()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/irql.c#L9) — [`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)`irql_raise(`[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` new_level)`
- [`irql_lower()`](https://github.com/bluegummi/charmos/blob/main/kernel/sch/irql.c#L37) — `void irql_lower(`[`enum irql`](https://github.com/bluegummi/charmos/blob/main/include/sch/irql.h#L2)` new_level)`

