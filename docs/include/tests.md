+++
title = "tests"
author = "Unknown"
status = "unknown"
+++

# [include/tests.h](https://github.com/bluegummi/charmos/blob/main/include/tests.h)

### struct [`kernel_test`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L10)

| Member Type | Member Name |
|-------------|-------------|
| `char` | [`*name`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L11) |
| `test_fn_t` | [`func`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L12) |
| `bool` | [`is_integration`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L13) |
| `bool` | [`should_fail`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L15) |
| `bool` | [`success`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L16) |
| `bool` | [`skipped`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L17) |
| `uint64_t` | [`message_count`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L19) |
| `char` | [`**messages`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L20) |


### type alias
[`(*test_fn_t)`](https://github.com/bluegummi/charmos/blob/main/include/tests.h#L8) : `void (void)`