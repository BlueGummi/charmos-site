# [include/stat_series.h](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h)

<!-- Auto-generated from stat_series.h, do not edit manually -->

### struct [`stat_bucket`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L18)

| Member Type | Member Name |
|-------------|-------------|
| [`struct stat_series`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L26) | [`*parent`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L19) |
| `atomic_size_t` | [`count`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L20) |
| `atomic_size_t` | [`sum`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L21) |
| `void` | [`*private`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L22) |


### struct [`stat_series`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L26)

| Member Type | Member Name |
|-------------|-------------|
| `stat_series_callback` | [`bucket_reset`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L27) |
| [`struct stat_bucket`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L18) | [`*buckets`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L28) |
| `uint32_t` | [`nbuckets`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L29) |
| `atomic_uint_fast32_t` | [`current`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L30) |
| [`time_t`](https://github.com/bluegummi/charmos/blob/main/include/types/types.h#L6) | [`bucket_us`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L31) |
| `atomic_uint_fast64_t` | [`last_update_us`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L32) |
| `void` | [`*private`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L33) |
| [`struct spinlock`](https://github.com/bluegummi/charmos/blob/main/include/sync/spinlock.h#L10) | [`lock`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L34) |


### type alias
[`(*stat_series_callback)`](https://github.com/bluegummi/charmos/blob/main/include/stat_series.h#L24) : `size_t (struct stat_bucket *bucket)`